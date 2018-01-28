from django.shortcuts import render, redirect
from django.core.exceptions import FieldDoesNotExist
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from urllib import parse
import json
import os

from bashim.models import BashQuote, BashAbyssQuote
from .forms import AbyssUpdateForm, BashUpdateForm

from .request_utils import get_abyss_best_urls
from .asyc_utils import *





files_quotes_body = 'quotes_body_list.txt'
quote_url = 'http://bash.im'

def bash_utils(request):
    abyss_form = AbyssUpdateForm()
    bash_form = BashUpdateForm()
    if request.method == 'POST':
        abyss_form = AbyssUpdateForm(request.POST)
        bash_form = BashUpdateForm(request.POST)
        if abyss_form.is_valid():
            days = abyss_form.cleaned_data['days']
            if days != None:
                days = int(days)
                quotes = __get_abyss_quotes(days)                
                update_quotes(quotes, BashAbyssQuote)

        if bash_form.is_valid():
            pages = bash_form.cleaned_data['pages']
            if pages != None:
                pages = int(pages)
                quotes = __get_bash_quotes(pages)             
                update_quotes(quotes, BashQuote)
    cnt = {
        'title': 'Bash Utils',
        'abyss_form': abyss_form,
        'bash_form':bash_form,
    }
    return render(request, 'bash_utils/index.html', cnt)


def __get_abyss_quotes(days=1):
    urls = get_abyss_best_urls(days)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(run(urls, abyss=True))
    result = loop.run_until_complete(future)
    return result

def __get_bash_quotes(pages=1):
    url = 'http://bash.im/'
    start_page = get_page_lxml(url)
    page_count = int(get_pages_count(start_page, max_page_xpath))
    page_number = range(page_count+1)[(page_count-pages+1):]
    urls = [url + 'index/' + str(page) for page in page_number]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(run(urls, abyss=False))
    result = loop.run_until_complete(future)
    return result



module_dir = os.path.dirname(__file__)  # get current directory
bash_json = os.path.join(module_dir, 'json_dump/quotes.json')
abyss_json = os.path.join(module_dir, 'json_dump/abyss_quotes.json')

def load_json(file):
    with open(file) as data_file:
        return json.loads(data_file.read())

# Manual Set BashQuote.is_comics to Active if quote have comics
def set_comics(request):
    quotes = BashQuote.objects.filter(comics__startswith='http')
    for q in quotes:
        q.is_comics = True
        q.save()
    return redirect('bash')


# Manual Set BashQuote.comics_img_url
def set_comics_url(request):
    xpath_config = QuoteXpath()
    quotes = BashQuote.objects.filter(is_comics=True, comics_img_url=None)
    for q in quotes:
        try:
            response = requests.get(q.comics, headers={'User-Agent': generate_user_agent() })
            comics_page = html.fromstring(response.text)
            comics_img_xpath = xpath_config.quote_detail['comics_img_url']
            comics_img_url = comics_page.xpath(comics_img_xpath)[0]
            q.comics_img_url = comics_img_url
            print('Yeah!!! We have comics url!')
        except:
            q.comics_img_url = None
            print('Whoooops!!! No comics URl, mb try again later')
        q.save()
    return redirect('bash_utils')
     
        
# Manual Set BashQuote.comics_image
def set_img_comics_from_url(request):
    quotes = BashQuote.objects.filter(is_comics=True, comics_image__exact='')
    for q in quotes:
        save_img_from_url(q)
    return redirect('bash_utils')

def save_img_from_url(object):
    url = object.comics_img_url
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        img_temp = NamedTemporaryFile(delete = True)
        img_temp.write(r.content)
        img_temp.flush()
        img_filename = parse.urlsplit(url).path[1:]
        (object.comics_image).save(img_filename, File(img_temp), save = True)
        print("Succefuly image setted!")
        return True
    print("Fail, sry ((")
    return False

def set_current_rating(request):
    quotes = BashQuote.objects.all()
    for quote in quotes:
        rating = quote.rating
        try:
            i_rating = float(rating)
            quote.rating = i_rating
            print('YEEEAP!')
        except ValueError:
            quote.rating = 1
            print('Misss (')
        quote.save()
        print('*'*50)


def create_bash_quote(request, file=bash_json):
    data = load_json(file)
    data_list = list(data.values())
    __try_save_quote(data_list, BashQuote)
    return redirect('bash')

def update_quotes(quotes_list, model):
    quotes_dict = dict()
    for i in quotes_list:
        quotes_dict.update(i)
    data_list = list(quotes_dict.values())
    __try_save_quote(data_list, model)
    print('Succefuly updated!')

def create_abyss_quote(request, file=abyss_json):
    data = load_json(file)
    data_list = list(data.values())
    __try_save_quote(data_list, BashAbyssQuote)
    return redirect('abyssbest')


def __try_save_quote(data_list, model):
    parts = [data_list[i::5] for i in range(5)]
    quote = model()
    fields = [(field.name) for field in model._meta.fields]
    fields.remove('id')
    for part in parts:
        for item in part:
            try:
                model.objects.get(quote_id=item['quote_id'])
                print('--- Quote allready added!')
            except model.DoesNotExist:
                if 'is_comics' in fields:
                    fields.remove('comics_image')
                    fields.remove('comics_img_url')
                    setattr(quote, 'is_comics', False)
                    fields.remove('is_comics')
                for field in fields:
                    try:
                        if field == 'comics':
                            try:
                                if quote.comics:
                                    setattr(quote, field, item[field])
                                    setattr(quote, 'is_comics', True)
                                    save_img_from_url(quote)
                                    setattr(quote, 'comics_img_url', item['comics_img_url'] )
                            except KeyError:
                                pass
                        else:
                            setattr(quote, field, item[field])
                    except FieldDoesNotExist:
                        pass
                quote.save()
                print('+++ Quote succefuly added')
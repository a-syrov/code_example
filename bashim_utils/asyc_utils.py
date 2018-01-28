from aiohttp import ClientSession
import asyncio
from lxml import html
from time import sleep
from user_agent import generate_user_agent
from .quotes import QuoteXpath, QuoteAbyssXpath
from .request_utils import *
import operator
import pickle

from colorama import Fore, Back, Style

total_checked = 0
unread_quotes_link = list()


files_quotes_body = 'quotes_body_list.txt'
quote_url = 'http://bash.im'

# Async Section
## Get one item from item list
async def get_one_quote(url, session, abyss):
    global total_checked
    # Set randomize User-Agent in headers
    async with session.get(url, headers={'User-Agent': generate_user_agent() }) as response:
        # Ожидаем ответа и блокируем таск.
        if response.status == 200:
            page_content = await response.text(encoding='windows-1251')
            # Получаем информацию  и сохраняем в список.
            item = get_quote_body(page_content, url, abyss)
            if item != None: 
                print(Fore.GREEN + 'Append! ' + Fore.WHITE + '  - - - Total checked: ' + str(total_checked))
                total_checked += 1
                return item
            else:                
                print(Fore.YELLOW + 'No Quote Links : ' + url + Fore.WHITE + '  - - - Total checked: ' + str(total_checked))
        else:
            total_checked += 1
            print(Fore.RED + "------------BAD RESPONSE STATUS {} ------------------".format(response.status))
            unread_quotes_link.append(url)
        print(Fore.BLUE)

async def bound_fetch(sm, url, session, abyss):
    try:
        async with sm:
            data = await get_one_quote(url, session, abyss)
            return data
    except Exception as e:
        print(e)
        # Блокируем все таски на 30 секунд в случае ошибки 429.
        sleep(30)

def get_quote_body(page_content, url, abyss):
    # Получаем корневой lxml элемент из html страницы.
    document = html.fromstring(page_content)
    if not abyss:
        xpath_config = QuoteXpath()
        quote_body = xpath_config.quote_body
        q_body = get_xpath(document, quote_body)

        quotes_obj = dict()
        for el in q_body:

            q_rating = el.xpath(xpath_config.quote_detail['rating'])[0]
            #check rating value
            try:
                float(q_rating)
                pass
            except ValueError:
                q_rating = 0.0

            quote_id = el.xpath(xpath_config.quote_detail['id'])[0]
            q_date = el.xpath(xpath_config.quote_detail['date'])[0]
            text = ['<p>' + text + '</p>' for text in el.xpath(xpath_config.quote_detail['text'])]
            q_text = " ".join(text)
            q_link = quote_url + el.xpath(xpath_config.quote_detail['link'])[0]

            q_comics = el.xpath(xpath_config.quote_detail['comics'])
            quote = dict()
            quote[quote_id] = {
                            'rating': q_rating,
                            'quote_id': quote_id,
                            'date': q_date,
                            'text': q_text,
                            'link': q_link,
                        }
            if q_comics:
                quote[quote_id]['comics'] = quote_url + q_comics[0]
                try:
                    response = requests.get(quote[quote_id]['comics'], headers={'User-Agent': generate_user_agent() })
                    comics_page = html.fromstring(response.text)
                    comics_img_url = comics_page.xpath(xpath_config.quote_detail['comics_img_url'])[0]
                    quote[quote_id]['comics_img_url'] = comics_img_url
                except:
                    quote[quote_id]['comics_img_url'] = None


            quotes_obj.update(quote)
    else:
        xpath_config = QuoteAbyssXpath()
        quote_body = xpath_config.quote_body
        q_body = get_xpath(document, quote_body)

        quotes_obj = dict()
        for el in q_body:
            quote_id = el.xpath(xpath_config.quote_detail['id'])[0]
            q_date = el.xpath(xpath_config.quote_detail['date'])[0]
            text = ['<p>' + text + '</p>' for text in el.xpath(xpath_config.quote_detail['text'])]
            q_text = " ".join(text)
            quote = dict()
            quote[quote_id] = {
                            'quote_id': quote_id,
                            'date': q_date,
                            'text': q_text,
                        }
            quotes_obj.update(quote)
    return quotes_obj

async def run(urls, abyss=False):
    tasks = []
    sm_count = 30
    sm = asyncio.Semaphore(sm_count)
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(bound_fetch(sm, url, session, abyss))
            tasks.append(task)
        result = await asyncio.gather(*tasks)
        return result

## Return result of element.xpath
def get_xpath(document, xpath):
    try:
        result = document.xpath(xpath)
        return result
    except:
        return("Cant get xpath")

def merge(lst, res=[]):
    for el in lst:
        merge(el) if isinstance(el, list) else res.append(el)
    return res



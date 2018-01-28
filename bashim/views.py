from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BashQuote, BashAbyssQuote
from .forms import QuotesFilterForm, QuotesAbyssFilterForm

# Create your views here.
def bash(request):
    title = 'Bash'
    order = None

    if not request.method == 'POST':
        if 'ordering' in request.session:
            request.POST = request.session['ordering']
            request.method = 'POST'

    if request.method == 'POST':
        form = QuotesFilterForm(request.POST)
        request.session['ordering'] = request.POST
        if form.is_valid():
            if form.cleaned_data['ordering'] != 'is_comics':
                order = form.cleaned_data['ordering']
                quotes_all = BashQuote.objects.order_by(order)
            else:
                quotes_all = BashQuote.objects.filter(is_comics=True)

    else:
        quotes_all = BashQuote.objects.all()
        form = QuotesFilterForm()

    paginator = Paginator(quotes_all, 25)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)
    index = paginator.page_range.index(quotes.number)
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    cnt = {
        'title': title,
        'quotes': quotes,
        'page_range': page_range,
        'form': form,
        'ordering': order
    }
    return render(request, 'bash/index.html', cnt)

def abyssbest(request):
    title = 'BashAbyssBest'
    order = None

    if not request.method == 'POST':
        if 'ordering' in request.session:
            request.POST = request.session['ordering']
            request.method = 'POST'

    if request.method == 'POST':
        form = QuotesAbyssFilterForm(request.POST)
        request.session['ordering'] = request.POST
        if form.is_valid():
            order = form.cleaned_data['ordering']
            quotes_all = BashAbyssQuote.objects.order_by(order)
        else:
            quotes_all = BashAbyssQuote.objects.all()
            form = QuotesAbyssFilterForm()

    paginator = Paginator(quotes_all, 25)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)

    index = paginator.page_range.index(quotes.number)
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    cnt = {
        'title': title,
        'quotes': quotes,
        'page_range': page_range,
        'form': form,
        'ordering': order
    }
    return render(request, 'bash/abyss_best.html', cnt)
import requests, os
from user_agent import generate_user_agent
from lxml import html
import pickle
import json

from datetime import datetime, timedelta


base_url = 'http://bash.im/'
# GET URSL FOR BASH ABYSS BEST
def get_abyss_best_urls(days=365):
    abyss_best = 'http://bash.im/abyssbest/'
    date_now = datetime.now()
    one_day = timedelta(1)
    abyss_urls = list()
    abyss_urls.append(abyss_best)
    for i in range(days):
        date_now -= one_day
        url = abyss_best + date_now.strftime("%Y%m%d")
        abyss_urls.append(url)
    return abyss_urls


file = 'urls_dump.pickle'

max_page_xpath = '//span[@class="current"]/input/@max'

def get_page_lxml(url):
    user_agent = {'User-Agent': generate_user_agent()}
    response_text = requests.get(url, headers=user_agent).text
    return html.fromstring(response_text)

def get_pages_count(page, max_page_xpath):
    return page.xpath(max_page_xpath)[0]
    
def get_pages_urls(page, pages_count):
    return [(base_url + 'index/' + str(page_num)) for page_num in range(1, int(pages_count)+1)]

def pickle_urls(data, file_name):
    if file_is_not_created(file_name):  
        with open(file_name, 'wb') as file:
            pickle.dump(data, file)
        print("Urls dump succefuly created")
    else:
        print("Urls dump file already existed.")

def dump_quotes_body():
    pass

# Checking for a file exist
def file_is_not_created(file):
    try:
        if os.path.getsize(file) > 0:
            return False
        print("File already created")
    except OSError:
        print("File not created")
        return True

def dump_open(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except EOFError:
        print("Check URL dump file")

def write_json(info, file):
    try:
        data = json.load(open(file))
        print('File succefuly find!')
    except:
        data = dict()
    data.update(info)
    with open(file, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        print('Json File Updated! Now we have {} quotes!'.format(len(data)))


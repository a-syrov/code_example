class QuoteXpath:
    def __init__(self):
        self.quote_detail = {
            'rating': './/span[@class="rating"]/text()',
            'id':     './/a[@class="id"]/text()',
            'date':   './/span[@class="date"]/text()',
            'text':   './/div[@class="text"]/text()',
            'link':   './/a[@class="id"]/@href',
            'comics': './/a[@class="comics"]/@href',
            'comics_img_url': './/div[@id="comics"]//div[@id="the_strip"]//img/@src'
        }
        self.quote_body = '//div[@class="quote"]'

    def show_xpath(self):
        for k,v in self.quote_detail.items():
            print("{} ===> {}".format(k, v))

class QuoteAbyssXpath:
    def __init__(self):
        self.quote_detail = {
            'id':     './/span[@class="id"]/text()',
            'date':   './/span[@class="date"]/text()',
            'text':   './/div[@class="text"]/text()',
        }
        self.quote_body = '//div[@class="quote"]'

    def show_xpath(self):
        for k,v in self.quote_detail.items():
            print("{} ===> {}".format(k, v))

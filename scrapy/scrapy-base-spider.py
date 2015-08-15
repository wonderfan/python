from scrapy.spiders import Spider
from scrapy.http import Request
from bs4 import BeautifulSoup as bs
from pprint import pprint as pretty_print

class BaseSpider(Spider):
    
    name = 'base'
    start_urls = ['http://www.msn.com']
    allowed_domains = ["www.msn.com"]
    custom_settings = {'DOWNLOAD_HANDLERS': {'s3': None}}
    
    def parse(self, response):
        soup = bs(response.body,'lxml')
        href_list = []
        title_list = []
        for el in soup.find_all('a'):
            if el.get('href').startswith('#'):
                continue
            
            if 'Sports' == el.getText():
                url = el.get("href")
                if url.startswith("http"):
                    yield  Request(url, callback=self.parse)
                elif url.startswith('/'):
                    url = 'http://www.msn'+url
                    yield Request(url,callback=self.parse)
                else:
                    print("can not find sport channel")
            else:
                print("I am not intersted in {0} and {1}".format(el.getText(),el.get('href')))

            
        

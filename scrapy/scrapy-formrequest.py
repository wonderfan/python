# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request
from card.items import Thread


class CardlandSpider(scrapy.Spider):
    name = "cardland"
    allowed_domains = ["carderland.com"]
    start_urls = (
        'http://carderland.com/',
    )
    
    def start_requests(self):
        return [Request("http://www.carderland.com/", callback = self.post_login)]
        
    def post_login(self,response):
        formdata = {'vb_login_username':'mavrf808','vb_login_password':'dasani11'}
        return [FormRequest.from_response(response, formdata = formdata,callback = self.after_login)]
    
    def after_login(self,response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
             
    def parse(self, response):
        elements = response.xpath("//a/@href")
        yield Thread(title='hell world',url='111111')
        '''
        for element in elements:
            yield Thread(title="test",url=element.extract())
        '''
    
    

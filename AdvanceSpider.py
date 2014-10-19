# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from tld import get_tld
from linksCrawl.items import LinkscrawlItem
from scrapy.utils.response import get_base_url


class AdvancedspiderSpider(CrawlSpider):
    name = 'advancedspider'
    allowed_domains = ['msn.com']
    start_urls = ['http://www.msn.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*'), callback='parse_item', follow=True,process_links='process_links'),
    )
    
    def process_results(self, response, results):
        self.top_domain = get_tld(response.url)
        self.base_url = get_base_url(response)
        return results
    
    def process_links(self,links):
        items = []
        self.external_items = []
        for link in links:
            target_domain = get_tld(link.url)
            if target_domain != self.top_domain:
                i = LinkscrawlItem()
                i['link'] = link.url
                i['source'] = self.base_url
                self.external_items.append(i)
            else:
                items.append(link)
        
        return items
        
    def parse_item(self, response):
        return self.external_items


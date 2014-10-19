# -*- coding: utf-8 -*-
import scrapy
from tld import get_tld
from linksCrawl.items import LinkscrawlItem
from linksCrawl import settings
from urlparse import urlparse


class LinkspiderSpider(scrapy.Spider):
    name = "linkSpider"
    #allowed_domains = ["msn.com"]
    start_urls = settings.START_URLS

    def parse(self, response):
        domain = get_tld(response.url)
        items = []
        url_result = urlparse(response.url)
        top_domain = url_result.scheme + '://'+url_result.netloc
        
        for sel in response.xpath('//a/@href'):
            item = LinkscrawlItem()
            link = sel.extract()
            if link.find("http://") == 0 or link.find("https://") == 0 or link.find("www.") == 0:
                try:
                    target_domain = get_tld(link)
                    #print domain +"==================="+target_domain +"==================" + link
                    if domain != target_domain:
                        item['link'] = link
                        item['source'] = top_domain
                        yield item
                        #items.append(item)
                    else:
                        yield scrapy.Request(link,callback=self.parse)
                except:
                    print "The url can't get the domain. Ignored..." + link
                    
            if link.startswith('/'):
                yield scrapy.Request(top_domain+link, callback=self.parse)         
        #print "items="+str(items)
        #return items

import unittest
import requests
from lxml import etree
from io import StringIO, BytesIO

class MyTest(unittest.TestCase):
    
    def test_scrape(self):
        url = "http://www.yahoo.com/search"
        payload = {'search': 'stock'}
        request = requests.get(url,params=payload)
        print(request.url)
        print(type(request.text))
        
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(request.text), parser)
        links = tree.xpath("//a[contains(@href,'stock')]")
        print(len(links))
        for item in links:
            print item.attrib.get("href")
    
if __name__ == '__main__':
    unittest.main()

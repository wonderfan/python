import unittest
import csv
import requests
import re
import uuid
from lxml import etree
from io import StringIO, BytesIO

class SimpleTest(unittest.TestCase):
    
    def test_download(self):
        url = "http://www.youtube.com/results?q=python regular expression"
        response = requests.get(url)
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(response.text), parser)
        link_list = tree.xpath("//a[contains(@href,'watch')]")
        uid = str(uuid.uuid4())
        print(">>> "+ uid)
        f = csv.writer(open(uid + ".csv", "w"))
        f.writerow(["#####     Name     #####","#####     Link     #####"])  
        for element in link_list:
            if element.text is not None:
                f.writerow([element.text.encode('utf-8'),"  http://www.youtube.com" + element.attrib.get("href")])
   
if __name__ == '__main__':
    unittest.main() 

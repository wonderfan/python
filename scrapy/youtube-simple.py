import unittest
import csv
import uuid
import requests
from lxml import etree
from io import StringIO

class SimpleTest(unittest.TestCase):
    
    def test_download(self):
        url = "http://www.youtube.com/results?q=python regular expression"
        response = requests.get(url)
        tree   = etree.parse(StringIO(response.text), etree.HTMLParser())
        link_list = tree.xpath("//a[contains(@href,'watch')]")
        uid = str(uuid.uuid4())
        print(">>> "+ uid)
        f = csv.writer(open(uid + ".csv", "w"))
        for element in link_list:
            if element.text is not None:
                f.writerow([element.text.encode('utf-8'),"    http://www.youtube.com" + element.attrib.get("href")])
   
if __name__ == '__main__':
    unittest.main() 

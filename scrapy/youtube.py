import unittest
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb

class MainTest(unittest.TestCase):
    
    def setUp(self):
        self.xvfb = Xvfb(width=1280, height=720)
        self.xvfb.start()
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
    
    def test_main(self):
        self.browser.get("http://www.youtube.com")
        #self.browser.get("http://www.youtube.com//results?search_query=ionic")
        
        search = self.browser.find_element_by_id("masthead-search-term")
        search.send_keys('angular',Keys.RETURN)
        
        self.browser.implicitly_wait(2)
        self.browser.save_screenshot("youtube.png")
    
        '''
        with open('youtube.html','w') as html:
            page = driver.page_source
            html.write(page.encode('utf-8'))
        '''
        
        link_elements = self.browser.find_elements_by_xpath("//a[@title]")
        f = csv.writer(open("youtube.csv", "w"))
        f.writerow(["Name", "   Link"])  
        for element in link_elements:
            if len(element.text) > 5:
                name = element.text
                f.writerow([name.encode('utf-8'),'    '+ element.get_attribute("href")])
    
if __name__ == '__main__':
    unittest.main()    

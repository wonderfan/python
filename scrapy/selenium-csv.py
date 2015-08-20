import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

class MainTest(unittest.TestCase):
    
    def test_main(self):
        driver = webdriver.Firefox()
        driver.get("http://www.yahoo.com/video/search?search=chinese&page=2")
        '''
        search = driver.find_element_by_id("searchInput")
        search.send_keys('vocal',Keys.RETURN)
        '''
        driver.implicitly_wait(2)
        driver.save_screenshot("search.png")
        '''
        with open('result.html','w') as html:
            page = driver.page_source
            html.write(page.encode('utf-8'))
        '''
        link_elements = driver.find_elements_by_xpath("//a[contains(@href,'view_video.php')]")
        f = csv.writer(open("test.csv", "w"))
        f.writerow(["Name", "Link"])  
        for element in link_elements:
            if len(element.text) > 6:
                f.writerow([element.text,element.get_attribute("href")])
        
        driver.quit()
    
if __name__ == '__main__':
    unittest.main()    

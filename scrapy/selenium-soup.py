import unittest
from selenium import webdriver

class ForumTest(unittest.TestCase):
    
    def test_scrape(self):
        driver = webdriver.Firefox()
        url = 'https://crdclub.ws'
        driver.get(url)
        driver.implicitly_wait(2) 
        modal = driver.find_element_by_css_selector(".box-modal_close")
        if modal is not None and modal.is_displayed():
            modal.click()
        username = driver.find_element_by_id("navbar_username")
        username.send_keys("marfa890")
        password = driver.find_element_by_id("navbar_password")
        password.send_keys("dasani11")
        submit = driver.find_element_by_xpath("//input[@type='submit']")
        submit.click()
        driver.implicitly_wait(2) 
        driver.save_screenshot("forum.png")
        
        driver.close()
        
    pass

if __name__ == '__main__':
    unittest.main()

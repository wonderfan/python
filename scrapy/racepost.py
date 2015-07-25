import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumCase(unittest.TestCase):

    def setUp(self):
        print "it is starting"
        self.driver = webdriver.Firefox()
        
    def test_description(self):
        driver = self.driver
        driver.get("http://www.racingpost.com")
        login = driver.find_element_by_id('signInLink')
        login.click()
        driver.implicitly_wait(10)
        print driver.page_source
        alert = driver.switch_to_alert()
        #print alert.find_element_by_id("sign-in-dropdown-frame").is_displayed()
        '''
        driver.find_element_by_id("input-email").send_keys("office@whitelabelservices.co.uk")
        driver.find_element_by_id("input-pwd").send_keys("Gahagan1")
        driver.find_element_by_id("button-sign-in").click()
        print driver.find_elements_by_class_name("betSlipHead").text
        '''
        
    def tearDown(self):
        self.driver.close()
        print "It is ending"
        
if __name__ == '__main__':
    unittest.main()        

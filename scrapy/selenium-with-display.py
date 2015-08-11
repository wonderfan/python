import unittest

class SeleniumCase(unittest.TestCase):
    
    def test_koding(self):
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.FIREFOX)
        driver.get("http://www.koding.com")
        display.stop()
        
if __name__ == '__main__':
    unittest.main()        

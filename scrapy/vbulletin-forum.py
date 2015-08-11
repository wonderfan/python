import unittest
from selenium import webdriver
from bs4 import BeautifulSoup

class ForumTest(unittest.TestCase):
    
    def test_scrape(self):
        driver = webdriver.Firefox()
        url = 'https://crdclub.ws'
        driver.get(url)
        driver.implicitly_wait(1) 
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
        driver.get(url)
        #driver.save_screenshot("forum.png")
        '''
        forum_links = driver.find_elements_by_xpath("//a[contains(@href,'forumdisplay.php?f')]")
        for forum_link in forum_links:
            href = forum_link.get_attribute("href")
            print href
        '''
        forum_link = driver.find_element_by_xpath("//a[contains(@href,'forumdisplay.php?f')]")
        href = forum_link.get_attribute("href")
        driver.get(href)
        thread_link = driver.find_element_by_xpath("//a[contains(@href,'showthread.php?t')]")
        thread_href = thread_link.get_attribute("href")
        print "The thread link is {0}".format(thread_href)
        print "The thread title is {0}".format(thread_link.text)
        driver.get(thread_href)
        posts = driver.find_elements_by_css_selector("div[id^='post_message']")
        for post in posts:
            print post.text
        driver.close()

if __name__ == '__main__':
    unittest.main()

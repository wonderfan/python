from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('CardBase')

class CardBase(object):
    
    def __init__(self,url,user,password):
        self.url = url
        self.user = user
        self.password = password
        self.threads = []       
        self.posts = []       
    
    def scrape(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        login_element = driver.find_element_by_link_text("Log in or Sign up")
        logger.info("The text of login is {0}".format(login_element.text))
        login_element.click()
        login_form = driver.find_element_by_id("login")
        if login_form.is_displayed():
            user = login_form.find_element_by_id("LoginControl")
            password = login_form.find_element_by_id("ctrl_password")
            registed = login_form.find_element_by_id("ctrl_registered")
            remembed = login_form.find_element_by_id("ctrl_remember")
            user.send_keys(self.user)
            password.send_keys(self.password)
            registed.send_keys(0)
            remembed.send_keys(0)
            login_button = login_form.find_element_by_css_selector("input[type='submit']")
            login_button.submit()
        driver.implicitly_wait(1)
        forum_elements = driver.find_elements_by_xpath("//a[contains(@href,'index.php?forums')]")
        forum_links = set()
        thread_links = set()
        for element in forum_elements:
            forum_links.add(element.get_attribute("href"))
            element = None
        del forum_elements
        logger.info("The total number of forum links is {0}".format(len(forum_links)))
        for link in forum_links:
            driver.get(link)
            driver.implicitly_wait(1)
            thread_elements = driver.find_elements_by_xpath("//a[contains(@href,'index.php?threads')]")
            for element in thread_elements:
                thread_links.add(element.get_attribute("href"))
                thread_info = {'title':element.text,'url':element.get_attribute("href")}
                self.threads.append(thread_info)
                element = None
            link = None
            del thread_elements
        
        for link in  thread_links:
            driver.get(link)
            driver.implicitly_wait(1)
            posts = driver.find_elements_by_xpath("//li[starts-with(@id,'post')]")
            for post in posts:
                content = post.find_element_by_css_selector(".messageContent")
                post_info = {'id':post.get_attribute('id'),'member':post.get_attribute('data-author'),'body':content.text}
                self.posts.append(post_info)
                post = None
            del posts
            break
            
        #driver.save_screenshot('login.png')
        driver.quit()
    
    def get_threads(self):
        return self.threads
    
    def get_posts(self):
        return self.posts

def main():
    url = 'https://carderbase.su/index.php'
    user = ''
    password = ''
    carder = CardBase(url,user,password)
    carder.scrape()
    print carder.get_threads()
    print '=' * 50
    print carder.get_posts()
    
if __name__ == '__main__':
    main()    

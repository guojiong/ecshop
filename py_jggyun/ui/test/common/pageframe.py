'''
Created on 2020年8月7日

@author: Administrator
'''
from ui.test.common.browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class PageFrame(Browser):

    def __init__(self, page=None, browser_type='firefox'):
        if page:
            self.driver = page.driver
        else:
            super(PageFrame, self).__init__(browser_type)
            
    def title(self):
        pass
    
    def current_window(self):
        pass
    
    def current_url(self):
        pass
    
    def get_driver(self):
        pass
    
    def move_to(self, elememt):
        pass
    
    def find_element(self, *args):
        return self.driver.find_element(*args)
    
    def find_elements(self, *args):
        return self.driver.find_elements(*args)
    
    def refresh(self):
        pass
    
    def quit(self):
        pass
    
    def close(self):
        pass
    
    def double_click(self, on_element):
        ActionChains(self.driver).double_click(on_element).perform()
    
    def wait(self, seconds=3):
        sleep(seconds)
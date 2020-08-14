'''
Created on 2020年8月6日

@author: Administrator
'''
from selenium import webdriver
import os
from ui.utils.config import DRIVER_PATH, REPORT_PATH
import time

# executable_path = os.path.join(path)
CHROMEDRIVER_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')
TYPE = {'chrome': webdriver.Chrome, 'firefox': webdriver.Firefox, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'chrome': CHROMEDRIVER_PATH, 'firefox': 'wire'}

class Browser(object):

    def __init__(self, browser_type=None):
        self._type = browser_type.lower()
        if self._type in TYPE:
            self.browser = TYPE[self._type]
        self.driver = None
    
    def get(self, url, maximize_window=True, implicitly_wait=10): 
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self
    
    def save_shot_screen(self, name='screen_shot'):
        day = time.strftime('%Y%m%d')
        screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S')
        screenshot = self.driver.save_shot_screen(os.path.join(screenshot_path, '%s_%s.png' % (name, tm)))
        return screenshot
    
    def add_img_to_report(self, imgs=[]):
        imgs.append(self.driver.get_screenshot_as_base64())
        return True
        
        
if __name__ == '__main__':
#     Browser('chrome').get('http://192.168.10.218/sudoku/')
    webdriver.Chrome(executable_path='D:\\AutoFuncSysTest\\py_jggyun\\ui\\drivers\\chromedriver.exe')
#     print(os.path.split(p))
#     print(os.path.abspath(__file__))
#     print(os.path.dirname(os.path.abspath(__file__)))
#     print(os.path.split(os.path.dirname(os.path.abspath(__file__))))
#     print(os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        
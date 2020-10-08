'''
Created on 2020年8月12日

@author: Administrator
'''
import unittest
from datadriven.utils.selenium_utils import SeleniumUtils
from datadriven.test.common.page import Page

class BaseParpare(unittest.TestCase):

    def setUp(self):
        self.page = Page(browser_type='chrome').get('http://192.168.10.218/sudoku/')
        self.seleniumUtils = SeleniumUtils(page=self.page)
        
    def tearDown(self):
        self.page.close()
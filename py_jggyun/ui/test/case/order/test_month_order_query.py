'''
Created on 2020年8月7日

@author: Administrator
'''
import unittest
from ui.test.page.login import Login
from ui.test.page.month_order_query_page import MonthOrderQueryPage
from ui.test.page.home_page import HomePage


class TestLogin(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        self.page = Login(browser_type="chrome").get('http://192.168.10.218/sudoku/')
        self.page.login('18200455856', 'qyt789', True)
        self.page.wait()
        self.page = HomePage(self.page).enter_module(self, '30天内的订单')

    def testLogin(self):
        self.page = MonthOrderQueryPage(self.page).query()
        
    def tearDown(self):
        self.page.quit()


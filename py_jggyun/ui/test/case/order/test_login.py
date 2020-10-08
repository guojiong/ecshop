'''
Created on 2020年8月7日

@author: Administrator
'''
import unittest
from ui.test.page.login import Login


class TestLogin(unittest.TestCase):
    '''
    classdocs
    '''
    def setUp(self):
        self.page = Login(browser_type="chrome").get('http://192.168.10.218/sudoku/')

    def testLogin(self):
        self.page.login('18200455856', 'qyt789', True)
        self.page.wait()
        
    def tearDown(self):
        self.page.quit()


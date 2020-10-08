'''
Created on 2020年8月7日

@author: Administrator
'''
from datadriven.test.common.base_parpare import BaseParpare
from datadriven.utils.super_actions import SuperActions

class TestLogin(BaseParpare):
    '''
    classdocs
    '''


    def testLogin(self):
        SuperActions().parseExcel(function=r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven\test\xls\xlscase\login.xlsx', caseName='001_LoginSuccessFunction', seleniumUtils=self.seleniumUtils)
        print('数据驱动测试')
        
    def tearDown(self):
        self.page.quit()


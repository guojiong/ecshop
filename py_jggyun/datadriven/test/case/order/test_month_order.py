'''
Created on 2020年8月18日

@author: Administrator
'''
import unittest
from datadriven.utils.super_actions import SuperActions
from datadriven.test.common.base_parpare import BaseParpare


class TestMonthOrder(BaseParpare):


    def testQuery(self):
        SuperActions().parseExcel(function=r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven\test\xls\xlscase\month_order_query.xlsx', caseName='001_LoginSuccessFunction', seleniumUtils=self.seleniumUtils)
        print('数据驱动测试')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

'''
Created on 2020年8月7日

@author: Administrator
'''
import os
from ui.utils.config import REPORT_PATH, BASE_PATH
import time
import unittest
from datadriven.test.case.order.test_login import TestLogin
from HTMLTestRunner_cn import HTMLTestRunner
from emailreport.mailreport import EmailClass

report = os.path.join(REPORT_PATH, 'report_%s.html' % time.strftime('%H-%m-%d_%H-%M-%S'))

def suitebyadd():
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("testLogin"))
    return suite

def suitebypath(*args):
    case_path = os.path.join(BASE_PATH, *args)
    suite = unittest.defaultTestLoader.discover(case_path)
    return suite

# runner = TextTestRunner()
path = ("test", "case", "order")
title="订单中台测试报告"
with open(report, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f, 
        verbosity=2, 
        title=title, 
        description="", 
        is_thread=True, 
        retry=1, 
        save_last_try=True)
    runner.run(suitebyadd())
#     runner.run(suitebypath(*path))
    f.close()
# 打开测试报告
os.startfile(report)

# 发送测试报告
EmailClass().send(title, report)

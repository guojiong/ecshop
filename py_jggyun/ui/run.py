'''
Created on 2020年8月7日

@author: Administrator
'''
import os
from ui.utils.config import REPORT_PATH
import time
import unittest
from ui.test.case.order.test_login import TestLogin
from unittest.runner import TextTestRunner

report = os.path.join(REPORT_PATH, 'report_%s.html' % time.strftime('%H-%m-%d_%H-%M-%S'))

suite = unittest.TestSuite()
suite.addTest(TestLogin)

runner = TextTestRunner
'''
Created on 2020年8月6日

@author: Administrator
'''
import os
from ui.utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
REPORT_PATH = os.path.join(BASE_PATH, 'reports')
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')

class Config(object):

    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data
    
    def get(self, element, index=0):
        return self.config[index].get(element)
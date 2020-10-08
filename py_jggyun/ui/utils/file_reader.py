'''
Created on 2020年8月6日

@author: Administrator
'''
import os
import yaml

class YamlReader(object):
    '''
    classdocs
    '''


    def __init__(self, yamlfilepath):
        if os.path.exists(yamlfilepath):
            self.yamlfilepath = yamlfilepath
        else:
            raise FileNotFoundError('')
        self._data = None
    
    @property
    def data(self):
        if not self._data:
            with open(self.yamlfilepath, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data
    
class ExcelReader():
    pass
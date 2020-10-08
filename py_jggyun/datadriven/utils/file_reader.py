'''
Created on 2020年8月6日

@author: Administrator
'''
import os
import yaml
from xlrd import open_workbook

class YamlReader(object):

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
    
    def __init__(self, excelfilepath):
        if os.path.exists(excelfilepath):
            self.excelfilepath = excelfilepath
        else:
            FileNotFoundError('%s文件不存在' % excelfilepath) 
        self._excel_data = None
        
    @property
    def data(self):
        self._excel_data = open_workbook(self.excelfilepath)
        return self._excel_data
    
    def get_sheet(self, sheet_name_or_index):
        if type(sheet_name_or_index) not in [int, str]:
            print('指定sheet格式不正确')
            assert False
        if type(sheet_name_or_index) == int:
            return self.data.sheet_by_index(sheet_name_or_index)
        else:
            return self.data.sheet_by_name(sheet_name_or_index)
    
if __name__ == '__main__':
    sheet = ExcelReader(r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven\test\xls\xlscase\login.xlsx').getTestCase('001_LoginSuccessFunction')
    
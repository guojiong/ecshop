'''
Created on 2020年8月12日

@author: Administrator
'''
import os
from datadriven.utils.file_reader import ExcelReader
from datadriven.utils.selenium_utils import SeleniumUtils
from selenium.webdriver.common.by import By

class SuperActions(object):
    def getLocateWay(self, locator_way, locator_value):
        if locator_way.upper() == 'ID':
            locator_by = (By.ID, locator_value)
        elif locator_way.upper() == 'NAME':
            locator_by = (By.NAME, locator_value)
        elif locator_way.upper() == 'XPATH':
            locator_by = (By.XPATH, locator_value)
        elif locator_way.upper() == 'CLASSNAME':
            locator_by= (By.CLASS_NAME, locator_value)
        elif locator_way.upper() == 'LINKTEXT':
            locator_by= (By.LINK_TEXT, locator_value)
        elif locator_way.upper() == 'CSS':
            locator_by= (By.CSS_SELECTOR, locator_value)
        elif locator_way.upper() == 'TAGNAME':
            locator_by= (By.TAG_NAME, locator_value)    
        else:
            print('你选择的定位方式：["%s"] 不被支持!' % locator_way)
            assert False
        return locator_by

    def getPageElementLocator(self, locator, page_file_path):
        locator_way = ''
        locator_value = ''
        locator_split = locator.split('.')
        page_sheet = ExcelReader(page_file_path+locator_split[0]+'.xlsx').get_sheet(0)
        for i in range(1,page_sheet.nrows):
            if locator_split[1] == page_sheet.row(i)[0].value:
                locator_way = page_sheet.row(i)[1].value
                locator_value =page_sheet.row(i)[2].value
                break
        if locator_way == ''  and locator_value == '':
            print('获取locator数据失败')
            assert False
        return locator_way, locator_value
    
    def parseExcel(self, function, caseName, seleniumUtils):
        if not os.path.exists(function):
            FileNotFoundError("文件不存在")
        page_file_path = function[0:function.index('xlscase')]+'xlspage/'
        case_sheet = ExcelReader(function).get_sheet(caseName) # 获取sheet
        nrows = case_sheet.nrows # 获取sheet行数
        row0_value = case_sheet.row(0)  # 首行
        
        # 定义动作列的角标
        actionColumnIndex=0
        # 定义元素定位列的角标
        locateColumnIndex = 0;
        # 定义测试数据列的角标
        testDataColumnIndex = 0;
        #动态获取这几个关键列所在位置
        for i in range(0, len(row0_value)):
            if '动作' ==row0_value[i].value:
                actionColumnIndex = i
            if '元素定位' == row0_value[i].value:
                locateColumnIndex = i
            if '测试数据' == row0_value[i].value:
                testDataColumnIndex = i   

        
        # 循环执行测试数据 
        for i in range(1, nrows):
            row_value = case_sheet.row(i)
            if row_value:
                # 动作action准备        
                def open_link():
                    testData = row_value[testDataColumnIndex].value
                    seleniumUtils.get(testData)
                            
                def input_text(): # 输入
                    # 先设置Cell的类型，然后就可以把纯数字作为String类型读进来了
                    if row_value[testDataColumnIndex].ctype==2:
                        testData = '%d' % row_value[testDataColumnIndex].value  # 测试数据
                    else:
                        testData = row_value[testDataColumnIndex].value  # 测试数据
                    locator = row_value[locateColumnIndex].value  # 获取步骤中的元素定位
                    # locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locate_way, locate_value = self.getPageElementLocator(locator, page_file_path) # 找到定位方式、定位值
                    seleniumUtils.type(testData,*self.getLocateWay(locate_way, locate_value))
                    
                def pause():
                    testData = row_value[testDataColumnIndex].value
                    seleniumUtils.pause(testData)
                    
                def wait_element_seconds():
                    pass
                
                def clear_content():
                    locator = row_value[locateColumnIndex].value  
                    locator_way, locator_value = self.getPageElementLocator(locator, page_file_path)
                    seleniumUtils.clear_value(*self.getLocateWay(locator_way, locator_value))
                
                def single_click():
                    # 1、获取用例步骤：测试数据与元素定位信息
                    locator = row_value[locateColumnIndex].value  
                    locator_way, locator_value = self.getPageElementLocator(locator, page_file_path)
                    seleniumUtils.single_click(*self.getLocateWay(locator_way, locator_value))
                    
                
                def validate_text():
                    pass
                            
                def default():
                    print("你输入的操作：["+action+"]不被支持，请自行添加")
                    AssertionError("你输入的操作：["+action+"]不被支持，请自行添加")
                    
                switcher = {
                    '打开链接' : open_link,
                    '导航链接' : open_link,
                    '暂停' : pause,
                    '输入' : input_text,
                    '等待元素' : wait_element_seconds,
                    '清除' : clear_content,
                    '点击' : single_click,
                    '检查文本' : validate_text,
                }
                action = row_value[actionColumnIndex].value
                switcher.get(action, default)()
        

if __name__ == '__main__':
    seleniumUtils = SeleniumUtils()
    SuperActions().parseExcel(r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven\test\xls\xlscase\login.xlsx', '001_LoginSuccessFunction', seleniumUtils)
    

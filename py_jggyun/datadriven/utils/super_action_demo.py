'''
Created on 2020年8月12日

@author: Administrator
'''
import os
from datadriven.utils.file_reader import ExcelReader
from datadriven.utils.selenium_utils import SeleniumUtils

class SuperActions(object):

    def getPageElementLocator(self):
        pass
    
    def parseExcel(self, function, caseName, seleniumUtilss):
        if not os.path.exists(function):
            FileNotFoundError("文件不存在")
        page_file_path = os.path.join(function[0, function.index('xlscase')], 'xlspage')
        case_sheet = ExcelReader(function).getTestCase(caseName) # 获取sheet
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
                    testData = row_value[testDataColumnIndex].value;
                    seleniumUtilss.get(testData);
                    break;
                            
                def input(): # 输入
                    # 先设置Cell的类型，然后就可以把纯数字作为String类型读进来了
                    testData = row_value[testDataColumnIndex].value; # 测试数据
                    locator = row_value[locateColumnIndex].value; # 获取步骤中的元素定位
                    # locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = self.getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0], page_file_path); # 找到定位方式、定位值
                    seleniumUtilss.type(getLocateWay(locateSplit[0], locateSplit[1]), testData);
                    break;
                            
                def click(): # 点击
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtilss.click(getLocateWay(locateSplit[0], locateSplit[1]));
                    break;
                            
                def click_btn(): # 点击 - 按钮":click_btn
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtilss.clickParent(getLocateWay(locateSplit[0], locateSplit[1]));
                    break;
                            
                def pause(): # 暂停": pause
                    # 先设置Cell的类型，然后就可以把纯数字作为String类型读进来了
                    testData = row_value[testDataColumnIndex].value;
                    seleniumUtilss.pause(testData);
                    break;
                            
                def wait(): # 等待元素
                    //先设置Cell的类型，然后就可以把纯数字作为String类型读进来了
                    row.getCell(testDataColumnIndex).setCellType(Cell.CELL_TYPE_STRING);
                    testData = row.getCell(testDataColumnIndex).getStringCellValue();
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtils.waitForElementToLoad(Integer.parseInt(testData), getLocateWay(locateSplit[0], locateSplit[1]));
                    break;
                            
        #         def "查找元素(尝试3次)":
        #                     //先设置Cell的类型，然后就可以把纯数字作为String类型读进来了
        #                     row.getCell(testDataColumnIndex).setCellType(Cell.CELL_TYPE_STRING);
        #                     testData = row.getCell(testDataColumnIndex).getStringCellValue();
        #                     locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
        #                     //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
        #                     locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
        #                     seleniumUtils.FindElementUtil3TimesTry(Integer.parseInt(testData), getLocateWay(locateSplit[0], locateSplit[1]));
        #                     break;
                            
                def clear_content(): # 清除
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtils.clear(getLocateWay(locateSplit[0], locateSplit[1]));
                    break;
                            
                def validate_content: # 检查文本
                    testData = row.getCell(testDataColumnIndex).getStringCellValue();
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtils.isTextCorrect(seleniumUtils.getText(getLocateWay(locateSplit[0], locateSplit[1])), testData);
                    break;
                            
                def enter_tab: # 进入Tab
                    # 需要改进，第二个窗口的driver问题
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    # locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtils.switchNewWindow(getLocateWay(locateSplit[0], locateSplit[1]));
                    break;
                            
                def js_click: # 执行JS点击
                    locator = row.getCell(locateColumnIndex).getStringCellValue(); # 获取步骤中的定位
                    # locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    seleniumUtils.executeJS("arguments[0].click();", seleniumUtils.findElementBy(getLocateWay(locateSplit[0], locateSplit[1])));
                    break;    
                            
                def refresh: # 刷新页面
                    seleniumUtilss.refresh();
                    break;    
                            
                def forward: # 前进页面
                    seleniumUtilss.forward();
                    break;
                            
                def back: # 后退页面
                    seleniumUtilss.back();
                    break;
                    
                def upfile: # 上传文件
                    testData = row.getCell(testDataColumnIndex).getStringCellValue();
                    String uploadValues[] = testData.split(",");
                    seleniumUtils.handleUpload(uploadValues[0], new File(uploadValues[1]));
                    break;
                    
                def validate_home_menu_content(): # 验证首页菜单栏文本
                    locator = row.getCell(locateColumnIndex).getStringCellValue();//获取步骤中的定位
                    //locator.split("\\.")[0]分离出页面名称，比如HomePage.我的单据，提取出HomePage
                    locateSplit = getPageElementLocator(sheet, i, locateColumnIndex,locator.split("\\.")[0]);
                    testData = row.getCell(testDataColumnIndex).getStringCellValue();
                    String menus[] = testData.split("，");
                    for (int i1 = 0; i1 < menus.length; i1++) {
                        seleniumUtils.isTextCorrect(seleniumUtils.findElementsBy(getLocateWay(locateSplit[0], locateSplit[1])).get(i1).getText().trim().toLowerCase(), menus[i1].toLowerCase());
                    }
                            
                            break;
                            
                def interface_form_post_json(): # 接口Post - Json' 
                    try {
                        testData = row.getCell(testDataColumnIndex).getStringCellValue();//{url=http://xxxx, json={}}
                        JSONObject jsonObj = (JSONObject)(new JSONParser().parse(testData));
                        seleniumUtils.httpPostWithJson(jsonObj.getString("url"), jsonObj.getString("json"));
                    } catch (ParseException e) {
                        e.printStackTrace();
                    }
                            
                def default():
                    print("你输入的操作：["+action+"]不被支持，请自行添加");
                    AssertionError("你输入的操作：["+action+"]不被支持，请自行添加")
                    
                switcher = {
                    '打开链接' : open_link,
                    '导航链接' : open_link,
                    '输入' : input,
                    '点击' : click,
                    '点击 - 按钮' : click_btn,
                    '暂停' : pause,
                    '等待元素' : wait_element_seconds,
                    '清除' : clear_content,
                    '检查文本' : validate_content,
                    '进入Tab' : enter_tab,
                    '执行JS点击' : js_click,
                    '刷新页面' : refresh,
                    '前进页面' : forward,
                    '后退页面' : back,
                    '上传文件' : upfile,
                    '验证首页菜单栏文本' : validate_home_menu_content，
                    '接口Post - Json' : interface_form_post_json
                }
                action = row_value[actionColumnIndex].value
                switcher.get(action, default)()
        

if __name__ == '__main__':
    seleniumUtilss = SeleniumUtils()
    SuperActions().parseExcel(r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven\test\xls\xlscase\login.xlsx', '001_LoginSuccessFunction', seleniumUtils)
    
                        
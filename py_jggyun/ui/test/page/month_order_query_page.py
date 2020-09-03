'''
Created on 2020年8月18日

@author: Administrator
'''
from ui.test.common.page import Page
from selenium.webdriver.common.by import By

class MonthOrderQueryPage(Page):
    '''
    classdocs
    '''
#功能按钮        
    loc_query_btn = (By.XPATH, "//span[contains(text(), '查 询')]/..")
    loc_reset_btn = (By.XPATH, "//span[contains(text(), '重 置')]/..")
    loc_morder_btn = (By.XPATH, "//span[contains(text(), '手工订单')]/..")
    loc_rorder_btn = (By.XPATH, "//span[contains(text(), '补 单')]/..")
    loc_export_btn = (By.XPATH, "//span[contains(text(), '导 出')]/..")
# 查询条件        
    loc_order_no_condition = (By.ID, 'orderNo')
    loc_start_time_condition = (By.XPATH, "//input[@placeholder='开始日期']")
    loc_end_time__condition = (By.XPATH, "//input[@placeholder='结束日期']")
# 数据列表        
    loc_orgName_table = (By.XPATH, "//div[@ref='eCenterViewport']//div[@col-id='orgName']")

    def query(self, order_no=None, start_time=None, end_time=None):
        if order_no:
            self.find_element(*self.loc_order_no_condition).send_keys(order_no)
        if start_time:
            self.find_element(*self.loc_start_time_condition)
        if end_time:
            self.find_element(*self.loc_end_time__condition)
            
        self.find_element(*self.loc_query_btn).click()
        
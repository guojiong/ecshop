'''
Created on 2020年8月7日

@author: Administrator
'''
from ui.test.common.page import Page
from selenium.webdriver.common.by import By


class HomePage(Page):
    
    loc_order_mgs = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'订单管理')]")
    loc_o2o_mgs     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'O2O订单管理')]")
    loc_process_order_mgs = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'进行中订单')]")
    loc_month_order = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'30天内的订单')]")
    loc_month_ago_order = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'30天前的订单')]")
    loc_pick_timeout_report = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'拣货超时报表')]")
    loc_order_evalute_query = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'订单评价查看')]")
    loc_test_tools     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'订单功能测试工具')]")
    loc_abnormal_order     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'异常订单查询')]")
    loc_audit_order     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'订单审核')]")
    loc_order_log     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'订单日志')]")
    loc_after_sale     = (By.XPATH, "//div[@class='ant-layout-sider-children']//span[contains(text(),'售后订单')]")

    def enter_module(self, module):
        if module == '订单管理':
            self.find_element(*self.loc_order_mgs).click()           #'订单管理'
        if module == 'O2O订单管理':
            self.find_element(*self.loc_o2o_mgs).click()             #'O2O订单管理'
        if module == '进行中订单':
            self.find_element(*self.loc_process_order_mgs).click()   #'进行中订单'
        if module == '30天内的订单':
            self.find_element(*self.loc_month_order).click()         #'30天内的订单'
        if module == '30天前的订单':
            self.find_element(*self.loc_month_ago_order).click()     #'30天前的订单'
        if module == '拣货超时报表':
            self.find_element(*self.loc_pick_timeout_report).click()  #'拣货超时报表'
        if module == '订单评价查看':
            self.find_element(*self.loc_order_evalute_query).click()  #'订单评价查看'
        if module == '订单功能测试工具':
            self.find_element(*self.loc_test_tools).click()         # '订单功能测试工具'
        if module == '异常订单查询':
            self.find_element(*self.loc_abnormal_order).click()      #'异常订单查询'
        if module == '订单审核':
            self.find_element(*self.loc_audit_order).click()         #'订单审核'
        if module == '订单日志':
            self.find_element(*self.loc_order_log).click()           #'订单日志'
        if module == '售后订单':
            self.find_element(*self.loc_after_sale).click()          #'售后订单'
        
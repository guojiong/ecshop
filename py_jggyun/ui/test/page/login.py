'''
Created on 2020年8月7日

@author: Administrator
'''
from ui.test.common.page import Page
from selenium.webdriver.common.by import By


class Login(Page):
    
    loc_username = (By.ID, 'userName')
    loc_password = (By.ID, 'password')
    loc_login_btn = (By.XPATH, '//button[@type="submit"]')
    loc_validate_code = (By.XPATH, "//input[@placeholder='请输入验证码']")

    def login(self, username, password, validate=False):
        self.find_element(*self.loc_username).send_keys(username)
        self.find_element(*self.loc_password).send_keys(password)
        self.find_element(*self.loc_login_btn).click()
        if validate:
            self.find_element(*self.loc_validate_code).send_keys('111111')
            self.find_element(*self.loc_login_btn).click()
        print('成功')

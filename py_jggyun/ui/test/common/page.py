'''
Created on 2020年8月7日

@author: Administrator
'''
from ui.test.common.pageframe import PageFrame

class Page(PageFrame):
    
    def delete(self,sql):
        pass
    
if __name__ == '__main__':
    Page(browser_type="chrome").get("http://192.168.10.218/sudoku/")
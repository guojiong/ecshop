'''
Created on 2020年8月11日

@author: Administrator
'''
from ui.utils.config import Config

class DBConnect(object):
    '''
    classdocs
    '''


    def __init__(self, database=""):
        data_info = Config().get(database)
        
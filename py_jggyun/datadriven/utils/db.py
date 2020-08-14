'''
Created on 2020年8月11日

@author: Administrator
'''
from ui.utils.config import Config
import pymysql

class DBConnect(object):
    '''
    classdocs
    '''


    def __init__(self, database='test-qyt-8600'):
        data_info = Config().get(database)
        self.ip = data_info.get('host')
        self.port = data_info.get('port')
        self.user = data_info.get('user')
        self.password = data_info.get('password')
        self.mysql_conn = None
        self.instance
#         logger.info("数据库连接信息：{}".format(data_info))
        print("数据库连接信息：{}".format(data_info))
    
    @property
    def instance(self):
        self.mysql_conn = pymysql.connect(
            host=self.ip,
            port=self.port,
            user=self.user,
            password=str(self.password),
            charset='utf8')
    
    def del_conn(self):
        if self.mysql_conn:
            self.mysql_conn.close()
        
    def query(self,sql):
        if not self.mysql_conn:
            self.instance
        cursor = self.mysql_conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def delete(self, sql):
        if not self.mysql_conn:
            self.instance
        cursor = self.mysql_conn.cursor()
        cursor.execute(sql)
        self.mysql_conn.commit()
        cursor.close()
    
if __name__ == '__main__':
    print(DBConnect('test-agent-8600').query("select * from order.order_info where order_No = '1573184510193806910'"))
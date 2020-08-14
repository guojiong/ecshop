'''
Created on 2020年8月11日

@author: Administrator
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time


class EmailClass():
    def __init__(self):
        # 邮件发送方地址
        self.fromaddr = 'jiong.guo@qyt1902.com'
        self.frompasswd = 'Qyt0304.' # 部分邮件为授权码
        # 邮件接收方地址
        self.toaddr = ['328905689@qq.com', 'jiong.guo@qyt1902.com']  # []包裹，可群发
        self.message = MIMEMultipart('mixed')
    
    def send_content(self, title, report):
        self.message['Subject'] = title
        self.message['From'] = self.fromaddr
        self.message['To'] = self.toaddr[0]
        with open(report, 'rb') as f:
            content = f.read()
        self.message.attach(MIMEText(content, 'html', 'utf-8'))
        self.html = self.addAttach(report, '%s_%s.html' % (title, time.strftime('%H-%m-%d_%H-%M-%S')))
        self.message.attach(self.html)
        
    def send(self, title, apath):
        self.send_content(title, apath)
        try:
            server = smtplib.SMTP('smtp.exmail.qq.com')
            server.login(self.fromaddr, self.frompasswd)
            server.sendmail(
                from_addr=self.fromaddr, 
                to_addrs=','.join(self.toaddr), 
                msg=self.message.as_string())
            print('Send Report Success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error', e)
    
    # 添加附件
    def addAttach(self, apath, filename):
        with open(apath, 'rb') as f:
            attach = MIMEBase('application','utf-8')
            attach.set_payload(f.read())
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            encoders.encode_base64(attach)
            return attach
            
if __name__ == '__main__':
    EmailClass().send(r"Order Test Report", r'D:\AutoFuncSysTest\mytest_rep\py_jggyun\datadriven/reports/report_17-08-14_17-25-54.html')
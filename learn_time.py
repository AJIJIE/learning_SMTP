#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import time
n=0
while n<10:
    n=n+1

    # 第三方 SMTP 服务
    mail_host="smtp.126.com"  #设置服务器
    mail_user="hahanihaoy@126.com"    #用户名
    mail_pass="asd123456"   #口令(第三方登录口令)


    sender = 'hahanihaoy@126.com'
    receivers = ['2408584647@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('Python 邮件发送测试...')
    message['From'] = sender
    # message['To'] = Header('ceshi')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = subject


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)

        smtpObj.sendmail(sender,receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error"
    time.sleep(5)
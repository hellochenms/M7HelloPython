#!/usr/bin/python
# -*- coding:utf-8 -*-

### sendemail.py
### chenms
### 2014-8-19

import smtplib
import email.utils
from email.mime.text import MIMEText

recipient = 'adf_test_1@126.com'
user = 'adf_test_0@126.com'
psw = 'chenmeisong1986'

msg = MIMEText('这又是消息体', 'plain', 'utf-8')
msg['To']= email.utils.formataddr(('Recipient', recipient))
msg['From'] = email.utils.formataddr(('Author', user))
msg['Subject'] = '这又是标题'
#msg['Accept-Language']='zh-CN'
#msg['Accept-Charset']='utf-8,ISO-8859-1'

server = smtplib.SMTP()
server.set_debuglevel(True)
server.connect('smtp.126.com')
server.login(user, psw)
try:
    server.sendmail(user, [recipient], msg.as_string())
finally:
    server.quit()


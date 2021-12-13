import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
1-进入qq邮箱--设置--打开stmp邮件服务-会获得一个密码
"""


def send_msg():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('443765159@qq.com', 'ihnrtwcajadtcaji')  #
    message = MIMEText('ceshi', 'utf-8')
    message['from'] = Header('nidie', 'utf-8')
    smtp.sendmail('443765159@qq.com', '443765159@qq.com', message.as_string())
    smtp.quit()


def send_xsl():
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('443765159@qq.com', 'ihnrtwcajadtcaji')  #
    message = MIMEMultipart()
    message['from'] = Header('nidie', 'utf-8')
    message.attach(MIMEText('ceshi'))
    att1 = MIMEText(open('1.xls', 'rb').read(), 'base64', 'uft-8')
    att1.add_header('Content-Disposition', 'attachment', filename='1.xls')
    message.attach(att1)
    smtp.sendmail('443765159@qq.com', '443765159@qq.com', message.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_xsl()

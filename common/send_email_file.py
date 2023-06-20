import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
class Email:
    def sendTest(self,file):
        smtpserver='smtp.qq.com'
        msg=MIMEMultipart('mixed')
        # 发送方邮箱地址
        msg_from='916215503@qq.com'
        # 发送方QQ邮箱授权码，不是QQ邮箱密码
        password='uqucbqwxkljqbffj'
        # 可添加多个收件人邮箱
        receives=['zhuyu@skillbox.cn']
        # 主题
        subject='自动化测试报告'
        # 正文
        content='打开附件查看详情信息'
        msg['Subject']=Header(subject,'utf-8')
        msg['From']=msg_from
        msg['TO']=",".join(receives)
        # 构造文字内容
        text_plain=MIMEText(content,'html','utf-8')
        msg.attach(text_plain)
        f=open(file,'rb')
        mail_body=f.read()
        f.close()
        text_attr=MIMEText(mail_body,'base64','utf-8')
        text_attr['Cotent-Type']='application/octet-stream'
        text_attr['Content-Disposition']='attachment;filename="report.html"'
        msg.attach(text_attr)
        smtp=smtplib.SMTP_SSL(smtpserver,465)
        smtp.helo(smtpserver)
        smtp.ehlo(smtpserver)
        smtp.login(msg_from,password)
        print('开始发送邮件')
        smtp.sendmail(msg_from,receives,msg.as_string())
        smtp.quit()
        print('已发送邮件')
if __name__ == '__main__':
    e=Email()
    report=r'C:\Users\91621\PycharmProjects\lxp项目\TestResult\Report\测试报告.html'
    e.sendTest(report)

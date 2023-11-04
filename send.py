from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发件人邮箱
sender_qq = '2194315388@qq.com'
pwd = 'svmgbbqbwtnteaii'
# 收件人列表
receiver_list = ['2919128969@qq.com', 'xxx@qq.com', 'xxx@qq.ocm']

def Send_Email(list_n,list_re):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # 创建SMTP对象
    smtp = SMTP_SSL(host_server)  # SSL登录
    # 登录邮箱
    smtp.login(sender_qq, pwd)
    # 循环发送邮件给每个收件人
    for i in range(3):
        # 邮件标题
        mail_title = f'{list_n[i]}同学成绩单'
        # 邮件正文内容
        mail_content = list_re[i]
        # 初始化一个邮件主体
        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq
        msg["To"] = receiver_list[i]
        # 邮件正文内容
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
        # 发送邮件
        smtp.sendmail(sender_qq, receiver_list[i], msg.as_string())
    # 退出SMTP会话
    smtp.quit()
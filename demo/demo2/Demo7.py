# 发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import time

# sender = "1063202628@qq.com"
# receivers = ['1063202628@qq.com']   # 接收邮箱
#
# # 第三方 SMTP 服务
# mail_host="smtp.qq.com"  #设置服务器
# mail_user="1063202628@qq.com"    #用户名
# mail_pass="19980325lzlll0.+"   #口令
#
# # 三个参数，第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
# message = MIMEText('python邮件发送测试','plain','utf-8')
# message['From'] = Header("菜鸟教程","utf-8")    # 发送者
# message["To"] = Header("测试","utf-8")    # 接收者
#
# subject = 'python SMTP 邮件测试'
# message['Subject'] = Header(subject,'utf-8')
#
# try:
#     smtpobj = smtplib.SMTP()
#     smtpobj.connect(mail_host,25)
#     smtpobj.login(mail_user,mail_pass)
#     smtpobj.sendmail(sender,receivers,message.as_string())
#     print('邮件发送成功')
# except smtplib.SMTPException:
#     print('error:无法发送邮件')
my_sender = '2368864108@qq.com'  # 发件人邮箱账号
my_pass = 'actbmgwmcpzfdicj'  # 发件人邮箱密码
my_user = '1063202628@qq.com'  # 收件人邮箱账号   2426874265 阿慧   610725928 凌峰   1932231714 刘宇

def mail():
    ret = True
    try:
        mail_msg = "胖子，你好，我从未来穿越过来的，以后的你是一个万亿富翁，对全球具有很大的影响力，可惜人往高处走，就有人想要害你，" \
                   "我这次穿越过来是想帮你找到那些害你的人，解决他们。我也不要你多大的报酬，你现在给我一万就行，" \
                   "我就去帮你把那些未来要还你的人解决掉"
        # 碧水寒潭之上，出尘如仙，傲世而立，恍如仙子下凡，令人不敢逼视。一袭紫衣临风而飘'
        #  '，一头长发倾泻而下，紫衬如花，长剑胜雪，说不尽的美丽清雅，高贵绝俗，姑娘，这是你吗？
        msg = MIMEText(mail_msg, 'plain', 'utf-8')
        msg['From'] = formataddr(["陌生人", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "来自朋友的问候"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


for i in range(1,2):

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
    time.sleep(3)
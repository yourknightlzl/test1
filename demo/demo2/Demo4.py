import requests
from bs4 import BeautifulSoup
import chardet
#打开我存放链接的文本，使用readlines方法读取文本内容，返回的是一个list列表，每一行为列表中的一项
with open('info.txt') as info:
     link = info.readlines()
#打开一个文本文件，存放抓取到的职位要求，编码格式设为utf-8
job = open('job.txt', 'a', encoding='UTF-8')
header = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                   'Safari/537.36',
     'Connection': 'keep-alive',
     }

for each in link:
    # info.txt中存放的信息是职位名 + 链接：Web前端开发工程师 https://*****
    # 所以先对列表中的每一项，也就是说一个字符串调用find方法，搜索关键字http,返回的是一个整数，表示的是字符串中http开头h的索引值
    index = each.find('http')
    # 利用这个索引值，可以获取字符串中链接的部分
    url = each[index:]
    pageConnect = requests.get(url, headers=header)
    pageConnect.encoding = chardet.detect(pageConnect.content)['encoding']
    page = pageConnect.text
    soup = BeautifulSoup(page, 'html.parser')
    # 所有的职位要求是放在一个div中，它的样式类为class=bmsg job_msg inbox,div中的p标签包含具体的信息，返回的是一个list列表
    div = soup.select('div.bmsg.job_msg.inbox p')
    # 经过测试发现，最后2个p标签存放着关键字，所以去掉
    jobInfo = div[:-2]
    for eachInfo in jobInfo:
        # 每个列表项存放着如<p>***</P>的bs4.element.Tag，要获取其中文字部分，要使用.string方法
        print(eachInfo.string, file=job)

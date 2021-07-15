#爬取职位链接这一步用到了3个库
import requests
from bs4 import BeautifulSoup
import chardet

f = open('info.txt', 'a') # f是我存储爬取信息的文本文件，使用追加模式，就是说后面写入的信息会放在已有的信息后面，这样就不会把之前的信息覆盖掉
url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF,2,{}.html?' \
      'lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&' \
      'lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&' \
      'specialarea=00&from=&welfare=#top' # url里面关乎页面跳转的数字我用{}占位，后面可以通过format函数动态替换
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 '
                  'Safari/537.36',
    'Connection': 'keep-alive',
    }# header是为了把爬虫伪装的像是正常的访问。

#for循环结构，循环10次，也就是说爬取10页上面的职位链接
for i in range(11):
    # 用requests库的get方法与服务器进行链接，返回一个requests.models.Response的类
    pageConnect = requests.get(url.format(i), headers=header)
    # 用chardet库的detect方法获取网页编码格式，返回的是dict字典，具体的编码格式在encoding这个键对应的值中
    pageConnect.encoding = chardet.detect(pageConnect.content)['encoding']
    # 设置好编码格式后，用text方法把Response这个类转化为字符串供beautifulSoup处理
    page = pageConnect.text
    # 使用BeautifulSoup函数把page字符串转化为一个BeautifulSoup对象，lxml是解析器的类型
    soup = BeautifulSoup(page, 'html.parser')
    # 使用BeautifulSoup对象的select方法，可以用css选择器把存放有职位链接的a标签选出来
    # 每一个a标签都是放在class=el的div标签下class=t1的p标签下
    aLabel = soup.select('div.el > p.t1 a')
    # 每一个搜索结果页有50个职位，也就有50个a标签，通过for循环，获取每个a标签的title属性，href属性
    # title属性存放了职位名称，我可以通过职位名称把不是我需要的职位链接筛选出去
    # href属性存放了每一个职位的链接
for each in aLabel:
    # 把这些信息存放到f也就是info.txt这个文本中
    print(each['title'], each['href'],file = f)
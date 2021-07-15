# 公共使用的功能类
import random


# 产生随机5个字母或数字的字符串
def randomNum_5():
    checkcode = ''
    for i in range(10):  # 循环4次输出四个字符
        index = random.randrange(0, 10)
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97, 122))  # 小写字母ASCII值为：97~122
        elif index + 1 == i:
            checkcode += chr(random.randint(65, 90))  # 大写字母ASCII值为：65~90
        else:
            checkcode += str(random.randint(0, 9))  # 随机输出数字0~9中的1个
    return checkcode.upper()





# 判断元素是否存在
def isexists(xpathStr, driver):
    try:
        driver.find_element_by_xpath(xpathStr)
        flag = True
    except:
        flag = False
    return flag

# 判断元素是否存在
def elementExists(page,element):
    boolstr = page.is_visible(element)
    return boolstr


def determineDigital(logisticsNumber):
    strNum = ''
    for i in range(len(logisticsNumber)):
        # 判断每个字符是否为数字，是的话拼接起来
        if logisticsNumber[i].isdigit():
            strNum += logisticsNumber[i]
        else:
            continue
    return strNum

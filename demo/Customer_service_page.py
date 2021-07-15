# 客服页面
from selenium import webdriver
import time
import DataBaseConnection


# 1.查看订单，并返回订单的物流编号
def selectOrderAndLogisticsNumber(driver):
    # 点击订单
    driver.find_element_by_xpath('//*[@id="app"]/section/header/div[2]/ul/li[2]').click()

    # 从mysql数据库获取指定订单号的订单进行搜索
    orderData = DataBaseConnection.selectOrder()
    str = orderData["订单号"]
    print("本次订单机型为：", orderData["umname"], "订单号为：", orderData["订单号"])
    time.sleep(1)

    # 输入订单号
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/div[1]/div[2]/section/header/div[2]/div[2]/input').send_keys(str)
    # 点击搜索
    driver.find_element_by_xpath('//*[@id="app"]/section/main/div[1]/div[2]/section/header/div[2]/button[1]').click()
    time.sleep(1)
    # 点击订单进入订单详情页面
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/div[1]/div[2]/section/main/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/div').click()

    time.sleep(1)
    # 获取订单物流编号
    logisticsNumber = driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/div[1]/div[2]/section/main/div[2]/div[1]/div[2]/div[4]/p[2]/span[1]/span').text
    strNum = ''
    for i in range(len(logisticsNumber)):
        # 判断每个字符是否为数字，是的话拼接起来
        if logisticsNumber[i].isdigit():
            strNum += logisticsNumber[i]
        else:
            continue
    return strNum

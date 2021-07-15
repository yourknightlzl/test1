# 客服页面
from selenium import webdriver
import time
import DataBaseConnection

# 打开谷歌浏览器驱动
driver = webdriver.Chrome()
# 打开指定页面
driver.get("https://test.sosotec.com/test/fastlogin/index.html?sign=03DE3F5C58078EBD5F4E4F1E067023E9")

time.sleep(1)
# 选择客服
driver.find_element_by_xpath('//*[@id="module"]/div[1]/button[5]').click()

# 获取当前窗口的句柄
currentWin = driver.current_window_handle

# 选择一个用户登录
driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[2]/a/button').click()
time.sleep(2)

"""
#获取所有窗口的句柄
handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        driver.close()
        driver.switch_to.window(handle)
"""

# 获取所有窗口的句柄
handles = driver.window_handles
for handle in handles:
    if currentWin == handle:
        continue
    else:
        # 将driver与新的页面绑定起来
        driver.switch_to.window(handle)
        # print(driver)

# 点击订单
driver.find_element_by_xpath('//*[@id="app"]/section/header/div[2]/ul/li[2]').click()

# 从mysql数据库获取指定订单号的订单进行搜索
orderData = DataBaseConnection.selectData()
str = orderData["订单号"]
print("订单号为：", str)
time.sleep(1)

# 输入订单号
driver.find_element_by_xpath('//*[@id="app"]/section/main/div[1]/div[2]/section/header/div[2]/div[1]/input').send_keys(
    str)
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
print(logisticsNumber, "长度为：", len(logisticsNumber))

strNum = ''
for i in range(len(logisticsNumber)):
    # 判断每个字符是否为数字，是的话拼接起来
    if logisticsNumber[i].isdigit():
        strNum += logisticsNumber[i]
    else:
        continue

time.sleep(2)
driver.quit()

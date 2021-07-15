# 登录首页
from selenium import webdriver
import time

# 1.进入首页
def loginPage(driver):
    # 打开指定页面
    driver.get("https://test.sosotec.com/test/fastlogin/index.html?sign=03DE3F5C58078EBD5F4E4F1E067023E9")
    return driver

# 2.选择客服端登录
def loginCustomerServicePage(driver):
    time.sleep(1)
    # 选择客服
    driver.find_element_by_xpath('//*[@id="module"]/div[1]/button[5]').click()

    # 选择一个用户登录
    driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[2]/a/button').click()
    # 登录进入之后等待1秒
    time.sleep(1)

# 3.登录仓库管理页面
def loginWarehousePage(driver):
    # 选择仓库系统
    driver.find_element_by_xpath('//*[@id="module"]/div[1]/button[7]').click()

    # 选择一个用户登录
    driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[2]/a/button').click()
    # 登录进入之后等待1秒
    time.sleep(1)

# 4.登录到MQC—质检中心
def loginQualityInspectionCenterPage(driver):
    # 选择MQC—质检中心
    driver.find_element_by_xpath('//*[@id="module"]/div[1]/button[1]').click()
    # 选择一个用户登录
    driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[2]/a/button').click()
    # 登录进入之后等待1秒
    time.sleep(1)

# 5.登录到QTO-质检类目
def loginQualityInspectionCategoryPage(driver):
    # 选择MQC—质检中心
    driver.find_element_by_xpath('//*[@id="module"]/div[1]/button[3]').click()
    # 选择一个用户登录
    driver.find_element_by_xpath('//*[@id="list"]/tr[1]/td[2]/a/button').click()
    # 登录进入之后等待1秒
    time.sleep(1)

# 转句柄
def switchHandle(driver,currentWin):
    # 获取所有窗口的句柄
    handles = driver.window_handles
    for handle in handles:
        if currentWin == handle:
            continue
        else:
            # 将driver与新的页面绑定起来
            driver.switch_to.window(handle)
    return driver


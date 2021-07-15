# 仓库管理页面
import time
import DataBaseConnection


# 1.进入到货窗口
def thearrivalofthegoods(driver, logisticsNumber):
    # 点击到货
    driver.find_element_by_xpath('//*[@id="app"]/section/header/div[2]/ul/li[3]').click()
    time.sleep(1)
    # 选择编码打印
    driver.find_element_by_xpath('//*[@id="app"]/section/main/section/aside/div/ul/li[12]/a').click()
    time.sleep(1)
    # 因为时间控件，所以手动输入时间
    # 获取系统当前时间
    newtime = time.strftime("%Y-%m-%d", time.localtime())
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/form/div/div[1]/div/div/input').send_keys(
        newtime)
    # 输入打印数量
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/form/div/div[2]/div/div/input').send_keys(
        '1')
    # 输入打印份数
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/form/div/div[3]/div/div/input').send_keys(
        '1')
    # 确定打印
    driver.find_element_by_xpath('//*[@id="app"]/section/main/section/main/section/main/div/div/div/button[2]').click()
    # 点击回收入库

    driver.find_element_by_xpath('//*[@id="app"]/section/main/section/aside/div/ul/li[2]/a').click()
    time.sleep(1)
    # 输入快递单号
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/div[1]/div[1]/input').send_keys(
        logisticsNumber)
    # 点击搜索按钮
    driver.find_element_by_xpath('//*[@id="app"]/section/main/section/main/section/main/div/div/div[1]/button').click()
    # 获取打印编码
    printCode = DataBaseConnection.printCode()
    code = printCode['code']
    # 输入打印编码
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/div[1]/div[1]/input').send_keys(
        code)
    # 点击提交
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/div[3]/button[2]').click()
    time.sleep(1)
    # 提交成功或者失败都返回此订单的库存编号
    inventorYnumber = driver.find_element_by_xpath(
        '//*[@id="app"]/section/main/section/main/section/main/div/div/div[2]/div[3]/table/tbody/tr/td[2]/div').text
    print("库存编号为：", inventorYnumber)
    return inventorYnumber

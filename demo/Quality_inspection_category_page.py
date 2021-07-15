# 质检类目
import time
import DataBaseConnection
import Functionalclass

# 核价
def chooseNuclearPrice(driver,inventorYnumber):

    # 选择核价
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/header/div[2]/ul/li[7]').click()
    time.sleep(1)
    # 选择阿曼里
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div/section/main/section/main/section/aside/ul/li[2]/a').click()

    # 输入库存编号
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div/section/main/section/main/section/main/div[1]/div[2]/div[2]/input').send_keys(
        inventorYnumber)

    # 点击搜索
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div/section/main/section/main/section/main/div[1]/div[2]/button[1]').click()

    time.sleep(60)

    # 点击进入核价
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div/section/main/section/main/section/main/div[2]/div[3]/table/tbody/tr/td[1]/div/div'
    ).click()

    # 点击小弹窗确定，判断是否存在
    xpathStr2 = '/html/body/div[3]/div/div[3]/button'
    flag1 = Functionalclass.isexists(xpathStr2, driver)
    if flag1:
        driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button').click()
    # time.sleep(0.5)
    # # 获取当前价 //*[@id="app"]/section/div/div/div/div/div[2]/section/div[1]/span[5]/div/input
    # thecurrentprice = driver.find_element_by_xpath(
    #         '//*[@id="app"]/section/div/div/div/div/div[2]/section/div[1]/span[5]/div/input').text
    # print("当前价为：",thecurrentprice)
    # # 推价在当前价的前提下减200
    # pushtheprice = float(thecurrentprice) - 100
    #
    # print("推价为：",pushtheprice)
    # # 清空输入框原来内容
    # driver.find_element_by_xpath(
    #     '//*[@id="app"]/section/div/div/div/div/div[2]/section/div[1]/span[5]/div/input').clear()
    # # 输入推价
    # driver.find_element_by_xpath(
    #     '//*[@id="app"]/section/div/div/div/div/div[2]/section/div[1]/span[5]/div/input').send_keys(pushtheprice)
    #
    # # 确定修改
    # driver.find_element_by_xpath('//*[@id="app"]/section/div/div/div/div/div[2]/section/div[1]/div/button[3]').click()
    #
    # # 弹窗确定
    # sureXpath = "/html/body/div[4]/div/div[3]/button[2]"
    # flag2 = Functionalclass.isexists(sureXpath, driver)
    # if flag2:
    #     driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button').click()
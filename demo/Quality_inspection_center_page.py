# MQC-质检中心
import time
import DataBaseConnection
from selenium.webdriver.common.keys import Keys  # 引入鼠标键盘事件
import Functionalclass


# 1.输入库存编码，回车进入质检
def writePrintCode(driver, inventorYnumber):
    # 输入编码
    driver.find_element_by_id('bcode').send_keys(inventorYnumber)
    # 键盘回车事件
    driver.find_element_by_id('bcode').send_keys(Keys.ENTER)
    time.sleep(1)
    # 小弹窗点击确定，先判断弹窗是否出现
    xpathStr1 = '/html/body/div[4]/div/div[3]/button'
    flag1 = Functionalclass.isexists(xpathStr1, driver)
    if flag1:
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button').click()

    time.sleep(1)
    # 获取随机5位数字符串
    strIMEI = Functionalclass.randomNum_5()

    # 输入IMEI码
    driver.find_element_by_xpath('//*[@id="pane-10"]/div/table/tr[1]/td[1]/div/div/input').send_keys(strIMEI)

    # 切换属性检测
    driver.find_element_by_id('tab-20').click()

    # 获取表格列表tr
    table = driver.find_element_by_xpath('//*[@id="pane-20"]/div/table')
    tr = table.find_elements_by_tag_name("tr")
    print("table下的的tr数量为：", len(tr))
    # 循环
    for n in range(len(tr)):
        if n == 0:  # 第一行是输入IMEI码，剔除
            continue

        # 获取tr下面的div盒子数 //*[@id="pane-20"]/div/table/tr[2]/td[1]
        div = driver.find_element_by_xpath('//*[@id="pane-20"]/div/table/tr[%d]/td[1]' % (n + 1))
        divNum = div.find_elements_by_css_selector('.select-box.clearfix')
        if len(divNum) > 1:  # 大于1则说明该tr下的属性类型有多种可选
            for m in range(len(divNum)):
                driver.find_element_by_xpath(
                    '//*[@id="pane-20"]/div/table/tr[2]/td[1]/div[%d]/div[2]' % (m + 1)).click()
        else:  # 否则就一种属性类型选择
            # 选择手机的最大内存
            nctext = driver.find_element_by_xpath('//*[@id="pane-20"]/div/table/tr[%d]/th' % (n + 1)).text
            if nctext == "内存":
                xpathStr2 = '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[3]' % (n + 1)
                flag2 = Functionalclass.isexists(xpathStr2, driver)
                flag3 = ""
                if flag2:
                    driver.find_element_by_xpath(
                        '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[3]' % (n + 1)).click()
                else:
                    xpathStr3 = '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[2]' % (n + 1)
                    flag3 = Functionalclass.isexists(xpathStr3, driver)
                    if flag3:
                        driver.find_element_by_xpath(
                            '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[2]' % (n + 1)).click()
                    else:
                        driver.find_element_by_xpath(
                            '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[1]' % (n + 1)).click()

            else:
                if nctext == "销售地":
                    driver.find_element_by_xpath(
                        '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[2]' % (n + 1)).click()
                else:
                    driver.find_element_by_xpath(
                        '//*[@id="pane-20"]/div/table/tr[%d]/td[1]/div/div[1]' % (n + 1)).click()
    # 切换外观检测
    driver.find_element_by_id('tab-30').click()
    # 判断是否有原彩需要选择
    xpathStr4 = '//*[@id="pane-30"]/div/table/tr[3]/td[1]/div[1]/div[2]'
    flag4 = Functionalclass.isexists(xpathStr4, driver)
    if flag4:
        driver.find_element_by_xpath('//*[@id="pane-30"]/div/table/tr[3]/td[1]/div[1]/div[2]').click()

    # 选择成色  95新
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div[2]/div[2]/div/div/div[2]/footer/div/div[4]/div[1]/div/input').click()
    time.sleep(0.5)
    xpathStr5 = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
    flag5 = Functionalclass.isexists(xpathStr5, driver)
    if flag5:
       driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[1]/ul/li[2]').click()
    else:
       driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[2]').click()


    # 选择级别  A1
    driver.find_element_by_xpath(
        '//*[@id="app"]/section/div[2]/div[2]/div/div/div[2]/footer/div/div[4]/div[2]/div/input').click()
    xpathStr6 = '/html/body/div[6]/div[1]/div[1]/ul/li[2]'
    time.sleep(0.5)
    flag6 = Functionalclass.isexists(xpathStr6, driver)
    if flag6:
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[2]').click()
    else:
        driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[2]').click()
    # 质检完成
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div[2]/footer/div/div[4]/button[2]').click()

# 主方法，调用
import The_login_page
import Customer_service_page
from selenium import webdriver
import time
import Warehouse_page
import Quality_inspection_center_page
import Quality_inspection_category_page

# 1.先创建浏览器驱动，打开谷歌浏览器驱动
driver = webdriver.Chrome()


def process(driver):
    # 2.进入首页
    driver.maximize_window()
    driver = The_login_page.loginPage(driver)
    # 获取当前窗口的句柄
    currentWin = driver.current_window_handle

    # 3.选择客服登录
    The_login_page.loginCustomerServicePage(driver)

    # 4.转句柄
    driver = The_login_page.switchHandle(driver, currentWin)
    # 5.根据指定订单号查询订单获取物流编号
    logisticsNumber = Customer_service_page.selectOrderAndLogisticsNumber(driver)

    # 6.返回到登录首页
    driver.switch_to.window(currentWin)

    # 7.登录仓库管理页面，转句柄到仓库页面
    The_login_page.loginWarehousePage(driver)
    driver = The_login_page.switchHandle(driver, currentWin)

    # 8.选择到货并打印编码，入库，并获取库存编码
    inventorYnumber = Warehouse_page.thearrivalofthegoods(driver, logisticsNumber)

    # 9.返回到首页
    driver.switch_to.window(currentWin)

    # 10.登录到MQC-质检中心,转句柄
    The_login_page.loginQualityInspectionCenterPage(driver)
    driver = The_login_page.switchHandle(driver, currentWin)

    # 11.输入库存编码，回车进入质检
    Quality_inspection_center_page.writePrintCode(driver, inventorYnumber)

    # 12.返回到首页
    driver.switch_to.window(currentWin)

    # 13.选择QTO-质检类目登录，转句柄
    The_login_page.loginQualityInspectionCategoryPage(driver)
    driver = The_login_page.switchHandle(driver, currentWin)

    # 14.输入库存编号进行核价
    Quality_inspection_category_page.chooseNuclearPrice(driver, inventorYnumber)
    time.sleep(20)
    driver.quit()


if __name__ == "__main__":
    process(driver)

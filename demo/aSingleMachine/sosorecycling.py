from aSingleMachine import customer
from aSingleMachine import assess
from aSingleMachine import inspection
from aSingleMachine import warehouse
from playwright.sync_api import sync_playwright
import time
import DataBaseConnection
import Functionalclass

"""
回收
"""
def run(playwright):
    # 创建浏览器驱动
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    # 客服端
    customerpage = customer.Customerservice(page)
    # 登录客服端
    customerpage.login()
    # 获取订单信息
    orderData = customerpage.getOrderInformation()
    print('订单信息', orderData)
    # 仓库端
    warehousepage = warehouse.Warehousemanagement(page, orderData['orderType'], orderData['traNumber'])
    # 登录
    warehousepage.login()
    # 打印编码
    warehousepage.printCode()
    # 回收入库,获取商品的库存编码
    ddCode = warehousepage.recoveryOfPutInStorage()
    print(ddCode)

    # 质检中心
    inspectionpage = inspection.Qualityinspection(page, orderData['orderType'], ddCode)
    # 登录
    inspectionpage.login()
    # 进行质检
    inspectionpage.forQualityInspection()

    # 核价端
    assesspage = assess.Assesstheprice(page, ddCode, orderData['orderNumber'], orderData['orderType'])
    # 登录
    assesspage.login()
    # 进行核价
    assesspage.toAssessThePrice()
    page.close()

with sync_playwright() as playwright:
    run(playwright)
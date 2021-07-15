import DataBaseConnection
import Functionalclass
import time
"""
客服系统
"""
class Customerservice():
    def __init__(self, page):
        self.page = page
        self.pageLogin = ''

    # 登录
    def login(self):
        # Go to https://test.sosotec.com/test/fastlogin/index.html?sign=AHTM05CYNYEFLKGWHXQKSB23ZVQINDJP
        self.page.goto("https://test.sosotec.com/test/fastlogin/index.html?sign=AHTM05CYNYEFLKGWHXQKSB23ZVQINDJP")

        # Click text=客服端
        self.page.click("text=客服端")

        # Click text=登陆
        with self.page.expect_popup() as popup_info:
            self.page.click("text=登陆")
        page1 = popup_info.value
        self.pageLogin = page1

    # 获取订单信息
    def getOrderInformation(self):
        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=订单")

        # 获得订单的订单号
        ddcodeList = DataBaseConnection.selectOrder()
        orderNumber = ddcodeList['订单号']
        # 点击订单号进入详情页
        element_handle = self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/"
                                                          "header/div[2]/div[2]/input")
        element_handle.type(orderNumber)
        self.pageLogin.click("button:has-text(\"搜索\")")
        self.pageLogin.click("text=" + orderNumber)

        time.sleep(0.5)

        # 获取物流单号
        # 自动等待元素出现再执行
        trackNumber = self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main"
                                                       "/div[2]/div/div[2]/div[4]/p[2]/span[1]/span").text_content()
        print('物流编号', trackNumber)
        traNumber = Functionalclass.determineDigital(trackNumber)

        # 获取订单类型
        orderType = self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main"
                                                     "/div[4]/div[1]/div[3]/table/tbody/tr/td[1]/div/div/"
                                                     "p[1]").text_content()
        data = {'traNumber': traNumber, 'orderType': orderType, 'orderNumber': orderNumber}
        # page.close()
        return data

    # 如果是一单多机，需手动到客服端推价
    def manuallyPushThePrice(self, orderNumber):
        self.login()
        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=订单")

        # 点击订单号进入详情页
        element_handle = self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/header/"
                                                "div[2]/div[2]/input")
        element_handle.type(orderNumber)
        self.pageLogin.click("button:has-text(\"搜索\")")
        self.pageLogin.click("text=" + orderNumber)
        self.pageLogin.click(":nth-match(button:has-text(\"推价\"), 2)")
        # Click button:has-text("确定推价")
        self.pageLogin.click("button:has-text(\"确定推价\")")
        # Click [aria-label="Close"]
        self.pageLogin.click("[aria-label=\"Close\"]")
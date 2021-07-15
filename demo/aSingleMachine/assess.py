from aSingleMachine import customer
import time
import Functionalclass
"""
核价系统
"""
class Assesstheprice():
    def __init__(self, page, code, orderNumber, orderType):
        self.page = page
        self.code = code
        self.orderNumber = orderNumber
        self.orderType = orderType
        self.pageLogin = ''

    # 登录
    def login(self):
        # Click text=QTO-质检类目
        self.page.click("text=QTO-质检类目")

        # Click text=登陆
        # with page.expect_navigation():
        with self.page.expect_popup() as popup_info:
            self.page.click("text=登陆")
        page4 = popup_info.value

        # Go to https://test.sosotec.com/qto/#/
        page4.goto("https://test.sosotec.com/qto/#/")
        self.pageLogin = page4

    # 核价推价
    def toAssessThePrice(self):
        # Click text=核价
        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=核价")

        # Click text=阿曼里
        self.pageLogin.click("text=阿曼里")

        # Click [placeholder="订单号"]
        self.pageLogin.click("[placeholder=\"订单号\"]")

        # Fill [placeholder="订单号"]
        self.pageLogin.fill("[placeholder=\"订单号\"]", self.orderNumber)

        # Click button:has-text("搜索")
        self.pageLogin.click("button:has-text(\"搜索\")")

        # Click text=1012104021406053280613
        self.pageLogin.click("text=" + self.orderNumber)

        # Click [aria-label="提示"] button:has-text("确定")
        time.sleep(0.5)
        el = Functionalclass.elementExists(self.pageLogin, "[aria-label=\"提示\"] button:has-text(\"确定\")")
        print("元素：", el)
        if el:
            self.pageLogin.click("[aria-label=\"提示\"] button:has-text(\"确定\")")
        time.sleep(10)

        if self.orderType == '一键回收':
            for r in self.code:
                self.pageLogin.click("button:has-text(\"确定修改\")")
                self.pageLogin.click("[aria-label=\"提示\"] button:has-text(\"确定\")")

            # 核价完成后需要到客服端进行手动推价
            customerpage = customer.Customerservice(self.page)
            customerpage.manuallyPushThePrice(self.orderNumber)
        else:
            self.pageLogin.click("button:has-text(\"确定修改\")")
            self.pageLogin.click("[aria-label=\"提示\"] button:has-text(\"确定\")")
        # self.pageLogin.close()
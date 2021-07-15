import DataBaseConnection
import time
"""
仓库管理系统
"""
class Warehousemanagement():
    def __init__(self, page, orderType, traNumber):
        self.page = page  # 页句柄
        self.orderType = orderType  # 订单类型  一单一机，一单多机
        self.traNumber = traNumber  # 物流单号
        self.pageLogin = ''

    # 登录
    def login(self):
        self.page.click("text=仓库管理系统")
        with self.page.expect_popup() as popup_info:
            self.page.click("text=登陆")
        page = popup_info.value
        self.pageLogin = page

    # 打印编码
    def printCode(self):
        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=到货")

        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=编码打印")

        # 输入时间
        time_obj = time.localtime(time.time())
        newTime = time.strftime('%Y-%m-%d', time_obj)
        element_handle = self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/section/main/section/main/div/div/"
                                                 "form/div/div[1]/div/div/input")
        element_handle.type(newTime)
        self.pageLogin.click("form div div div")
        # 打印数量。如果是一单多机就打印多个编码
        self.pageLogin.click("[placeholder=\"请输入\"]")

        if self.orderType == "一键回收":
            self.pageLogin.fill("[placeholder=\"请输入\"]", "2")
        else:
            self.pageLogin.fill("[placeholder=\"请输入\"]", "1")

        # 打印份额
        self.pageLogin.click(":nth-match([placeholder=\"请输入\"], 2)")
        self.pageLogin.fill(":nth-match([placeholder=\"请输入\"], 2)", "1")

        # 确定打印
        self.pageLogin.click("button:has-text(\"确定打印\")")

    # 回收入库,入库成返回入库的商品编码
    def recoveryOfPutInStorage(self):
        with self.pageLogin.expect_navigation():
            self.pageLogin.click("text=回收入库")

            # 输入物流单号
        self.pageLogin.click("[placeholder=\"库存编号/快递单号\"]")
        self.pageLogin.fill("[placeholder=\"库存编号/快递单号\"]", self.traNumber)

        # Click button:has-text("搜索")
        self.pageLogin.click("button:has-text(\"搜索\")")

        # 入库，输入商品库存编码
        # 获取打印的库存编码
        ddCode = DataBaseConnection.printCode(self.orderType)

        if self.orderType == '一键回收':
            for c in ddCode:
                print('编码：', c['code'])
                self.pageLogin.click("[placeholder=\"库存编号/快递单号\"]")
                # Fill [placeholder="库存编号/快递单号"]
                self.pageLogin.fill("[placeholder=\"库存编号/快递单号\"]", c['code'])
                self.pageLogin.click("button:has-text(\"搜索\")")
                time.sleep(0.5)
                self.pageLogin.click("button:has-text(\"添加\")")
                # self.pageLogin.wait_for_selector("xpath=//*[@id='app']/section/main/section/main/section/main/div/div/"
                #                                 "div[3]/button[1]").click()
        else:
            inventoryCoding = ddCode['code']
            self.pageLogin.click("[placeholder=\"库存编号/快递单号\"]")
            # Fill [placeholder="库存编号/快递单号"]
            self.pageLogin.fill("[placeholder=\"库存编号/快递单号\"]", inventoryCoding)
            self.pageLogin.click("button:has-text(\"搜索\")")
        # self.pageLogin.close()
        return ddCode
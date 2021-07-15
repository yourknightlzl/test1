import Functionalclass
import time
"""
质检系统
"""
class Qualityinspection():
    def __init__(self, page, orderType, ddCode):
        self.page = page
        self.orderType = orderType
        self.ddCode = ddCode
        self.pageLogin = ''

    # 登录
    def login(self):
        self.page.click("text=MQC-质检中心")
        # Click text=登陆
        with self.page.expect_popup() as popup_info:
            self.page.click("text=登陆")
        page = popup_info.value
        self.pageLogin = page

    # 进行质检
    def forQualityInspection(self):
        # 判断是否为一单多机
        if self.orderType == '一键回收':
            models = 1      # 用于选择不同品牌机型
            for r in self.ddCode:
                # Click [placeholder="扫描商品的库存编号"]
                self.pageLogin.click("[placeholder=\"扫描商品的库存编号\"]")

                # Fill [placeholder="扫描商品的库存编号"]
                self.pageLogin.fill("[placeholder=\"扫描商品的库存编号\"]", r['code'])

                # Press Enter
                self.pageLogin.press("[placeholder=\"扫描商品的库存编号\"]", "Enter")

                time.sleep(0.5)
                # Click button:has-text("确定")
                el = Functionalclass.elementExists(self.pageLogin, "button:has-text(\"确定\")")
                print("元素：", el)
                if el:
                    self.pageLogin.click("button:has-text(\"确定\")")

                # 选择机型品牌
                self.pageLogin.click("[placeholder=\"请选择机型\"]")
                if models == 1:
                    # Click [placeholder="请选择机型"]
                    # Click div[role="tooltip"] >> text=苹果
                    self.pageLogin.click("div[role=\"tooltip\"] >> text=苹果")
                    # Click text=iPhone XR
                    self.pageLogin.click("text=iPhone XR")
                else:
                    # Click [placeholder="请选择机型"]
                    # Click div[role="tooltip"] >> text=华为
                    self.pageLogin.click("div[role=\"tooltip\"] >> text=华为")
                    # Click :nth-match(:text("华为 Mate 30 Pro"), 2)
                    self.pageLogin.click(":nth-match(:text(\"华为 Mate 30 Pro\"), 2)")

                self.propertiesTest(self.pageLogin, r['code'])
                models += 1
        else:
            # Click [placeholder="扫描商品的库存编号"]
            self.pageLogin.click("[placeholder=\"扫描商品的库存编号\"]")

            # Fill [placeholder="扫描商品的库存编号"]
            self.pageLogin.fill("[placeholder=\"扫描商品的库存编号\"]", self.ddCode['code'])

            # Press Enter
            self.pageLogin.press("[placeholder=\"扫描商品的库存编号\"]", "Enter")

            time.sleep(0.5)
            # Click button:has-text("确定")
            el = Functionalclass.elementExists(self.pageLogin, "button:has-text(\"确定\")")
            print("元素：", el)
            if el:
                self.pageLogin.click("button:has-text(\"确定\")")
            self.propertiesTest(self.pageLogin, self.ddCode['code'])
        # self.pageLogin.close()


    # 属性检测
    def propertiesTest(self, page, code):
        # Fill [placeholder="请输入IMEI码"]
        page.fill("[placeholder=\"请输入IMEI码\"]", code)

        # 判断元素是否存在
        el = Functionalclass.elementExists(page, "text=属性检测")
        if el:
            cp = Functionalclass.elementExists(page, "text=开机运行正常")
            if cp:
                # Click text=初级检测
                page.click("text=开机运行正常")
            # Click text=属性检测
            page.click("text=属性检测")

            element_handle1 = page.inner_text("xpath = //*[@id='pane-20']/div/table")

            # 将文本内容根据空行拆分成列表
            datas = element_handle1.splitlines()
            print("长度为：", len(datas))
            print(datas)

            # 定义一个列表，用来储存根据\t隔开的数据
            datalist = []
            for data in datas:
                # 碰到空元素，跳过
                if data == '':
                    continue
                # 碰到\t元素，结束添加，循环此前已存储的元素
                if data == "\t":
                    for i, da in enumerate(datalist):
                        if "IMEI码\t" in datalist:
                            break

                        if "渠道" in datalist:
                            page.click(":nth-match(:text(\"国行\"), 2)")
                            break

                        if "销售地" in datalist:
                            page.click("text=国行")
                            break

                        page.click("text=%s" % datalist[1])
                        break
                    print(datalist)
                    # 清除已添加的元素
                    datalist.clear()
                    continue
                # 加入元素到列表中
                datalist.append(data)

            # Click text=功能检测
            page.click("text=功能检测")

            element1 = "text=SIM卡2功能 正常 不读卡 无服务 信号不稳定 卡槽损坏 不支持 >> :nth-child(2)"
            element2 = "text=NFC 正常 坏 不支持 >> :nth-child(3)"
            element3 = "text=面容 不支持 正常 坏 >> :nth-child(3)"
            element4 = "text=面容 正常 坏 >> :nth-child(2)"
            boolstr1 = Functionalclass.elementExists(page, element1)
            boolstr2 = Functionalclass.elementExists(page, element2)
            boolstr3 = Functionalclass.elementExists(page, element3)
            boolstr4 = Functionalclass.elementExists(page, element4)
            print("bool1:", boolstr1, " bool2:", boolstr2, " bool3:", boolstr3)
            if boolstr1:
                page.click(element1)

            if boolstr2:
                page.click(element2)

            if boolstr3:
                page.click(element3)

            if boolstr4:
                page.click(element4)
        else:
            # Click text=初级检测
            el = Functionalclass.elementExists(page, "text=开机运行正常")
            if el:
                page.click("text=开机运行正常")

        # 获取指定元素的文本内容
        # element_handle = page3.eval_on_selector_all(".editable","nodes => nodes.map(n => n.innerText)")
        # element_handle = page3.eval_on_selector(".editable", "node => node.innerText")

        # Click [placeholder="成色"]
        page.click("[placeholder=\"成色\"]")

        # Click :nth-match(li:has-text("9新"), 2)
        page.click(":nth-match(li:has-text(\"9新\"), 2)")

        # Click [placeholder="等级"]
        page.click("[placeholder=\"等级\"]")

        # Click :nth-match(span:has-text("B"), 2)
        page.click("li:has-text(\"A3\")")

        # Click button:has-text("质检完成")
        page.click("button:has-text(\"质检完成\")")

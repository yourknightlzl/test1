from playwright.sync_api import sync_playwright
import time
import DataBaseConnection
import Functionalclass
# 一单一机

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://test.sosotec.com/test/fastlogin/index.html?sign=AHTM05CYNYEFLKGWHXQKSB23ZVQINDJP
    page.goto("https://test.sosotec.com/test/fastlogin/index.html?sign=AHTM05CYNYEFLKGWHXQKSB23ZVQINDJP")

    # Click text=客服端
    page.click("text=客服端")

    # Click text=登陆
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page1 = popup_info.value

    # Go to https://test.sosotec.com/kf/#/
    # page1.goto("https://test.sosotec.com/kf/#/")

    # Click text=订单
    # with page1.expect_navigation(url="https://test.sosotec.com/kf/#/odr/list"):
    with page1.expect_navigation():
        page1.click("text=订单")

    # 获得订单的订单号
    ddcodeList = DataBaseConnection.selectOrder()
    ddcode = ddcodeList['订单号']
    # 点击订单号进入详情页
    # Click text=1012104021406053280613
    page1.click("text="+ddcode)

    # time.sleep(1)

    # 获取物流单号
    # //*[@id="app"]/section/main/div[1]/div[2]/section/main/div[2]/div/div[2]/div[4]/p[2]/span[1]/span
    # trackNumber = page1.query_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main/div[2]/div/"
    #                                    "div[2]/div[4]/p[2]/span[1]/span").text_content()
    # 自动等待元素出现再执行
    trackNumber = page1.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main/div[2]/div/"
                                       "div[2]/div[4]/p[2]/span[1]/span").text_content()
    traNumber = Functionalclass.determineDigital(trackNumber)

    # Click text=仓库管理系统
    page.click("text=仓库管理系统")

    # Click text=登陆
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page2 = popup_info.value
    # time.sleep(1)
    # Click text=到货
    # with page2.expect_navigation(url="https://test.sosotec.com/stc/#/rec/stick"):
    with page2.expect_navigation():
        page2.click("text=到货")

    # Click text=编码打印
    with page2.expect_navigation():
        page2.click("text=编码打印")
    # time.sleep(1)
    # 输入时间
    time_obj = time.localtime(time.time())
    newTime = time.strftime('%Y-%m-%d', time_obj)
    element_handle = page2.wait_for_selector("xpath=//*[@id='app']/section/main/section/main/section/main/div/div/"
                                  "form/div/div[1]/div/div/input")
    element_handle.type(newTime)
    page2.click("form div div div")
    # 打印数量
    page2.click("[placeholder=\"请输入\"]")
    page2.fill("[placeholder=\"请输入\"]", "1")

    # 打印份额
    page2.click(":nth-match([placeholder=\"请输入\"], 2)")
    page2.fill(":nth-match([placeholder=\"请输入\"], 2)", "1")

    # 确定打印
    page2.click("button:has-text(\"确定打印\")")

    # Click text=回收入库
    with page2.expect_navigation():
        page2.click("text=回收入库")

    # 输入物流单号
    page2.click("[placeholder=\"库存编号/快递单号\"]")
    page2.fill("[placeholder=\"库存编号/快递单号\"]", traNumber)

    # Click button:has-text("搜索")
    page2.click("button:has-text(\"搜索\")")

    # 入库，输入商品库存编码
    # 获取打印的库存编码
    ddCode = DataBaseConnection.printCode("一单一机")
    inventoryCoding = ddCode['code']
    page2.click("[placeholder=\"库存编号/快递单号\"]")
    # Fill [placeholder="库存编号/快递单号"]
    page2.fill("[placeholder=\"库存编号/快递单号\"]", inventoryCoding)
    page2.click("button:has-text(\"搜索\")")

    # Click text=MQC-质检中心
    page.click("text=MQC-质检中心")
    # Click text=登陆
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page3 = popup_info.value


    # Click [placeholder="扫描商品的库存编号"]
    page3.click("[placeholder=\"扫描商品的库存编号\"]")

    # Fill [placeholder="扫描商品的库存编号"]
    page3.fill("[placeholder=\"扫描商品的库存编号\"]", inventoryCoding)

    # Press Enter
    page3.press("[placeholder=\"扫描商品的库存编号\"]", "Enter")

    time.sleep(0.5)
    # Click button:has-text("确定")
    el = Functionalclass.elementExists(page3, "button:has-text(\"确定\")")
    print("元素：", el)
    if el:
        page3.click("button:has-text(\"确定\")")

    # Fill [placeholder="请输入IMEI码"]
    page3.fill("[placeholder=\"请输入IMEI码\"]", inventoryCoding)


    # 判断元素是否存在
    el = Functionalclass.elementExists(page3, "text=属性检测")
    if el:
        cp = Functionalclass.elementExists(page3, "text=开机运行正常")
        if cp:
            # Click text=初级检测
            page3.click("text=开机运行正常")
        # Click text=属性检测
        page3.click("text=属性检测")

        element_handle1 = page3.inner_text("xpath = //*[@id='pane-20']/div/table")

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
                        page3.click(":nth-match(:text(\"国行\"), 2)")
                        break

                    if "销售地" in datalist:
                        page3.click("text=国行")
                        break

                    page3.click("text=%s" % datalist[1])
                    break
                print(datalist)
                # 清除已添加的元素
                datalist.clear()
                continue
            # 加入元素到列表中
            datalist.append(data)

        # Click text=功能检测
        page3.click("text=功能检测")

        element1 = "text=SIM卡2功能 正常 不读卡 无服务 信号不稳定 卡槽损坏 不支持 >> :nth-child(2)"
        element2 = "text=NFC 正常 坏 不支持 >> :nth-child(3)"
        element3 = "text=面容 不支持 正常 坏 >> :nth-child(3)"
        element4 = "text=面容 正常 坏 >> :nth-child(2)"
        boolstr1 = Functionalclass.elementExists(page3, element1)
        boolstr2 = Functionalclass.elementExists(page3, element2)
        boolstr3 = Functionalclass.elementExists(page3, element3)
        boolstr4 = Functionalclass.elementExists(page3, element4)
        print("bool1:", boolstr1, " bool2:", boolstr2, " bool3:", boolstr3)
        if boolstr1:
            page3.click(element1)

        if boolstr2:
            page3.click(element2)

        if boolstr3:
            page3.click(element3)

        if boolstr4:
            page3.click(element4)
    else:
        # Click text=初级检测
        page3.click("text=开机运行正常")

    # 获取指定元素的文本内容
    # element_handle = page3.eval_on_selector_all(".editable","nodes => nodes.map(n => n.innerText)")
    # element_handle = page3.eval_on_selector(".editable", "node => node.innerText")


    # Click [placeholder="成色"]
    page3.click("[placeholder=\"成色\"]")

    # Click :nth-match(li:has-text("9新"), 2)
    page3.click(":nth-match(li:has-text(\"9新\"), 2)")

    # Click [placeholder="等级"]
    page3.click("[placeholder=\"等级\"]")

    # Click :nth-match(span:has-text("B"), 2)
    page3.click("li:has-text(\"A3\")")

    # Click button:has-text("质检完成")
    page3.click("button:has-text(\"质检完成\")")

    # Click text=QTO-质检类目
    page.click("text=QTO-质检类目")

    # Click text=登陆
    # with page.expect_navigation():
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page4 = popup_info.value

    # Go to https://test.sosotec.com/qto/#/
    page4.goto("https://test.sosotec.com/qto/#/")


    # Click text=核价
    # with page4.expect_navigation(url="https://test.sosotec.com/qto/#/check/odr/wait/11"):
    with page4.expect_navigation():
        page4.click("text=核价")

    # Click text=阿曼里
    page4.click("text=阿曼里")
    # assert page4.url == "https://test.sosotec.com/qto/#/check/odr/wait/13"

    # Click [placeholder="库存编号"]
    page4.click("[placeholder=\"库存编号\"]")

    # Fill [placeholder="库存编号"]
    page4.fill("[placeholder=\"库存编号\"]", inventoryCoding)

    # Click button:has-text("搜索")
    page4.click("button:has-text(\"搜索\")")

    # Click text=1012104021406053280613
    page4.click("text="+ddcode)

    # Click [aria-label="提示"] button:has-text("确定")
    page4.click("[aria-label=\"提示\"] button:has-text(\"确定\")")

    time.sleep(10)
    # Click button:has-text("确定修改")
    page4.click("button:has-text(\"确定修改\")")

    # Click [aria-label="提示"] button:has-text("确定")
    page4.click("[aria-label=\"提示\"] button:has-text(\"确定\")")

    # Close page
    page1.close()

    # Close page
    page2.close()

    # Close page
    page3.close()

    # Close page
    page4.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()



with sync_playwright() as playwright:
    run(playwright)
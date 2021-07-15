from playwright.sync_api import sync_playwright
import time
import Functionalclass
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
    # with page.expect_navigation(url="https://test.sosotec.com/kf/#/"):
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page1 = popup_info.value

    # Click text=订单
    # with page1.expect_navigation(url="https://test.sosotec.com/kf/#/odr/list"):
    with page1.expect_navigation():
        page1.click("text=订单")

    # Click text=[placeholder="订单号/快递单/退回单/库存编码/手机号码"]
    # //*[@id="app"]/section/main/div[1]/div[2]/section/header/div[2]/div[2]/input

    # 元素高级定位Xpath
    page1.click("//*[@id='app']/section/main/div[1]/div[2]/section/header/div[2]/div[2]/input")
    page1.fill("//*[@id='app']/section/main/div[1]/div[2]/section/header/div[2]/div[2]/input", "15096134249")

    # 元素定位
    # element_handle = page1.query_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/header/div[2]/div[2]/input")
    # element_handle.type("15096134249")

    # Click button:has-text("搜索")
    page1.click("button:has-text(\"搜索\")")

    with page1.expect_navigation():
        page1.click("text=1012104061615752960119")


    trackNumber = page1.query_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main/div[2]/div/"
                                           "div[2]/div[4]/p[2]/span[1]/span").text_content()
    number = Functionalclass.determineDigital(trackNumber)

    nm = page1.query_selector_all("class = el-table__row")
    print(nm)
    # element = page1.query_selector("xpath=//*[@id='app']/section/header/div[2]/ul/li[1]/p").text_content()
    print(number)


    time.sleep(1)
    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
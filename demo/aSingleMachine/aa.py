from playwright.sync_api import sync_playwright

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
    page1.goto("https://test.sosotec.com/kf/#/")

    # Click text=订单
    # with page1.expect_navigation(url="https://test.sosotec.com/kf/#/odr/list"):
    with page1.expect_navigation():
        page1.click("text=订单")

    # Click text=3062107081641112752387
    page1.click("text=3062107081641112752387")

    orderType = page1.wait_for_selector("xpath=//*[@id='app']/section/main/div[1]/div[2]/section/main/div[4]/div[1]"
                                       "/div[3]/table/tbody/tr/td[1]/div/div/p[1]").text_content()

    print(orderType)

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
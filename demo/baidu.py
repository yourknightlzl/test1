from playwright.sync_api import sync_playwright
import time
def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://test.sosotec.com/test/fastlogin/index.html?sign=AHTM05CYNYEFLKGWHXQKSB23ZVQINDJP")

    page.click("text=MQC-质检中心")
    # Click text=登陆
    with page.expect_popup() as popup_info:
        page.click("text=登陆")
    page2 = popup_info.value

    inventoryCoding = "21042316248932"

    # Click [placeholder="扫描商品的库存编号"]
    page2.click("[placeholder=\"扫描商品的库存编号\"]")

    # Fill [placeholder="扫描商品的库存编号"]
    page2.fill("[placeholder=\"扫描商品的库存编号\"]", inventoryCoding)

    # Press Enter
    page2.press("[placeholder=\"扫描商品的库存编号\"]", "Enter")

    # yuansu = page2.query_selector("xpath = //*[@id='app']/section/div/div[2]/div/div/div[2]")
    yuansu = page2.wait_for_selector("xpath = //*[@id='app']/section/div/div[2]/div/div/div[2]")
    print("元素是否存在：", yuansu)
    snapshot = page2.accessibility.snapshot()
    node = find_focused_node(snapshot)
    if node:
        print(node["name"])
    # Close page
    page.close()
    page2.close()

    # ---------------------
    context.close()
    browser.close()


def find_focused_node(node):
    if (node.get("focused")):
        return node
    for child in (node.get("children") or []):
        # found_node = find_focused_node(child)
        # return found_node
        print(child)
    return None

with sync_playwright() as playwright:
    run(playwright)
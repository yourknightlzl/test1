from playwright.sync_api import sync_playwright
import asyncio
import time
from playwright.async_api import async_playwright


# 同步获取标题
# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     page.goto("https://www.baidu.com")
#     print(page.title())
#     browser.close()

# 异步获取标题
async def main():
    async with async_playwright() as p:
      for browser_type in [p.chromium,p.firefox,p.webkit]:
        browser = await browser_type.launch()
        page = await browser.new_page()
        await page.goto("https://www.baidu.com")
        await page.screenshot(path=f'{browser_type.name}.png')
        print(await page.title())
        await browser.close()

asyncio.run(main())
# 同步
# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch()
#         page = browser.new_page()
#         page.goto('http://whatsmyuseragent.org/')
#         page.screenshot(path=f'example-{browser_type.name}.png')
#         browser.close()

# 异步
# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             browser = await browser_type.launch()
#             page = await browser.new_page()
#             await page.goto('https://www.baidu.com/')
#             await page.screenshot(path=f'example-{browser_type.name}.png')
#             await browser.close()
#
# asyncio.run(main())

# 手机模式
# with sync_playwright() as p:
#     phone_name = 'iPhone 11 Pro'
#     iphone_11 = p.devices[phone_name]
#     browser = p.webkit.launch(headless=False)
#     context = browser.new_context(
#         **iphone_11,
#         locale='zh-CN'
#     )
#     page = context.new_page()
#     page.goto('https://map.baidu.com/mobile/webapp/index/index/')
#     page.screenshot(path=f'{phone_name}.png')
#     time.sleep(10)
#     browser.close()


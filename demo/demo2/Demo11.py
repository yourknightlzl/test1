from threading import Thread
from selenium import webdriver
from time import ctime, sleep
def test_baidu(browser, search):
    """测试用例"""
    print('start:%s' % ctime())
    print('browser:%s' % browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ie':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        print('browser参数有误')

    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
        lists = {'chrome': 'threading'}
        threads = []
        files = range(len(lists))
        # 创建线程
        for browser, serach in lists.items():
            t = Thread(target=test_baidu, args=(browser, serach))
            threads.append(t)

        # 启动线程
        for t in files:
            threads[t].start()

        for t in files:
            threads[t].join()
        print('end:%s' % ctime())

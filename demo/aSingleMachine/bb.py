from playwright.sync_api import sync_playwright
import time
import DataBaseConnection

def aaa():
    a = 1
    sum = 0
    while a <= 30:
        sum = sum + a
        a += 1
    print(sum)

def bbb():
    a = 1
    sum = 1
    while a <= 365:
        if a > 1:
            sum = sum + 2**(a-1)
        a += 1
    print(sum)

if __name__ == "__main__":
    bbb()

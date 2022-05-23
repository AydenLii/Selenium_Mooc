from selenium import webdriver
import os
import time
import json


def browser_initial():
    """"
    进行浏览器初始化
    """
    os.chdir('./')
    browser = webdriver.Firefox()
    log_url = 'https://mooc.icve.com.cn/'
    return log_url, browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(50)  # 进行扫码登录
    dictCookies = browser.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open('cookie.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
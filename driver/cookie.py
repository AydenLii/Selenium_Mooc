from selenium import webdriver
import os
import time
import json


def browser_init():
    """"
    进行浏览器初始化
    """
    os.chdir('../out/')
    _browser = webdriver.Firefox()
    log_url = 'https://mooc.icve.com.cn/'
    return log_url, _browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(50)  # 进行扫码登录
    dict_cookies = browser.get_cookies()  # 获取list的cookies
    json_cookies = json.dumps(dict_cookies)  # 转换成字符串保存

    with open('../out/cookie.txt', 'w') as f:
        f.write(json_cookies)
    print('cookies保存成功！')


if __name__ == "__main__":
    tur = browser_init()
    get_cookies(tur[0], tur[1])

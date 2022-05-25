import time
from selenium import webdriver


def driver_init():
    _driver = webdriver.Chrome()
    url = 'https://mooc.icve.com.cn/'
    _driver.get(url)
    time.sleep(2)
    return _driver

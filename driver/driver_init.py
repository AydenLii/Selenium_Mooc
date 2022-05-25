from selenium import webdriver


def driver_init():
    _driver = webdriver.Chrome()
    url = 'https://mooc.icve.com.cn/'
    _driver.get(url)
    return url, _driver




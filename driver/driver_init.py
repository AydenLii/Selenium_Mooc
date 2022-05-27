from selenium import webdriver


def driver_url():
    url = 'https://mooc.icve.com.cn/'
    return url


def driver_init():
    _driver = webdriver.Chrome()
    _driver.get(driver_url())
    _driver.implicitly_wait(10)
    return _driver

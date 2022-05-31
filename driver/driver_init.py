from selenium import webdriver


def driver_url():
    url = 'https://mooc.icve.com.cn/'
    return url


def driver_init():
    _driver = webdriver.Chrome()
    _driver.set_window_size(1080, 720)
    _driver.get(driver_url())
    _driver.implicitly_wait(20)

    return _driver

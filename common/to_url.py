import time


def to_url(_driver, _url):
    _driver.get(_url)
    time.sleep(3)
    _driver.switch_to.window(_driver.window_handles[0])

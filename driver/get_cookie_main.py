from driver.driver_init import *
from driver.write_in_cookie import get_cookies


if __name__ == "__main__":
    url = driver_url()
    driver = driver_init()
    get_cookies(driver, url)

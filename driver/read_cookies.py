import json
import os
import time


def read_cookies(_driver):
    # 读取cookie并写入浏览器
    cookie_establish_time = time.ctime(os.path.getctime('out/cookie.txt')).split(" ")[3]
    f2 = open("./out/cookie.txt")
    cookies = json.loads(f2.read())
    for cook in cookies:
        _driver.add_cookie(cook)


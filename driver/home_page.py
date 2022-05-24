import json
import time

from selenium import webdriver

def driver_init():
    set_driver = webdriver.Chrome()
    url = 'https://mooc.icve.com.cn/'
    set_driver.get(url)
    time.sleep(2)
    return set_driver


def read_cookies(set_driver):
    """
    读取cookie并写入浏览器
    """
    f2 = open("../out/cookie.txt")
    cookies = json.loads(f2.read())
    for cook in cookies:
        set_driver.add_cookie(cook)


# 跳转至[作业考试]页面
def to_homework_exam_page(set_driver):
    time.sleep(2)
    set_driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")


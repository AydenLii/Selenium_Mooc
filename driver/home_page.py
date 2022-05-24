import json
import time

from selenium import webdriver

def driver_init():
    _driver = webdriver.Chrome()
    url = 'https://mooc.icve.com.cn/'
    _driver.get(url)
    time.sleep(2)
    return _driver


def read_cookies(_driver):
    """
    读取cookie并写入浏览器
    """
    f2 = open("./out/cookie.txt")
    cookies = json.loads(f2.read())
    for cook in cookies:
        _driver.add_cookie(cook)


# 跳转至[作业考试]页面
def to_homework_exam_page(_driver):
    time.sleep(2)
    _driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")


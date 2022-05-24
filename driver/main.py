import time
import json
from selenium import webdriver

from driver.work_1_correcting import work_1_correcting


def driver_init():
    _driver = webdriver.Chrome()
    url = 'https://mooc.icve.com.cn/'
    _driver.get(url)
    time.sleep(2)
    return _driver


def read_cookies(_driver):
    # 从cookies.txt文件读取cookies
    f2 = open("../out/cookie.txt")
    cookies = json.loads(f2.read())
    # 使用cookies登录
    for cook in cookies:
        _driver.add_cookie(cook)
    # 刷新页面
    _driver.refresh()


# 跳转至[作业考试]页面
def to_homework_exam_page(_driver):
    _driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")
    time.sleep(3)  # 等待页面加载完毕
    _driver.switch_to.window(driver.window_handles[0])


if __name__ == "__main__":
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    to_homework_exam_page(driver)
    work_1_correcting(driver)  # 批阅 <体育（篮球）--第四次开课> 的 <第一次课作业>

import time
from works.essay_question.correct import work_1_correct
from works.subject_question import accessory
from driver.read_cookies import read_cookies
from driver.driver_init import *


def diver_web():
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    # 跳转至[作业考试]页面
    time.sleep(2)
    driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")
    time.sleep(2)
    return driver


def works():
    value = input('输入审批课程索引值(1~11):\n')
    driver = diver_web()
    if value == '1':
        work_1_correct(driver)
    else:
        accessory(driver, value)

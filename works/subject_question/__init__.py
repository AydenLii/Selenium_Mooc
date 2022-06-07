import time
from works.essay_question.correct import work_1_correct

from driver.read_cookies import read_cookies
from driver.driver_init import *
from works.subject_question.first_phase import first_accessory
from works.subject_question.first_phase.examination import one_examination
from works.subject_question.second_phase import second_accessory
from works.subject_question.second_phase.ques_answer_combination import Second_dict


def diver_web_1():
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    time.sleep(1)
    # 跳转至[作业考试]页面
    driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")
    time.sleep(1)
    return driver


def diver_web_2():
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    time.sleep(1)
    # 跳转至[作业考试]页面
    driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=sutuaeouilzafewi27dexw")
    time.sleep(1)
    return driver


def works_statr_1(course_value):
    # course_value = input('输入审批课程索引值(1~11):')
    driver = diver_web_1()
    if course_value == '1':
        work_1_correct(driver)
    else:
        first_accessory(driver, course_value)
    print('任务' + course_value + '批改完成')


def works_statr_auto_1():
    max_course = int(input("最大批改数:"))
    min_course = int(input("最小批改数:"))
    for i in range(min_course, max_course + 1):
        work_num = str(i)
        driver = diver_web_1()
        if work_num == '1':
            work_1_correct(driver)
        else:
            first_accessory(driver, work_num)
            print('任务' + work_num + '批改完成')
    diver_web_1()


def works_statr_2(course_value):
    # course_value = input('输入审批课程索引值(1~11):')
    driver = diver_web_2()
    if course_value == 1:
        Second_dict(driver)
    else:
        second_accessory(driver, course_value)
    print('任务' + course_value + '批改完成')


def works_statr_auto_2():
    max_course = int(input("最大批改数:"))
    min_course = int(input("最小批改数:"))
    for i in range(min_course, max_course + 1):
        work_num = str(i)
        driver = diver_web_2()
        if work_num == '1':
            Second_dict(driver)
            print('任务' + work_num + '批改完成')
        else:
            second_accessory(driver, work_num)
            print('任务' + work_num + '批改完成')
    diver_web_2()

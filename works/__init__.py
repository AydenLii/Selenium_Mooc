import time
from works.essay_question.correct import work_1_correct
from works.subject_question import accessory
from driver.read_cookies import read_cookies
from driver.driver_init import *


def diver_web():
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    time.sleep(2)
    # 跳转至[作业考试]页面
    driver.get("https://mooc.icve.com.cn/design/workExam/homework/homework.html?courseOpenId=x6nvaeouv5tfvankjlmxsq")
    time.sleep(2)
    return driver


def works_statr():
    course_value = input('输入审批课程索引值(1~11):')
    driver = diver_web()
    if course_value == '1':
        work_1_correct(driver)
    else:
        accessory(driver, course_value)
    print('任务' + course_value + '批改完成')

    '''
    被注释掉的方法用于批量执行作业批改任务
    course_num:该课程需要批改的作业总数
    '''

# def works_statr():
#     course_num = 11
#     for i in range(6, course_num + 1):
#         work_num = str(i)
#         driver = diver_web()
#         if work_num == '1':
#             work_1_correct(driver)
#             print('任务' + work_num + '批改完成')
#         else:
#             accessory(driver, work_num)
#             print('任务' + work_num + '批改完成')


import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from two.two_text import *


def run_work_two(_driver):
    """
    切换到作业二，并获取当前需要批改的作业数
    """
    time.sleep(2)
    _driver.find_element(By.CSS_SELECTOR, work_two_CSS).click()
    time.sleep(1)
    people_count = int(_driver.find_element(By.XPATH, people_num).text.split("人")[0])
    """
    遍历所有学生
    """
    for i in range(1, people_count + 1):

        b = str(i)
        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + b + "]/a").click()
        time.sleep(1)

        question_text1_bool = _driver.find_element(By.XPATH, question_text1).text
        question_text2_bool = _driver.find_element(By.XPATH, question_text2).text
        question_file1_bool = _driver.find_element(By.XPATH, question_file1).text
        question_file2_bool = _driver.find_element(By.XPATH, question_file2).text

        if question_file1_bool == "未上传附件":
            if question_text1_bool == " ":
                _driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
                _driver.find_element(By.XPATH, question_1).send_keys('0')
            else:
                _driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
                _driver.find_element(By.XPATH, question_1).send_keys(random.randint(30, 33))
        else:
            _driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
            _driver.find_element(By.XPATH, question_1).send_keys(random.randint(43, 45))

        if question_file2_bool == "未上传附件":
            if question_text2_bool == " ":
                _driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
                _driver.find_element(By.XPATH, question_2).send_keys('0')
            else:
                _driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
                _driver.find_element(By.XPATH, question_2).send_keys(random.randint(31, 34))
        else:
            _driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
            _driver.find_element(By.XPATH, question_2).send_keys(random.randint(43, 46))

        _driver.find_element(By.CSS_SELECTOR, "#submitHomeWork").click()
        time.sleep(1)
        _driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(1)
        _driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(1)




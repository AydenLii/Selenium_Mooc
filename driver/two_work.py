import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver.two_text import *


def run_work_two(set_driver):
    time.sleep(1)
    set_driver.find_element(By.CSS_SELECTOR, work_two_CSS).click()
    time.sleep(1)
    people_count = int(set_driver.find_element(By.XPATH, people_num).text.split("人")[0])

    for i in range(1, people_count + 1):
        b = str(i)
        set_driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + b + "]/a").click()
        time.sleep(1)
        question_text1_bool = set_driver.find_element(By.XPATH, question_text1).text
        question_text2_bool = set_driver.find_element(By.XPATH, question_text2).text
        question_file1_bool = set_driver.find_element(By.XPATH, question_file1).text
        question_file2_bool = set_driver.find_element(By.XPATH, question_file2).text
        if question_file1_bool == "未上传附件":
            if question_text1_bool == " ":
                set_driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
                set_driver.find_element(By.XPATH, question_1).send_keys('0')
            else:
                set_driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
                set_driver.find_element(By.XPATH, question_1).send_keys(random.randint(30, 33))
        else:
            set_driver.find_element(By.XPATH, question_1).send_keys(Keys.CONTROL, 'a')
            set_driver.find_element(By.XPATH, question_1).send_keys(random.randint(43, 45))

        if question_file2_bool == "未上传附件":
            if question_text2_bool == " ":
                set_driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
                set_driver.find_element(By.XPATH, question_2).send_keys('0')
            else:
                set_driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
                set_driver.find_element(By.XPATH, question_2).send_keys(random.randint(31, 34))
        else:
            set_driver.find_element(By.XPATH, question_2).send_keys(Keys.CONTROL, 'a')
            set_driver.find_element(By.XPATH, question_2).send_keys(random.randint(43, 46))

        set_driver.find_element(By.CSS_SELECTOR, "#submitHomeWork").click()
        time.sleep(1)
        set_driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(1)
        set_driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(1)




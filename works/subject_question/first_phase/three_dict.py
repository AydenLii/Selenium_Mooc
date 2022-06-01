import time

from selenium.webdriver.common.by import By
from common.input_cycle import *
from common.wait_submit import wait_submit
from tqdm import tqdm

from works.subject_question.first_phase.information import *


def three_dict_correct(_driver, value):
    """
    切换到作业二，并获取当前需要批改的作业数
    """
    time.sleep(1)
    _driver.find_element(By.XPATH, work_variable(value)).click()
    time.sleep(0.5)
    people_count = int(_driver.find_element(By.XPATH, people_num).text.split("人")[0])
    """
    遍历所有学生
    """
    people_print = str(people_count)
    print('当前作业任务为:作业' + value + ',需要批改的作业共计:' + people_print + '份')
    for i in tqdm(range(1, people_count + 1)):
        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a").click()

        time.sleep(0.3)
        question_text1_bool = _driver.find_element(By.XPATH, question_text1).text
        question_text2_bool = _driver.find_element(By.XPATH, question_text2).text
        question_text3_bool = _driver.find_element(By.XPATH, question_text3).text
        question_file1_bool = _driver.find_element(By.XPATH, question_file1).text
        question_file2_bool = _driver.find_element(By.XPATH, question_file2).text
        question_file3_bool = _driver.find_element(By.XPATH, question_file3).text

        time.sleep(0.1)
        cycle_3(_driver, question_file1_bool, question_text1_bool, question_1)
        cycle_3(_driver, question_file2_bool, question_text2_bool, question_2)
        cycle_3(_driver, question_file3_bool, question_text3_bool, question_3)

        time.sleep(0.1)
        wait_submit(_driver)


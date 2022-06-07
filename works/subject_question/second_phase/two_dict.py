import time

from selenium.webdriver.common.by import By
from common.input_cycle import *
from common.wait_submit import wait_submit
from works.subject_question.second_phase.information import *
from tqdm import tqdm


def Second_dict_correct(_driver, value):

    time.sleep(2)
    _driver.find_element(By.XPATH, work_variable(value)).click()
    time.sleep(1)
    people_count = int(_driver.find_element(By.XPATH, people_num).text.split("人")[0])
    people_print = str(people_count)
    print('当前作业任务为:作业' + value + ',需要批改的作业共计:' + people_print + '份')

    for i in tqdm(range(1, people_count + 1)):
        for_click = _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a")
        for_click.click()

        time.sleep(0.3)
        question_text1_bool = _driver.find_element(By.XPATH, question_text1).text
        question_text2_bool = _driver.find_element(By.XPATH, question_text2).text
        question_file1_bool = _driver.find_element(By.XPATH, question_file1).text
        question_file2_bool = _driver.find_element(By.XPATH, question_file2).text

        time.sleep(0.3)
        cycle(_driver, question_file1_bool, question_text1_bool, question_1)
        cycle(_driver, question_file2_bool, question_text2_bool, question_2)

        time.sleep(0.2)

        wait_submit(_driver)


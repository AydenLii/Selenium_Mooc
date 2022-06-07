import time

from selenium.webdriver.common.by import By


from common.input_cycle import *
from common.wait_submit import exam_wait_submit, wait_submit

from tqdm import tqdm

from works.subject_question.second_phase.information import *


def Second_dict(_driver):
    time.sleep(2)
    _driver.find_element(By.XPATH, work_variable(1)).click()
    time.sleep(1)
    people_count = int(_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/h2/span').text.split("人")[0])
    people_print = str(people_count)
    print('需要批改的考试共计:' + people_print + '份')

    for i in tqdm(range(1, people_count + 1)):
        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a").click()

        time.sleep(0.3)
        question_text1_bool = _driver.find_element(By.XPATH, question_text1).text
        question_file1_bool = _driver.find_element(By.XPATH, question_file1).text
        question_file_two = _driver.find_element(By.XPATH, Second_text1).text

        cycle(_driver, question_file1_bool, question_text1_bool, question_1)
        cycle_exam_two(_driver, question_file_two, Second_input1)

        time.sleep(0.1)
        wait_submit(_driver)

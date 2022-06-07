import time

from selenium.webdriver.common.by import By


from common.input_cycle import *
from common.wait_submit import exam_wait_submit

from tqdm import tqdm

from works.subject_question.second_phase.information import *


def Second_examination(_driver):
    time.sleep(2)
    _driver.get(theTestPage)
    time.sleep(1)
    people_count = int(_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/h2/span').text.split("人")[0])
    people_print = str(people_count)
    print('需要批改的考试共计:' + people_print + '份')

    for i in tqdm(range(1, people_count + 1)):
        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a").click()

        time.sleep(0.3)
        question_file_one = _driver.find_element(By.XPATH, TestPage_file_one).text
        question_file_two = _driver.find_element(By.XPATH, TestPage_file_two).text
        cycle_exam_two(_driver, question_file_one, TestPage_input_one)
        cycle_exam_two(_driver, question_file_two, TestPage_input_two)

        time.sleep(0.1)
        exam_wait_submit(_driver)

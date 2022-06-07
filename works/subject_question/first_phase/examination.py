import time

from selenium.webdriver.common.by import By


from common.input_cycle import *
from common.wait_submit import exam_wait_submit

from tqdm import tqdm

from works.subject_question.first_phase.information import *


def first_examination(_driver):
    time.sleep(2)
    _driver.get(theTestPage)
    time.sleep(1)
    people_count = int(_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/h2/span').text.split("人")[0])
    people_print = str(people_count)
    print('需要批改的考试共计:' + people_print + '份')

    for i in tqdm(range(1, people_count + 1)):
        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a").click()

        time.sleep(0.3)
        question_text_bool = _driver.find_element(By.XPATH, TestPage_text).text
        question_file_bool = _driver.find_element(By.XPATH, TestPage_file).text
        cycle_exam(_driver, question_file_bool, question_text_bool, TestPage_input)

        time.sleep(0.1)
        exam_wait_submit(_driver)



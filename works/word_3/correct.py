import time

from selenium.webdriver.common.by import By
from common.input_cycle import *
from works.work_2.information import *
from tqdm import tqdm




def work_2_correct(_driver):
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

    for i in tqdm(range(1, people_count + 1)):

        _driver.find_element(By.XPATH, "//*[@id=\"container\"]/div[1]/div[2]/ul/li[" + str(i) + "]/a").click()

        time.sleep(0.4)
        question_text1_bool = _driver.find_element(By.XPATH, question_text1).text
        question_text2_bool = _driver.find_element(By.XPATH, question_text2).text
        question_file1_bool = _driver.find_element(By.XPATH, question_file1).text
        question_file2_bool = _driver.find_element(By.XPATH, question_file2).text

        cycle(_driver, question_file1_bool, question_text1_bool, question_1)
        cycle(_driver, question_file2_bool, question_text2_bool, question_2)
        time.sleep(0.4)
        _driver.find_element(By.CSS_SELECTOR, "#submitHomeWork").click()

        _driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(0.5)
        _driver.find_element(By.CLASS_NAME, "sgBtn").click()
        time.sleep(0.5)



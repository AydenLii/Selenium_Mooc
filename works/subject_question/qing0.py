import time

from selenium.webdriver.common.by import By
from common.input_cycle import *
from common.wait_submit import wait_submit
from works.subject_question.second_phase.information import *
from tqdm import tqdm


def qing0(_driver, people_count):
    for i in tqdm(range(1, people_count + 1)):
        _driver.get(
            'https://mooc.icve.com.cn/design/workExam/onlineExam/onlineExamStu.html?courseOpenId=x6nvaeouv5tfvankjlmxsq&examId=warvaeoualfpi67gb9qgng#page=250')
        _driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) .preview").click()
        time.sleep(0.5)
        _driver.find_element(By.XPATH, '//*[@id="againHomework"]').click()
        _driver.find_element(By.CLASS_NAME, 'sgBtn').click()



from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random


def input_score_random(_driver, _xpath, min_score, max_score):
    """
    :param _driver: 当前 Driver
    :param _xpath: 分数输入框 XPATH 地址
    :param min_score: 最小分数
    :param max_score: 最大分数
    :return:
    """
    score = random.randint(min_score, max_score)
    send_a = _driver.find_element(By.XPATH, _xpath)
    send_a.send_keys(Keys.CONTROL, 'a')
    send_score = _driver.find_element(By.XPATH, _xpath)
    send_score.send_keys(score)


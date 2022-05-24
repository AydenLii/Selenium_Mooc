from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def input_score(_driver, _xpath, score):
    """
    :param _driver: 当前 Driver
    :param _xpath: 分数输入框 XPATH 地址
    :param score: 输入分数
    :return:
    """
    _driver.find_element(By.XPATH, _xpath).send_keys(Keys.CONTROL, 'a')
    _driver.find_element(By.XPATH, _xpath).send_keys(score)


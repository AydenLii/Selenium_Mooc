from selenium.webdriver.common.by import By

from works.subject_question.second_phase.two_dict import Second_dict_correct


def second_accessory(_driver, value):
    _driver.find_element(By.XPATH, "//option[@value='20']").click()
    Second_dict_correct(_driver, value)
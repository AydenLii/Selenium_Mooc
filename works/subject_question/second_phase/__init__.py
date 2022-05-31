from selenium.webdriver.common.by import By

from works.subject_question.second_phase.two_dict import two_dict_correct


def second_accessory(_driver, value):

    if value == 1:
        print("还未开发")
    else:
        _driver.find_element(By.XPATH, "//option[@value='20']").click()
        two_dict_correct(_driver, value)
from works.subject_question.first_phase.three_dict import three_dict_correct
from works.subject_question.first_phase.two_dict import two_dict_correct
from selenium.webdriver.common.by import By


def first_accessory(_driver, value):
    course_list = [2, 7]
    if_value = int(value)
    if if_value in course_list:
        two_dict_correct(_driver, value)
    elif value == '11':
        _driver.find_element(By.XPATH, "//option[@value='20']").click()
        three_dict_correct(_driver, value)
    else:
        three_dict_correct(_driver, value)


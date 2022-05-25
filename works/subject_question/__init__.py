from works.subject_question.three_dict import three_dict_correct
from works.subject_question.two_dict import two_dict_correct
from selenium.webdriver.common.by import By



def accessory(_driver, value):
    if value == '2':
        two_dict_correct(_driver, value)
    elif value == '11':
        _driver.find_element(By.XPATH, "//option[@value='20']").click()
        three_dict_correct(_driver, value)
    else:
        three_dict_correct(_driver, value)

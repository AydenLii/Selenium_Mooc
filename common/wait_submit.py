from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_submit(_driver):
    wait = WebDriverWait(_driver, 10, 0.5)
    wait.until(expected_conditions.presence_of_element_located((By.ID, "submitHomeWork"))).click()
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sgBtn"))).click()
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sgBtn"))).click()

def exam_wait_submit(_driver):
    wait = WebDriverWait(_driver, 5, 0.5)
    wait.until(expected_conditions.presence_of_element_located((By.ID, "bntSubmit"))).click()
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sgBtn"))).click()
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sgBtn"))).click()


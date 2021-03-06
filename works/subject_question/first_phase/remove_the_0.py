import time

from selenium.webdriver.common.by import By
from works.subject_question.first_phase.information import remove_page
from tqdm import tqdm


def remove_0(_driver, people_count):
    for i in tqdm(range(1, people_count + 1)):
        _driver.get(remove_page)
        _driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) .preview").click()
        time.sleep(0.5)
        _driver.find_element(By.XPATH, '//*[@id="againHomework"]').click()
        _driver.find_element(By.CLASS_NAME, 'sgBtn').click()


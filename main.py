import driver
from works.work_3.correct import work_3_correct
from works.work_1.correct import work_1_correct
from works.work_2.correct import work_2_correct

if __name__ == "__main__":
    driver = driver.diver_web()
   # work_1_correct(driver)
   # work_2_correct(driver)
    work_3_correct(driver)


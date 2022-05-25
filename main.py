import driver
from works.work_3.correct import work_3_correct
from works.work_1.correct import work_1_correct
from works.work_2.correct import work_2_correct

if __name__ == "__main__":

    value = input('输入审批课程索引值(1~11):\n')
    driver = driver.diver_web()

    if value == '1':
        work_1_correct(driver)
    elif value == '2':
        work_2_correct(driver)
    elif value == '3':
        work_3_correct(driver)

    driver.quit()

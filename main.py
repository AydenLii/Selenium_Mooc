import driver
from works.work_3.correct import work_3_correct
from works.work_1.correct import work_1_correct
from works.work_2.correct import work_2_correct


def init(_driver, _value):

    if _value == 1:
        work_1_correct(_driver)
    elif _value == 2:
        work_2_correct(_driver)


if __name__ == "__main__":
    value = input('输入审批课程索引值:\n')
    driver = driver.diver_web()
<<<<<<< Updated upstream
   # work_1_correct(driver)
   # work_2_correct(driver)
    work_3_correct(driver)

=======
    init(driver, value)
>>>>>>> Stashed changes

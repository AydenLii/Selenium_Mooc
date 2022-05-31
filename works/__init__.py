from works.essay_question.correct import work_1_correct
from works.subject_question import *

from works.subject_question.first_phase.examination import one_examination
from works.subject_question.first_phase.remove_the_0 import remove_0


def test_task():
    driver = diver_web_1()
    one_examination(driver)

def qing_test():
    driver = diver_web_1()
    remove_0(driver, 44)

def works_statr():
    course_value = input('输入审批期数索引值(1~2):')
    if course_value == '2':
        # works_statr_2()
        works_statr_auto_2()
    elif course_value == '1':
        # works_statr_1()
        works_statr_auto_1()




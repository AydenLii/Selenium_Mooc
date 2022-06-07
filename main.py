import threading

from works import works_statr, works_statr_1, test_task, works_statr_auto_1, qing_test, works_statr_2

if __name__ == "__main__":
    works_statr()
    # works_statr_2(1)
    # test_task()
    # t1 = threading.Thread(target=works_statr_2, args=("14",))
    # t2 = threading.Thread(target=works_statr_2, args=("13", ))
    # t3 = threading.Thread(target=test_task())
    # t4 = threading.Thread(target=works_statr_2, args=("8",))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

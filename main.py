import threading

from works import works_statr, works_statr_1, test_task, works_statr_auto_1, qing_test

if __name__ == "__main__":
    # test_task()
    works_statr()
    # t1 = threading.Thread(target=works_statr_1, args=("9",))
    # t2 = threading.Thread(target=works_statr_auto_1)
    # t3 = threading.Thread(target=test_task())
    # t4 = threading.Thread(target=works_statr_1, args=("10",))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

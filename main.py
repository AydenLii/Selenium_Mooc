import driver
from works.work_2.correct import work_2_correct

if __name__ == "__main__":
    driver = driver_init()  # 浏览器初始化
    read_cookies(driver)  # 读取本地cookie文本文件,写入浏览器,刷新网页查看是否登录成功
    to_homework_exam_page(driver)
    run_work_two(driver)

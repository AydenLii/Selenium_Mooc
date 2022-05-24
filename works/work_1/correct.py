import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.to_url import to_url


# 批阅 <体育（篮球）--第四次开课> 的 <第一次课作业>

def work_1_correct(_driver):
    # 跳转到 <未审批> 页面
    to_url(_driver, "https://mooc.icve.com.cn/design/workExam/homework/preview.html?courseOpenId=x6nvaeouv5tfvankjlmxsq" \
                    "&homeworkId=warvaeouy4zia4becmb7ew&pageType=mark ")

    #   获取当前未审批人数 (234人 -> 234)
    people_num = _driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/h2/span').text[:-1]

    for i in range(2, int(people_num) + 1):
        check_answers(_driver)
        time.sleep(2)
        _driver.find_element(By.XPATH, '//*[@id="submitHomeWork"]').click()  # 点击 <批阅> 按钮
        _driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[3]/div/a[1]').click()  # 确定批阅
        time.sleep(2)
        # 点击 <确定> 关闭弹窗
        _driver.find_element(By.CLASS_NAME, 'sgBtn').click()
        time.sleep(2)
        # 点击左侧列表切换下一个同学
        _driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/ul/li[' + str(i) + ']/a').click()
        time.sleep(3)


def check_answers(_driver):
    answer_1 = _driver.find_element(By.XPATH,
                                    '//*[@id="questionContainer"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div').text
    input_1 = _driver.find_element(By.XPATH,
                                   '//*[@id="questionContainer"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/input')
    answer_2 = _driver.find_element(By.XPATH,
                                    '//*[@id="questionContainer"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div['
                                    '4]/div[2]/div').text
    input_2 = _driver.find_element(By.XPATH,
                                   '//*[@id="questionContainer"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div['
                                   '3]/div/input')
    answer_3 = _driver.find_element(By.XPATH,
                                    '//*[@id="questionContainer"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div['
                                    '4]/div[2]/div').text
    input_3 = _driver.find_element(By.XPATH,
                                   '//*[@id="questionContainer"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div['
                                   '3]/div/input')
    answer_4 = _driver.find_element(By.XPATH,
                                    '//*[@id="questionContainer"]/div/div[2]/div[5]/form/div/div[1]/div[2]/div['
                                    '4]/div[2]/div').text
    input_4 = _driver.find_element(By.XPATH,
                                   '//*[@id="questionContainer"]/div/div[2]/div[5]/form/div/div[1]/div[2]/div['
                                   '3]/div/input')

    answer_list = [answer_1, answer_2, answer_3, answer_4]  # 答案列表
    input_list = [input_1, input_2, input_3, input_4]  # 分数框<input>对象列表
    correct_answer_list = ['银', '13', '1891', '奈史密斯']  # 正确的答案包含的字符串列表

    # 填入分数
    for i in range(4):
        # ctl+A全选<input>内的值
        input_list[i].send_keys(Keys.CONTROL, "a")
        if correct_answer_list[i] in answer_list[i] and len(answer_list[i]) != 0:
            input_list[i].send_keys("25")
        else:
            input_list[i].send_keys("0")

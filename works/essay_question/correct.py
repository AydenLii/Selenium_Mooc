import time
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.to_url import to_url


def work_1_correct(_driver):
    # 跳转到 <未审批> 页面
    to_url(_driver,
           "https://mooc.icve.com.cn/design/workExam/homework/preview.html?courseOpenId=x6nvaeouv5tfvankjlmxsq"
           "&homeworkId=warvaeouy4zia4becmb7ew&pageType=mark")
    # 获取当前未审批人数
    people_num = int(_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/h2/span').text[:-1])
    print('当前作业任务为:作业1' + ',需要批改的作业共计:' + str(people_num) + '份')

    for i in tqdm(range(people_num)):  # //循环people_num次
        check_answers(_driver)
        _driver.find_element(By.XPATH, '//*[@id="submitHomeWork"]').click()  # 点击 <批阅> 按钮
        _driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[3]/div/a[1]').click()  # 确定批阅
        time.sleep(1.5)
        _driver.find_element(By.CLASS_NAME, 'sgBtn').click()  # 点击 <确定> 关闭弹窗

        # 判断当前是否是最后一名同学
        if i != people_num - 1:
            # 点击左侧列表切换下一个同学
            _driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/ul/li[' + str(i + 2) + ']/a').click()
            time.sleep(1)


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

    answer_list = [answer_1, answer_2, answer_3, answer_4]  # 提交答案列表
    input_list = [input_1, input_2, input_3, input_4]  # 分数框<input>对象列表
    correct_answer_list = ['银', '13', '1891', '奈史密斯']  # 正确答案包含的字符串列表

    # 填入分数
    for i in range(4):
        # ctl+A全选<input>内的值
        input_list[i].send_keys(Keys.CONTROL, "a")
        if correct_answer_list[i] in answer_list[i] and len(answer_list[i]) != 0:
            input_list[i].send_keys("25")
        else:
            input_list[i].send_keys("0")

import os
import time
import json
from selenium.webdriver.common.by import By

def get_cookies(_driver, url):
    if not os.path.exists('../out/'):  # 判断<out>文件夹是否存在
        os.makedirs('../out/')  # 不存在则新建<out>文件夹
    os.chdir('../out/')
    _driver.get(url)
    _driver.find_element(By.ID, "home-login-register").click()
    time.sleep(30)  # 进行扫码登录
    dict_cookies = _driver.get_cookies()  # 获取list的cookies
    json_cookies = json.dumps(dict_cookies)  # 转换成字符串保存

    with open('../out/cookie.txt', 'w') as f:
        f.write(json_cookies)
    print('cookies保存成功！')


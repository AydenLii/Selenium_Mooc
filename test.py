from selenium import webdriver

def test():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("范冰冰")  # 在百度输入框中输入范冰冰

    driver.find_element_by_id("kw")



def test():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("k11w").send_keys("范冰冰")

if __name__ == "__main__":
    test()
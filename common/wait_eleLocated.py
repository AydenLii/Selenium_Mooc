from datetime import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_eleLocated(self, loc, timeout=30, poll_frequency=0.5, model=None):
    """
    :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)，示例：(By.ID, "kw")
    :param timeout:超时时间
    :param poll_frequency:轮询频率
    :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
    :return:None
    """
    self.logger.info(f'等待"{model}"元素,定位方式:{loc}')
    try:
        start = datetime.now()
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        end = datetime.now()
        self.logger.info(f'等待"{model}"时长:{end - start}')
    except TimeoutException:
        self.logger.exception(f'等待"{model}"元素失败,定位方式:{loc}')
        # 截图
        self.save_webImgs(f"等待元素[{model}]出现异常")
        raise
# 示例
'''
target = EC.visibility_of_element_located(By.ID,'user')
'''
# 配合until()使用（等待元素可见）
# 5表示 最长超时时间，默认以秒为单位； 1表示检测的间隔步长，在等待期间，每隔一定时间(默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.
'''
WebDriverWait(driver, 5, 1).until(EC.visibility_of_element_located(By.ID,'user'))
'''
# 配合until_not()使用（等待元素不可见）
'''
WebDriverWait(driver, 5, 1).until_not(EC.visibility_of_element_located(By.ID,'user'))
'''
# 在类中封装为一个函数
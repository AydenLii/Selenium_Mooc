from common.input_score import input_score
from common.input_score_random import input_score_random


def cycle(_driver, file, text, question):
    """
    :param _driver: 当前 Driver
    :param file: 输入文件类型的答案
    :param text: 输入文本类型的答案
    :param question: 分数框地址
    :return:
    """
    if file == "未上传附件":
        if text == " ":
            input_score(_driver, question, 0)
        else:
            input_score_random(_driver, question, 30, 33)
    else:
        input_score_random(_driver, question, 43, 45)
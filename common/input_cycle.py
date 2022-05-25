from common.input_score import input_score
from common.input_score_random import input_score_random


def cycle_2(_driver, file, text, question):
    """
    !!!用于判断2个选项的题目
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

def cycle_3(_driver, file, text, question):
    """
    !!!用于判断三个选项的题目
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
            input_score_random(_driver, question, 20, 22)
    else:
        input_score_random(_driver, question, 30, 33)

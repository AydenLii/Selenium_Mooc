people_num = "/html/body/div[2]/div/div/div/form/div/div[1]/div[2]/h2/span"
question_text1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div"
question_text2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[4]/div[2]/div"
question_text3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[4]/div[2]/div"
question_file1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[3]/a"
question_file2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[4]/div[3]/a"
question_file3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[4]/div[3]/a"
question_1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/input"
question_2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[3]/div/input"
question_3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[3]/div/input"


def work_variable(value):
    work_value = '//*[@id="maintab_homework"]/li['+value+']/div[2]/a[3]'
    return work_value

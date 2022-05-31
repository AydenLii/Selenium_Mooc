people_num = "/html/body/div[2]/div/div/div/form/div/div[1]/div[2]/h2/span"

# 第一期作业
question_text1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div"
question_text2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[4]/div[2]/div"
question_text3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[4]/div[2]/div"
question_file1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[3]/a"
question_file2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[4]/div[3]/a"
question_file3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[4]/div[3]/a"
question_1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/input"
question_2 = "//*[@id=\"questionContainer\"]/div/div[2]/div[3]/form/div/div[1]/div[2]/div[3]/div/input"
question_3 = "//*[@id=\"questionContainer\"]/div/div[2]/div[4]/form/div/div[1]/div[2]/div[3]/div/input"


# 第一期考试

theTestPage = "https://mooc.icve.com.cn/design/workExam/onlineExam/markPreview.html?courseOpenId" \
              "=x6nvaeouv5tfvankjlmxsq&examId=warvaeoualfpi67gb9qgng "
TestPage_text = "/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div[3]/div[3]/div"
TestPage_file = "/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div[3]/div[4]/a"
TestPage_input = '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div[3]/div[1]/input'

remove_page = 'https://mooc.icve.com.cn/design/workExam/homework/homeworkStu.html?courseOpenId=x6nvaeouv5tfvankjlmxsq&homeworkId=warvaeoug6xmgahqfdc7vw#page=255'


def work_variable(value):
    work_value = '//*[@id="maintab_homework"]/li[' + str(value) + ']/div[2]/a[3]'
    return work_value

people_num = "/html/body/div[2]/div/div/div/form/div/div[1]/div[2]/h2/span"

question_text1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[2]/div"
question_text2 = "//*[@id=\"questionContainer\"]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[4]/div[2]/div"
question_file1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[4]/div[3]/a"
question_file2 = "//*[@id=\"questionContainer\"]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[4]/div[3]/a"
question_1 = "//*[@id=\"questionContainer\"]/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/input"
question_2 = "//*[@id=\"questionContainer\"]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[3]/div/input"

Second_text1 = '/html/body/div[2]/div/div/div/form/div/div[2]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[3]/div[3]/a'
Second_input1 = '/html/body/div[2]/div/div/div/form/div/div[2]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[3]/div[1]/input'
theTestPage = "https://mooc.icve.com.cn/design/workExam/onlineExam/markPreview.html?courseOpenId=sutuaeouilzafewi27dexw&examId=pubuaeoupiffkwxqfoeyw"
TestPage_file_one = "/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div[3]/div[3]/a"
TestPage_file_two = "/html/body/div[2]/div/div/div/div/div[2]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[3]/div[3]/a"
TestPage_input_one = '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div[3]/div[1]/input'
TestPage_input_two = '/html/body/div[2]/div/div/div/div/div[2]/div/div[3]/div[2]/form/div/div[1]/div[2]/div[3]/div[1]/input'


def work_variable(value):
    work_value = '//*[@id="maintab_homework"]/li[' + str(value) + ']/div[2]/a[3]'
    return work_value

# Selenium_Mooc

基于Selenium的Mooc自动化批改学生作业脚本



## 开发说明

本脚本仅为Mooc建课管理后台的学生作业提供**开发样例**，实现批量批改的任务，本脚本使用了`cookie`免密登录的方式实现后续的脚本作业，并引入`tqdn`库实现预览批改作业进度，以及预计时间的功能。

## 第三方库

```python
# pip install -r requirements.txt
selenium>=4.1.0
tqdm
```

## Usage

使用前请正确配置`python>=3.7`+`第三方库`+`chrome`,以及对应的Chrome驱动

- 运行 `driver`文件夹下的 `get——cookie——main.py` ，并在30秒内输入账号密码，以实现在本地生成`cookie.txt`文件进行免密登录。

  ⚠**注意: cookie的默认保存时长为90-120分钟，请注意及时重复步骤，保证程序正常运行。**

- 运行 `main.py` ，并输入对应的需要批改的作业，程序将会自动完成批改任务。

  ⚠ **如果需要: 可取消`works`-`__init__.py`的批量任务注释,以实现批量批改作业。**

## function
- `to_url()` : 跳转至指定url链接网页
- `input_score()` : 在指定input框内输入分数
- `input_score_random()` : 在指定input框内输入随机分数
- `input_cycle.py`:根据题目的不同数量，配置对应的值
- `read_cookies.py`：读取cookie并保存到本地
- `driver_init.py`：被执行网站以及浏览器的配置文件
- `write_in_cookie.py`:读取本地的cookie，并写入浏览器
- `.\works\`:本示例的具体批改任务

## versions

### V1.0

- 完全支持体育第四次作业的批改任务 

- 优化了cookie的储存地址

### V1.1

- 完善了README.md文档
- 新增一次性遍历所有任务功能(被注释)
- 完善了在命令行的输出，以获得完整信息

#### v1.1.2

- 引入了“implicitly_wait(10)”
- 极大的缩短了运行所需要的时间，从原本的2s降低到1秒，600份作业仅需10分钟

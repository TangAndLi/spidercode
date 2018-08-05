from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('http://fanyi.youdao.com/')
#
# driver.find_element_by_id('kw').send_keys('python')
#
# driver.find_element_by_id('kw').submit()

# 增加cookie
driver.add_cookie({'name': 'foo','value': 'bar'})
# 抓取cookie
driver.get_cookie('foo')
for i in driver.get_cookies():
    print(i)


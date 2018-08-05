

from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('hello world')

time.sleep(5)
# 全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# 复制
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'c')
time.sleep(5)
# 删除
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(4)
# 粘贴
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
time.sleep(3)

driver.close()

















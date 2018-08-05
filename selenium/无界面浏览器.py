

import selenium
from selenium import webdriver
import time

# driver = webdriver.Chrome()
# 无头浏览器

options =webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options = options)

driver.get('http://www.baidu.com')
time.sleep(3)
driver.save_screenshot('baidu.png')
driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 等待一个页面加载完成
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 控制操作的时间在10秒以內
# driver.implicitly_wait(10)

# 最多等待15秒  ，必须等待这个元素的出现，根据 By.ID 查找 'kw'的出现 也有许多参数,  节约时间
elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'kw')))

elem.send_keys('selenium')

time.sleep(10)

driver.close()

















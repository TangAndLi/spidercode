from selenium import webdriver
from time import sleep

# 设置
mobileEmulation = {'deviceName': 'iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

# 启动driver
driver = webdriver.Chrome(options=options)

# 访问百度wap页
driver.set_window_size(375, 700)
# driver.get('http://m.baidu.com')
driver.get('http://m.taobao.com')
# driver.get('http://m.jd.com')
sleep(20)

driver.quit()

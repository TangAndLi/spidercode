

from selenium import  webdriver
import time

# 设置
mobilesetting = {'deviceName':'iPhone 6'}
options = webdriver.ChromeOptions()

# 模拟手机
options.add_experimental_option('mobileEmulation',mobilesetting)

# 配置参数
driver = webdriver.Chrome(chrome_options = options)

# 设置浏览器大小
driver.set_window_size(480, 800)

#全屏
driver.maximize_window()

driver.get('https://www.baidu.com')
time.sleep(10)
driver.get('https://www.jd.com')
time.sleep(10)
driver.back() # 后退
time.sleep(5)
driver.forward() # 前进
driver.refresh() # 刷新
driver.close()





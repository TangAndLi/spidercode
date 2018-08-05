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


driver.get('https://www.baidu.com')
time.sleep(1)
elem = driver.find_element_by_id('index-kw')
elem.send_keys('你妹')
time.sleep(1)
click = driver.find_element_by_id('index-bn')
click.click()
time.sleep(10)


driver.close()



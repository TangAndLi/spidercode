


import selenium.webdriver
import selenium
import time

driver = selenium.webdriver.Chrome()
driver.get('https://qzone.qq.com/')
time.sleep(3)
driver.switch_to_frame('login_frame')
elem = driver.find_element_by_id('switcher_plogin')
elem.click()
time.sleep(5)
username = driver.find_element_by_id('u')
password = driver.find_element_by_id('p')
login_btn = driver.find_element_by_id('login_button')
username.send_keys('738951797')
password.send_keys('tl-18077024323')
login_btn.click()
time.sleep(5)
driver.close()

s = driver.current_window_handle









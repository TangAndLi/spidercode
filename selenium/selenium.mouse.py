



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.set_window_size(400,800)
driver.get('https://www.baidu.com')

# 把鼠标移动到设置
above = driver.find_element_by_link_text('设置')

ActionChains(driver).move_to_element(above).perform() #s鼠标停留

ActionChains(driver).move_to_element(above).move_to_element() #移动
ActionChains(driver).move_to_element(above).context_click() # 鼠标单击
ActionChains(driver).move_to_element(above).double_click()  # 双击
ActionChains(driver).move_to_element(above).drag_and_drop() # 拖放
time.sleep(10)

driver.close()





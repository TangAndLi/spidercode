

from selenium import webdriver
import time
#
from selenium.webdriver.common.action_chains import ActionChains
#
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)
above = driver.find_element_by_link_text('设置')
# 鼠标悬浮
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

# 选择下拉框id
sel = driver.find_element_by_id('nr')
# 选择索引 0,1,2....
Select(sel).select_by_index(2)

driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(3)

# 给弹框点击确定
driver.switch_to.alert.accept()

driver.close() # 关闭当前
time.sleep(2)
driver.quit() # 关闭所有

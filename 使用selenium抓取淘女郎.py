#coding:utf-8
from selenium import webdriver
from urllib.error import URLError

driver = webdriver.Chrome()

driver.get('https://v.taobao.com/v/content/live?')

driver.implicitly_wait(2)
# 获取列表使用 elements  单个使用element
div_list = driver.find_elements_by_xpath('//div[@class="anchor-card-content"]/div')
# print(div_list)
for div, i in zip(div_list, range(len(div_list))):

    driver.implicitly_wait(5)
    try:
        print('正在下载第%d张....' % (i+1,))
        img_src = div.find_element_by_xpath('.//div[@class="ice-img sharp anchor-avatar"]/img').get_attribute('src')
        driver.implicitly_wait(3)
        print(img_src)
    except Exception:
        print('请求网络失败..')
    # with open()
driver.quit()














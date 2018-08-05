from selenium import webdriver
import time
import re, requests


def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://music.163.com/#/discover/toplist?id=2250011882")
    time.sleep(5)
    driver.switch_to.frame('g_iframe')
    return driver


def parse(driver):
    tr_list = driver.find_elements_by_xpath('//tr')[1:]
    # print(tr_list)
    for tr in tr_list:
        # print(tr.text)
        song_name = tr.find_elements_by_xpath('.//td[3]/div/span[2]')[0].get_attribute("data-res-name")
        song_id = tr.find_elements_by_xpath('.//td[3]/div/a')[0].get_attribute("data-res-id")
        print(song_name, ',', song_id)
    return driver


def driver_close(driver):
    driver.switch_to.default_content()
    driver.quit()


def main():
    driver = get_driver()
    driver_parse = parse(driver)
    driver_close(driver_parse)


if __name__ == '__main__':
    main()

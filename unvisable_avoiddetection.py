# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/11 10:46
# @File :unvisable_avoiddetection.py
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions


def unvisable():
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')
    return chrome_option

def avoiddetection():
    option=ChromeOptions()
    option.add_experimental_option('excludeSwitches',['enable-automation'])
    return option

# chrome_options=unvisable()
# option=avoiddetection()
# bro=webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)
#
# bro.get('https://www.baidu.com')
# print(bro.page_source)
# time.sleep(5)
# bro.quit()


# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/21 21:18
# @File :search.py
import time


#搜索操作
def search_option(url,name,bro):
    #访问搜书网站首页
    bro.get(url)
    time.sleep(5)

    #定位到搜索区域
    def search_area(brower,url):
        '''
        :param brower: 浏览驱动对象
        :param url: 对应网址
        :return: bro.page_source 搜索结果页面
        '''
        bro = brower
        if url == 'https://www.xiashu9.com/':
            area = bro.find_element_by_name('searchkey')
        elif url == 'https://www.mapleso.top/':
            area = bro.find_element_by_tag_name('input')
        else:
            return f'网站不可用'

        return area

    #定位到搜索按钮
    def search_button(brower, url):
        bro = brower

        if url == 'https://www.xiashu9.com/':
            button = bro.find_element_by_xpath('//*[@id="post"]/button')
        elif url == 'https://www.mapleso.top/':
            button = bro.find_element_by_class_name('search')
        else:
            return f'网站不可用'

        return button

    #输入要搜索的书
    search_area = search_area(brower=bro, url=url)
    search_content = name
    search_area.send_keys(search_content)
    time.sleep(1)

    #点击搜索按钮
    search_button = search_button(brower=bro, url=url)
    search_button.click()
    time.sleep(5)

    return bro.page_source


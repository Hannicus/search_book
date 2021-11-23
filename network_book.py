# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/21 21:23
# @File :network_book.py
import time
from lxml import etree

#爬取书的详情页面
def book_detail(detail_url,bro):
    '''

    :param detail_url: 书籍的详情页面
    :param bro: webdriver
    :return: None
    '''


    #访问详情页面url
    bro.get(detail_url)
    time.sleep(1)

    #解析网页，找出下载链接
    detail_tree=etree.HTML(bro.page_source)
    # print('下载链接为：')
    download_url=detail_tree.xpath('/html/body/div[2]/div[4]/div/div[2]/ul/li[3]/a/@href')[0]
    # print(download_url)
    return download_url
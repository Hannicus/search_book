# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/21 21:20
# @File :published_book.py
import re
import urllib.parse
from lxml import etree


#爬取书籍的详情页面
def book_detail(detail_url,bro):
    '''

    :param detail_url: 书籍的详情页面
    :param bro: webdriver
    :return: None
    '''

    import time
    #访问详情页面url
    bro.get(detail_url)
    time.sleep(5)

    #解析网页
    detail_tree = etree.HTML(bro.page_source)
    #获取同一本书的多个item
    book_list = detail_tree.xpath('//*[@id="app"]/div/div/div[1]/div[6]/div')
    if len(book_list)==0:
        return '无结果'

    #遍历每个item找到每个item的属性和特征
    num=0
    for book in book_list:

        #下载文件的大小
        book_size = book.xpath('./p[1]/span[1]/text()')[0]

        #文件的名字，后缀为文件的格式，例如：txt,equb,pdf。。。
        book_name = book.xpath('./p[1]/span[2]/text()')[0]
        # print(book_name)

        #文件下载的次数（反映文件的受欢迎程度和成功下载的概率）
        download_num = book.xpath('./div/button/text()')[0]
        num=str(num)
        #打印文件的大小，名字，下载次数
        # print(num+'.',book_size,book_name,download_num,'\n')
        num=int(num)
        num=num+1

        #通过隐藏在网页源代码中的时间和秒获得下载链接
        time = book.xpath('./p[2]//text()')[0]
        time.format()
        time = re.sub(' ', '', time)
        time = re.sub(',上传者:', '', time)
        time = re.sub(':', '', time)
        time = re.sub('-', '/', time)
        second = time[-6:]
        second = int(second)
        second = second - 1
        second = str(second)
        # print(second)

        time = time[:11]
        time = time.strip()
        # print(time)

        #将文件名转码，作为网站的一部分进行拼接
        book_name = urllib.parse.quote(book_name)
        # print(book_name)

        # 'https://ebookimg.lorefree.com/assets/file/2019/04/27/162913/%E4%B8%89%E4%BD%93.epub'
        #参照上面url的范例，对几个元素进行拼接获得下载链接
        book_download_url = 'https://ebookimg.lorefree.com/assets/file/' + time + '/' + second + '/' + book_name
        return book_download_url
        # print('下载链接为：')
        # print(book_download_url,'\n')

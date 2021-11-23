# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/21 9:20
# @File :main.py

import sys
from PyQt5.QtWidgets import QComboBox,QLineEdit,QLabel,QPushButton,QWidget,QApplication,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.Qt import *
from PyQt5 import QtGui
from selenium import webdriver
import time
from unvisable_avoiddetection import unvisable
from unvisable_avoiddetection import avoiddetection
from search import search_option
from result_analyse import search_result_annalyse
import published_book
import network_book
from UI import Example

app = QApplication(sys.argv)
win = Example()
win.show()
sys.exit(app.exec_())

























# def back():
#     # 'https://www.xiashu9.com/'
#     # 'https://www.mapleso.top/'
#     url = 'https://www.xiashu9.com/'
#
#     #设置webdriver参数
#     chrome_option = unvisable()
#     option = avoiddetection()
#     bro = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_option,options=option)
#
#     #搜索
#     page_text = search_option(url=url, bro=bro)
#     #搜索结果
#     result = search_result_annalyse(url=url, page_text=page_text)
#     #查询
#     result_id = eval(input('请输入想要查看的结果编号：'))
#
#     #判断
#     detail_url = result[result_id][1]
#     if url == 'https://www.mapleso.top/':
#         published_book.book_detail(detail_url=detail_url, bro=bro)
#     elif url == 'https://www.xiashu9.com/':
#         network_book.book_detail(detail_url=detail_url, bro=bro)


# if __name__=='__main__':
#     start=time.time()
#     main()
#     end=time.time()
#     print(end-start)




# def search_option(url,bro):
#
#     bro.get(url)
#     time.sleep(5)
#
#     def search_area(brower, url):
#         '''
#
#         :param brower: 浏览驱动对象
#         :param url: 对应网址
#         :return:
#         '''
#         bro = brower
#         if url == 'https://www.xiashu9.com/':
#             area = bro.find_element_by_name('searchkey')
#         elif url == 'https://www.mapleso.top/':
#             area = bro.find_element_by_tag_name('input')
#         else:
#             return f'网站不可用'
#
#         return area
#
#     def search_button(brower, url):
#         bro = brower
#
#         if url == 'https://www.xiashu9.com/':
#             button = bro.find_element_by_xpath('//*[@id="post"]/button')
#         elif url == 'https://www.mapleso.top/':
#             button = bro.find_element_by_class_name('search')
#         else:
#             return f'网站不可用'
#
#         return button
#
#     search_area = search_area(brower=bro, url=url)
#     search_content = input('请输入要搜索的书籍名称：')
#     search_area.send_keys(search_content)
#     time.sleep(1)
#
#     # searchm
#     search_button = search_button(brower=bro, url=url)
#     search_button.click()
#     time.sleep(5)
#
#     return bro.page_source
#
#
#
#
# def search_result_annalyse(url,page_text):
#
#     if url=='https://www.mapleso.top/':
#         tree = etree.HTML(page_text)
#         item_list = tree.xpath('/html/body/div[1]/div[2]/div')
#         num = 1
#         result = {}
#         for item in item_list:
#             data = []
#             name = item.xpath('./a/h3//text()')
#             str_name=''.join(name)
#             data.append(str_name)
#
#             book_url = item.xpath('./a/div/text()')
#             if len(book_url) != 0:
#                 data.append(book_url[0])
#             else:
#                 data.append(' ')
#             situation = item.xpath('./div/text()')
#             if len(situation) != 0:
#                 situation[0] = re.sub('\n', '', situation[0])
#                 data.append(situation[0])
#             else:
#                 data.append(' ')
#             # num=str(num)
#             result[num] = data
#             print(num, ':', result[num][0], '\n', 'situation:', result[num][2])
#             # num=int(num)
#             num = num + 1
#
#         return result
#
#     elif url=='https://www.xiashu9.com/':
#         tree=etree.HTML(page_text)
#         item_list=tree.xpath('/html/body/div[2]/div[5]/ol/li')
#         num=1
#         result={}
#         for item in item_list:
#             data=[]
#
#             name=item.xpath('./a/div/h4/text()')[0]
#             data.append(name)
#
#
#             book_url=item.xpath('./a/@href')[0]
#             book_url='https://www.xiashu9.com'+book_url
#             data.append(book_url)
#
#             info=item.xpath('./a/div/p/text()')[0]
#             data.append(info)
#
#             author=item.xpath('./a/div/div/div[1]/span//text()')[0]
#             if len(author)!=0:
#                 data.append(author)
#
#             attribute=item.xpath('./a/div/div/div[2]/span/em[1]/text()')[0]
#             data.append(attribute)
#
#             status=item.xpath('./a/div/div/div[2]/span/em[2]/text()')[0]
#             data.append(status)
#
#             result[num]=data
#             print(num, ':', result[num][0],'author:', result[num][3],'attribute:',result[num][4],'status:',result[num][5])
#             print('url:',result[num][1])
#             print('info:')
#             print(result[num][2])
#
#             num=num+1
#         return result
#
#
#
#
#
#
#
#
#
# def book_detail(detail_url,bro):
#     import time
#     bro.get(detail_url)
#     time.sleep(5)
#
#     # bro.find_elements_by_xpath()
#     # detail_tree=etree.HTML(bro.page_source)
#     detail_tree = etree.HTML(bro.page_source)
#     book_list = detail_tree.xpath('//*[@id="app"]/div/div/div[1]/div[6]/div')
#     if len(book_list)==0:
#         return '无结果'
#     num=0
#     for book in book_list:
#         '//*[@id="70347"]/p[1]/span[2]'
#         './p[1]/span[1]'
#         book_size = book.xpath('./p[1]/span[1]/text()')[0]
#
#         book_name = book.xpath('./p[1]/span[2]/text()')[0]
#         form = book_name.split('.')[-1]
#         # print(book_name)
#         download_num = book.xpath('./div/button/text()')[0]
#         num=str(num)
#         print(num+'.',book_size,book_name,download_num,'\n')
#         num=int(num)
#         num=num+1
#         'https://ebookimg.lorefree.com/assets/file/' + 'year' + 'month' + 'day' + 'second-1' + 'str.turn' + '.equb'
#
#         time = book.xpath('./p[2]//text()')[0]
#         time.format()
#         time = re.sub(' ', '', time)
#         time = re.sub(',上传者:', '', time)
#         time = re.sub(':', '', time)
#         time = re.sub('-', '/', time)
#         second = time[-6:]
#         second = int(second)
#         second = second - 1
#         second = str(second)
#         # print(second)
#
#         time = time[:11]
#         time = time.strip()
#         # print(time)
#
#         book_name = urllib.parse.quote(book_name)
#         # print(book_name)
#
#         'https://ebookimg.lorefree.com/assets/file/2019/04/27/162913/%E4%B8%89%E4%BD%93.epub'
#         book_download_url = 'https://ebookimg.lorefree.com/assets/file/' + time + '/' + second + '/' + book_name
#         print('下载链接为：')
#         print(book_download_url,'\n')
#
# def xiashu_detail(detail_url,bro):
#     bro.get(detail_url)
#     time.sleep(1)
#     detail_tree=etree.HTML(bro.page_source)
#     print('下载链接为：')
#     download_url=detail_tree.xpath('/html/body/div[2]/div[4]/div/div[2]/ul/li[3]/a/@href')[0]
#     print(download_url)
#


# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/21 21:19
# @File :result_analyse.py
import time
from lxml import etree
import re


#对搜索的结果进行分析
def search_result_annalyse(url,page_text):

    '''
    :param url: 来源的搜书网站
    :param page_text: 搜索结果页面
    :return: result   返回提取整理过的搜索结果
    '''



    #判断：如果是出版书的下载，使用枫影搜索
    if url=='https://www.mapleso.top/':
        #解析网页，获得结果item_list
        tree = etree.HTML(page_text)
        item_list = tree.xpath('/html/body/div[1]/div[2]/div')

        #遍历列表，获取每个item的属性和特征
        num = 1
        result = {}    #用于存储全部item的数据
        for item in item_list:
            #新建data列表存储每个item的数据
            data = []
            #获取item的名字
            name = item.xpath('./a/h3//text()')
            str_name=''.join(name)
            data.append(str_name)

            #获取item的url
            book_url = item.xpath('./a/div/text()')
            if len(book_url) != 0:
                data.append(book_url[0])
            else:
                data.append(' ')

            #获取item的详情
            situation = item.xpath('./div/text()')
            if len(situation) != 0:
                situation[0] = re.sub('\n', '', situation[0])
                data.append(situation[0])
            else:
                data.append(' ')

            #将data保存到result中
            result[num] = data
            #提取并打印item的名字,详情
            # print(num, ':', result[num][0], '\n', 'situation:', result[num][2])
            num = num + 1

        return result

    #判断：如果是网络小说的下载，使用下书网url
    elif url=='https://www.xiashu9.com/':
        #解析网页
        tree=etree.HTML(page_text)
        #遍历列表，获取每个item的属性和特征
        item_list=tree.xpath('/html/body/div[2]/div[5]/ol/li')

        num=1
        result={}   #用于存储全部item的数据
        for item in item_list:
            # 新建data列表存储每个item的数据
            data=[]

            # 获取item的名字
            name=item.xpath('./a/div/h4/text()')[0]
            data.append(name)

            # 获取item的url
            book_url=item.xpath('./a/@href')[0]
            book_url='https://www.xiashu9.com'+book_url
            data.append(book_url)

            #获取item的简介
            info=item.xpath('./a/div/p/text()')[0]
            data.append(info)

            #获取item的作者
            author=item.xpath('./a/div/div/div[1]/span//text()')[0]
            if len(author)!=0:
                data.append(author)
            else:
                data.append(' ')

            #获取书籍的小说类别（属性）
            attribute=item.xpath('./a/div/div/div[2]/span/em[1]/text()')
            if len(attribute)!=0:
                data.append(attribute[0])
            else:
                data.append(' ')

            #获取小说的更新状态
            status=item.xpath('./a/div/div/div[2]/span/em[2]/text()')
            if len(status)!=0:
                data.append(status[0])

            #保存数据到result

            result[num]=data

            # 提取并打印序号，书名，作者，类别，详情链接，简介
            # print(num, ':', result[num][0],'author:', result[num][3],'attribute:',result[num][4],'status:',result[num][5])
            # print('url:',result[num][1])
            # print('info:')
            # print(result[num][2])

            num=num+1
        return result









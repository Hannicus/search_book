# Author:Hannicus
# -*- coding=utf-8 -*-
# @Time :2021/11/23 9:24
# @File :UI.py

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




class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('搜书')
        self.setGeometry(300,300,600,300)
        self.setWindowIcon(QtGui.QIcon('R-C.jpg'))
        # self.setFixedWidth(250)

        book_name_label=QLabel('请输入书籍名字:',self)
        self.book_lineEdit=QLineEdit(self)
        self.book_lineEdit.setAlignment(Qt.AlignLeft)
        book_name_label.setBuddy(self.book_lineEdit)

        search_url_label=QLabel('搜索源:',self)
        items=['https://www.xiashu9.com/','https://www.mapleso.top/']
        self.comboBox=QComboBox()
        self.comboBox.addItems(items)
        self.comboBox.setCurrentIndex(0)


        self.logue_items=['请选择要查看书籍','1','2']
        self.download_comboBox=QComboBox()
        self.download_comboBox.addItems(self.logue_items)
        self.download_comboBox.setCurrentIndex(0)


        self.search_btn=QPushButton('搜索')
        self.search_btn.clicked.connect(self.search_btn_clicked)


        self.search_result_label=QLabel('搜索结果：')
        self.search_result=QTextEdit(self)
        # self.search_result.resize(300,100)
        self.search_result.setAlignment(Qt.AlignLeft)
        self.search_result_label.setBuddy(self.search_result)

        self.search_clear=QPushButton('清空')
        self.search_clear.clicked.connect(self.search_clear_clicked)


        self.download_comboBox=QComboBox()
        self.download_comboBox.addItem('请选择要查看书籍编号')
        self.download_comboBox.setCurrentIndex(0)

        self.add_btn=QPushButton('添加')
        self.add_btn.clicked.connect(self.add_option)



        self.download_btn=QPushButton('确定')
        self.download_btn.clicked.connect(self.download_btn_clicked)

        self.clear_btn=QPushButton('清空')
        self.clear_btn.clicked.connect(self.clear_btn_clicked)


        self.download_result_label=QLabel('下载链接：')
        self.download_result=QTextEdit(self)
        self.download_result.setAlignment(Qt.AlignLeft)
        self.download_result_label.setBuddy(self.download_result)



        mainlayout=QGridLayout(self)
        mainlayout.addWidget(book_name_label,0,0)
        mainlayout.addWidget(self.book_lineEdit,0,1,1,1)
        mainlayout.addWidget(search_url_label,1,0)
        mainlayout.addWidget(self.comboBox,1,1,1,1)
        mainlayout.addWidget(self.search_btn,0,2)


        mainlayout.addWidget(self.search_result_label,2,0)
        mainlayout.addWidget(self.search_result,3,0,1,3)
        mainlayout.addWidget(self.search_clear,3,3)

        mainlayout.addWidget(self.download_result_label,4,0)
        mainlayout.addWidget(self.download_comboBox,4,1)
        mainlayout.addWidget(self.add_btn,4,2)
        mainlayout.addWidget(self.download_btn,4,3)
        mainlayout.addWidget(self.download_result,5,0,1,3)
        mainlayout.addWidget(self.clear_btn,5,3)


    def search_btn_clicked(self):
        name=self.book_lineEdit.text()
        self.url=self.comboBox.currentText()

        # 设置webdriver参数
        chrome_option = unvisable()
        option = avoiddetection()
        self.bro = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_option, options=option)

        # 搜索
        page_text = search_option(url=self.url,name=name,bro=self.bro)
        # 搜索结果
        self.result = search_result_annalyse(url=self.url, page_text=page_text)
        # self.search_result.append('123213213')
        if self.url=='https://www.xiashu9.com/':
            # print(len(result))s
            # for num in range(len(result)):
                # row1=str(num)+':'+result[num][0]+'author:'+result[num][3]+'attribute:'+result[num][4]+'status:'+result[num][5]
            length=len(self.result)
            for num in range(1,length):
                self.row1=str(num)+':'+self.result[num][0]+' author:'+self.result[num][3]+' attribute:'+self.result[num][4]+'  status:'+self.result[num][5]
                self.search_result.append(self.row1)
                # row2='url:'+result[num][1]
                # self.search_result.append(row2)
                row3='info:'
                self.search_result.append(row3)
                row4=self.result[num][2]
                self.search_result.append(row4)

        elif self.url=='https://www.mapleso.top/':
            for num in range(1,len(self.result)):
                row1=str(num)+':'+self.result[num][0]+'\n'+'situation:'+self.result[num][2]
                self.search_result.append(row1)


    def add_option(self):
        for num in range(1,len(self.result)):
            line=str(num)+':'+self.result[num][0]
            self.download_comboBox.addItem(line)

    def download_btn_clicked(self):
        t_num=self.download_comboBox.currentIndex()
        detail_url=self.result[t_num][1]

        if self.url=='https://www.mapleso.top/':
            download_url=published_book.book_detail(detail_url=detail_url, bro=self.bro)
        elif self.url=='https://www.xiashu9.com/':
            download_url=network_book.book_detail(detail_url=detail_url, bro=self.bro)

        self.download_result.append('下载链接为：\n')
        self.download_result.append(download_url)

    def search_clear_clicked(self):
        self.search_result.clear()

    def clear_btn_clicked(self):
        self.download_result.clear()
        self.download_comboBox.clear()
        self.download_comboBox.addItem('请选择要查看书籍编号')




if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Example()
    win.show()
    sys.exit(app.exec_())
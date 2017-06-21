#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup
import time
import socket
import gzip
import StringIO
"""
主页源码
获取每个产品6位数字超链接
打开网页，获取源码

获取产品信息
写入文件
禁止爬虫，模拟浏览器进行访问,加上头部信息
"""

#获取主页源码
fanly_url = "http://zhide.fanli.com/p"      #多页
format_url = "http://zhide.fanli.com/detail/1-"  #商品链接

class Faly(): #首字母大写
    def __init__(self):       #初始化构造函数,self=this 本身
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        self.html_data = []  #放置商品信息的列表


    #获取主页源码，多页
    def get_html(self,start_page=1,end_page=3):
        for i in range(start_page,end_page+1):
            rt = urllib2.Request(fanly_url+str(i))     #利用一个地址创建一个对象
            rt.add_header('User_Agent',self.user_agent)
            try:

                my_data = urllib2.urlopen(rt).read()  #打开网页，获取源码
                #print my_data
                self.html_data.append(my_data)
                time.sleep(2)
                socket.setdefaulttimeout(15)  #下载内容等待时间
            except urllib2.URLError,e:
                if hasattr(e,'reason'):  #判断异常是否存在的一个函数
                    print u'连接错误',e.reason

        return str(self.html_data)

#html = Faly().get_html()
#获取产品超链接
class GetData():
    def __init__(self):
        self.html = Faly().get_html()  #获取源码
        self.href = []  #获取6位数字的列表
        self.ls = []
        self.url = []

    #获取产品的超链接
    def get_hrefurl(self):
        reg = r'data-id="\d{6}"' #商品正则
        result = re.compile(reg) #编译，提高效率
        tag = result.findall(self.html)
        #tag = re.findall(result,self.html)
        #print tag
        for i in tag:
            self.href.append(i)
            #print self.href

        #去重
        reg2 = r"\d{6}"
        result2 = re.findall(reg2,str(self.href))
        if len(result2):
            for data in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url = format_url + str(data) #完整的商品链接
                    self.url.append(url)
                    #print self.url[-1]
        return self.url

a = GetData().get_hrefurl()


#获取产品信息
class Href_mg():
    def __init__(self):
        self.list = GetData().get_hrefurl()
        self.txt_list = []  #商品信息


    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url = str(self.list[item])
                mg = urllib2.Request(url)
                try:
                    req = urllib2.urlopen(mg).read()
                    encoding = "gb18030"
                    #req = StringIO.StringIO(req)
                    #req = gzip.GzipFile(fileobj=req)
                    #req = req.read()
                    soup = BeautifulSoup(req,'html.parser',fromEncoding=encoding)
                    txt = soup.find_all('h1') #找到标签h1
                    self.txt_list.append(txt)
                    #print self.txt_list #打印商品列表
                except urllib2.URLError,e:
                    print e.reason

        return str(self.txt_list)

if __name__ == '__main__':     #判断文件入口
    path = "test.txt"
    with open(path,'a') as file:
        data = Href_mg().show_mg() #获取产品的内容
        #reg4 = r'<.*+>'
        #data_s = re.sub(reg4,' ',data).replace(u'全网最低','').replace('[','').replace(']','').replace(',','\n').strip().replace(' ','')
        print data
        file.write(data)


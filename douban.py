#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup

#打来网页，获取源码

#url = 'http://dbmeinv.com/?pager_offset=1'
x = 0

def dowban(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    url = urllib2.Request(url,headers=headers)
    req = urllib2.urlopen(url,timeout=20)   #打开网页时间
    contents = req.read()    #获取源码
    #print contents
    soup = BeautifulSoup(contents,'html.parser')     #创建一个soup对象
    my_girl = soup.find_all('img')     #找到所有img标签
    for girl in my_girl:     #遍历list，选取属性
        link = girl.get('src')     #获取src图片路径
        print link
        
        #下载的文件，取名字
        global x
        urllib.urlretrieve(link,'/root/show_me_code/XTeach/inage/%s.jpg'%x)
        print "正在下载第%s张"%x
        x+=1
for page in xrange(1,4):
    url = "http://dbmeinv.com/?pager_offset=%s"%page
    dowban(url)

print "下载完毕"

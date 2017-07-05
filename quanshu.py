#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import  re
def getSortList():
    res = urllib.urlopen('http://www.quanshuwang.com/map/1.html')

    html =  res.read()
    html = html.decode('gbk')
    html = html.encode('utf-8')
    reg = r'<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    return  re.findall(reg,html)

def getChapterlList(url):
    html = urllib.urlopen('http://www.quanshuwang.com%s'%url).read()
    html = html.decode('gbk').encode('utf-8')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    return re.findall(reg,html)

def getChapter(url,chapterurl):
    urls = url.split('/')[-1]    #取出url/后的一部分
    html = urllib.urlopen('http://www.quanshuwang.com%s'%url.replace('index.html',chapterurl)).read()
    html = html.decode('gbk').encode('utf-8')
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    return re.findall(reg,html)[0]    
for novel in getSortList():        #调用getSortList
    #i=('1.html','书名')
    #print i[0],i[1]
    url = novel[0]
    name = novel[1]
    for chapter in  getChapterlList(url):
        #print chapter[0],chapter[1]
        chapterurl = chapter[0]
        chaptername = chapter[1]
        print getChapter(url,chapterurl)
        break
    break


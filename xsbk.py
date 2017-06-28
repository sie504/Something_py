#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

articleUrl = "https://www.qiushibaike.com/textnew/page/%d" # 文章地址
commentUrl = "https://www.qiushibaike.com/article/%s"     #评论地址
page = 3

#while True:
#    raw = raw_input("点击enter查看或输入exit退出,请输入你的选择: ")
#    if raw == "exit":
#        break
#    Url = articleUrl % page #字符串格式化

#打开网页，获取源码

def getContentOrComment(Url):
    #增加头部信息，模拟浏览器
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(url=Url,headers=headers)
    response = urllib2.urlopen(req)         #带来网址
    content = response.read()

    #print content
    return content

while True:
    raw = raw_input("点击enter查看或者输入exit退出，请输入你的选择：")
    if raw == "exit":
        break
    page += 1
    Url = articleUrl % page
    print Url
    articlePage = getContentOrComment(Url)      #调用上面的函数

    #获取话题内容
    soupArticle = BeautifulSoup(articlePage,'html.parser')  #解析网页源码
    articleFloor = 1 #第一条
    for string in soupArticle.find_all(attrs="article block untagged mb15"):
        commentId = str(string.get('id')).strip()[11:]   #attrs标签
        #print commentId   #9位数字连接
        print "\n"
         #获取内容
        print articleFloor,".",string.find(attrs="content").get_text().strip()
        articleFloor += 1
    


        #获取评论
        commentPage = getContentOrComment(commentUrl % commentId)
        soupComment = BeautifulSoup(commentPage,'html.parser')
        commentFloor = 1 #楼层数
        for comment in soupComment.find_all(attrs="body"):
            print "     ",commentFloor,"楼回复：",comment.get_text()
            commentFloor += 1
    


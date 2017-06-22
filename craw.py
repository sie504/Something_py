#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import urllib2
import threading
import Queue
import time
import random

q = Queue.Queue()     #FIFO 先进先出
threading_num = 10

domain_name= "http://192.168.86.209/wordpress46/"
Baidu_spider = "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
#User-Agent
exclude_list = ['.jpg','.gif','.css','.png','.js']     #过滤排除列表

"""
代理服务
proxy_list = [
    {'http':'219.232.125.232:3128'},
    {'http':'124.88.31.80'},
    {'http':'113.69.252:9000'},
]"""


#f = open('/root/show_me_code/XTeach/urlfuzzing/CMS/wordpress.txt')
#lines = f.readlines()
#f.close()
with open('/root/show_me_code/XTeach/urlfuzzing/CMS/wordpress.txt','r') as lines:

    for line in lines:
        line = line.rstrip()
        if os.path.splitext(line)[1] not in exclude_list:
         #判断后缀是否是jpg,gif,不是的就输出
            q.put(line)      #将line传入队列

def crawler():
    while not q.empty():      #只要队列不为空
        path = q.get()
        url = "%s%s" % (domain_name,path)
        #random_proxy = random.choice(proxy_list)
        #proxy_support = urllib2.ProxyHandler(random_proxy)    #使用代理
        #opener = urllib2.build_opener(proxy_support)   #开启
        #urllib2.install_opener(opener)    #安装


        headers = {}
        headers['User-Agent'] = Baidu_spider
        request = urllib2.Request(url,headers=headers)
        try:

            response = urllib2.urlopen(request)
            content = response.read()

            if len(content):
                print "Status [%s]  -path: %s" %(response.code,path)
        
            response.close()
            time.sleep(4)
        except urllib2.HTTPError as e:
            print e.code, path
            #pass

if __name__ == '__main__':
    for i in range(threading_num):
        t = threading.Thread(target=crawler)
        t.start()


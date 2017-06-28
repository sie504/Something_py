##### Something_py
记录一些通过学习网络资源敲的python脚本
##### [fanli.py](https://github.com/sie504/Something_py/blob/master/fanli.py)
通过一个简单的爬虫脚本，来学习爬虫的原理。
比如获取fanli网上每个商品的情况，先获取每个主页的源码，在里面获取每个商品后面的六位数字，获取到完整的商品链接，利用该完整的链接可以下载到具体的内容。

##### [craw.py](https://github.com/sie504/Something_py/blob/master/craw.py)
多线程的来扫描一个网站的敏感目录，首先读取本地的文件，进行判断处理，然后通过HTTP请求来判断是否存在该目录。

##### [xsbk.py](https://github.com/sie504/Something_py/blob/master/xsbk.py)
获取源码、打印话题内容 从超链接中间获取文本、打印评论内容、用户输入操作。。。。

首先是在主页中获取源码内容，通过BeautifulSoup解析源码，在源码中找到话题内容以及话题的链接，再读取具体话题下的评论。直接使用一个函数来进行的获取内容和话题评论。。其中的attrs、get_text获取对应的标签以及文本内容。需要学习BS4其中的具体使用技巧。

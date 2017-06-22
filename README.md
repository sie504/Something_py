##### Something_py
记录一些学习python的脚本
##### [fanli.py](https://github.com/sie504/Something_py/blob/master/fanli.py)
通过一个简单的爬虫脚本，来学习爬虫的原理。
比如获取fanli网上每个商品的情况，先获取每个主页的源码，在里面获取每个商品后面的六位数字，获取到完整的商品链接，利用该完整的链接可以下载到具体的内容。

##### [craw.py](https://github.com/sie504/Something_py/blob/master/craw.py)
多线程的来扫描一个网站的敏感目录，首先读取本地的文件，进行判断处理，然后通过HTTP请求来判断是否存在该目录。

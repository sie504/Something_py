##### Something_py
记录一些学习python的脚本

#####fanli.py
爬虫：打开网页获取源码---找到图片链接---下载

	urllib
	import urllib
	a = urllib.urlopen('www.baidu.com')
	a.read      读取源码。。。
	urlretrieve（图片，文章，路径地址） 下载

	urllib2:不同点，网址禁止爬虫，可以解决，，伪装浏览器，，设置头部，模拟浏览器进行访问，加上头部信息headers。
	f12--network--f5--name---user-agent
	 
	data数据，，
	

	beautifulsoup ：python2 bsp4， python3 bsp3
	提取标签的内容，解析方式，自带html.parser,lxml安装
	指定html的内容，进行解析。。
	打开html文件，BeautifulSoup(open('a.html'),'html.parser')
	


	re正则
	正则匹配获取的内容
	findall(正则，源码)，获取所有的。。

	requests
	r = requests.get('www.baidu.com')
	r.status_code
	r.encoding
	r.text   源码
	r.content 编码
	post请求，
	url传递参数。。手动组成url。。

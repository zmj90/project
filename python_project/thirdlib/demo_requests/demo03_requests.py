"""
【1】定义 : 代替你原来的IP地址去对接网络的IP地址

【2】作用 : 隐藏自身真实IP,避免被封

参数类型
   proxies = { '协议':'协议://IP:端口号' }
   proxies = {
    	'http':'http://IP:端口号',
    	'https':'https://IP:端口号',
   }

私密代理+独享代理
【1】语法结构
   proxies = { '协议':'协议://用户名:密码@IP:端口号' }

【2】示例
   proxies = {
	  'http':'http://用户名:密码@IP:端口号',
      'https':'https://用户名:密码@IP:端口号',
   }
"""
import requests

# 免费普通代理
url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
# 定义代理,在代理IP网站中查找免费代理IP
proxies = {
    'http': 'http://112.85.164.220:9999',
    'https': 'https://112.85.164.220:9999'
}
html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)

# 私密代理+独享代理
url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://309435365:szayclhp@106.75.71.140:16816',
    'https': 'https://309435365:szayclhp@106.75.71.140:16816',
}
headers = {
    'User-Agent': 'Mozilla/5.0',
}

html = requests.get(url, proxies=proxies, headers=headers, timeout=5).text
print(html)

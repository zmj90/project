"""
包装好请求头后,向测试网站发请求,并验证
养成好习惯，发送请求携带请求头，重构User-Agent    User-Agent参数详解
"""
import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) '
                  'Chrome/14.0.835.163 Safari/535.1'}
# html = requests.get(url=url,headers=headers).text
# 'ignore' 忽略无法转码的字符串 防止网页中带有无法识别字符串而报错
html = requests.get(url=url, headers=headers).content.decode('utf-8', 'ignore')
# Uni codeDecodeError: utf-8 xxx cannot decode char \xxx in.
# ignore 可解决
# UnicodeEncodeError: gbk code cannot encode char \xxx in,
# windows 写入文件时常报错误
# with open('xxx. txt', 'w’, encoding='gb18030') as f:
print(html)

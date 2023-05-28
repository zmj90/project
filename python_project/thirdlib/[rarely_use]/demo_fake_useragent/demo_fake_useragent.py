# 爬虫生成useragent的插件，大概有250个UserAgent
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().random}
print(headers)

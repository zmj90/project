"""
1、导模块
   from lxml import etree
2、创建解析对象
   parse_html = etree.HTML(html)
3、解析对象调用xpath
   r_list = parse_html.xpath('xpath表达式')
"""
from lxml import etree

html = ""
parse_html = etree.HTML(html)

r_list = parse_html.xpath('xpath表达式')

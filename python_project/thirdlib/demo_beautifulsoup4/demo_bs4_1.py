from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story123</b></p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup = BeautifulSoup(html_doc)
soup = BeautifulSoup(html_doc, 'lxml')
# print(type(soup), id(soup), soup)
r1 = soup.title
# print(type(r1), id(r1), r1)
r2 = soup.title.name
# print(type(r2), id(r2), r2)
r3 = soup.title.string
# print(type(r3), id(r3), r3)
r4 = soup.title.parent.name
# print(type(r4), id(r4), r4)
r5 = soup.p.string
print(type(r5), id(r5), r5)
r6 = soup.p['class']
# print(type(r6), id(r6), r6)
r7 = soup.a
# print(type(r7), id(r7), r7)
r8 = soup.find_all('a')
# print(type(r8), id(r8), r8)
r9 = soup.find(id="link3")
# print(type(r9), id(r9), r9)
r10 = soup.get_text()
# print(type(r10), id(r10), r10)

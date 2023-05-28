from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="lxml")
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="html.parser")
# print(soup, type(soup), id(soup))
r1 = soup.prettify()
# print(r1, type(r1), id(r1))
r2 = soup.find(text="bad")
# r2 = soup.find(string="bad")
print(r2, type(r2), id(r2))
r3 = soup.i
# print(r3, type(r3), id(r3))

soup1 = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
r4 = soup1.prettify()
# print(r4, type(r4), id(r4))

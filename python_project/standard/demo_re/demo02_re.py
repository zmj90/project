import re

html = '''<div class="animal">
    <p class="name">
        <a title="Tiger"></a>
    </p>

    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
        <a title="Rabbit"></a>
    </p>

    <p class="content">
        Small white rabbit white and white
    </p>
</div>'''

p = re.compile('<div class="animal">.*?title="(.*?)".*?content">(.*?)</p>.*?</div>', re.S)
r_list = p.findall(html)
print(r_list)

for rt in r_list:
    print('动物名称:', rt[0].strip())  # strip() 去掉字符串两头的空白包括\n\t和空格
    print('动物描述:', rt[1].strip())
    print('*' * 50)

# 把想要提取的数据先复制出来，再按需删除，删除的地方加上.*?,需要提取的地方加(.*?)

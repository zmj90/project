"""
https://docs.python.org/zh-cn/3/library/re.html
"""

import re

with open("xs.json", encoding="utf8") as f1, \
     open("result.txt", "w", encoding="utf8") as f2:
    pattern = r'.*?"title": "(.*?)",' \
              r'.*?"name": "(.*?)",' \
              r'.*?"salesPrice": (.+?),'
    r1 = re.findall(pattern, f1.read().replace(r"\n", "\n").replace(r"\"", "\""), re.S)
    print(r1)
    for i, ele in enumerate(r1, 1):
        # r2 = map(lambda x: x.replace(r"\n", "\n"), ele)
        # r3 = tuple(r2)
        # print(tuple(r2))
        # _s = f"第{i:02}题: '{r3[0]}'\n" \
        #      f"{r3[1]}\n" \
        #      f"{r3[2]}\n\n"
        _s = f"第{i:02}题: {ele[0]}" \
             f"{ele[1]}\n" \
             f"{ele[2]}\n\n"
        f2.write(_s)

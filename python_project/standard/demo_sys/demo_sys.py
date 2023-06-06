import sys

# s1 = sys.copyright
# print(s1, type(s1))
"""
Copyright (c) 2001-2021 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved. <class 'str'>
"""


# s2 = sys.version
# print(s2, type(s2))
# 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] <class 'str'>


# s3 = sys.platform
# print(s3, type(s3))
# win32 <class 'str'>


# s4 = sys.version_info
# print(s4, type(s4))
# sys.version_info(major=3, minor=9, micro=6, releaselevel='final', serial=0) <class 'sys.version_info'>

s5 = sys.stdin.read()
print(type(s5), s5)

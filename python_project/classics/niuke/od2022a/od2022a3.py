"""
d = {"0": "abc", "1": "def", "2": "ghi", "3": "jkl", "4": "mno", "5": "pqr", "6": "st", "7": "uv",
     "8": "wx", "9": "yz"}
输入数字，字符按数字排序，排序包含给定字符，输出剩余字符
eg：
78
ux
输出：uw,vw,vx
说明：
78：uw,ux,vw,vx

78
x
输出：uw,vw,
说明：
78：uw,ux,vw,vx

"""
import time

d = {"0": "abc", "1": "def", "2": "ghi", "3": "jkl", "4": "mno", "5": "pqr", "6": "st", "7": "uv", "8": "wx", "9": "yz"}


def fun1(a):
    start = time.time()
    n = len(a)
    i = 0
    if n == 0:
        target = []
    else:
        target = [i for i in d[a[0]]]
    while i + 1 < n:
        tg = []
        for j in target:
            for k in d[a[i + 1]]:
                tg.append(j + k)
        i += 1
        target = tg
    end = time.time()
    print(target)
    print(f"{start - end:.9f}")


if __name__ == '__main__':
    s = "0123456789"
    fun1(s)

"""
自定义进程类
"""
from multiprocessing import Process
import requests
import re, time
# Crypto模块安装很坑,没装上的建议百度
from Crypto.Cipher import AES


def func_time(func):
    def inner(*args,**kw):
        start_time = time.time()
        func(*args,**kw)
        end_time = time.time()
        print('下载时间为：',end_time-start_time,'s')
    return inner


class MyProcess(Process):
    def __init__(self, str1, str2, str3):
        """

        :param str1: 01a,01p
        :param str2: 0606a,0606p
        """
        super().__init__()
        # TODO 需要自己添加
        self.name = f'python_datascience_day{str1}m.mp4'
        # m3u8文件的url,需要去抓包看地址,有规律
        # TODO 需要自己添加
        self.m3u8_url = f'http://c.it211.com.cn/aid2002{str2}m/aid2002{str2}m.m3u8'
        self.headers = {
            "Origin": "http://tts.tmooc.cn",
            # TODO 需要自己添加
            "Referer": f"http://tts.tmooc.cn/video/showVideo?menuId={str3}&version=AIDTN202004",
            # 建议写本机的User-Agent
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
        }
        self.f = open(self.name, 'wb')

    def get_key_ts(self):
        """通过正值表达式获取m3u8文件内容中key和ts的url"""
        # 获取m3u8内容
        m3u8_content = requests.get(url=self.m3u8_url, headers=self.headers).text
        # key的正则匹配
        k = re.compile(r"http://.*?\.key")
        # ts的正则匹配
        t = re.compile(r"http://.*?\.ts")
        # key的url
        key_url = k.findall(m3u8_content)[0]
        # ts的url列表
        ts_urls = t.findall(m3u8_content)
        # 下载key的二进制数据
        key = self.get_key(key_url)
        # 解密,保存ts文件
        self.decrypt_save_ts(key, ts_urls)

    def get_key(self, key_url):
        """功能函数1-下载key的二进制数据"""
        key = requests.get(url=key_url,headers=self.headers).content
        return key

    def decrypt_save_ts(self, key, ts_urls):
        """功能函数2:解密,保存"""
        for ts_url in ts_urls:
            ts_name = ts_url.split("/")[-1]  # ts文件名
            # 解密，new有三个参数，
            # 第一个是秘钥（key）的二进制数据，
            # 第二个使用下面这个就好
            # 第三个IV在m3u8文件里URI后面会给出，如果没有，可以尝试把秘钥（key）赋值给IV
            sprytor = AES.new(key, AES.MODE_CBC, IV=key)

            # 获取ts文件二进制数据
            print("正在下载：" + ts_name)
            ts = requests.get(url=ts_url,headers=self.headers).content
            # 密文长度不为16的倍数，则添加b"0"直到长度为16的倍数
            while len(ts) % 16 != 0:
                ts += b"0"

            # with open(self.name, "ab") as file:
            #     # decrypt方法的参数需要为16的倍数，如果不是，需要在后面补二进制"0"
            #     file.write(sprytor.decrypt(ts))
            self.f.write(sprytor.decrypt(ts))

    @func_time
    def run(self):
        self.get_key_ts()
        self.f.close()
        print(self.name, "下载完成")


if __name__ == '__main__':

    list1 = [
        ('05a', '0628a', '720886'),
        ('05p', '0628p', '720886'),
    ]
    list2 = []
    for item in list1:
        p = MyProcess(item[0], item[1], item[2])
        p.start()
        list2.append(p)

    for i in list2:
        i.join()



import re
import time

import requests
from Crypto.Cipher import AES


def func_time(func):
    def inner(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        print('下载时间为：', end_time - start_time, 's')

    return inner


class SpiderVideo:
    def __init__(self, name, url):
        """

        :param name: 电影名称
        :param url: m3u8
        """
        self.name = f'{name}.mp4'
        # m3u8文件的url,需要去抓包看地址,有规律
        self.m3u8_url = f'{url}'
        self.headers = {
            "Origin": "http://www.zs-yijin.com",
            "Referer": "http://www.zs-yijin.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }
        self.f = open(self.name, 'wb')

    def get_key_ts(self):
        """
        通过正值表达式获取m3u8文件内容中key和ts的url
        :return:
        """

        # 获取m3u8内容
        m3u8_text = requests.get(url=self.m3u8_url, headers=self.headers).text
        print(m3u8_text)

        # key的正则匹配
        k = re.compile(r"https://.*?\.key")

        # ts的正则匹配
        t = re.compile(r"https://.*?\.ts")

        # key的url
        print(k.findall(m3u8_text))
        key_url = k.findall(m3u8_text)[0]

        # ts的url列表
        print(t.findall(m3u8_text))
        ts_urls = t.findall(m3u8_text)

        # 下载key的二进制数据
        key = self.get_key(key_url)

        # 解密,保存ts文件
        self.decrypt_save_ts(key, ts_urls)

    def get_key(self, key_url):
        """
        功能函数1-下载key的二进制数据
        :param key_url: key url
        :return:
        """
        key = requests.get(url=key_url, headers=self.headers).content
        return key

    def decrypt_save_ts(self, key, ts_urls):
        """
        功能函数2:解密,保存
        :param key: key
        :param ts_urls: ts urls
        :return:
        """
        for ts_url in ts_urls:
            ts_name = ts_url.split("/")[-1]
            # 解密，new有三个参数，
            # 第一个是秘钥（key）的二进制数据，
            # 第二个使用下面这个就好
            # 第三个IV在m3u8文件里URI后面会给出，如果没有，可以尝试把秘钥（key）赋值给IV
            cipher = AES.new(key, AES.MODE_CBC)

            # 获取ts文件二进制数据
            print("正在下载：" + ts_name)
            time.sleep(1)
            ts = requests.get(url=ts_url, headers=self.headers).content
            # 密文长度不为16的倍数，则添加b"0"直到长度为16的倍数
            while len(ts) % 16 != 0:
                ts += b"0"

            # with open(self.name, "ab") as file:
            #     file.write(sprytor.decrypt(ts))  # decrypt方法的参数需要为16的倍数，如果不是，需要在后面补二进制"0"
            self.f.write(cipher.decrypt(ts))

    @func_time
    def run(self):
        self.get_key_ts()
        self.f.close()
        print(self.name, "下载完成")


if __name__ == '__main__':
    name = "绝地击杀"
    url = "https://vod8.wenshibaowenbei.com/20210703/6D598D5h/1000kb/hls/index.m3u8"
    sv = SpiderVideo(name, url)
    sv.run()

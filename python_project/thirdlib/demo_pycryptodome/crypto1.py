from base64 import b64encode, b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def get_secret_key(n=16):
    """
    密钥
    <class 'str'> 密钥：GOw40mjkE8y6CaPnmbRgDA==
    :param n: 位数
    :return: <class 'str'> UANafploHWEx2vG2/7aYrA==
    """
    return b64encode(get_random_bytes(n)).decode()


def en_crypt(key, plaintext):
    """
    加密
    <class 'str'> 密文：MJLyqQY1/Iw3mTmfBaPVKWqHzH2hUGU94qT8qu7b2dU=
    :param key: 密钥
    :param plaintext: 明文
    :return: <class 'str'> 9bfO9ibDAmsGohCmjldCQMCmsStw5myUnHifsrF7UV8=
    """
    data = pad(plaintext.encode(), AES.block_size)
    cipher = AES.new(b64decode(key), AES.MODE_ECB)
    return b64encode(cipher.encrypt(data)).decode()


def de_crypt(key, ciphertext):
    """
    解密
    <class 'str'> 明文：Tatai#libing2021
    :param key: 密钥
    :param ciphertext: 密文
    :return:
    """
    cipher = AES.new(b64decode(key), AES.MODE_ECB)
    return unpad(cipher.decrypt(b64decode(ciphertext)), AES.block_size).decode()


if __name__ == '__main__':
    plain_text = "Tatai#libing2021"
    secret_key = get_secret_key()
    print(type(secret_key), "密钥：" + secret_key)
    cipher_text = en_crypt(secret_key, plain_text)
    print(type(cipher_text), "密文：" + cipher_text)
    pw = de_crypt(secret_key, cipher_text)
    print(type(pw), "明文：" + pw)

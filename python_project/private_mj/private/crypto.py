from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


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

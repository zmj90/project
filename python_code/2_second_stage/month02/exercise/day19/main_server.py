from bll import *


if __name__ == '__main__':
    host = "0.0.0.0"
    port = 2048
    dsc = DictServerController(host, port)
    dsc.start()
import requests
from requests import session
import yaml

rs = session()


def t_get():
    with open("get.yaml", "r") as f:
        d = yaml.safe_load(f)
        res = requests.request(**d)
    return res


def t_post():
    method = "get"
    url = "http://httpbin.org/get"
    res = rs.request(method, url)
    return res


if __name__ == '__main__':
    r = t_get()
    print(r, f"{r=}, {type(r)=}")
    print(r.json())


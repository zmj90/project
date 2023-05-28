import json
from string import Template

import yaml


class GetDate:
    def __init__(self):
        self.file = "demo1.yaml"

    def load(self):
        payload, expect = yaml.safe_load_all(open(self.file))
        print(type(payload), payload)
        print(type(expect), expect)
        s_ = Template(json.dumps(payload)).safe_substitute(
            all="广东省"
        )
        print(type(s_), s_)
        y_ = yaml.safe_load(s_)
        print(type(y_), y_)


if __name__ == '__main__':
    gd = GetDate()
    gd.load()

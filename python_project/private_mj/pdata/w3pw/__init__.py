import os

_ = os.path.dirname(__file__)

def get_value(file_path):
    with open(file_path, "r") as f:
        return f.read()

key = get_value(os.path.join(_, "key.aes"))
cipher = get_value(os.path.join(_, "cipher.aes"))

import base64

a = base64.b64encode(b"qwec45645")
print(a, f"{a=}, {type(a)=}")
# b'cXdl' a=b'cXdl', type(a)=<class 'bytes'>
b = base64.b64decode(a)
print(b, f"{b=}, {type(b)=}")
# b'qwec45645' b=b'qwec45645', type(b)=<class 'bytes'>

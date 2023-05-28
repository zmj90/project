import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
r1 = m.digest()
print(type(r1), r1)
# r2 = r1.decode()
# print(type(r2), r2)
# b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'

m.hexdigest()

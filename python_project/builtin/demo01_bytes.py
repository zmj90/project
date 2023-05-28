# r1 = "\xe9\x92\x9f".replace(r"\x", " ")
r1 = bytes.fromhex("e9929f").decode()
r2 = b"\xe9\x92\x9f\x61".decode()

print(type(r1), r1)
print(type(r2), r2)

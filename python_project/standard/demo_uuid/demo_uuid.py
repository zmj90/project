import uuid
import random

# a = uuid.uuid4()
# print(f"{a=},{type(a)=}")
# r = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
# print(type(r), r)
# print(type(r.node), r.node)
# r1 = uuid.uuid1(random.getrandbits(48))
# print(type(r1), r1)

r = uuid.UUID(bytes=b'\x12\x34\x56\x78'*4)
print(type(r), r)

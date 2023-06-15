import sys

sr = [_.strip().split(".") for _ in sys.stdin]


def is_mask(ls):
    if not is_ip(ls):
        return 0
    if not int(ls[0]) >> 7 or int(ls[3]) & 1:
        return 0
    sbin = "".join([f"{int(_):08b}" for _ in ls])
    if sbin.find("0") == 1 + sbin.rfind("1"):
        return int(sbin, 2)
    else:
        return 0


def is_ip(ls):
    if len(ls) != 4:
        return 0
    for i in ls:
        if not i.isdigit() or int(i) >> 8:
            return 0
    sbin = "".join([f"{int(_):08b}" for _ in ls])
    return int(sbin, 2)


for i in range(0, len(sr) + 1, 3):
    mask, ip1, ip2 = is_mask(sr[i]), is_ip(sr[i+1]), is_ip(sr[i+2])
    if all((mask, ip1, ip2)):
        if ip1 & mask == ip2 & mask:
            print(0)
        else:
            print(2)
    else:
        print(1)

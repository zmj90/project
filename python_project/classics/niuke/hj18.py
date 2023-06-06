import sys


def ip_valid(l_ip):
    if len(l_ip) != 4:
        return False
    for i in l_ip:
        if not i.isdigit() or int(i) < 0 or int(i) > 255:
            return False
    return True


def mask_valid(l_mask):
    if len(l_mask) != 4 or set(l_mask) in ({"0"}, {"255"}):
        return False
    for i in l_mask:
        if not i.isdigit() or int(i) < 0 or int(i) > 255:
            return False
    sb = "".join(f"{int(i):08b}" for i in l_mask)
    if sb.find("0") != sb.rfind("1") + 1:
        return False
    return True


def classify():
    r = 7*[0]  # A B C D E error private
    for line in sys.stdin:
        im = line.strip().split("~")
        l_ip, l_mask = im[0].split("."), im[1].split(".")
        if l_ip[0] not in ("0", "127"):
            if not ip_valid(l_ip) or not mask_valid(l_mask):
                r[5] += 1
            else:
                if 1 <= int(l_ip[0]) <= 126:
                    r[0] += 1  # A类
                    if l_ip[0] == "10":
                        r[6] += 1  # 私有ip
                elif 128 <= int(l_ip[0]) <= 191:
                    r[1] += 1  # B类
                    if l_ip[0] == "172" and 16 <= int(l_ip[1]) <= 31:
                        r[6] += 1  # 私有ip
                elif 192 <= int(l_ip[0]) <= 223:
                    r[2] += 1  # C类
                    if l_ip[0] == "192" and l_ip[1] == "168":
                        r[6] += 1  # 私有ip
                elif 224 <= int(l_ip[0]) <= 239:
                    r[3] += 1  # D类
                else:
                    r[4] += 1  # E类
    return " ".join([str(i) for i in r])


if __name__ == '__main__':
    print(classify())

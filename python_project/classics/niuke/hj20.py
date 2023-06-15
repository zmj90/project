import sys

for line in sys.stdin:
    a = line.strip()
    if len(a) <= 8:
        print("NG")
        continue

    m = [0, 0, 0, 0]
    for i in a:
        if i.islower():
            if m[0] == 0:
                m[0] = 1
            continue
        if i.isupper():
            if m[1] == 0:
                m[1] = 1
            continue
        if i.isdigit():
            if m[2] == 0:
                m[2] = 1
            continue
        if i != " ":
            if m[3] == 0:
                m[3] = 1
            continue
    if sum(m) < 3:
        print("NG")
        continue

    dc = {}
    for i in range(len(a) - 2):
        if a[i:i+3] in dc:
            print("NG")
            break
        else:
            dc[a[i:i+3]] = None
    else:
        print("OK")

# 111156789

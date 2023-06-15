import sys

d = {}
for line in sys.stdin:
    f, l_num = line.strip().split(" ")
    f = f.split("\\")[-1]
    key = f"{f[-16:]}{l_num}"
    if key in d and d[key][1] == l_num:
        d[key][2] += 1
    else:
        d[key] = [f[-16:], l_num, 1]
for i in list(d)[-8:]:
    d[i][2] = str(d[i][2])
    print(" ".join(d[i]))

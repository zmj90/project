import sys

d1 = {
    "a": "2", "b": "2", "c": "2", "d": "3", "e": "3", "f": "3", "g": "4", "h": "4", "i": "4", "j": "5",
    "k": "5", "l": "5", "m": "6", "n": "6", "o": "6", "p": "7", "q": "7", "r": "7", "s": "7", "t": "8",
    "u": "8", "v": "8", "w": "9", "x": "9", "y": "9", "z": "9"
}
for line in sys.stdin:
    l1 = []
    for i in line.strip():
        if i in ("0", "1"):
            l1.append(i)
            continue
        if i.islower():
            l1.append(d1[i])
            continue
        if i.isupper():
            if i.lower() == "z":
                l1.append("a")
                continue
            else:
                l1.append(chr(ord(i.lower()) + 1))
                continue
        l1.append(i)
    print("".join(l1))

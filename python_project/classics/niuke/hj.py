"""
A Famous Saying: Much Ado About Nothing (2012/8).

A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

"""
s = input()
s_asc = list(filter(str.isalpha, sorted(s, key=str.lower)))
for i, v in enumerate(s):
    if not v.isalpha():
        s_asc.insert(i, v)
print("".join(s_asc))

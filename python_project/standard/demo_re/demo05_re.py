import re

# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m = re.search(r"(\w+) (\w+)", "Isaac Newton, physicist")
r1 = m.group(0)       # The entire match
print(type(r1), r1)

r2 = m.group(1)       # The first parenthesized subgroup.
print(type(r2), r2)

r3 = m.group(2)       # The second parenthesized subgroup.
print(type(r3), r3)

r4 = m.group(2, 1)    # Multiple arguments give us a tuple.
print(type(r4), r4)

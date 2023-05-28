# r1 = sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
r1 = sorted("This is a test string from Andrew".split(), key=lambda x: x.lower())
print(r1)

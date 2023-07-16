
a = input().upper()
b = input().upper()
n = 0
for i in range(len(a)):
    if a[i-n:i+1] in b:
        n += 1
print(n)

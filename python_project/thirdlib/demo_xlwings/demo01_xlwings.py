import xlwings as xw
import datetime as dt
sheet = xw.Book().sheets[0]
sheet['A1'].value = 1
r1 = sheet['A1'].value
print(type(r1), r1)
sheet['A2'].value = 'Hello'
r2 = sheet['A2'].value
print(type(r2), r2)
r3 = sheet['A3'].value is None
print(type(r3), r3)
sheet['A4'].value = dt.datetime(2000, 1, 1)
r4 = sheet['A4'].value
print(type(r4), r4)

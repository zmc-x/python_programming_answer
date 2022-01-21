x=input('输入一个数字')
y=input('再输一个')
try:
    x=int(x)
    y=int(y)
except ValueError:
    print('这是字符')
else:
    print(x+y)
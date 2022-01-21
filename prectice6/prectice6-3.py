language={
    'if':'判断',
    'for':'循环',
    'print':'打印'
}
for name,explain in language.items():
    print(f'{name}:{explain}')
mid=language.get('else',"没有这个键")#get方法
print(mid)
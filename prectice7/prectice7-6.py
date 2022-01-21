flag=True
while flag:
    num=input('你的年龄是？')
    if num=='quit':
        flag=False
    else:
        num=int(num)
        if num>0 and num<3 :
            print('free')
        elif num>=3 and num<12:
            print('$10')
        else :
            print('$15')

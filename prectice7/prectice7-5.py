while True:
    num=input('你的年龄是？')
    num=int(num)
    if num>0 and num<3 :
        print('free')
    elif num>=3 and num<12:
        print('$10')
    else :
        print('$15')

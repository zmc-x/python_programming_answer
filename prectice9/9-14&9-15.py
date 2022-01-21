from random import choice

list=[i for i in range(1,10)]
list.append('a')
list.append('b')
list.append('c')
cnt=0
flag=1
while True:
    tests=[]
    flag=1
    for i in range(0,4):
        tests.append(type(choice(list)))
    cnt+=1
    for test in tests:
        if tests[0]!=test:
            flag=0
            break
    if flag==1:
        break
print(cnt)
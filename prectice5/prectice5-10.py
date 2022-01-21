current_users=['a','b','c','d','e']
new_users=['A','B','C','d','e']
current_length=len(current_users)
new_length=len(new_users)
flag=0
for i in new_users:
    flag=0
    for j in current_users:
        if i==j :
            print('replace')
            flag=1
            break
    if flag==0 :
        print('the username is not use')
#不区分大小写
flag=0
for i in new_users:
    for j in current_users:
        if i.lower()==j or i.upper()==j:
            print('replace')
            flag=1
            break
    if flag==0:
        print("the username is not use")

invite=['mother','father','friends']
for people in invite:
    print(f'{people},I invite you to participate my party')
print("father don't to party")
invite.remove("father")
invite.append("classmates")
for people in invite:
    print(f'{people},I invite you to participate my party')
print('Now,I find a big tabble,so I want to invate more people to participate my party!')
invite.insert(0,'grandfather')
length=len(invite)
invite.insert((int)(length/2),'grandfather')
invite.append('uncle')
for people in invite:
    print(f'{people},I invite you to participate my party')
print(invite)
# 删除元素
length=len(invite)
print(length)
i=length-1
while i>1:
    people=invite.pop(i)
    print(f"{people},sorry")
    i=i-1
for i in invite:
    print(f"{i},you in list")
del invite
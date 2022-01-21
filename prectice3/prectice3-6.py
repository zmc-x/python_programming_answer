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
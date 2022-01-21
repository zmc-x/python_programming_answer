invite=['mother','father','friends']
for people in invite:
    print(f'{people},I invite you to participate my party')
print("father don't to party")
invite.remove("father")
invite.append("classmates")
for people in invite:
    print(f'{people},I invite you to participate my party')

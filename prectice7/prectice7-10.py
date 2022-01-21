places=[]
cnt=0
while True:
    place=input('if you could visit one place in the world,where would you go?')
    places.append(place)
    cnt+=1
    if cnt==5:
        break
print(places)
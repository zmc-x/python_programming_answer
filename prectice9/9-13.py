import random

class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(random.randint(1,self.sides))

test=Die()
cnt=0
while cnt<10:
    test.roll_die()#20,10
    cnt+=1
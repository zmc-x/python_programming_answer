sandwich_orders=['a','b','c','d','e']
finished_sandwich=[]
while sandwich_orders:
    mid=sandwich_orders.pop()
    print(f'i made your {mid}')
    finished_sandwich.append(mid)
print(finished_sandwich)
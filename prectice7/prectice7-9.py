sandwich_order=['pastrami','pastrami','pastrami','a','b']
while True:
    if 'pastrami' not in sandwich_order:
        break
    else:
        sandwich_order.remove('pastrami')
print(sandwich_order)
foods=['vegetable','fruit','turkey']
for food in foods:
    print(f'I like eat {food}')
print("I really love eating this foods!")
foods.append('barbecue')
friends_foods=foods[:]
friends_foods.append('milk')
print(f'foods:{foods}')
print(f'friends_foods:{friends_foods}')
#4-12题使用for来打印列表与前面的类似
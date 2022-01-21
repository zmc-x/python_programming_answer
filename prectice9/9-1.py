class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):#每一个类中都存在__init__,进行初始化，每次创建实列是都先运行这个方法，可以看为默认的方法
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('嗯，描述,其实我也不知道怎么描述！')

    def open_restaurant(self):
        print('opening')

restaurant=Restaurant('黄焖鸡米饭','黄焖鸡米饭')
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()
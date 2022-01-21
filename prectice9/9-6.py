class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):#每一个类中都存在__init__,进行初始化，每次创建实列是都先运行这个方法，可以看为默认的方法
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print('嗯，描述,其实我也不知道怎么描述！')

    def open_restaurant(self):
        print('opening')

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def desplay(self):
        print(self.flavors)
# wei=['原味','草莓味','more']
icecreamstand=IceCreamStand('蜜雪冰城','icecream',['原味','草莓味','more'])
icecreamstand.desplay()
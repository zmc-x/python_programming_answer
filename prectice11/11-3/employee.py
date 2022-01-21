class Employee:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def give_raise(self,increase=5000):
        self.money+=increase
        return self.money


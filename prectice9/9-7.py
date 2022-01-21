class User:
    def __init__(self,first,last):
        self.first_name=first
        self.last_name=last
        self.location='HNUST'

    def describe_user(self):
        print(f'{self.first_name}{self.last_name},address:{self.location}')

    def greet_user(self):
        print(f'welcome to {self.location}')

class Admin(User):
    def __init__(self,first,last,):
        super().__init__(first,last)
        self.privileges=['can add post','can delete post','can ban user']

    def show(self):
        print(f'your privileges is {self.privileges}')

admin=Admin('zhang','mengchao')
admin.show()
class User:
    def __init__(self,first,last):
        self.first_name=first
        self.last_name=last
        self.location='HNUST'

    def describe_user(self):
        print(f'{self.first_name}{self.last_name},address:{self.location}')

    def greet_user(self):
        print(f'welcome to {self.location}')

user1=User('zhang','mengchao')
user2=User('Hello','World')
user1.describe_user()
user2.describe_user()
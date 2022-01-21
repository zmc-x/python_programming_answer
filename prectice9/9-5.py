class User:
    def __init__(self,first,last):
        self.first_name=first
        self.last_name=last
        self.location='HNUST'
        self.login_attempt=0

    def describe_user(self):
        print(f'{self.first_name}{self.last_name},address:{self.location}')

    def greet_user(self):
        print(f'welcome to {self.location}')

    def increment_login_attempts(self):
        self.login_attempt+=1

    def reset_login_attempts(self):
        self.login_attempt=0
user=User('zhang','mengchao')
cnt=0
while cnt<10:
    user.increment_login_attempts()
    cnt+=1
print(user.login_attempt)
user.reset_login_attempts()
print(user.login_attempt)
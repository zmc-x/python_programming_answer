class Privileges:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']

    def show_privileges(self):
        print(self.privileges)

class Admin:
    def __init__(self):
        self.qx=Privileges()

user=Admin()
user.qx.show_privileges()
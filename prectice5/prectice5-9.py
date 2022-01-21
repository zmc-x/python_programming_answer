users=['Admin','Jaden','Tom','jerry','bob']
for user in users:
    if user=='Admin' :
        print("Hello Admin,would you like to see a status report?")
    else :
        print(f'hello {user} ,thank you for logging in again.')
if users:
    print('no empty')
else:
    print('empty')
for i in range(0,5):
    users.pop()
if users:
    print('no empty')
else:
    print('empty')
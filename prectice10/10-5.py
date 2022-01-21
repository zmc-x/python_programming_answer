while True:
    reason=input('hello,please tell me your like programming reason?')
    # print(reason)
    reason+='\n'
    with open('file\\reason.txt','a') as file_object:
        file_object.write(reason)

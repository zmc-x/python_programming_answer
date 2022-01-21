while True:
    name=input('hello,please tell me your name')
    print(f'hello,{name}')
    name+='\n'
    with open('file\guest_book.txt','a') as file_object:
        file_object.write(name)
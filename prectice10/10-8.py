def read(filename):
    try:
        with open(filename) as f:
            mid = f.read()
    except FileNotFoundError :
        print('没有找到')
    else:
        print(mid)

read('file\\dogs.txt')
read('file\\cats.txt')
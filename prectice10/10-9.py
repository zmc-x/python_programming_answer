def read(filename):
    try:
        with open(filename) as f:
            mid = f.read()
    except FileNotFoundError :
        pass
    else:
        print(mid)

read('file\\dogs.txt')
read('file\\cats.txt')
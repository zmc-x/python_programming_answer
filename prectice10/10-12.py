import json

def find(file_name):
    try:
        with open(file_name) as f:
            mid=json.load(f)
    except FileNotFoundError:
        print('没有这个文件')
        x=input('please write your like number')
        x=int(x)
        with open(file_name,'w') as f:
            json.dump(x,f)
    else:
        print(f'you like number is {mid}')


find('file\\number.json')
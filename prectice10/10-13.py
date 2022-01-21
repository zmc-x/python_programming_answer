import json

def getname(file_name):
    try:
        with open(file_name) as f:
            name=json.load(f)
    except FileNotFoundError:
        print('没有这个文件，需要重新创建该文件')
        name=input('your name\n')
        writename(file_name,name)
        return False
    else:
        return name

def writename(file_name,name):
    with open(file_name,'w') as f:
        json.dump(name,f)

print('welcome back')
name=getname('file\\name.json')
if name:
    while True:
        compare=input('请输入你的username')
        if name==compare :
            print('yes')
            break
        else :
            print('no，请再输入一次')
else:
    print('ok,创建成功')

import json

file_name='file\\number.json'
# write
# number=input('输入你喜欢的一个数字')
# number=int(number)
# with open(file_name,'w') as f:
#     json.dump(number,f)

#read
with open(file_name) as f:
    mid=json.load(f)
print(mid)
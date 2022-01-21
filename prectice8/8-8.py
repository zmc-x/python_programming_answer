def make_album(name,album,number='None'):
    singer={}
    singer['name']=name
    singer['album']=album
    if number=='None':
        return singer
    else:
        singer['number']=number
        return singer

cnt=0
while True:
    name=input('姓名：')
    album=input('album:')
    number=input('专辑中歌曲数目：')
    print(make_album(name,album,number))
    cnt+=1
    if cnt==5:
        break


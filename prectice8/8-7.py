def make_album(name,album,number='None'):
    singer={}
    singer['name']=name
    singer['album']=album
    if number=='None':
        return singer
    else:
        singer['number']=number
        return singer

print(make_album('jj','kkkk'))
print(make_album('kkk','jkkk','455'))
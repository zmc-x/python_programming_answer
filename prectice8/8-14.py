def car(brand,shape,**other):
    other['brand']=brand
    other['shape']=shape
    print(other)


car('subaru','outback',color='red',tow_package='True')
# 关键字实参的写法
def build_profile(first,last,**user_info):
    """"创建一个字典，其中包含我们知道的有关的用户的一切"""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info


mid=build_profile('zhang','mengchao',local='China',age='19')
print(mid)


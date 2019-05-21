from collections import ChainMap

user_dict1 = {'a':'booby1','b':'booby2'}
user_dict2 = {'c':'booby2','d':'booby3'}

# for key,value in user_dict1.items():
#     print(key,value)
# for key,value in user_dict2.items():
#     print(key,value)

new_dict = ChainMap(user_dict1,user_dict2)
new_dict2 = new_dict.new_child({'e':'ccc'})
print(new_dict2.maps)
for key,value in new_dict.items():
    print(key,value)
print(new_dict['c'])
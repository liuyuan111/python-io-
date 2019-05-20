name_list = ["booby1",'booby2']
for name in name_list:
    print(name)

name_tuple = ("bobby",29,175,'beijing')
# name,age,height=name_tuple
name, *others = name_tuple
print(name,others)

user_tuple = ("bobby", [29,175], 'beijing')
user_tuple[1].append("ok")
print(user_tuple)
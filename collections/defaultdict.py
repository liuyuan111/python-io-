from collections import defaultdict
#实现dict统计功能
user_dict={}
users = ['booby1','booby2','booby3','booby1','booby2','booby1','booby2',]
#1
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1

#2 setdefault
for user in users:
    user_dict.setdefault(user,0)
    user_dict[user]+=1
    
#3 defaultdict
default_dict = defaultdict(int)
for user in users:
    default_dict[user] += 1
    
print(default_dict)

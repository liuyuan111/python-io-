from collections import deque

#双端队列
user_tuple = deque(('bobby1','bobby2'))
user_list = deque(['bobby1','bobby2'])
user_dict = deque({"bobby1":21,"bobby2":22})
print(user_dict)

user_list.appendleft('abc')
user_dict.clear()
user_tuple.copy()
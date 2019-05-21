from collections import OrderedDict

#是dict的子类,有序
user_dict = OrderedDict()
user_dict['b'] = 'boo2'
user_dict['a'] = 'boo1'
user_dict['c'] = 'boo3'


print(user_dict.move_to_end('b'))
print(user_dict) 
print(user_dict.popitem())
print(user_dict.pop('a'))

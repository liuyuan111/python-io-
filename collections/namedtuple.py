from collections import namedtuple

User = namedtuple("User",['name','age','height','edu'])
# user = User(name='bobby',age=29,height=175)
# user.edu="master"
user_tuple = ('bobby',19,175)
user_list = ['bobby',19,175,'master']

user_dict = {
        "name":"booby",
        'age':29,
        'height':175,
        'edu':'master'
}
#3种方法
user = User(*user_tuple,edu='master')
# user = User._make(user_list)
user_info_dict = user._asdict()
print(user)
print(user.name,user.age,user.height)
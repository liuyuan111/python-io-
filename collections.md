# collections模块使用

# 一、collections模块介绍:  
+ 常用数据结构
+ 抽象基类

# 二、tuple的功能:
+ 不可变、iterable

+ 拆包

        name_tuple = ("bobby",29,175,'beijing')
        # name,age,height=name_tuple
        name, *others = name_tuple
        print(name,others)
+ tuple不可变性不是绝对的

        user_tuple = ("bobby", [29,175], 'beijing')
        user_tuple[1].append("ok")
        print(user_tuple)
+ tuple比list好的地方:  
    1. immutable(不可变)的重要性:   
        + 性能优化 ：指出元素全部为immutable的tuple会作为常量在编译时确定，因此产生了如此显著的速度差异 
        + 线程安全
        + 可作为dict的key(可hash)
        + 拆包特性
    2. 相比于c语言，`tuple`对应`struct`，`list`对应`array`  
    3. 一般数据库驱动取出来的数据为`tuple`

# 三、namedtuple
namedtuple时tuple的子类，节省空间，效率高，适用于创建一些对象
    
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

# 四、defaultdict
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

# 五、deque
`deque.extend()`直接在原deque上扩容不创建新对象
    
    from collections import deque
    from queue import Queue
    #双端队列
    user_tuple = deque(('bobby1','bobby2'))
    user_list = deque(['bobby1','bobby2'])
    user_dict = deque({"bobby1":21,"bobby2":22})
    print(user_dict)

    user_list.appendleft('abc')
    user_dict.clear()
    user_tuple.copy()

# 六、counter功能

    from collections import Counter

    users= ['bobby1','bobby2',3,4,5]
    user_counter = Counter(users)

    print(user_counter) 
    print(Counter('aabbccdds'))

# 七、ChainMap功能:

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
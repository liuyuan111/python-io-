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
# python高级编程和异步io并发编程<br>
## 一、python中一切皆对象
动态语言和静态语言的区别:
+ python面向对象更彻底

### 1.函数和类也是对象,属于python的一等公民:

+ 赋值给变量
+ 可以添加到集合对象中
+ 可以作为参数传递给函数
+ 可以当作函数的返回值

all_is_object.py:

    def ask(name="bobby"):
        print(name)

    class person:
        def __init__(self):
            print("bobby1")

    def print_type(item):
        print(type(item))

    def decorator_func():
        print("dec start")
        return ask

    myask = decorator_func()
    myask("tom")
    # ob_list = []
    # ob_list.append(ask)
    # ob_list.append(person)
    # for i in ob_list:
    #     print(i())
    # my_func = ask
    # my_func()
    #
    # my_class = person
    # my_class()

### 2.**<font color="red">type、object和class的关系:</font>**
<img src="images/101.jpg">

## 3.python中的常见内置类型:

 + 对象的3个特征：
    + 身份： 对象在内存中的地址 id()
    + 类型
    + 值
 + None(全局只有一个)
 + 数值:
     + int
     + float
     + complex(复数)
     + bool  
 + 迭代类型:
     + list
     + bytes、bytearray、memoryview(二进制序列)
     + range
     + tuple
     + str
     + array   
 + 序列类型
 + 映射(dict)
 + 集合:
     + set
     + frozenset(不可修改)
 + 上下文管理类型(with)
 + 其他:
     + 模块类型
     + class和实例
     + 函数类型
     + 方法类型
     + 代码类型
     + object对象
     + type类型
     + ellipsis对象
     + notimplemented类型


## 二、魔法函数

 1.什么是魔法函数
```
    class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    # 魔法函数
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    company = Company(["tom", "bob", "jane"])

    # company1= company[:2]
    #
    # print(len(company))
    # 可迭代类型
    # for em in company1:
    #     print(em)
  ```
 2.python的数据模型以及数据模型对python的影响<br>    
    python语法会识别某个对象或自定义类中的魔法函数，调用是隐式的，不需要直接调用getitem方法。魔法函数式独立存在的，类加入这些会增强功能。

 3.魔法函数一览： 
  + 数字运算:
  + 非数字运算:
    
    1.字符串表示 `__repr__`,`__str__`    
    2.集合、序列相关 `__len__,__getitem__,__setitem__,__delitem__,__contains__`     
    3.迭代相关 `__iter__,__next__`  
    4.可调用 `__cell__`     
    5.with上下文管理器 `__enter__,__exit__`     
    6.数值转换 `__abs__,__bool__,__int__,__float__,__hash__,__index__`  
    7.元类相关 `__new__,__init__`       
    8.属性相关 `__getattr__,__setattr__,__getattribute__,__setattribute__,__dir__`      
    9.属性描述符 `__get__,__set__,__delete__`       
    10.协程 `__await__,__aiter__,__anext__,__aenter__,__aexit__`


 4.魔法函数的重要性
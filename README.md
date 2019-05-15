# python高级编程和异步io并发编程<br>
# 一、python中一切皆对象
动态语言和静态语言的区别:
+ python面向对象更彻底

## 1.函数和类也是对象,属于python的一等公民:

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

## 2.**<font color="red">type、object和class的关系:</font>**
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


# 二、魔法函数

 ## 1.什么是魔法函数
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
 ## 2.python的数据模型以及数据模型对python的影响<br>    
    python语法会识别某个对象或自定义类中的魔法函数，调用是隐式的，不需要直接调用getitem方法。魔法函数式独立存在的，类加入这些会增强功能。

 ## 3.魔法函数一览： 
  + 数字运算:

    1.一元运算符 `__neg__(-),__pos__(+),__abs__`
    2.二元运算符 `___lt__(<),__le__(<=),__eq__(==),__ne__(!=),__gt__(>),__ge__(>=)`     
    3.算数运算符:  `__add__+,__sub__-,__mul__*,__truediv__ /,__floordiv__ //,__mod__ %,__divmod__ divmod(),__pow__ **或pow(),__round__ round()`     
    4.反向运算符:   `__radd__,__rsub__,__rmul__,__rtruediv__,__rfloordiv__,__rmod__,__rdivmod__,__rpow__`       
    5.增量复制运算符       `__iadd__ 、 __isub__ 、 __imul__ 、 __itruediv__ 、 __ifloordiv__ 、 __imod__ 、
__ipow__` 
    6.位运算符      `__invert__ ~ 、 __lshift__ << 、 __rshift__ >> 、 __and__ & 、 __or__ | 、 __
xor__ ^`        
    7.反向位运算符       `__rlshift__ 、 __rrshift__ 、 __rand__ 、 __rxor__ 、 __ror__`        
    8.增量赋值位运算符 `__ilshift__ 、 __irshift__ 、 __iand__ 、 __ixor__ 、 __ior__`

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


 ## 4.魔法函数的重要性


 ## 三、深入类和对象
 
### 1. 鸭子类型和多态  
   维基百科：
   >动态编程语言是一类在运行时可以改变其结构的语言：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力如PHP、Ruby、Python 都属于动态语言，而C、C++、Java等语言则不属于动态语言。

这个解释很抽象，其实动态语言是相对静态语言而言的，静态语言的特点是在程序执行前，代码编译时从代码中就可以知道一切，比如变量的类型，方法的返回值类型：

    String s = "hello"
    s = "world"
    s = 1 // 编译时就会报错

在静态语言中，变量有类型信息，它是一块内存区域，静态语言的优点是代码结构非常规范，便于调试，但有时显得啰嗦。而动态语言只有等到程序运行时才知道一切，变量（严格来说叫名字，就像人的名字一样）不需要指定类型，变量本身没有任何类型信息，类型信息在对象身上，对象是什么类型，必须等到程序运行时才知道，动态类型语言的优点在于方便阅读，不需要写很多类型相关的代码；缺点是不方便调试，命名不规范时会造成读不懂，不利于理解等。

    s = "hello"
    s = "world"
    s = 1  # 可以给变量随意赋值，无论是什么类型都可以

**鸭子类型:**<br>
    
---

动态语言中经常提到鸭子类型，所谓鸭子类型就是：如果走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子（If it walks like a duck and quacks like a duck, it must be a duck）。鸭子类型是编程语言中动态类型语言中的一种设计风格，一个对象的特征不是由父类决定，而是通过对象的方法决定的。

如果你学的是Java或者C++等静态语言，可能对鸭子类型的理解没那么深刻，因为静态语言中对象的特性取决于其父类。而动态语言则不一样，比如迭代器，任何实现了 __iter__ 和 __next__方法的对象都可称之为迭代器，但对象本身是什么类型不受限制，可以自定义为任何类

    # python3
    class Foo:
        def __iter__(self):
            pass

        def __next__(self):
            pass

    from collections import Iterable
    from collections import Iterator

    print(isinstance(Foo(), Iterable)) # True
    print(isinstance(Foo(), Iterator)) # True

我们并不需要继承 Iterator 就可以实现迭代器的功能。当有一函数希望接收的参数是 Iterator 类型时，但是我们传递的是 Foo 的实例对象，其实也没问题，换成是Java等静态语言，就必须传递 Iterator或者是它的子类。鸭子类型通常得益于"不"测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用，这既是优点也是缺点，缺点是需要通过文档才能知道参数类型，为了弥补这方面的不足，Python3.6引入了类型信息，定义变量的时候可以指定类型，例如：
        
    def greeting(name: str) -> str:
        return 'Hello ' + name

如下代码:   

    class Cat(object):
        def say(self):
            print("i am a cat")

    class Dog(object):
        def say(self):
            print("i am a fish")

    class Duck(object):
        def say(self):
            print("i am a duck")

    animal_list = [Cat, Dog, Duck]
    for animal in animal_list:
        animal().say()

### **2.抽象基类 (abc模块)**      
    
定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法

使用 abc 模块可以很轻松的定义抽象基类：

    from abc import ABCMeta, abstractmethod

    class IStream(metaclass=ABCMeta):
        @abstractmethod
        def read(self, maxbytes=-1):
            pass

        @abstractmethod
        def write(self, data):
            pass

抽象类的一个特点是它不能直接被实例化，比如你想像下面这样做是不行的：

    a = IStream() # TypeError: Can't instantiate abstract class
                    # IStream with abstract methods read, write
        
抽象类的目的就是让别的类继承它并实现特定的抽象方法：

    class SocketStream(IStream):
        def read(self, maxbytes=-1):
            pass

        def write(self, data):
            pass

抽象基类的一个主要用途是在代码中检查某些类是否为特定类型，实现了特定接口：

    def serialize(obj, stream):
        if not isinstance(stream, IStream):
            raise TypeError('Expected an IStream')
        pass
除了继承这种方式外，还可以通过注册方式来让某个类实现抽象基类：

    import io

    # Register the built-in I/O classes as supporting our interface
    IStream.register(io.IOBase)

    # Open a normal file and type check
    f = open('foo.txt')
    isinstance(f, IStream) # Returns True

@abstractmethod 还能注解静态方法、类方法和 properties 。 你只需保证这个注解紧靠在函数定义前即可：

    class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass
### 3.使用`isinstance`而不是`type`

    class A:
    pass

    class B(A):
        pass

    b = B()

    print(isinstance(b, B)) #True
    print(isinstance(b, A))  #True
    print(type(b) is A)  #False

### 4.类变量和对象变量

    class A:
    aa = 1
    def __init__(self, x, y):
        self.x = x
        self.y = y

    a = A(2,3)

    A.aa = 11
    a.aa = 100
    print(a.x, a.y, a.aa)
    print(A.aa)

    >>>  2 3 100
    >>>11
    b = A(3,5)
    print(b.aa)
    >>> 11

### 5.类属性和实例属性以及查找顺序
    



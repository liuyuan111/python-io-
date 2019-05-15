#新式类
class D:
    pass

class E:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    name="A"
    def __init__(self):
        self.name='obj'

a=A()

print(a.name)
print(A.__mro__)

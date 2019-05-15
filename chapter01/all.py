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

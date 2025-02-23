class __Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls.__instances)
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


class MyClass(metaclass=__Singleton):
    def __init__(self, value):
        self.value = value

my_class = MyClass(10)
print(my_class.value) 

my_clas1s = MyClass(11)
print(my_clas1s.value) 
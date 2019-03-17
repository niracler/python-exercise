# """
# 题目：
#
# """


## 方法1:装饰器

def singleton1(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton1
class Foo1(object):
    """docstring for Foo1."""
    pass

## 方法2:使用基类new

class Singleton2(object):
    """docstring for Singleton2."""
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo2(Singleton2):
    """docstring fo Foo2."""
    pass




## 方法3:元类, 这个方法好像已经不行了

class Singleton(type):
    def __call__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instance

class Foo(object):
    __metaclass__ = Singleton

if __name__ == '__main__':

    foo1 = Foo1()
    foo2 = Foo1()
    print("singleton1 foo1 is foo2:" + str(foo1 is foo2))

    foo1 = Foo2()
    foo2 = Foo2()
    print("singleton2 foo1 is foo2:" + str(foo1 is foo2))

    foo1 = Foo()
    foo2 = Foo()
    print("singleton3 foo1 is foo2:" + str(foo1 is foo2))

# """
# 分析:
#
# """

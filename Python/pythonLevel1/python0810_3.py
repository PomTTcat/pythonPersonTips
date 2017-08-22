# -*- coding: utf-8 -*-


print '-------使用元类-------'
from Human import Hello
h = Hello()
h.hello()

print(type(Hello))  # Hello是一个class，它的类型就是type
print(type(h))  # h是一个实例，它的类型就是class Hello。


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()

print(type(Hello))
print(type(h))

print '-------动态 创建一个class对象-------'
# 要创建一个class对象，type()函数依次传入3个参数：
# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

print '-------metaclass-------'

# metaclass是创建类，所以必须从`type`类型派生：


class ListMetaclass(type):

    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, base, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来定制类
    # Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建

L = MyList()
L.add(2)
L.append(3)
print L

print '-------__new__()方法接收到的参数依次-------'
# __new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。

print '-------未完成-------'
# 让我们来尝试编写一个ORM框架。
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820064557c69858840b4c48d2b8411bc2ea9099ba000
print '-------模块-------'

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division

print '-------模块-------'
# https://docs.python.org/2/library/functions.html
# python内置函数

# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包

' a test module '

__author__ = 'Jeff Guan'

import sys


def test():
    args = sys.argv
    # 第一个参数永远是该.py文件的名称 比如此处是 python0810.py\
    print args[0]
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()

# test()


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# Python并没有一种方法可以完全限制访问private函数或变量

print '-------安装第三方模块-------'
# http://blog.csdn.net/xiangjai/article/details/51725106
from PIL import Image

im = Image.open('testImage.png')
print im.format, im.size, im.mode

im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

import sys
print sys.path
# ['', '/Library/Python/2.7/site-packages/pycrypto-2.6.1-py2.7-macosx-10.9-intel.egg', '/Library/Python/2.7/site-packages/PIL-1.1.7-py2.7-macosx-10.9-intel.egg', ...]

print '-------我们要添加自己的搜索目录，有两种方法：-------'
# 临时生效
# >>> import sys
# >>> sys.path.append('/Users/michael/my_py_scripts')

# 设置环境变量PYTHONPATH
# 该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

print '-------__future__-------'


# 而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。???
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3

print '-------面向对象编程-------'


# class Student(object):

#         # 第一个参数永远是实例变量self，并且，调用时，不用传递该参数
#     def __init__(self, name='jeff', score=5):
#         self.name = name
#         self.score = score

#     def print_score(self):
#         print '%s: %s' % (self.name, self.score)

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'


# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

# print '-------类和实例类和实例-------'

# # class Student(object):
# #     pass

# newbart = Student()
# print newbart
# print Student

# newbart.name = 'Bart Simpson'
# print newbart.name

# print '-------访问限制-------'
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）


import Human

jeff = Human.Student('jeff', 26)
# jeff.__name = 'jeff Guan'	# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# jeff = Student('jeff', 26)
# “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# jeff.__name = 'jeffre'	# 也是可以赋值的。但别这么干。
print jeff

dog = Human.Dog()
dog.run()

cat = Human.Cat()
cat.run()

a = list()  # a是list类型
b = Human.Animal()  # b是Animal类型
c = Human.Dog()  # c是Dog类型

print isinstance(a, list)
print isinstance(b, Human.Animal)
print isinstance(c, Human.Dog)  # c 即是狗，也是动物
print isinstance(c, Human.Animal)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Human.Animal())
run_twice(Human.Dog())

print '-------获取对象信息 type()-------'
# 用type()判断的基本类型

print type(123)
print type('str')
print type(None)
print type(abs)
print type(c)

import types
type('abc') == types.StringType
type(u'abc') == types.UnicodeType
type([]) == types.ListType
type(str) == types.TypeType  # 类型本身的类型就是TypeType

print '-------class的继承关系 isinstance()-------'
# 能用type()判断的基本类型也可以用isinstance()判断：

print '-------dir()-------'
aaa = Human.Student
print dir(aaa)
print len(Human.Student())

print len('ABC')
print 'ABC'.__len__()

print '---Human obj---'
obj = Human.MyObject()
print hasattr(obj, 'x')  # 有属性'x'吗？
print obj.x
print hasattr(obj, 'y')  # 有属性'y'吗？
print setattr(obj, 'y', 19)  # 设置一个属性'y'
print hasattr(obj, 'y')  # 有属性'y'吗？
print getattr(obj, 'y')  # 获取属性'y'
print obj.y  # 获取属性'y'

print getattr(obj, 'z', 404)  # 可以传入一个default参数，如果属性不存在，就返回默认值

# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81


print '-------面向对象高级编程-------'
print '-------使用__slots__-------'


class Student(object):
        # __slots__ = ('name', 'age')
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


print '-------实例绑定一个方法-------'
from types import MethodType
s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print s.age  # 测试结果

# 给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法


def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)
s.set_score(100)
print s.score


print '-------__slots__ 限制class的属性-------'


class snake(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

ssnak = snake()
ssnak.name = 'nanake'
ssnak.age = 10
# ssnak.male = 'man'	# 这个属性不能用来设置

# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。

# -*- coding: utf-8 -*-

print '-------@property-------'


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print s.get_score()


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
# s.score(60)
print s.score


# s.score = 9999
# @property ,重写setter方法，getter方法。加 @property 描述 getter 和 @score.setter 描述 setter
# @property装饰器就是负责把一个方法变成属性调用
# @property只定义getter方法，不定义setter方法。

print '-------只读属性-------'


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth

print '-------多重继承-------'
print '-------多重继承 相当于分类-------'


class Animal(object):
    pass

# 大类:


class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 各种动物:


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):

    def run(self):
        print('Running...')


class Flyable(object):

    def fly(self):
        print('Flying...')

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。


class Dog(Mammal, Flyable):
    pass


class BigDog(Dog):
    """docstring for BigDog"""

    def __init__(self, arg):
        super(BigDog, self).__init__()
        self.arg = arg


d = Dog()
d.fly()

bd = BigDog('name')
bd.fly()
print bd.arg

print '-------Mixin-------'
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868200511568dd94e77b21d4b8597ede8bf65c36bcd000

print '-------定制类-------'
print '-------__str__ 相当于 description -------'


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print Student('Michael')

print '-------__iter__-------'
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    # 实现了这个方法，循环的时候才会不断去调用 next。所以next这个方法也要实现
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

for n in Fib():
    print n

print '-------__getitem__-------'
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法


class Fib(object):

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()

print f[0]
print f[1]
print f[2]
print f[10]


class Fib(object):
        # 判断是 单个值 还是 切片

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print f[2]
print f[0:5]
print f[:10]

print '-------__getattr__() 有机会返回一个不存在的属性-------'


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # 捕获这个属性，并返回一个值
    # 当调用不存在的属性时，我们就有机会返回score的值
    # 返回函数也是完全可以的.
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

print '-------抛出属性异常-------'


class StudentNew(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError(
            '\'Student\' object has no attribute \'%s\'' % attr)

print '-------REST API-------'


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

print '-------__call__-------'


class Student234(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

sN = StudentNew()
s = Student234('Jeff')
print s()
print sN


print 'test sN', callable(sN)	   # sN 不能调用 sN() ，而 s() 可以。
print 'test s', callable(s)	         # 因为该类实现了 __call__ 方法。
x = [1, 2]
print 'test x', callable(x)

print 'test return', s() if callable(s) else s

print '----------'
if callable(s):
    print s(), 'line s()'
else:
    print s
    print 'line s'


class JeffClass(object):

    _count = 0

    """docstring for JeffClass"""

    def __init__(self, arg):
        super(JeffClass, self).__init__()
        self.arg = arg
        self._order = JeffClass._count + 1
        JeffClass._count = JeffClass._count + 1

    @property
    def orderNumber(self):
        return self._order


j1 = JeffClass(2)
j2 = JeffClass(3)
j3 = JeffClass(5)
j4 = JeffClass(5)
j5 = JeffClass(7)

print j1.orderNumber
print j2.orderNumber
print j3.orderNumber
print j4.orderNumber
print j5.orderNumber

print JeffClass._count


class CustomField(object):
    """docstring for CustomField"""

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'text'
        super(CustomField, self).__init__(**kw)

print '330---------------------'


class Fjs(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print "said by : ", self.name

    # 对于对象的所有特性的访问，都将会调用这个方法来处理。。。可以理解为在__getattr__之前
    def __getattribute__(self, item):
        print "访问了特性：" + item
        return object.__getattribute__(self, item)

    @classmethod
    def pCls(cls):
        print 'class method test'
        print cls


fjs = Fjs("fjs")
print '------347'
print fjs.name
print '------349'
Fjs.pCls()
print 'class method test over'
fjs.hello()

print 'newClass---------------------'
class newClass(object):
    """docstring for newClass"""

    def __init__(self):
        super(newClass, self).__init__()


class oldClass():
    """docstring for oldClass"""

    def __init__(self):
        pass


class oldToNew():
    """docstring for oldToNew"""
    __metaclass__ = type

    def __init__(self):
        super(oldToNew, self).__init__()


# 旧式类
ooC = oldClass()
print ooC.__class__     # __main__.oldClass
print type(ooC)         # <type 'instance'>

# 旧式 to 新式
onC = oldToNew()
print onC.__class__
print type(onC)

# 新式类   统一了 type 和 __class__
nnC = newClass()
print nnC.__class__
print type(nnC)
# <class '__main__.newClass'>
# <class '__main__.newClass'>

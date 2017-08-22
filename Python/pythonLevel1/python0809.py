# -*- coding: utf-8 -*-

import math

print '-------递归函数相关内容-------'


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(5)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact_iter(5, 1)

# 尾递归做优化???
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00137473836826348026db722d9435483fa38c137b7e685000

print '-------切片-------'
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]  # 从索引0开始取，直到索引3为止 L[0:3] = L[:3]

L[1:3]
L[-2:]

L = range(100)
L[:10]
L[-10:]
L[10:20]
L[:10:2]
L[::5]
L[:]
(0, 1, 2, 3, 4, 5)[:3]

print '-------迭代-------'
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key, d[key]

for ch in 'ABC':
    print ch

print '-------如何判断一个对象是可迭代对象呢？ isinstance-------'
from collections import Iterable
isinstance('abc', Iterable)  # str是否可迭代
# True
isinstance([1, 2, 3], Iterable)  # list是否可迭代
# True
isinstance(123, Iterable)  # 整数是否可迭代
# False

print '-------遍历有下标-------'
for i, value in enumerate(['A', 'B', 'C']):
    print i, value


print '-------列表生成式 iteritems()-------'
print[x * x for x in range(1, 11)]

print[x * x for x in range(1, 11) if x % 2 == 0]

print[m + n for m in 'ABC' for n in 'XYZ']

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, '=', v
# dict的iteritems()可以同时迭代key和value

x = 'abc'
y = 123
isinstance(x, str)
# True
isinstance(y, str)
# False

print '-------生成器-------'
# 一边循环一边计算的机制，称为生成器（Generator）
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
g = (x * x for x in range(10))
print g.next()
print g.next()
print g.next()
print '----'
for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


print 'fib'
fib(6)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(6)
ge = fib(6)

print ge.next()
print ge.next()
print ge.next()
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
o.next()
o.next()
o.next()

# for n in fib(6):
# 	print n

# 纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的。这种纯函数我们称之为没有副作用。
# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数


print '-------高阶函数-------'


def add(x, y, f):
    return f(x) + f(y)


def addNum(x):
    return x + 10

print add(-5, 6, addNum)


print '-------map()和reduce()-------'
# map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]) -> [1, 4, 9, 16, 25, 36, 49, 64, 81]
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


def JIEsquare(x):
    return x * x

print map(JIEsquare, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def JIEsum(x, y):
    return x + y

print reduce(JIEsum, [1, 3, 5, 7, 9])

# ------------------------------------


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print map(char2num, '13579')
print reduce(fn, map(char2num, '13579'))

#	^^||
#	||VV


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

testList = ['adam', 'LISA', 'barT']


def JIEfirstCharUp(x):
    str = x.lower()
    str = str[0].upper() + str[1:]
    return str

print '-----------'
print map(JIEfirstCharUp, testList)

strr = 'dasdas'
print strr.upper


def prod(x, y):
    return x * y

print reduce(prod, [1, 2, 3, 4, 5])


def prod2(*customNumbers):
    return reduce(prod, customNumbers)

List228 = [1, 2, 3, 4, 5]
print prod2(*List228)

print '-------filter()-------'


def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


print '-------sorted-------'
# 对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

print '-------返回函数-------'


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)

print f
print f()


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1()
print f2()
print f3()
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

print '-------匿名函数-------'

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def build(x, y):
    return lambda: x * x + y * y

bb = build(5, 6)

print bb()

print '-------装饰器-------'

# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# def log(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper

import functools
# def log(func):
#     @functools.wraps(func)	# 可以取消上面的注释，比较下两个函数的差别。
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         backfunc = func
#         return func(*args, **kw)
#     return wrapper


def log(func):
    @functools.wraps(func)  # 可以取消上面的注释，比较下两个函数的差别。
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__

        def backfunc():
            func(*args, **kw)
            print 'end %s():' % func.__name__

        return backfunc()
    return wrapper


# @log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print '2013-12-25'

f = now

print now.__name__  # 'now'
print f.__name__  # 'now'


print now()


print '-------偏函数-------'
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int('12345')
# 12345
int('12345', base=8)
# 5349
int('12345', 16)
# 74565


def int2(x, base=2):
    return int(x, base)

int2('1000000')
int2('1010101')

int2 = functools.partial(int, base=2)
int2('1000000')

max2 = functools.partial(max, 10)
print max2(5, 6, 7)


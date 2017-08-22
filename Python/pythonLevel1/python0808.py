# -*- coding: utf-8 -*-

import math
import mysql

print ord('A')

a = int('12313123') + 5
print a

print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#---------------------------	list 相当于 mutableArray
print '-------list相关内容-------'
classmates = ['Michael', 'Bob', 'Tracy']
print classmates[-1]

classmates.append('Jack')
print classmates

classmates.insert(1, 'Jeff')
print classmates

classmates.pop(1)  # pop index 1
print classmates

classmates[1] = 'Sarah'  # 直接赋值
print classmates

#---------------------------	tuple 一旦初始化就不能修改,相当于array
print '-------tuple相关内容-------'
tupleTest = (1, 2, 3)
print tupleTest

tupleTest = (1, 2)
print tupleTest

t = (1,)  # 如果只有一个元素，要加 逗号 。不然python会理解为这是一个数
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
#---tuple的每个元素，指向永远不变. t[2]是一个list，指向list没变，list内的元素发生变化。


#------if else
print '-------if判断相关内容-------'
maleage = 30
if maleage >= 18:
    print 'your age is', maleage
else:
    print 'naive'


age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

#-------for in
print '-------for in 循环相关内容-------'
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

print '-------range-------'
print range(5)

print '-------dict 相关内容-------'
# 相当于nsmutableDictionary
# 如果key不存在，dict就会报错.

nameScoreDict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print nameScoreDict['Michael']

# 要避免key不存在的错误，有两种办法
'Thomas' in nameScoreDict
nameScoreDict.get('Thomas')

nameScoreDict.get('Thomas')
nameScoreDict.get('Thomas', -1)  # 可以返回None，或者自己指定的value

nameScoreDict.pop('Bob')  # 移除
# key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

print '-------set 无序和无重复元素的集合-------'
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 2, 3, 3])  # 过滤重复的值
print s
s.add(4)
s.remove(4)  # 如果该key没有则会报错

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
# set([2, 3])
print s1 | s2
# set([1, 2, 3, 4])
# set和dict的唯一区别仅在于没有存储对应的value.同样不可以放入可变对象（key）

print '-------对象总结-------'
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# ------------------------------ 函数 ------------------------------
# ------------------------------ 内置函数 ------------------------------
abs(-100)
cmp(1, 2)  # -1
cmp(2, 1)  # 1
cmp(2, 2)  # 0

# ------------------------------ 自定义函数 ------------------------------
print '------------- 自定义函数 -------------'


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 如果参数类型不对，Python解释器就无法帮我们检查. 	但可以用abs('A')来检查错误的类型

my_abs(2)
# my_abs('a')	# 可以添加手动检查

print '------------- 返回多个值 -------------'

# 其实返回的是tuple


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r

print '-------函数的参数相关内容-------'

# n 如果有默认参数，那传入参数时可以不传这个参数


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(4)
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错。
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738449338c8a122a7f2e047899fc162f4a7205ea3000


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

# enroll('Sarah', 'F')
# enroll('Adam', 'M', 'Tianjin')	# 如果不写city='Tianjin','Tianjin'会被付给age
enroll('Adam', 'M', city='Tianjin', age=3)  # 正确写法,顺序可以变化

print '-------定义默认参数要牢记一点：默认参数必须指向不变对象-------'
# 定义默认参数要牢记一点：默认参数必须指向不变对象!!!!!!!

# 一个 * 是list或tuple


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 两个 ** 是dict


def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

print calc(1, 2, 3)
print calc(1, 3, 5, 7)
nums = [1, 2, 3]
print calc(*nums)

person('Adam', 45, gender='M', job='Engineer')

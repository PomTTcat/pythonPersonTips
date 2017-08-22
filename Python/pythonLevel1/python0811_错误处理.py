# -*- coding: utf-8 -*-
import os
import logging

print '-------try-------'

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:  # 如果没有捕获异常 else 会执行。
    print 'no error!'
finally:
    print 'finally...'
print 'END'

print '-------except 不但捕获该类型的错误，还把其子类也“一网打尽”-------'
print '-------错误继承关系-------'
# https://docs.python.org/2/library/exceptions.html#exception-hierarchy

print '-------非ASCII编码的文本文件-------'

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('5') # 改成 bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END Last'

print '-------抛出自定义错误-------'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo(1)


print '-------raise语句如果不带参数，就会把当前错误原样抛出-------'
# err.py
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise # raise语句如果不带参数，就会把当前错误原样抛出

def main():
    bar('1') # 要设置 bar('0')

main()

print '-------不应该把一个IOError转换成毫不相干的ValueError-------'

try:
    10 / 1 # 10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

print '-------抛出自定义错误-------'
print '-------抛出自定义错误-------'
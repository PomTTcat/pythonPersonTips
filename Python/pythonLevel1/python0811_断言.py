# -*- coding: utf-8 -*-
import logging
import pdb
logging.basicConfig(level=logging.INFO)
# debug，info，warning，error


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('1')

main()


print '-------关闭断言-------'
# 启动Python解释器时可以用-O参数来关闭assert。关闭后，你可以把所有的assert语句当成pass来看。
# python -O err.py

print '-------try-------'


s = '2'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

print '-------pdb-------'
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138683229901532c40b749184441dbd428d2e0f8aa50e000

# pdb.set_trace()
print 'asd'
print 'asd'
print 'asd'
print 'asd'
print 'asd'
# pdb.set_trace()
s = '0'
n = int(s)
# print 10 / n


# n 执行下一行命令
# c 继续执行 到下一个pdb.set_trace() YES
# q 退出
# p x 打印变量名
# pdb.set_trace() 程序会自动在pdb.set_trace()暂停

print '-------单元测试-------'
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140137128705556022982cfd844b38d050add8565dcb9000


print '-------单元测试 父类super-------'


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

nmm = Dict(a=1, b=4, c=8)
print nmm.a
print nmm.c


print '-------单元测试 TestDict-------'
import unittest

# self.assertEquals(abs(-1), 1) # 断言函数返回的结果与1相等
# self.assertTrue(isinstance(d, dict)) #

# setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：
class TestDict(unittest.TestCase):

        # 这个方法必须写在最前面
    def setUp(self):
        print 'setUp...'

        # 这个方法不一定写最前面，建议写在一起
    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()



print '-------文档测试-------'
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

print abs(2)

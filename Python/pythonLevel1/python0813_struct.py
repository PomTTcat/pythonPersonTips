# -*- coding: utf-8 -*-

import struct
# 未学习

print '-------hashlib-------'


import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()

print '-------itertools-------'

import itertools
natuals = itertools.count(1)
print natuals
# for n in natuals:
# 	print n

print '-------cycle()-------'
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
# 	print c


print '-------repeat()-------'
ns = itertools.repeat('A', 10)
for n in ns:
	print n


print '-------takewhile()-------'
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
	print n

print '-------chain()-------'
for c in itertools.chain('ABC', 'XYZ'):
    print c


print '-------groupby()-------'
for key, group in itertools.groupby('AAABBBCCAAA'):
	print key, list(group) # 为什么这里要用list()函数呢？

print '--------------'
for key, group in itertools.groupby('AAaBBBCCAAA'):
	print key, list(group) # 为什么这里要用list()函数呢？

print '--------------'
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print key, list(group)

print '-------imap()-------'
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
	print x
# imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准

r = itertools.imap(lambda x: x*x, [1, 2, 3])
# r只是一个迭代对象

r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
	print n

# 迭代对象，只有用for循环迭代的时候才真正计算。
# -*- coding: utf-8 -*-

import struct
# δѧϰ

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
cs = itertools.cycle('ABC') # ע���ַ���Ҳ�����е�һ��
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
	print key, list(group) # Ϊʲô����Ҫ��list()�����أ�

print '--------------'
for key, group in itertools.groupby('AAaBBBCCAAA'):
	print key, list(group) # Ϊʲô����Ҫ��list()�����أ�

print '--------------'
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print key, list(group)

print '-------imap()-------'
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
	print x
# imap()�����������������У����ң�����������еĳ��Ȳ�һ�£��Զ̵��Ǹ�Ϊ׼

r = itertools.imap(lambda x: x*x, [1, 2, 3])
# rֻ��һ����������

r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
	print n

# ��������ֻ����forѭ��������ʱ����������㡣
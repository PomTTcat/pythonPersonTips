# -*- coding: utf-8 -*-
import os

print '-------namedtuple-------'
# 定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 新建一个子类，叫Point

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y

print isinstance(p, Point)
print isinstance(p, tuple)

print '-------坐标和半径表示一个圆-------'
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])


print '-------list存储数据-------'
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低

print '-------deque-------'

from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。

print '-------defaultdict-------'

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']  # key1存在
'abc'
print dd['key2']  # key2不存在，返回默认值
'N/A'

# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
print '-------二进制文件-------'

from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d  # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('d', 4), ('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od.keys()  # 按照插入的Key的顺序返回
['z', 'y', 'x']

print '-------FIFO（先进先出）的dict-------'


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

print '-------Counter-------'

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。

print '-------base64-------'

# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001399413803339f4bbda5c01fc479cbea98b1387390748000

import base64
print base64.b64encode('binary\x00string')
'YmluYXJ5AHN0cmluZw=='
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
'binary\x00string'


print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd++//'
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd--__'
print base64.urlsafe_b64decode('abcd--__')

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。


def safe_b64decode(str):
    needAddNumber = 4 - len(str) % 4
    if needAddNumber != 4:
        for x in xrange(0, needAddNumber):
            str = str + '='
    return base64.b64decode(str)

print safe_b64decode('YWJjZA==')
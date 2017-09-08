# -*- coding: utf-8 -*-

print '-------Zip 小技巧-------'

# zip 输出的是一个tuple，但如果有两个参数去接收。则接收一个tuple中对象的第一个参数和第二个参数。
# cols, args = zip(*kw.iteritems())


a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)

print zipped
print zip(a, c)
print zip(*zipped)

params = dict()
for k, v in zip(a, b):
    params[k] = v

print params

print dict(zip(a, b))


_HEADER_X_POWERED_BY = ('X-Powered-By', 'transwarp/1.0')
print _HEADER_X_POWERED_BY.__class__
print[_HEADER_X_POWERED_BY].__class__

import urllib


def _quote(s, encoding='utf-8'):
    '''
    Url quote as str.

    >>> _quote('http://example/test?a=1+')
    'http%3A//example/test%3Fa%3D1%2B'
    >>> _quote(u'hello world!')
    'hello%20world%21'
    '''
    if isinstance(s, unicode):
        s = s.encode(encoding)
    # 对s进行编码。get方式提交数据的时候，会在url中添加key=value这样的字符串。保证value没有'='这个符号。
    return urllib.quote(s)


# 用utf-8解码
def _unquote(s, encoding='utf-8'):
    '''
    Url unquote as unicode.

    >>> _unquote('http%3A//example/test%3Fa%3D1+')
    u'http://example/test?a=1+'
    '''
    # 先用urllib解码，然后用utf-8解码。
    return urllib.unquote(s).decode(encoding)


str1 = 'http://example/test?a=1+'
# str1 = 'http://example/test?a=1+'
str2 = _quote(str1)
print str2
str3 = _unquote(str2)
print str3

import re

_re_route = re.compile(r'(\:[a-zA-Z_]\w*)')
str44 = '/:user/:comments/list'
print _re_route.split(str44)
print _re_route.split
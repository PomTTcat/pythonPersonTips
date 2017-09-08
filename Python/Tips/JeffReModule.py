# -*- coding: utf-8 -*-

import re

pattern = 'h*'
patternDiff = r'ABC\-001'

string = 'h'
pat = re.compile(pattern)
result = pat.match(string)

if result:
    print 'ok'
else:
    print 'failed'

# 等同與
result3 = re.match(pattern, string)
print 'result3:',result3


result2 = re.match(patternDiff, r'ABC-001')
if result2:
    print 'ok'
else:
    print 'failed'

'''
\d		可以匹配 一个数字
\w		可以匹配 一个字母 或 数字
. 		可以匹配任意字符（不包括0个）。 比如 h. 不匹配 'h',因为这里只有一个h，至少再加任意的字符才行。
*		表示任意个字符（包括0个）

+		表示至少一个字符
?		表示0个或1个字符
{n}		表示n个字符
\s 		可以匹配一个空格（也包括Tab 等空白符）

- 		特殊字符，所以需要加'\'

A|B可以匹配A或B		所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头			^\d表示必须以数字开头。
$表示行的结束			\d$表示必须以数字结束。


'''

re.split(r'([\s\,\;]+)', 'a,b;; c  d')


    >>> _build_regex('/path/to/:file')
    '^\\/path\\/to\\/(?P<file>[^\\/]+)$'
    >>> _build_regex('/:user/:comments/list')
    '^\\/(?P<user>[^\\/]+)\\/(?P<comments>[^\\/]+)\\/list$'
    >>> _build_regex(':id-:pid/:w')


re.compile(r'[\s\,\;]+').split('a,b;; c  d')



re.compile(r'(\:[a-zA-Z_]\w*)').split('/path/to/:file')
['/path/to/', ':file', '']
'^\\/path\\/to\\/(?P<file>[^\\/]+)$'


re.compile(r'(\:[a-zA-Z_]\w*)').split('/:user/:comments/list')
['/', ':user', '/', ':comments', '/list']
'^\\/(?P<user>[^\\/]+)\\/(?P<comments>[^\\/]+)\\/list$'


re.compile(r'(\:[a-zA-Z_]\w*)').split(':id-:pid/:w')
['', ':id', '-', ':pid', '/', ':w', '']
'^(?P<id>[^\\/]+)\\-(?P<pid>[^\\/]+)\\/(?P<w>[^\\/]+)$'




# -*- coding: utf-8 -*-

# encoding:UTF-8


def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)
    # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    return i * 2

# # 使用for循环
# for i in yield_test(5):
#     print(i, ",")


str1 = "this is string example....wow!!!"
str2 = "exam"

print str1.find(str2)
print str1.find(str2, 10)
print str1.find(str2, 40)

info = 'abca'
print info.find('a')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0

print info.find('a', 1)  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3

print info.find('3')    # 查找不到返回-1

import urllib
# 用utf-8解码


def _unquote(s, encoding='utf-8'):
    '''
    Url unquote as unicode.

    >>> _unquote('http%3A//example/test%3Fa%3D1+')
    u'http://example/test?a=1+'
    '''
    # 先用urllib解码，然后用utf-8解码。
    return urllib.unquote(s).decode(encoding)

_cookies = 'Cookie:BAIDUID=353F4FF9B434EAB6113F1C3E6C0E49B3:FG=1; BIDUPSID=353F4FF9B434EAB6113F1C3E6C0E49B3; PSTM=1503311383; BD_CK_SAM=1; BD_HOME=0; BD_UPN=123253; bd_traffictrace=051619; plus_lsv=8b4f19c2305ae69a; plus_cv=1::m:21732389; BDICON=10294984.98; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; lsv=globalTjs_8d1c9eb-wwwT_newuxcss_c62473f-new_rcmdcss_67a57d1-wwwBcss_a64e9cc-framejs_7957add-globalBjs_e697cc6-sugjs_5b65c32-wwwjs_56c2446; BDRCVFR[5GQZCjFg8mf]=mk3SLVN4HKm; H_WISE_SIDS=114750_117615_118308_110137_115654_118506_100097_118592_114243_119023_119005_118943_118933_118897_118859_118842_118836_118795_118674_118624_107313_119044_118450_118969_118235_117581_117335_117235_117432_118327_118325_118132_118219_118473_118966_117554_117635_118323_116408_110085; BDSVRTM=564; PSINO=2; MSA_WH=310_851; MSA_PBT=146; MSA_ZOOM=1000'

cookies = {}
cookie_str = _cookies
if cookie_str:
    for c in cookie_str.split(';'):
        pos = c.find('=')
        if pos > 0:
            cookies[c[:pos].strip()] = _unquote(c[pos + 1:])

# print cookies

str = "         0000000this is string example....wow!!!0000000"
# print str.strip()

# {'PSINO': u'2', 'BD_CK_SAM': u'1', 'BDRCVFR[5GQZCjFg8mf]': u'mk3SLVN4HKm', 'bd_traffictrace': u'051619', 'BIDUPSID': u'353F4FF9B434EAB6113F1C3E6C0E49B3', 'BDICON': u'10294984.98', 'H_WISE_SIDS': u'114750_117615_118308_110137_115654_118506_100097_118592_114243_119023_119005_118943_118933_118897_118859_118842_118836_118795_118674_118624_107313_119044_118450_118969_118235_117581_117335_117235_117432_118327_118325_118132_118219_118473_118966_117554_117635_118323_116408_110085', 'BDSVRTM': u'564', 'plus_lsv': u'8b4f19c2305ae69a', 'lsv': u'globalTjs_8d1c9eb-wwwT_newuxcss_c62473f-new_rcmdcss_67a57d1-wwwBcss_a64e9cc-framejs_7957add-globalBjs_e697cc6-sugjs_5b65c32-wwwjs_56c2446', 'MSA_WH': u'310_851', 'BD_UPN': u'123253', 'MSA_ZOOM': u'1000', 'BDORZ': u'AE84CDB3A529C0F8A2B9DCDD1D18B695', 'plus_cv': u'1::m:21732389', 'Cookie:BAIDUID': u'353F4FF9B434EAB6113F1C3E6C0E49B3:FG=1', 'MSA_PBT': u'146', 'PSTM': u'1503311383', 'BD_HOME': u'0'}

from StringIO import StringIO

# print StringIO('a=1&b=M%20M&c=ABC&c=XYZ&e=')

import cgi


def main():
    print "Content-type: text/html\n"
    form = cgi.FieldStorage()  # parse query
    if form.has_key("firstname") and form["firstname"].value != "":
        print "<h1>Hello", form["firstname"].value, "</h1>"
    else:
        print "<h1>Error! Please enter first name.</h1>"
main()


cgi.FieldStorage('xixi1'='haha1','xixi2'='haha2',[])

cgi.FieldStorage('xixi1'='haha1','xixi2'='haha2','xixi12'='haha12')
# -*- coding: utf-8 -*-
import os

currentFilePath = os.getcwd()
filePath = currentFilePath + '/IO.txt'
imageFilePath = currentFilePath + '/testImage.png'
txtFilePath = currentFilePath + '/测试.txt'
print filePath

# f = open(filePath, 'r')

# print f.read()
# f.close()

# 有可能产生IOError，一旦出错，后面的f.close()就不会调用
try:
    f = open(filePath, 'r')
    print f.read()
finally:
    if f:
        f.close()
        print 'close success' # 前提是打开文件成功。不然 f 不存在。


with open(filePath, 'r') as f:
    print f.read()


f = open(filePath, 'r')


print dir(f)
size = 10
print f.read(size)
f.close()

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉

print '-------二进制文件-------'

print imageFilePath
f = open(imageFilePath, 'rb')
print f.read()
f.close()

print '-------非ASCII编码的文本文件-------'
f = open(txtFilePath, 'rb')
u = f.read().decode('utf-8')
print u
f.close()


print '-------写文件-------'
f = open(txtFilePath, 'w')
f.write('中文测试')
f.close()

with open(txtFilePath, 'w') as f:
    f.write('中文测试')

print '-------codecs自动转换成指定编码-------'
import codecs
with codecs.open(txtFilePath, 'r', 'utf-8') as f:
    print f.read() 
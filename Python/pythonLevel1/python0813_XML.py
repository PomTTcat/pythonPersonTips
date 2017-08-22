# -*- coding: utf-8 -*-

print '-------DOM vs SAX-------'
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
print parser.Parse(xml)


print '-------生成XML-------'
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
# return ''.join(L)

print '-------HTMLParser-------'
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed(
    '<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

print '-------操作图像-------'
from PIL import Image
from PIL import ImageFilter

import os

currentFilePath = os.getcwd()
imageFilePath = currentFilePath + '/testImage.png'
thumbImageFilePath = currentFilePath + '/thumbnail.png'
blurImageFilePath = currentFilePath + '/testblur.png'
# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open(imageFilePath)
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save(thumbImageFilePath, 'jpeg')

print '-------blur-------'

im = Image.open(imageFilePath)
im2 = im.filter(ImageFilter.BLUR)
im2.save(blurImageFilePath, 'jpeg')

http://effbot.org/imagingbook/
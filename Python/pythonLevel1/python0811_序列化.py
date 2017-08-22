# -*- coding: utf-8 -*-


print '-------序列化-------'
# 变量从内存中变成可存储或传输的过程称之为序列化

# pickle.dumps(d)	序列化
# pickle.dump(d, f)	序列化并导入文件
# pickle.load(f)	从文件中加载内容

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
# print d

print '-------json-------'
import json

# json.dumps(d)

d = dict(name='Bob', age=20, score=88)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)

print '-------JSON进阶-------'
# https://docs.python.org/2/library/json.html#json.dumps


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s))

# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str, object_hook=dict2student))

# print(json.loads(json_str, object_hook=lambda obj.__dict__:obj))

# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name='Jeff', score=100):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 可以判断传入的值是不是适合
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def __len__(self):
        return 100


class Animal(object):

    def run(self):
        print 'Animal is running...'


class Dog(Animal):

    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'


class Cat(Animal):

    def run(self):
        print 'Cat is running...'


class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
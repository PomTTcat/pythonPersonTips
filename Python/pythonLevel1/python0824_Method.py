# -*- coding: utf-8 -*-

print '-------@property-------'


class Model(dict):

    def __init__(self, **kw):
        self.fly = 'flyMe'
        super(Model, self).__init__(**kw)

    # method before __getattr__ 调用普通对象方法，也会走这个方法。方法调用视为getattr。
    # def __getattribute__(self, item):
    #     print "访问了特性：" + item
    #     return object.__getattribute__(self, item)

    def __getattr__(self, key):
        print 'get happen', key
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

        # 当试图对象的item特性赋值的时候将会被调用
    def __setattr__(self, key, value):
        print 'set key:', key, value
        self[key] = value

    def hello(self):
        print 'hello world'

    @property
    def score(self):
    	print 'in happen?'
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


mod = Model()
mod.hello() # 直接调用hello，因为有该方法，所以不会调用getattr
mod.score = 10
print mod.score
# mod.name = 'ZQY'

# print mod.name

# # # fly 函数本来就有。所以没走 __setattr__
# mod.fly = 'GYJ'
# print mod.fly

# mod.hello()

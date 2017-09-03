# -*- coding: utf-8 -*-


class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
    	print cls
    	print name
    	print bases
    	print attrs
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来定制类


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
    	print 'In:', attrs
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        # 如果属性是Field的实例 则添加到mapping中
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        # 这一步是不是可以放到attrs遍历中。最好还是分开？
        # 所以的field对象剔出attrs
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name  # 假设表名和类名一致
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        print 'Out:', attrs
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            # self 对象中有属性k则添加到args，否则添加none。
            args.append(getattr(self, k, None))
        # 自动生成sql的语句
        sql = 'insert into %s (%s) values (%s)' % (
            self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

print '----------'

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

'''
In: {'__module__': '__main__', '__metaclass__': <class '__main__.ModelMetaclass'>, '__setattr__': <function __setattr__ at 0x106d14668>, '__getattr__': <function __getattr__ at 0x106d145f0>, 'save': <function save at 0x106d146e0>, '__init__': <function __init__ at 0x106d14578>}

In: {'email': <__main__.StringField object at 0x106d1a450>, '__module__': '__main__', 'password': <__main__.StringField object at 0x106d1a490>, 'id': <__main__.IntegerField object at 0x106d1a3d0>, 'name': <__main__.StringField object at 0x106d1a410>}
'''


mappings = {'abc': '1ogo1', 'abd': '2ogo2', 'bbc': '4ogo4', 'ccc': '5ogoz'}
app = dict()
print sorted(mappings.values(), lambda x, y: cmp(x._order, y._order))
print mappings.values()


#-*- coding:utf-8 -*-

class Field(object):
    def __init__(self, name, column_type):
        self.m_Name = name
        self.m_ColType = column_type

    def __str__(self):
        return "<%s:%s>"%(self.__class__.__name__, self.m_Name)

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print("New:%s" % name)
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model:%s" % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s -> %s"%(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __int__(self, **kw):
        super(Module, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model has no attr '%s'"%key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.m_Name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)'%(self.__table__, \
                ','.join(fields), ','.join(params))
        print("SQL: %s" % sql)
        print("ARGS: %s" % str(args))

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")


#创建一个类时，会先创建父类
class User1(object):
    pass

user1 = User1()#因为此处生成了类，所以下面User类生成时，不会生成父类User1

class User(Model, User1):
    iID = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

    def Func(self):
        pass
u = User()
print("New User")#第一次创建类的时候才会调用Meataclass
u1 = User()
u = User(a=1, iID = 12345, name="xhx", email = "hehe@qq.com", password = "mypwd")
u.save()


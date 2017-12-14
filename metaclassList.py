#-*- coding:utf-8 -*-

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print("CLS", cls)
        print("Name", name)
        print("Bases", bases)
        print("Attr", attrs)
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

if __name__ == '__main__':
    L = MyList()
    L.add(1)
    print(L)

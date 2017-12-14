#-*- coding:utf-8 -*-

def createCount():
    i = 0
    def counter():
        return i
    return counter

counter = createCount()
print(counter(), counter())

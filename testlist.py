#-*- coding:utf-8 -*-

from time import time

t=time()
list = ['a', 'b', 'is', 'python', 'jason', 'hello', 'hill']
for i in range(1000000):
    total = []
    for w in list:
        total.append(w)
print "len1:", len(total)
print "total run time 1",time()-t

t=time()
for i in range(1000000):
    a=[w for w in list]

print "len2:", len(a)
print "total run time 2",time()-t

t=time()
for i in range(1000000):
    a=(w for w in list)

print "total run time 3",time()-t

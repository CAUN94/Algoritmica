# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:12:13 2016

@author: Cristobal
"""
a0=[]
a1=[]
def fib(x):
    
    if(x==0):
        
        return 0
    if(x==1):
        
        return 1
        
    a=fib(x-1)
    b=fib(x-2)
    if a==0:
        print 0,"a"
        a0.append(0)
    else:
        print 1,"a"
        a1.append(1)
    if b==0:
        print 0,"b"
        a0.append(0)
    else:
        print 1,"b"
        a1.append(1)
    return [a0,a1]
    
print fib(1)
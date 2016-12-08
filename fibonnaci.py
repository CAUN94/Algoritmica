# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:32:37 2016

@author: Cristobal
"""

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-2) + fib(n-1)


def solution (target):
    n=0;
    fibo=[];
    
    value=fib(n);
    
    while(value<=target):
        n=n+1;
        
        value=fib(n);
        fibo.append(value);

    print fibo;
    print n;
    
    a=fibo[n-1]-target;
    b=target-fibo[n-2];
    print a,b
    

solution (19)
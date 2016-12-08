# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 00:03:04 2016

@author: Cristobal
"""

numCreates = 14
loadsize = 3
array=[]

def 	numTrucks(n,l):
    if n%2==0:
        div=n/2
        a=div
        b=div
    else:
        div=n/2
        a=div
        b=div+1
    if a<=l :
        array.append(a)       
    else:
        numTrucks(a,l)
    if b<=l :
        array.append(b)        
    else:
        numTrucks(b,l)
    
numTrucks(numCreates,loadsize)
print array

print len(array)



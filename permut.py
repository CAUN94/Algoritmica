# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:50:41 2016

@author: Cristobal
"""
def permut(array):
    res=[]
    if len(array) == 1:
        return [array]
        
    for permutation in permut(array[1:]):
        for i in range(len(array)): 
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    return res
    
array=[1,2,3,4,5,6]
a=permut(array)
print a
n=3
b=1110



    




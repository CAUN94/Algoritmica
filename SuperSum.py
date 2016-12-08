# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:21:08 2016

@author: Cristobal
"""

#
#SuperSum(0 , n) = n, for all positive n.
#SuperSum(k , n) = SuperSum(k-1 , 1) + SuperSum(k-1 , 2) + ... + SuperSum(k-1 , n), for all positive k, n.


def SuperSum(k,n):
    answer=0
    if(k==0):
        return n
    
    for i in xrange(1,n+1):
        
        value=SuperSum(k-1,i)
        answer=answer+ value
    
    return answer
answer=SuperSum(10,10)
print answer
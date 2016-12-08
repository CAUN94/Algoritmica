# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 22:48:34 2016

@author: Cristobal
"""
import random as r
import copy


def binary_search(S,X,i):
    
    while (len(S)!=0):
  
       if(S[i]==X):
           
           return True
       elif S[i]<X:
           
           for x in xrange (i+1):
               S.pop(0)

       else:
           length=len(S)
           for x in xrange (i,length):
               S.pop(len(S)-1)   

       if(len(S)!=0):
           i=r.randrange(0,len(S))
       
    return False


S=[5, 4, 3, 2, 1, 0 ]

final=0
for j in xrange(len(S)):
    cont=0
    for i in xrange (len(S)):
        array=copy.copy(S)
        
        value=binary_search(array,S[j],i)          
        if (value):
            cont=cont+1
    if (cont==len(S)):
        final=final+1
        
print final
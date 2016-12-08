# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:07:36 2016

@author: Cristobal
"""

vec=[1,2,3,4]
n=3
b=1109


def cumber(vec,n,b):
    for i in xrange(len(vec)):
        for j in xrange(len(vec)):
            if(i!=j):
                for k in xrange(len(vec)):
                    if(i!=j and j!=k and k!=i):
                        print vec[i],vec[j],vec[k]
                        


count=0
while (count!=len(vec)):
    count=count+1
    for i in range(len(vec)):
        print vec[i]
        
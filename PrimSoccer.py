# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 00:41:59 2016

@author: Cristobal
"""
import random as r
def getProbability (a,b):
    
    ax= r.randrange(1,100)
    bx= r.randrange(1,100)
    
    print ax,bx
    
    
    if(ax<=a):
        print "Gol A"
    else:
        print "No Gol A"
    if(bx<=b):
        print "Gol B"
    else:
        print "No Gol B"
        

getProbability (70,100)
            


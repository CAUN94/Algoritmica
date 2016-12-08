# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 23:08:27 2016

@author: Cristobal
"""

from random import randrange
final =  [3,2,1,7,9,4,5,10]
first = [1,9,3,1,2,7,6,8]
firstfinal = []
ifc = []
price = []
time = []
cost = []
sets = []
sums = []
union= []
all=[]
numeros  =[]
numeros2  =[]
numeros3  =[]
finalfinal = []
last=[]

table= []
for i in xrange(int(len(final))):
    price.append(randrange(1,9))
for i in xrange(int(len(final))):
    time.append(int(final[i])-int(first[i])+1)
for i in xrange(int(len(final))):
    a=first[i]
    b=final[i]
    c=a,b
    firstfinal.append(c)    
for i in xrange(int(len(final))):
    a=price[i]
    b=firstfinal[i]
    c=b,a
    ifc.append(c)
for i in xrange(int(len(ifc))):
    a=ifc[i]
    b=price[i]
    c=a,b
    cost.append(c)
    
def opt(first,final,price):
    for i in xrange(int(len(cost))):
        for j in xrange(int(len(cost))):
          if (cost[i][0][0][1]<cost[j][0][0][0] ):
              a=firstfinal[i]
              b=firstfinal[j]
              d=a,b
              sets.append(d)
             

    for i in xrange(int(len(sets))):
        suma = 0
        sumas = 0
        for j in xrange(int(len(ifc))):
            if sets[i][0]==ifc[j][0]:
                suma = ifc[j][1]
                
            elif sets[i][1]==ifc[j][0]:
                sumas = ifc[j][1]
                
                
        sumita = suma+sumas
        sums.append(sumita)
    for i in xrange(int(len(sets))):
        d=sums[i]
        e=sets[i]
        f = d,e
        union.append(f)
        
    size = int(len(union))
    for i in xrange(size):
        for j in xrange(size):
            if union[i][1][1]==union[j][1][0]:
                    a=union[i]
                    b=union[j]
                    c=a,b
                    all.append(c)
            
        
    
    for i in xrange(int(len(all))):
        
        a=all[i][0][1][0]
        b=all[i][0][1][1]
        c=all[i][1][1][1]
        
        e=a,b,c
        finalfinal.append(e)
    for i in xrange(int(len(finalfinal))):
        exsum=0
        for j in xrange(int(len(ifc))):
            if finalfinal[i][0]==ifc[j][0]:
                exsum+=ifc[j][1]
        numeros.append(exsum)
    for i in xrange(int(len(finalfinal))):
        exsuma=0
        for j in xrange(int(len(ifc))):
            if finalfinal[i][1]==ifc[j][0]:
                exsuma+=ifc[j][1]
        numeros2.append(exsuma)
    for i in xrange(int(len(finalfinal))):
        exsumas=0
        for j in xrange(int(len(ifc))):
            if finalfinal[i][2]==ifc[j][0]:
                exsumas+=ifc[j][1]
        numeros3.append(exsumas)
    for i in xrange(int(len(numeros))):
        a=numeros[i]
        b=numeros2[i]
        c=numeros3[i]
        d=a+b+c
        table.append(d)
    for i in xrange(int(len(finalfinal))):
        a=table[i]
        b=finalfinal[i]
        c=a,b
        last.append(c)
        
    for i in xrange(int(len(union))):
        print union[i]
    for i in xrange(int(len(last))):
        print last[i]
       
    
        
opt(first, final, price)
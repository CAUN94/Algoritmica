# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:56:35 2016

@author: FcoMerino
"""
import networkx as nx
g = nx.Graph()
costo = 2100
banco = [12, 1000, 1100, 200]
largo = len(banco)
bol=False


for i in xrange(largo):
    if costo == banco[i]:
        print 'POSSIBLE'
        print i, banco[i]
        break
    
    elif banco[i] <  costo:
        for j in xrange(i+1,largo):
            value1= banco[i]+banco[j]  
            if value1 == costo:
                print 'POSSIBLE'
                print i,j,value1
                bol=True 
                break
            elif value1 < costo:
                for k in xrange(j+1,largo):
                    value2=value1+banco[k]  
                    if value2 == costo:
                        print 'POSSIBLE'
                        print i,j,k,value2
                        bol=True 
                        break
                    elif value2<costo:
                        for l in xrange(k+1,largo):
                            value3 = value2+banco[l]
                            if value3 == costo:
                                print 'POSSIBLE'
                                print i,j,k,l,value3
                                bol=True 
                                break
                        
            
            
if bol==False:
    print 'IMPOSSIBLE'
        
                

    
    
    

                
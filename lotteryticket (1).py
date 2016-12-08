# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:56:35 2016

@author: FcoMerino
"""
import networkx as nx
g = nx.Graph()
costo = 65
banco = [1, 5, 10, 50]
largo = len(banco)




for i in xrange(largo):
    if costo == banco[i]:
        print 'POSSIBLE1'
        break
    for j in xrange(i+1,largo):
        value1=banco[i]+banco[j]
        if value1==costo:
            print 'POSSIBLE2'
            break
        elif value1<costo:
            for k in xrange(j+1,largo):
                value2=value1+banco[k]
                if value2==costo:
                    print 'POSSIBLE3'
                    break
                elif value2<costo:
                    for l in xrange(k+1,largo):
                        value3=value2+banco[l]
                        if value3==costo:
                            print 'POSSIBLE4'
                            break
    else:
        print 'IMPOSSIBLE'
        break
print value1, value2, value3
    

    
                
            
            

        
                

    
    
    

                
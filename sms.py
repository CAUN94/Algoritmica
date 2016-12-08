# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:32:01 2016

@author: 
"""
import networkx as nx


g = nx.Graph()

array=[100, 200, 300, 400]

sort=sorted(array);


def maximo(sort):
    count=0

    g.add_nodes_from(sort)
    
    for i in xrange(len(sort)-1):
        a=sort[i+1]
        b=sort[i]
        resta=a-b
        
        if resta==1:
            g.add_edge(b,a)
    
    length=len(g.nodes())
    for i in xrange(length):
        
        node=sort[i]
        nei=g.neighbors(node)
        
        
        if(len(nei)==0):
            #print node
            g.remove_node(node)
            count=count+1
            
    length=len(g.nodes())
    array=g.nodes()

    for i in xrange(length):
        
        node=array[i]
        nei=g.neighbors(node)
        

        
        if(len(nei)==1):
            g.remove_node(node)
            
            count=count+1

    print g.nodes()    
    print count
        



respuesta= maximo (sort);
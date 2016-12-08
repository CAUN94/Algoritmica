# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 14:50:11 2016

@author: Cristobal
"""
import networkx as nx

g=nx.Graph()

value=[1,2,3]

def sort(array):
    global g
    g.add_nodes_from(value)
    
    
    for i in xrange(len(value)):
        
        for j in xrange(i,len(value)):
            if array[i]>array[j]:
                
                
    
    



sort(value);

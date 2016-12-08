# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:32:01 2016

@author: 
"""
import networkx as nx
g = nx.Graph()
vec='RGGGB'

largo = len(vec)
for i in xrange(largo):
    g.add_node(i, char=vec[i])
for i in xrange(largo):
    for j in xrange( i+1,largo):
        
        if vec[i] == 'R' and vec[j] == 'G':
            g.add_edge(i, j, n=((i-j)**2))
        if vec[i] == 'G' and vec[j] == 'B':
            g.add_edge(i, j, n=((i-j)**2))
        if vec[i] == 'B' and vec[j] == 'R':
            g.add_edge(i, j, n=((i-j)**2))


path = nx.shortest_path(g,0,largo-1,'n')



final=0
for a in xrange(len(path)-1):
    final=final+(path[a+1]-path[a])**2
print final
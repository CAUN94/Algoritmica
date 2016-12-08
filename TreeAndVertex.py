# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:37:44 2016

@author: Cristobal
"""
import networkx as nx

 
G=nx.Graph()
vec=[0, 1, 2, 3]
vec=sorted(vec)

length=len(vec)

nodos=[]
for A in xrange (length+1):
    nodos.append(A)
    
G.add_nodes_from(nodos)

pos=None
for A in xrange (length):
    
    if pos !=vec[A]:
        n=1
        
    pos=vec[A]
    has=G.has_edge(nodos[pos],nodos[pos+n])

    if has:
        n=n+1
        G.add_edge(nodos[pos],nodos[pos+n])
        
    else:
        
        G.add_edge(nodos[pos],nodos[pos+n])

    
    


Dict=[]

for A in xrange(length+1): 
    Neighbors=G.neighbors(A) 
    
    Dict.append(len(Neighbors))


MAX= max(Dict)

Eliminar=[]

for A in xrange(length+1): 
    Neighbors=G.neighbors(A) 
    if MAX==len(Neighbors):

        G.remove_node(A)
        break





for A in G.nodes(): 
    Neighbors=G.neighbors(A) 
    print Neighbors















    
    
    
    

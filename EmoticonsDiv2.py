# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:30:33 2016

@author: Cristobal
"""

 
import networkx as nx
g = nx.Graph();
g.add_node(1);



def smile(val,n,i):
    
    
    if(n==1):
        node=n+n;
        #print n,node,"s=2";
        g.add_edge(n, node, s=2); #copy paste    
        smile(val,node,n);
        
        path = nx.shortest_path(g,1,val,'s');
    
        return path
    
    if(val<=n):
        
        return ;
    
    else:
        
        node1=n+i; #paste
        #print n,node1,"s=1";
        g.add_edge(n,node1, s=1);
        smile(val,node1,i);
    
        node2=2*n; #copy paste
        i=n;
        #print n,node2,"s=2";
        g.add_edge(n,node2, s=2)
        smile(val,node2,i);
    
    

    
    
    
smile=smile(6,1,1)
print smile;
sec=0;
length=len(smile);
for i in xrange (0,length-1):
    
    sec=sec + g[smile[i]][smile[i+1]]['s'];


print sec







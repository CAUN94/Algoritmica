# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:02:47 2016

@author: Cristobal
"""

import networkx as nx


g = nx.Graph()

g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(2,5)
g.add_edge(3,2)
g.add_edge(3,6)
g.add_edge(4,1)
g.add_edge(4,5)
g.add_edge(4,7)
g.add_edge(5,2)
g.add_edge(5,4)
g.add_edge(5,6)
g.add_edge(5,8)
g.add_edge(6,3)
g.add_edge(6,5)
g.add_edge(6,9)
g.add_edge(7,4)
g.add_edge(7,8)
g.add_edge(7,0)
g.add_edge(8,5)
g.add_edge(8,7)
g.add_edge(8,9)
g.add_edge(9,6)
g.add_edge(9,8)
g.add_edge(0,7)



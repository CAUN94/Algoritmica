# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:17:52 2016

@author: Cristobal
"""

import csv as c
import networkx as nx


G=nx.Graph()
count=0


def distance(path):
    final=0
    for a in xrange(len(path)-1):
        final=final+G[path[a]][path[a+1]]['n']

    return final
    
def join_array(array1,array2):
    for X in xrange(len(array2)):
        array1.append(array2[X])
    
    return array1
    
    
def choose(A,B):
    PA=nx.shortest_path(G,0,int(A),'n')
    PB=nx.shortest_path(G,0,int(B),'n')
    
    DA= distance(PA)
    DB= distance(PB)

    if DA>DB:
        Path=nx.shortest_path(G,int(B),int(A),'n')
        Resp=join_array(PB,Path[1:])

       
    elif DB>DA:
        Path=nx.shortest_path(G,int(A),int(B),'n')
        Resp=join_array(PA,Path[1:])
    
    return Resp
    
  


with open('/Users/Cristobal/Desktop/letras.csv', 'rb') as csvfile:
    spamreader = c.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:

        
        G.add_node(int(row[0]),name=row[1])

         
with open('/Users/Cristobal/Desktop/distancias.csv', 'rb') as csvfile:
    spamreader = c.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if count!=0:
            
            G.add_edge(int(row[0]),int(row[1]), n=int(row[2]))
 
        count=count+1
path = nx.shortest_path(G,2,3,'n')


print G.nodes(data="True")

print "Elija los 2 pedidos que quiere hacer desde la"+ G.node[0]['name']

#
for X in xrange(1,len(G.nodes())):
    print "Escriba", X ,"para seleccionar la dirección "+ G.node[X]['name']

A=raw_input("Primera elección:")
B=raw_input("Segunda elección:")



if(A==B):
    print "Elija denuevo"
    A=raw_input("Primera elección:")
    B=raw_input("Segunda elección:")


BestWay=choose(A,B)


print "Tu mejor ruta es:"
GF = nx.DiGraph()
GF.add_nodes_from(BestWay)
print BestWay

for i in xrange(len(BestWay)):
    if(i!=(len(BestWay))-1):
        GF.add_edge(BestWay[i],BestWay[i+1])


nx.draw(GF,with_labels=True)
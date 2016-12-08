# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:53:27 2016

@author: Cristobal
"""
import networkx as nx


g=nx.Graph();


#función kmeans busca el mejor centroide para el set de data que se tiene
def kmeans (array,centroid):
    cluster={'c1':[],'c2':[],'c3':[]};
    
        
    #calcula la distancia de manhattan entre todos los valores
    dist=distance(array,centroid);
    
    #busca la distancia más cercana entre 2 puntos
    for key, i in array.items():
        nei=dist.neighbors(key);
        max=100000;
        key_c=0;
        for c in xrange(len(nei)):
            centroide=nei[c]
            weigth=dist[key][centroide]['dist'] ;
            
            if weigth<max:
                max=weigth;
                key_c=centroide;
               
            
                
        #se crea un cluster 
        cluster[key_c].append(key);
      
    
    #cuando al hacer una nueva iteración los centroides no cambian se debe terminar el algoritmo
    new_cent=new_centroid(cluster,array);
    value = compare_list (new_cent,centroid);
    
    if(value==False):
        kmeans(array,new_cent);
    else:
        print cluster;

#compara si los 2 list son iguales 
def compare_list(list1,list2):
    
    value=True;    
    
    for key, i in list1.items():
        
        if  list1[key][0]!=list2[key][0]:
            value=False;

                
        if  list1[key][1]!=list2[key][1]:
        
            value=False;

        
    return value;
    
   

#calcular nuevo centroide    
def new_centroid(cluster,array):
    centroid={'c1':[],'c2':[],'c3':[]};

    for key, i in cluster.items():
        x=0;
        y=0;

        for j in xrange(len(i)):
            key2= i[j];
            

            xy = array[key2];
            x=x+xy[0];
            y=y+xy[1];
            
 
        x= x/float(len(i));
        y= y/float(len(i));
        centroid[key].append(x);
        centroid[key].append(y);
    
    return centroid;
  

#calcular distancias de manhattan
def distance (array,centroid):
    
    for key1, i in centroid.items():
            
        xi=i[0];
        yi=i[1];
        
        for key2, j in array.items():
            xj=j[0];
            yj=j[1];
            x=xi-xj;
            y=yi-yj;    
            if(x<0):
                x=x*(-1);
            if(y<0):
                y=y*(-1);
                 
            d=x+y;
            g.add_edge(key1,key2,dist=d);  

    return g;
    
    


#Coordenadas de 6 bodegas en una ciudad

A=[7,8];
B=[9,9];
C=[7,2];
D=[8,3];
E=[1,2];
F=[2,5];

#almacenar las coordenadas

array={};
array['A']=A
array['B']=B
array['C']=C
array['D']=D
array['E']=E
array['F']=F

#Uasar A,B,F como primer centroide
centroid={};
centroid['c1']=A;
centroid['c2']=B;
centroid['c3']=F;

#invocar a la función
kmeans=kmeans(array,centroid);











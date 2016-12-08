# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:35:18 2016

@author: Cristobal
"""

String = "TodapatrullaescogeaunmuchachocomoGuiaElJefedeTropaesperagrandescosasdelosGuiasylesdejamanoslibresparaquedesarrolleneltrabajodesuspatrullasElGuiadePatrullaadiestrandoydirigiendolasuyaganaalmismotiempoenpracticayexperienciaparaconstituirseenindividuocapazdeaceptarresponsabilidades";


P=[];
L=[];
A=[];
T=[];
E=[];
R=[];
O=[];



length=len(String);
cont=1;
#
#def printear (array):
#    for a in xrange(len(array)):
#        print array[a];
#    
    
    

for a in xrange(length):
    
    if((String[a]!="  ") or (String[a]!=".") or (String[a]!=",")):  
       
        if cont==1:
            P.append(String[a]);
        elif cont==2:
            L.append(String[a]);
        elif cont==3:
            A.append(String[a]);
        elif cont==4:
            T.append(String[a]);
        elif cont==5:
            E.append(String[a]);
        elif cont==6:
            R.append(String[a]);
        elif cont==7:
            O.append(String[a]);
    
    if(cont==7):
        cont=1;
    else:
        cont=cont+1;
        

        
print "A",A;

print "E",E;

print "L",L;

print "O",O;

print "P",P;

print "R",R;

print "T",T;
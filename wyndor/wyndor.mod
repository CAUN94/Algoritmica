option solver gurobi;
set productos;
set plantas;

param tiempo_disponible{plantas};
param ganancia_unitaria{productos};
param tiempo_produccion{plantas, productos};

var produccion {productos} >= 0;

subject to disponibilidad_de_tiempo{planta in plantas}:
    sum{producto in productos} produccion[producto]*tiempo_produccion[planta,producto] 
    <= tiempo_disponible[planta];
    
maximize ganancia_total: 
    sum{producto in productos} ganancia_unitaria[producto]*produccion[producto];    

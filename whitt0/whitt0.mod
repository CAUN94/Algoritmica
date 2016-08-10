option solver gurobi;
set productos = {"madera", "aluminio"};

var produccion {productos} >= 0;

subject to capacidad_doug: produccion["madera"] <= 6;

subject to capacidad_linda: produccion["aluminio"] <= 4;

subject to capacidad_bob: produccion["madera"]*6 + produccion["aluminio"]*8 <= 48;
    
maximize ganancia_total: 180*produccion["madera"] + 90*produccion["aluminio"];

from pyomo.environ import \
    ConcreteModel, Var, Objective, Constraint, maximize, NonNegativeReals
from pyomo.opt import SolverFactory, SolverManagerFactory

modelo = ConcreteModel()
modelo.produccion = Var(["madera", "aluminio"], domain=NonNegativeReals)


def funcion_ganancias(modelo):
    return 180*modelo.produccion["madera"] + 90*modelo.produccion["aluminio"]
modelo.ganancias = Objective(rule=funcion_ganancias, sense=maximize)


def funcion_capacidad_doug(modelo):
    return modelo.produccion["madera"] <= 6
modelo.capacidad_doug = Constraint(rule=funcion_capacidad_doug)


def funcion_capacidad_linda(modelo):
    return modelo.produccion["aluminio"] <= 4
modelo.capacidad_linda = Constraint(rule=funcion_capacidad_linda)


def funcion_capacidad_bob(modelo):
    return (
        modelo.produccion["madera"]*6 +
        modelo.produccion["aluminio"]*8 <= 48
    )
    
modelo.capacidad_bob = Constraint(rule=funcion_capacidad_bob)

opt = SolverFactory("cbc")

solver_manager = SolverManagerFactory('neos')

resultados = solver_manager.solve(modelo, opt=opt)  # resolver en la nube

# resultados = opt.solve(modelo)  # resolver localmente

modelo.display()

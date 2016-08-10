from pyomo.environ import \
    AbstractModel, Var, Set, Param,\
    Objective, Constraint, maximize, NonNegativeReals
from pyomo.opt import SolverFactory, SolverManagerFactory

modelo = AbstractModel()

modelo.productos = Set()
modelo.plantas = Set()

modelo.tiempo_disponible = Param(modelo.plantas)
modelo.ganancia_unitaria = Param(modelo.productos)
modelo.tiempo_produccion = Param(modelo.plantas, modelo.productos)

modelo.produccion = Var(modelo.productos, domain=NonNegativeReals)


def funcion_disponibilidad_tiempo(modelo, planta):
    return (
        sum(
            modelo.tiempo_produccion[planta, producto] *
            modelo.produccion[producto]
            for producto in modelo.productos
        ) <= modelo.tiempo_disponible[planta]
    )
modelo.disponibilidad_tiempo = Constraint(
    modelo.plantas, rule=funcion_disponibilidad_tiempo
)


def funcion_ganancias(modelo):
    return sum(
        modelo.ganancia_unitaria[producto] * modelo.produccion[producto]
        for producto in modelo.productos
    )
modelo.ganancias = Objective(rule=funcion_ganancias, sense=maximize)

instancia = modelo.create_instance("wyndor.dat")

opt = SolverFactory("cbc")

solver_manager = SolverManagerFactory('neos')

resultados = solver_manager.solve(instancia, opt=opt)  # resolver en la nube

# resultados = opt.solve(instancia)  # resolver localmente

instancia.display()

from pyomo.environ import \
    AbstractModel, Var, Set, Param,\
    Objective, Constraint, minimize, NonNegativeReals
from pyomo.opt import SolverFactory, SolverManagerFactory

model = AbstractModel()

model.NUTR = Set()
model.FOOD = Set()

model.cost = Param(model.FOOD)
model.f_min = Param(model.FOOD)
model.f_max = Param(model.FOOD)

model.n_min = Param(model.NUTR)
model.n_max = Param(model.NUTR)

model.amt = Param(model.NUTR, model.FOOD)


def variable_constraints_function(model, i):
    return (model.f_min[i], model.f_max[i])
model.buy = Var(
    model.FOOD, domain=NonNegativeReals, bounds=variable_constraints_function
)


def total_cost_function(model):
    return sum(model.buy[i]*model.cost[i] for i in model.FOOD)
model.total_cost = Objective(rule=total_cost_function, sense=minimize)


def main_constraints_function(model, i):
    return (
        model.n_min[i],
        sum(model.amt[i, j] * model.buy[j] for j in model.FOOD), model.n_max[i]
    )
model.main_constraints = Constraint(model.NUTR, rule=main_constraints_function)

instance = model.create_instance("diet_pyomo_odbc.dat")

opt = SolverFactory("gurobi", solver_io="python")

# # resolver en la nube
# opt = SolverFactory("gurobi")
# solver_manager = SolverManagerFactory('neos')
# results = solver_manager.solve(instance, opt=opt)

# resolver localmente
resultados = opt.solve(instance)

instance.display()

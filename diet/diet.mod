set nutr;
set food;

param cost {food} > 0;
param f_min {food} >= 0;
param f_max {j in food} >= f_min[j];

param n_min {nutr} >= 0;
param n_max {i in nutr} >= n_min[i];

param amt {nutr,food} >= 0;

var buy {j in food} >= f_min[j], <= f_max[j];

minimize total_cost:  sum {j in food} cost[j] * buy[j];

subject to diet {i in nutr}:
   n_min[i] <= sum {j in food} amt[i,j] * buy[j] <= n_max[i];

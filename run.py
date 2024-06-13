from src.run_exp import exp_centralized,  exp_centralized_for
from src.solver import QUBO_solver
import json

#'configs/maxind_random_coarsen.json'

with open('/home/neusha/GNN/HypOp_May_2024/configs/Partitioning_new.json') as f:
   params = json.load(f)
exp_centralized(params)





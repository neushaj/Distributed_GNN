#from src.run_exp import exp, exp_traditional, exp_centralized, exp_gradient, exp_centralized_for, exp_centralized_for_multi
from src.run_exp import exp_centralized, exp_centralized_for, exp_centralized_for_multi
from src.solver import QUBO_solver
import json
import torch
import torch.distributed as dist
import torch.multiprocessing as mp


if __name__ == '__main__':  

   with open('./configs/maxcut_R_for_seq.json') as f:
      params = json.load(f)
   
   if params["multi_gpu"]:
      params["logging_path"] = params["logging_path"].split(".log")[0] +str(params["multi_gpu"]) + "_" + params["data"] + "_test.log"
      mp.spawn(exp_centralized_for_multi, args=(list(range(params["num_gpus"])), params), nprocs=params["num_gpus"])
   else:
      exp_centralized_for(params)

   # if test_mode == "infer":
   #    if dataset == "stanford":
   #       with open('./infer_configs/maxcut_R_for_seq.json') as f:
   #          params = json.load(f)
   #    elif dataset == "arxiv":
   #       with open('./infer_configs/maxcut_arxiv_for.json') as f:
   #          params = json.load(f)
   #    exp_centralized(params)

   

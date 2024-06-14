# distributed_GNN


## Parameters/Configs

#### Mode Parameters

    - data: uf/stanford/hypergraph
    - mode: sat/maxcut
    - K: 10 default
    - Adam: True/False; False default
    - fast: Ture/False; 

#### Model Parameters
    - lr:
    - epoch：

#### Utils Parameters
    - mapping: trival/algo/distribution
    - boosting_mapping: 1.0 default
    - logging_path:  
    - res_path:
    - folder_path:
    - N_realize: only used when mapping = distribution
    - Niter_h: only used when mapping = distribution
    - num_samples: 1 default


#### Sampling Paramters

    - minimum_good_samples: 4 default
    - random_portion: 0.6 default
    - local_portion: 0.2 default
    - cross_portion: 0.2 default

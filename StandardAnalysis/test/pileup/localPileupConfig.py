import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "pu_cfg.py"

# create list of datasets to process
# add datasets as lists instead of the usual dict keys so mergeOutputHadd.py can handle them
#datasets = []
#datasets.extend(composite_dataset_definitions['all_bg_mc'])
#datasets.extend(composite_dataset_definitions['DisplacedSUSYSignal'])

processes = ['stopToLB','stopToLD']
masses = [m for m in range(100, 1801, 100)]
#lifetimes = [10**e for e in range(-2, 5)]
#lifetimes = [0.1]
lifetimes = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1]
datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
datasets = [lt.replace(".", "p") for lt in datasets]

import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "pu_cfg.py"

# create list of datasets to process
# add datasets as lists instead of the usual dict keys so mergeOutputHadd.py can handle them
datasets = ['DYJetsToTauTauLeptonic']
#datasets.extend(composite_dataset_definitions['all_bg_mc'])
#datasets.extend(composite_dataset_definitions['DisplacedSUSYSignal'])

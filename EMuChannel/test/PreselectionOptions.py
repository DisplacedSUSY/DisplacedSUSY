#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
#datasets = default_datasets
#datasets.remove('DisplacedSUSYSignal')
#datasets.append()

# full list of signal jobs we need to run,
# now that lifetime reweighting is in trees
processes = ['stopToLB','stopToLD']
masses = [m for m in range(100, 1801, 100)]
lifetimes = [10**e for e in range(-1, 4)]
datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
datasets = [lt.replace(".", "p") for lt in datasets]

#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    #datasets = ['stopToLB800_500mm_2021', #each sample needs different global tag in protoConfig_cfg.py
                #'stopToLB800_500mm_2023',
                #'stopToLB800_500mm_2024'
    #]
    #colors['stopToLB800_500mm'] = 8

#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets.append('stopToLB1800_1000mm_private') #private version of a centrally-produced sample, for validation of other private samples

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets.append('stopToLB400_1mm_private') #private version of a centrally-produced sample, for validation of other private samples

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    datasets = default_datasets
    datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets = ['MuonEG_2016_2017_2018']

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    datasets = [#'stopToLB800_500mm_2021', #each sample needs different global tag in protoConfig_cfg.py
                #'stopToLB800_500mm_2023',
                'stopToLB800_500mm_2024'
    ]
    #colors['stopToLB800_500mm'] = 8

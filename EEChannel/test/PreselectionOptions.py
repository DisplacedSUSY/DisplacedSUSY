#!/usr/bin/env python
from DisplacedSUSY.EEChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    datasets = default_datasets
    datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets = ['DoubleEG_2016_2017_2018']

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    datasets = [
        #'stopToLB300_1000mm',
        'stopToLB300_1000mm_preVFP',
        #'stopToLB300_1000mm_postVFP'
    ]

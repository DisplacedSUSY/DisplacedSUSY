#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Skim_cfg.py"

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
    datasets.remove('DisplacedSUSYSignal') #NOT ready for stop-->l+b, NOT ready for stop-->l+d

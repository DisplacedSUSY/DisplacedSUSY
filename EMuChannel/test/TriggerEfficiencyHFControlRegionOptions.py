#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiencyHFControlRegion_cfg.py"

# create list of datasets to process
datasets = [
    'QCD_MuEnriched',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets.append('MET_2016_postHIP')
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets.append('MET_2017_withoutB')
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    datasets.append('MET_2018')

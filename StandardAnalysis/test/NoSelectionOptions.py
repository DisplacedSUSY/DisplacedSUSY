#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "NoSelection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #ready for stop-->l+b, m=200 to 1300 GeV; NOT ready for stop-->l+b, m=1400 to 1800 GeV and NOT ready for stop-->l+d, m=200 to 1800 GeV

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    #datasets = default_datasets
    datasets = ['stop1000_1mm',
                'stop1000_100mm',
                'stopToLD1000_1mm',
                'stopToLD1000_100mm',
                ]
    colors['stop1000_1mm'] = 4
    colors['stop1000_100mm'] = 8
    #datasets.append()
    #datasets.remove('DisplacedSUSYSignal') #NOT ready for stop-->l+b, NOT ready for stop-->l+d

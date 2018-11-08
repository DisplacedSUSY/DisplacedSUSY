#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "ChannelOverlapSelection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    #datasets.remove('DisplacedSUSYSignal') #ready for stop-->l+b, m=200 to 1300 GeV; NOT ready for stop-->l+b, m=1400 to 1800 GeV and NOT ready for stop-->l+d, m=200 to 1800 GeV

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    #datasets = default_datasets
    datasets = [#'Background',
                'stop500_1mm',
                'stop500_100mm',
                'stop1000_1mm',
                'stop1000_100mm',
                'stop1500_1mm',
                'stop1500_100mm',
                ]
    colors['stop500_1mm'] = 1
    colors['stop500_100mm'] = 2
    colors['stop1000_1mm'] = 3
    colors['stop1000_100mm'] = 4
    colors['stop1500_1mm'] = 5
    colors['stop1500_100mm'] = 8
    #datasets.append()
    #datasets.remove('DisplacedSUSYSignal') #NOT ready for stop-->l+b, NOT ready for stop-->l+d

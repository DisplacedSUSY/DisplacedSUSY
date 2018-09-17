#!/usr/bin/env python
import os
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #ready for stop-->l+b, m=200 to 1300 GeV; NOT ready for stop-->l+b, m=1400 to 1800 GeV and NOT ready for stop-->l+d, m=200 to 1800 GeV

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    #datasets = ['Background']
    datasets.remove('DisplacedSUSYSignal') #NOT ready for stop-->l+b, NOT ready for stop-->l+d
    #datasets.remove('TTJets_Lept')
    #datasets = [
        #'stopToLD1000_1mm',
        #'stopToLD1000_100mm',

        #'stop1000_1mm',
        #'stop1000_100mm',

        #'stop500_1mm',
        #'stop500_10mm',
        #'stop500_100mm',
        #'stop500_1000mm',

        #'stop400_10mm',
        #'stop500_10mm',
        #'stop600_10mm',
        #'stop700_10mm',
        #'stop800_10mm',
        #'stop900_10mm',
        #'stop1000_10mm',
        #'stop1400_10mm',
        #'stop1700_10mm',
        #]

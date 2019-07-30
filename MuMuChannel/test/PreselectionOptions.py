#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    #datasets = []
    datasets = default_datasets
    #datasets.append()
    #datasets.append('Background')
    datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets = [
    #    'stopToLB400_10mm',
    #    'stopToLB500_10mm',
    #    'stopToLB600_10mm',
    #    'stopToLB700_10mm',
    #    'stopToLB800_10mm',
    #    'stopToLB900_10mm',
    #    'stopToLB1000_10mm',
    #    'stopToLB1400_10mm',
    #    'stopToLB1500_10mm',
    #    'stopToLB1700_10mm',
    #    ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    #datasets = []
    #datasets.append('TTJets_inclusive')
    #datasets.append('Background')
    #datasets = [
        #DisplacedSUSYSignal',
        #'stopToLB500_1mm',
        #'stopToLB500_10mm',
        #'stopToLB500_100mm',
        #'stopToLB500_1000mm',
        #]
    #datasets.append()
    #datasets = [
        #'Background'
        #'stopToLD1000_1mm',
        #'stopToLD1000_100mm',

        #'stopToLB1000_1mm',
        #'stopToLB1000_100mm',
        #]
    datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    datasets = default_datasets
    datasets.remove('DisplacedSUSYSignal') #NOT ready for stop-->l+b, NOT ready for stop-->l+d
    #datasets = ['DoubleMu_2016_2017_2018']

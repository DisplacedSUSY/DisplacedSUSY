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
    #datasets = default_datasets
    #datasets.remove('DisplacedSUSYSignal') #all samples ready
    datasets = [
        #'DYJetsToTauTauLeptonic',
        #'DYJetsToLL',
        'TTJets_Lept',
        #'stopToLB300_1000mm',
        ##'stopToLB200_1mm',
        #'stopToLB200_10mm',
        #'stopToLB200_100mm',
        'stopToLB200_1000mm',
        ##'stopToLB1000_1mm',
        #'stopToLB1000_10mm',
        #'stopToLB1000_100mm',
        'stopToLB1000_1000mm',
        ##'stopToLB1800_1mm',
        #'stopToLB1800_10mm',
        #'stopToLB1800_100mm',
        'stopToLB1800_1000mm',
        #'stopToLD200_1mm',
        #'stopToLD200_10mm',
        #'stopToLD200_100mm',
        #'stopToLD200_1000mm',
        #'stopToLD1000_1mm',
        #'stopToLD1000_10mm',
        #'stopToLD1000_100mm',
        #'stopToLD1000_1000mm',
        #'stopToLD1800_1mm',
        #'stopToLD1800_10mm',
        #'stopToLD1800_100mm',
        #'stopToLD1800_1000mm',
    ]
    #datasets = ['MuonEG_2016_2017_2018']
    #colors['stopToLB1000_1mm'] = 1
    #colors['stopToLB1000_10mm'] = 2
    #colors['stopToLB1000_100mm'] = 4
    #colors['stopToLB1000_1000mm'] = 8

    colors['stopToLB200_1mm'] = 1
    colors['stopToLB1000_1mm'] = 2
    colors['stopToLB1800_1mm'] = 4
    colors['stopToLB200_1000mm'] = 8
    colors['stopToLB1000_1000mm'] = 6
    colors['stopToLB1800_1000mm'] = 7
    #colors['stopToLD200_1mm'] = 8
    #colors['stopToLD1000_1mm'] = 6
    #colors['stopToLD1800_1mm'] = 7


elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    datasets = [#'stopToLB800_500mm_2021', #each sample needs different global tag in protoConfig_cfg.py
                #'stopToLB800_500mm_2023',
                'stopToLB800_500mm_2024'
    ]
    #colors['stopToLB800_500mm'] = 8

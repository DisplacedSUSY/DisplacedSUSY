#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets = default_datasets
    #datasets.append()
    datasets.remove('DisplacedSUSYSignal') #all samples ready

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets = default_datasets
    #datasets.remove('DisplacedSUSYSignal') #all samples ready

#elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_6_"):
    #datasets = default_datasets
    #datasets.remove('DisplacedSUSYSignal') #all samples ready
    #datasets = ['DoubleMu_2016_2017_2018']

    datasets = [#'stopToLB200_1mm',
                #'stopToLB200_10mm',
                #'stopToLB200_100mm',
                #'stopToLB200_1000mm',
        #'stopToLB300_1000mm',
                #'stopToLB1000_1mm',
                #'stopToLB1000_10mm',
                #'stopToLB1000_100mm',
                #'stopToLB1000_1000mm',
                #'stopToLB1800_1mm',
                #'stopToLB1800_10mm',
                #'stopToLB1800_100mm',
                #'stopToLB1800_1000mm',
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

        #'HTo4Mu125_50_50mm',
        #'HTo4Mu125_50_500mm',
        #'HTo4Mu125_50_5000mm',
        #'HTo4Mu125_20_13mm',
        #'HTo4Mu125_20_130mm',
        #'HTo4Mu125_20_1300mm',

        #'stopToLB300_1000mm',
        #'stopToLB300_1000mm_preVFP',
        'stopToLB300_1000mm_postVFP'
                ]
    #colors['stopToLB1000_1mm'] = 1
    #colors['stopToLB1000_10mm'] = 2
    #colors['stopToLB1000_100mm'] = 4
    #colors['stopToLB1000_1000mm'] = 8

    #colors['stopToLB200_1mm'] = 1
    #colors['stopToLB1000_1mm'] = 2
    #colors['stopToLB1800_1mm'] = 4
    #colors['stopToLD200_1mm'] = 8
    #colors['stopToLD1000_1mm'] = 6
    #colors['stopToLD1800_1mm'] = 7

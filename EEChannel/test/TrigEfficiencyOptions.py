import os
from DisplacedSUSY.EEChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TrigEfficiency_cfg.py"

# create list of datasets to process
datasets = [


    #signal
    # 'stopToLB200_1mm',
    # 'stopToLB200_10mm',
    # 'stopToLB200_100mm',
    # 'stopToLB200_1000mm',
    # 'stopToLB800_1mm',
    # 'stopToLB800_10mm',
    # 'stopToLB800_100mm',
    # 'stopToLB800_1000mm',
    # 'stopToLB1200_1mm',
    # 'stopToLB1200_10mm',
    # 'stopToLB1200_100mm',
    # 'stopToLB1200_1000mm',

    #data
    'MET_2016_postHIP',
    # 'MET_2016G',
    # 'MET_2016H',

    #ttbar
    'TTJets_Lept',
]

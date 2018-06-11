import os
from DisplacedSUSY.EEChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TrigEfficiency_cfg.py"

# create list of datasets to process
datasets = [


    #signal
    # 'stop200_1mm',
    # 'stop200_10mm',
    # 'stop200_100mm',
    # 'stop200_1000mm',
    # 'stop800_1mm',
    # 'stop800_10mm',
    # 'stop800_100mm',
    # 'stop800_1000mm',
    # 'stop1200_1mm',
    # 'stop1200_10mm',
    # 'stop1200_100mm',
    # 'stop1200_1000mm',

    #data
    'MET_2016_postHIP',
    # 'MET_2016G',
    # 'MET_2016H',
    
    #ttbar
    'TTJets_Lept',
]




#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    'TTJets_Lept',

    #'MET_2016_postHIP',
    #'MET_2017_withoutB',
    'MET_2018',

    ### Signal MC
    #'DisplacedSUSYSignal',
]

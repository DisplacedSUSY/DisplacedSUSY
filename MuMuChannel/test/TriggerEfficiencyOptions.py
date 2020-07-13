#!/usr/bin/env python
import os
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',

    ### single top
    #'SingleTop',

    ### Diboson
    #'Diboson',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    #'MET_2018',

]

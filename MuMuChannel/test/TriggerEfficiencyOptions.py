#!/usr/bin/env python
import os
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# choose luminosity used for MC normalization
intLumi = 4407 # intersection of 2017D and DCS-only JSON

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',

    ### single top
    #'SingleTop',

    ### Diboson
    #'Diboson',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    'JetHT_2017',
    #'JetHT_2017C',
    #'JetHT_2017D',
    #'MET_2017D',
    #'MuonEG_2017D',
    #'MuonEG_2016',
    #'MuonEG_2016B',
    #'MuonEG_2016C',
    #'MuonEG_2016D',
    #'MuonEG_2016E',
    #'MuonEG_2016F',
    #'MuonEG_2016G',
    #'MuonEG_2016H',
]


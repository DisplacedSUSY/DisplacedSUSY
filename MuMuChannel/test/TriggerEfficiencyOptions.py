#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308 # Wrong. I haven't calculated lumi for 2017D yet

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

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
    'JetHT_2017D',
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


InputCondorArguments = {}

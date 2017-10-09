#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 4407 # intersection of dcs-only json and 2017D
intLumi = -1 # need to calculate for 2016

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    'TTJets_Lept',

    ### single top
    #'SingleTop',

    ### Diboson
    #'Diboson',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    #'JetHT_2017',
    #'JetHT_2017C',
    #'JetHT_2017D',
    'JetHT_2016H',
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

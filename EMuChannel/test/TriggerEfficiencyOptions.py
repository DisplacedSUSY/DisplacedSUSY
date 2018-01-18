#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *
#from OSUT3Analysis.Configuration.miniAODV2_92X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 4407 # intersection of dcs-only json and 2017D
intLumi = 16146 # DCSOnly AND (2016G OR 2016H)

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',
    'TTJets_DiLept',
    'TTJets_SingleLeptFromT',
    'TTJets_SingleLeptFromTbar',

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
    #'JetHT_2016',
    #'JetHT_2016_preHIP',
    'JetHT_2016_postHIP',
    #'JetHT_2016D',
    #'JetHT_2016E',
    #'JetHT_2016G',
    #'JetHT_2016H',
]


InputCondorArguments = {}

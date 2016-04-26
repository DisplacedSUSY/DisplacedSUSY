#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "PromptControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613  #from 13 TeV MuEG dataset 2015D Silver JSON

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"
# create list of datasets to process
datasets = [
    'Diboson',
    'WJetsToLNu',
    'DYJetsToLL_50',
    'SingleTop',
    'TTJets_Lept',
    #'QCD_MuEnriched',
    'MuonEG_2015D',
    #'DisplacedSUSYSignal',
    #'stop200_1mm', 
    #'stop300_1mm', 
    #'stop400_1mm', 
    #'stop500_1mm', 
    #'stop700_1mm', 
]

InputCondorArguments = {'hold': 'true'}

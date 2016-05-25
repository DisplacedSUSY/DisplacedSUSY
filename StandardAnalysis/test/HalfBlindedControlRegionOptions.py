#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "HalfBlindedControlRegion_cfg.py"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# choose luminosity used for MC normalization
intLumi = 2613 # for 13 TeV 2015D Silver Json 

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    #'QCD_MuEnriched',
    #'QCD_EMEnriched',
    #'QCD_bcToE'
    'MuonEG_2015D',
    #'DisplacedSUSYSignal',
]
InputCondorArguments = {'hold': 'true', 'request_memory':'2048MB'}


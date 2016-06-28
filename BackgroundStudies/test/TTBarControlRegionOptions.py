#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *
# specify which config file to pass to cmsRun
config_file = "TTbarControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613# from 13 TeV MuEG 2015D dataset, Silver Json

# create list of datasets to process
datasets = [
    'Diboson',
    'QCD_MuEnriched',
    'WJetsToLNu',
    'SingleTop',
    'TTJets_Lept',
    'DYJetsToLL_50',
    'SingleMu_2015D',
    #'WG',
    #'ZZToLLLL',
    #'WWToLNuLNu',
    #'ZG',
    #'WZToLLLNu',
    #'WZToLNu2QorQQ2L',
    #'ZZToLLQQ',
    #'WZToLNuNuNu',
    #'ZZToNuNuQQ',
]

InputCondorArguments = {'hold':'true','request_memory':'2048MB'}

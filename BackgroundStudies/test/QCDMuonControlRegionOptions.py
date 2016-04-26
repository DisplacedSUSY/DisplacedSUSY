#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

#from OSUT3Analysis.Configuration.configurationOptions_13TeV_miniAODv2 import *
# specify which config file to pass to cmsRun
config_file = "QCDMuonControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 28.67 # for HLT_Mu28NoFiltersNoVtx_CentralCaloJet40_v* path, 2015D 

# create list of datasets to process
datasets = [
    #'Diboson',
    #'DYJetsToLL_50',
    #'WJetsToLNu',
    #'SingleTop',
    #'TTJets_Lept',
    'SingleMu_2015D',
    #'QCD_MuEnriched',
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
InputCondorArguments = {'hold': 'true'}

#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

#from OSUT3Analysis.Configuration.configurationOptions_13TeV_miniAODv2 import *
# specify which config file to pass to cmsRun
config_file = "QCDMuonControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 118.434 # for HLT_Mu20_v* path, 2015D 

# create list of datasets to process
datasets = [
    'SingleMu_2015D',
    'QCD_MuEnriched',
    'WJetsToLNu',
    'SingleTop',
    'TTJets_Lept',
    'DYJetsToLL_50',
    'Diboson',
]
#InputCondorArguments = {'hold': 'true'}

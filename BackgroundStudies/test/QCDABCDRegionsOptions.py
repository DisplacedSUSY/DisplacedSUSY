#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "QCDABCDRegions_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2538.43 # for 13 TeV Silver Json, 2015D 

# create list of datasets to process
datasets = [
    'Diboson_MiniAOD',
    'WJetsToLNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',
#    'QCD_MuEnriched_MiniAOD',
    'QCDFromData',
    'MuonEG_2015D',
]
InputCondorArguments = {'hold': 'true'}

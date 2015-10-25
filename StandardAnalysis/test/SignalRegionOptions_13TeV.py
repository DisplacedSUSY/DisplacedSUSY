#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "SignalRegion_13TeV_cfg.py"

# choose luminosity used for MC normalization
intLumi = 1263.88  # from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    'QCD_MuEnriched_MiniAOD',
    'Diboson_MiniAOD',
    'WJetsToLNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',
    #'TTJets_MiniAOD',
    'MuonEG_2015D',
    'stop200_1mm_MiniAOD',
    'stop200_10mm_MiniAOD',
    'stop200_100mm_MiniAOD',
    'stop200_1000mm_MiniAOD',
    'stop500_1mm_MiniAOD',
    'stop500_10mm_MiniAOD',
    'stop500_100mm_MiniAOD',
    'stop500_1000mm_MiniAOD',
    'stop800_1mm_MiniAOD',
    'stop800_10mm_MiniAOD',
    'stop800_100mm_MiniAOD',
    'stop800_1000mm_MiniAOD', 
]

InputCondorArguments = {}

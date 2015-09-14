#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *

# specify which config file to pass to cmsRun
config_file = "eMuAnalyzer_cfg_miniAOD.py"

# choose luminosity used for MC normalization
intLumi = 31.47 # from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    'MuonEG_2015',
    'WJetsToLNu_MiniAOD',
    'TTJets_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'WW_MiniAOD',
    'ZZ_MiniAOD',
    'WZ_MiniAOD',
    'WJetsToLNu_50ns_MiniAOD',
    'TTJets_50ns_MiniAOD',
    'DYJetsToLL_50_50ns_MiniAOD',
    'WW_50ns_MiniAOD',
    'ZZ_50ns_MiniAOD',
    'WZ_50ns_MiniAOD',
]

InputCondorArguments = {}

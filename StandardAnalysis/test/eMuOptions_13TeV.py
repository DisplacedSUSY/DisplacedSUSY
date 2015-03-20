#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "eMuAnalyzer_cfg_miniAOD.py"

# choose luminosity used for MC normalization
#intLumi = 19700 # from 8 TeV MuEG dataset
intLumi = 1000 # for 13 TeV 

# create list of datasets to process
datasets = [
    'DY',
    'TTbar',
    'Wjets',
]

InputCondorArguments = {}

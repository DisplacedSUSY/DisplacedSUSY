#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py "

# choose luminosity used for MC normalization
intLumi = -1# from 8 TeV MuEG dataset

# create list of datasets to process
datasets = [
    'TTJets_Lept_MiniAOD',
    'MET_2015D'
]

InputCondorArguments = {'hold':'true'}

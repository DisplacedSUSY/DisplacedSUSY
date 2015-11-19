#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

# specify which config file to pass to cmsRun
config_file = "EMuSkimSelection.py"

# choose luminosity used for MC normalization
#intLumi = 19700 # from 8 TeV MuEG dataset
intLumi = 2445.23 # for 13 TeV 

# create list of datasets to process
datasets = [
    'Diboson_MiniAOD',
    'WJetsToLNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',
    'QCD_MuEnriched_MiniAOD',
    'MuonEG_2015D',
    'DisplacedSUSY'
]

InputCondorArguments = {}

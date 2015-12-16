#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

# specify which config file to pass to cmsRun
config_file = "ZTauTauControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2538.43# from 13 TeV MuEG dataset 2015D SilverJson

# create list of datasets to process
datasets = [
    'Diboson',
    'QCD_MuEnriched',
    'WJetsToLNu',
    'SingleTop',
    'TTJets_Lept',
    'DYJetsToLL_50',
    'MuonEG_2015D',
]

InputCondorArguments = {'hold':'true'}

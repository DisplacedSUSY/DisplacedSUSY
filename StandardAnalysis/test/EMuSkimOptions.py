#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

# specify which config file to pass to cmsRun
config_file = "EMuSkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2504 # for 13 TeV Silver Json

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    #'QCD_MuEnriched',
    #'MuonEG_2015D',
    #'DisplacedSUSYSignal'
    #'stop600_1mm',
    'stop700_1mm',
]

InputCondorArguments = {}

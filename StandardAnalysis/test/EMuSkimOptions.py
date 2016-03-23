#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_76X_Samples import *

# specify which config file to pass to cmsRun
config_file = "EMuSkim_cfg.py"

# choose luminosity used for MC normalization
intLumi = 2613 # for 13 TeV Silver Json

# create list of datasets to process
datasets = [
    #'Diboson',
    #'WJetsToLNu',
    #'DYJetsToLL_50',
    #'SingleTop',
    #'TTJets_Lept',
    #'TTJets_SingleLeptFromT',
    #'QCD_MuEnriched',
    #'MuonEG_2015D',
    #'MET_2015D',
    'DisplacedSUSYSignal'
    #'stop600_1mm',
    #'stop700_1mm',
    #'WZToLNu2QorQQ2L',
    #'WG', 
    #'WWToLNuLNu',
    #'ZZToLLNuNu',
    #'WWToLNuQQ',
    #'ZZToLLQQ',
    #'QCD_MuEnriched_170to300',
    #'ZG',
    #'WZToLLLNu',
]

InputCondorArguments = {}

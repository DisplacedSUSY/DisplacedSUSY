#!/usr/bin/env python

# to be run with submitToCondor.py -l protoBatchConfig.py

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "QCDMuonControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36260 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
# create list of datasets to process
datasets = [
    'WJetsToLNu',
    'Diboson',
    'DYJetsToLL',
    'SingleTop',
    'TTJets_Lept',
    'QCD_MuEnriched',
    'SingleMu_2016',
]
InputCondorArguments = {'request_memory':'2048MB'}
secondaryCollections ={'bjets':"objectSelector0"}

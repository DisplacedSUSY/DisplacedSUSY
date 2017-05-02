#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "Skim_cfg.py"

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# choose luminosity used for MC normalization
intLumi = 36814 # final golden json

# create list of datasets to process
datasets = [

    # DY
#    'DYJetsToLL',

    # TTbar
#    'TTJets_Lept',
#   'TTJets_DiLept',



#    'SingleTop',

    # tW
##    'SingleTop_tW',
##    'SingleTop_tbarW',






    # Diboson
#    'Diboson',


#    'WWToLNuLNu',
##    'WZToLNu2QorQQ2L',
##    'ZZToLLNuNu',
##    'ZG',

    # QCD (mu-enriched is bigger)
#    'QCD_MuEnriched',

    # Data
    'MuonEG_2016',
#    'MuonEG_2016H',

#    'DisplacedSUSYSignal'    

]


#print datasets['DisplacedSUSYSignal']
#print composite_dataset_definitions['DisplacedSUSYSignal']

#print 'dataset_names', dataset_names
InputCondorArguments = {}

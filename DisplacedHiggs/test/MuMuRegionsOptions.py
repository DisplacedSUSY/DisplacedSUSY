#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "MuMuRegions_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308 # full 2016 data
#intLumi = 5784.596 # 2016B 
#intLumi = 2573.399 # 2016C 
#intLumi = 4248.384 # 2016D 
#intLumi = 4009.132 # 2016E 
#intLumi = 3101.618 # 2016F 
#intLumi = 7540.488 # 2016G 
#intLumi = 8605.69  # 2016H 

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL',

    ### TTbar

#    'TTJets_Lept',
    # 'TTJets_SingleLeptFromT',
    # 'TTJets_SingleLeptFromTbar',
#    'TTJets_DiLept',

    

    ### Diboson
#    'Diboson',
    # 'WWToLNuLNu',
    # 'WWToLNuQQ',
    # 'WZToLLLNu',
    # 'WZToLNuNuNu',
    # 'ZZToLLLL',
    # 'ZZToLLNuNu',
    # 'ZZToLLQQ',
    # 'ZZToNuNuQQ',

    ### single top
#    'SingleTop',
#    'SingleTop_s_channel',
#    'SingleTop_tW',
#    'SingleTop_tbarW',
#    'SingleTop_t_channel_antitop',
#    'SingleTop_t_channel_top',


    ### QCD (mu-enriched is bigger)
#    'QCD_MuEnriched',

    ### Data
#    'DoubleMu_2016',
]

# datasets = [
#     'DoubleMu_2016',
#     'SingleTop',
#     'Diboson',
#     'TTJets_Lept',
#     'DYJetsToLL'
#]



InputCondorArguments = {}

#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.cmsswVersion import *
if (cmssw_version()[0]>8 and cmssw_version()[1]>-1):
    from DisplacedSUSY.Configuration.miniAODV2_94X_Samples import *
else:
    from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *


# specify which config file to pass to cmsRun
config_file = "PromptControlRegion_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 35863.308
intLumi = 16146.2 # 2016G,H only

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL',

    ### TTbar
    'TTJets_Lept',
    #'TTJets_SingleLeptFromT',
    #'TTJets_SingleLeptFromTbar',
    #'TTJets_DiLept',

    ### single top
    'SingleTop',
    #'SingleTop_s_channel',
    #'SingleTop_tW',
    #'SingleTop_tbarW',
    #'SingleTop_t_channel_antitop',
    #'SingleTop_t_channel_top',

    ### Diboson
    'Diboson',
    #'WWToLNuLNu',
    #'WWToLNuQQ',
    #'WZToLLLNu',
    #'WZToLNuNuNu',
    #'ZZToLLLL',
    #'ZZToLLNuNu',
    #'ZZToLLQQ',
    #'ZZToNuNuQQ',

    ### QCD (mu-enriched is bigger)
    'QCD_MuEnriched',

    ### Data
    #'MuonEG_2016',
    'MuonEG_2016_postHIP',
    #'MuonEG_2016B',
    #'MuonEG_2016C',
    #'MuonEG_2016D',
    #'MuonEG_2016E',
    #'MuonEG_2016F',
    #'MuonEG_2016G',
    #'MuonEG_2016H',
]


InputCondorArguments = {}

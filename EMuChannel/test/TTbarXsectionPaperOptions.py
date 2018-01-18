#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TTbarXsectionPaper_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35900.

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL',
    #'DYJetsToLL_10to50',
    #'DYJetsToLL_50',

    ### TTbar
    #'TTJets_DiLept',
    #'TTJets_SingleLeptFromT',
    #'TTJets_SingleLeptFromTbar',
    'TT_AN2017_022',

    ### single top
    #'SingleTop',
    #'SingleTop_s_channel',
    #'SingleTop_tW',
    #'SingleTop_tbarW',
    #'SingleTop_t_channel_antitop',
    #'SingleTop_t_channel_top',
    'SingleTop_tW_AN2017_022',
    'SingleTop_tbarW_AN2017_022',

    ### Diboson
    #'Diboson',
    #'WWToLNuLNu',
    #'WWToLNuQQ',
    #'WZToLLLNu',
    #'WZToLNuNuNu',
    #'ZZToLLLL',
    #'ZZToLLNuNu',
    #'ZZToLLQQ',
    #'ZZToNuNuQQ',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    'MuonEG_2016_03Feb2017',
    'SingleEle_2016_03Feb2017',
    'SingleMu_2016_03Feb2017',
    'SingleEle_2016B_03Feb2017',
    'SingleEle_2016C_03Feb2017',
    'SingleEle_2016H_03Feb2017',
    'SingleMu_2016B_03Feb2017',
    'SingleMu_2016C_03Feb2017',
    'SingleMu_2016D_03Feb2017',
    'SingleMu_2016E_03Feb2017',
    'SingleMu_2016F_03Feb2017',
    'SingleMu_2016G_03Feb2017',
    'SingleMu_2016H_03Feb2017',
    #'MuonEG_2016',
    #'MuonEG_2016B',
    #'MuonEG_2016C',
    #'MuonEG_2016D',
    #'MuonEG_2016E',
    #'MuonEG_2016F',
    #'MuonEG_2016G',
    #'MuonEG_2016H',
]


InputCondorArguments = {}

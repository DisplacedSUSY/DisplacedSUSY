#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "TTbarXsectionPaper_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',
    # 'TTJets_SingleLeptFromT',
    # 'TTJets_SingleLeptFromTbar',
     #'TTJets_DiLept',

    ### single top
    #'SingleTop',
    # 'SingleTop_s_channel',
    # 'SingleTop_tW',
    # 'SingleTop_tbarW',
    # 'SingleTop_t_channel_antitop',
    # 'SingleTop_t_channel_top',

    ### Diboson
    #'Diboson',
    # 'WWToLNuLNu',
    # 'WWToLNuQQ',
    # 'WZToLLLNu',
    # 'WZToLNuNuNu',
    # 'ZZToLLLL',
    # 'ZZToLLNuNu',
    # 'ZZToLLQQ',
    # 'ZZToNuNuQQ',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    #'MuonEG_2016',
    'MuonEG_2016B',
]


InputCondorArguments = {}

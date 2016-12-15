#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "BackgroundValidation_cfg.py"

# choose luminosity used for MC normalization
intLumi = 36460 # from  final re-reco golden json
#intLumi = 27910 # without 2016H v2
systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets_composite = [

    ### DY
    'DYJetsToLL_50',

    ### TTbar
    'TTJets_Lept',

    ### single top
    'SingleTop',

    ### Diboson
    'Diboson',

    ### QCD (mu-enriched is bigger)
    'QCD_MuEnriched',

    ### Data
    'MuonEG_2016_23Sep',
#     'MuonEG_2016B_23Sep',
#     'MuonEG_2016C_23Sep',
#     'MuonEG_2016D_23Sep',
#     'MuonEG_2016E_23Sep',
#     'MuonEG_2016F_23Sep',
#     'MuonEG_2016G_23Sep',
#     'MuonEG_2016Hv2',
#     'MuonEG_2016Hv3',
]

datasets_split = [

    'DYJetsToLL_50',

    'TTJets_DiLept',
    'TTJets_SingleLeptFromT',
    'TTJets_SingleLeptFromTbar',

    'SingleTop_s_channel',
    'SingleTop_t_channel_top',
    'SingleTop_t_channel_antitop',
    'SingleTop_tW',
    'SingleTop_tbarW',

    'WZToLNu2QorQQ2L',
    'WWToLNuLNu',
    'WZToLNuNuNu',
    'WZToLLLNu',
    'ZZToNuNuQQ',
    'ZZToLLQQ',
    'ZZToLLNuNu',
    'ZZToLLLL',
    'WG',
    'ZG',

    'QCD_MuEnriched_15to20',
    'QCD_MuEnriched_20to30',
    'QCD_MuEnriched_30to50',
    'QCD_MuEnriched_50to80',
    'QCD_MuEnriched_80to120',
    'QCD_MuEnriched_120to170',
    'QCD_MuEnriched_170to300',
    'QCD_MuEnriched_300to470',
    'QCD_MuEnriched_470to600',
    'QCD_MuEnriched_600to800',
    'QCD_MuEnriched_800to1000',
    'QCD_MuEnriched_1000toInf',
    
    'MuonEG_2016_23Sep',
    # 'MuonEG_2016B_23Sep',
    # 'MuonEG_2016C_23Sep',
    # 'MuonEG_2016D_23Sep',
    # 'MuonEG_2016E_23Sep',
    # 'MuonEG_2016F_23Sep',
    # 'MuonEG_2016G_23Sep',
    # 'MuonEG_2016Hv2',
    # 'MuonEG_2016Hv3',

]

datasets = datasets_split

InputCondorArguments = {}

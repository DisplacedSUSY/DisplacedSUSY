#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "PromptControlRegion_cfg.py"

# choose luminosity used for MC normalization
intLumi = 27660 # from 2016BCDEFG Prompt reco golden json

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL_50',

    ### TTbar
    'TTJets_DiLept',

    ### tW
#    'SingleTop_tbarW',

    ### Diboson
#    'WWToLNuLNu',
#    'ZZToLLNuNu',
#    'ZG',

    ### QCD (mu-enriched is bigger)
#    'QCD_MuEnriched',
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

    ### Data
#    'MuonEG_2016_23Sep',
    'MuonEG_2016B_23Sep',
    'MuonEG_2016C_23Sep',
    'MuonEG_2016D_23Sep',
    'MuonEG_2016E_23Sep',
    'MuonEG_2016F_23Sep',
    'MuonEG_2016G_23Sep',

]

InputCondorArguments = {}

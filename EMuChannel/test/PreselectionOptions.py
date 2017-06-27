#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.miniAODV2_80X_Samples import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# choose luminosity used for MC normalization
intLumi = 35863.308 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"


#composite_dataset_definitions['Background'] = ['DYJetsToLL_50','TTJets_Lept','SingleTop','Diboson','QCD_MuEnriched']

# create list of datasets to process
datasets = [

    ### DY
    'DYJetsToLL',

    ### TTbar

    'TTJets_Lept',
    # 'TTJets_SingleLeptFromT',
    # 'TTJets_SingleLeptFromTbar',
    # 'TTJets_DiLept',

    ### single top
    'SingleTop',
    # 'SingleTop_s_channel',
    # 'SingleTop_tW',
    # 'SingleTop_tbarW',
    # 'SingleTop_t_channel_antitop',
    # 'SingleTop_t_channel_top',
    

    ### Diboson
    'Diboson',
    # 'WWToLNuLNu',
    # 'WWToLNuQQ',
    # 'WZToLLLNu',
    # 'WZToLNuNuNu',
    # 'ZZToLLLL',
    # 'ZZToLLNuNu',
    # 'ZZToLLQQ',
    # 'ZZToNuNuQQ',

    ### QCD (mu-enriched is bigger)
#    'QCD_MuEnriched',

    ### Sum of background
#    'Background',

    ### Data
    'MuonEG_2016',  # !!! Don't run over while we're blinded !!!

#    'stop200_1mm',
#    'stop200_10mm',
#    'stop200_100mm',
#    'stop200_1000mm',

    ### Signal MC
#    'DisplacedSUSYSignal',
#    'DisplacedSUSYSignal_Unweighted',
]

#from ROOT import kRed
#colors['DisplacedSUSYSignal'] = kRed +1
#labels['DisplacedSUSYSignal'] = "Signal"
#types['DisplacedSUSYSignal'] = "bgMC"

InputCondorArguments = {}

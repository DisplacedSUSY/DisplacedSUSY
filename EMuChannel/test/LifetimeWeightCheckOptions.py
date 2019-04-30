#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "LifetimeWeightCheck_cfg.py"

composite_dataset_definitions['Background'] = ['DYJetsToLL','TTJets_Lept','SingleTop','Diboson','QCD_MuEnriched']

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',
    #'TTJets_SingleLeptFromT',
    #'TTJets_SingleLeptFromTbar',
    #'TTJets_DiLept',

    ### single top
    #'SingleTop',
    #'SingleTop_s_channel',
    #'SingleTop_tW',
    #'SingleTop_tbarW',
    #'SingleTop_t_channel_antitop',
    #'SingleTop_t_channel_top',

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

    ### Sum of background
    #'Background',

    ### Data
    #'MuonEG_2016',          # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016_postHIP',  # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016G',         # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016H',         # !!! Don't run over while we're blinded !!!

    ### Signal MC
    #'DisplacedSUSYSignal',
]

#from ROOT import kRed
#colors['DisplacedSUSYSignal'] = kRed +1
#labels['DisplacedSUSYSignal'] = "Signal"
#types['DisplacedSUSYSignal'] = "bgMC"

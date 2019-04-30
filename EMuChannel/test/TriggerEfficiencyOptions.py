#!/usr/bin/env python
from DisplacedSUSY.EMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "TriggerEfficiency_cfg.py"

# create list of datasets to process
datasets = [

    ### DY
    #'DYJetsToLL',

    ### TTbar
    #'TTJets_Lept',
    #'TTJets_DiLept',
    #'TTJets_SingleLeptFromT',
    #'TTJets_SingleLeptFromTbar',

    ### single top
    #'SingleTop',

    ### Diboson
    #'Diboson',

    ### QCD (mu-enriched is bigger)
    #'QCD_MuEnriched',

    ### Data
    #'JetHT_2017',
    #'JetHT_2017C',
    #'JetHT_2017D',
    #'JetHT_2016',
    #'JetHT_2016_preHIP',
    #'JetHT_2016_postHIP',
    #'MET_2016_postHIP',
    #'MET_2016G',
    #'MET_2016H',
    #'JetHT_2016D',
    #'JetHT_2016E',
    #'JetHT_2016G',
    #'JetHT_2016H',

    ### Signal MC
    #'DisplacedSUSYSignal',
]

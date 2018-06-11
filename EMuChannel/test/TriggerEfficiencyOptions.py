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
    'stop200_1mm',
    'stop200_10mm',
    'stop200_100mm',
    'stop200_1000mm',
    #'stop300_1mm',
    #'stop300_10mm',
    #'stop300_100mm',
    #'stop300_1000mm',
    #'stop400_1mm',
    #'stop400_10mm',
    #'stop400_100mm',
    #'stop400_1000mm',
    #'stop500_1mm',
    #'stop500_10mm',
    #'stop500_100mm',
    #'stop500_1000mm',
    #'stop600_1mm',
    #'stop600_10mm',
    #'stop600_100mm',
    #'stop600_1000mm',
    #'stop700_1mm',
    #'stop700_10mm',
    #'stop700_100mm',
    #'stop700_1000mm',
    'stop800_1mm',
    'stop800_10mm',
    'stop800_100mm',
    'stop800_1000mm',
    #'stop900_1mm',
    #'stop900_10mm',
    #'stop900_100mm',
    #'stop900_1000mm',
    #'stop1000_1mm',
    #'stop1000_10mm',
    #'stop1000_100mm',
    #'stop1000_1000mm',
    #'stop1100_1mm',
    #'stop1100_10mm',
    #'stop1100_100mm',
    #'stop1100_1000mm',
    'stop1200_1mm',
    'stop1200_10mm',
    'stop1200_100mm',
    'stop1200_1000mm',
]

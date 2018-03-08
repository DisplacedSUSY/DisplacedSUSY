#!/usr/bin/env python

# import the definitions of all the datasets on the T3
from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.cmsswVersion import *
if (cmssw_version()[0]>8 and cmssw_version()[1]>-1): #2017 data
    from DisplacedSUSY.Configuration.miniAODV2_94X_Samples import *
else: #2016 data
    from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *


# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"
#config_file = "Preselection_puScalingFactorUp_cfg.py"
#config_file = "Preselection_puScalingFactorDown_cfg.py"

# choose luminosity used for MC normalization
#intLumi = 35863.308 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
intLumi = 16146.2 # 2016G,H only

systematics_file = "DisplacedSUSY.Configuration.systematicsDefinitions"
external_systematics_directory = "DisplacedSUSY/Configuration/data/"


composite_dataset_definitions['Background'] = ['DYJetsToLL','TTJets_Lept','SingleTop','Diboson','QCD_MuEnriched']

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

    ### Sum of background
    #'Background',

    ### Data
    #'MuonEG_2016',          # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016_postHIP',  # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016G',         # !!! Don't run over while we're blinded !!!
    #'MuonEG_2016H',         # !!! Don't run over while we're blinded !!!

    ### Signal MC
    #'DisplacedSUSYSignal',
    'stop200_1mm',
    'stop200_10mm',
    'stop200_100mm',
    'stop200_1000mm',
    'stop300_1mm',
    'stop300_10mm',
    'stop300_100mm',
    'stop300_1000mm',
    'stop400_1mm',
    'stop400_10mm',
    'stop400_100mm',
    'stop400_1000mm',
    'stop500_1mm',
    'stop500_10mm',
    'stop500_100mm',
    'stop500_1000mm',
    'stop600_1mm',
    'stop600_10mm',
    'stop600_100mm',
    'stop600_1000mm',
    'stop700_1mm',
    'stop700_10mm',
    'stop700_100mm',
    'stop700_1000mm',
    'stop800_1mm',
    'stop800_10mm',
    'stop800_100mm',
    'stop800_1000mm',
    'stop900_1mm',
    'stop900_10mm',
    'stop900_100mm',
    'stop900_1000mm',
    'stop1000_1mm',
    'stop1000_10mm',
    'stop1000_100mm',
    'stop1000_1000mm',
    'stop1100_1mm',
    'stop1100_10mm',
    'stop1100_100mm',
    'stop1100_1000mm',
    'stop1200_1mm',
    'stop1200_10mm',
    'stop1200_100mm',
    'stop1200_1000mm',
]

#from ROOT import kRed
#colors['DisplacedSUSYSignal'] = kRed +1
#labels['DisplacedSUSYSignal'] = "Signal"
#types['DisplacedSUSYSignal'] = "bgMC"

InputCondorArguments = {}

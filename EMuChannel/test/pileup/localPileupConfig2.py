from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *

config_file = "pu_cfg.py"


InputCondorArguments = {}


# choose luminosity used for MC normalization
#intLumi = 35863.308 # from  Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
intLumi = 16146.2 # 2016G,H only

# create list of datasets to process
datasets = [

    'DYJetsToLL_10to50',
    'DYJetsToLL_50',

    'QCD_MuEnriched_1000toInf',
    'QCD_MuEnriched_120to170',
    'QCD_MuEnriched_15to20',
    'QCD_MuEnriched_170to300',
    'QCD_MuEnriched_20to30',
    'QCD_MuEnriched_300to470',
    'QCD_MuEnriched_30to50',
    'QCD_MuEnriched_470to600',
    'QCD_MuEnriched_50to80',
    'QCD_MuEnriched_600to800',
    'QCD_MuEnriched_800to1000',
    'QCD_MuEnriched_80to120',

    'QCD_EMEnriched_20to30',
    'QCD_EMEnriched_30to50',
    'QCD_EMEnriched_50to80',
    'QCD_EMEnriched_80to120',
    'QCD_EMEnriched_120to170',
    'QCD_EMEnriched_170to300',
    'QCD_EMEnriched_300toInf',

    'QCD_bcToE_15to20'
    'QCD_bcToE_20to30'
    'QCD_bcToE_30to80'
    'QCD_bcToE_80to170'
    'QCD_bcToE_170to250'
    'QCD_bcToE_250toInf'

    'SingleTop_s_channel',
    'SingleTop_tW',
    'SingleTop_t_channel_antitop',
    'SingleTop_t_channel_top',
    'SingleTop_tbarW',

    'TTJets_DiLept',
    'TTJets_SingleLeptFromT',
    'TTJets_SingleLeptFromTbar',

    'WG',
    'WWToLNuLNu',
    'WWToLNuQQ',
    'WZToLLLNu',
    'WZToLNu2QorQQ2L',
    'WZToLNuNuNu',

    'ZG',
    'ZZToLLLL',
    'ZZToLLNuNu',
    'ZZToNuNuQQ',


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



#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

composite_dataset_definitions['Background'] = ['DYJetsToLL','TTJets_DiLept','SingleTop','Diboson','QCD_MuEnriched']

# create list of datasets to process
datasets = [

    # DY
    'DYJetsToLL',

    # TTbar
    'TTJets_DiLept',

    # tW
    'SingleTop',

    # Diboson
    'Diboson',

    # QCD
    'QCD_MuEnriched',

    # Signal
    #'DisplacedSUSYSignal',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets.append(
        # Data
        'DoubleMu_2016_postHIP',
        #'DoubleMu_2016G',
        #'DoubleMu_2016H',
        )

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets.append(
        # Data
        'DoubleMu_2017',
        )



from ROOT import kRed
colors['DisplacedSUSYSignal'] = kRed +1
labels['DisplacedSUSYSignal'] = "Signal"
types['DisplacedSUSYSignal'] = "bgMC"



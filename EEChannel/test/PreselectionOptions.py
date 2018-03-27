#!/usr/bin/env python
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

composite_dataset_definitions['Background'] = ['DYJetsToLL','TTJets_DiLept','SingleTop','Diboson','QCD_EMEnriched','QCD_bcToE']

# create list of datasets to process
datasets = [

    # DY
    #'DYJetsToLL',

    # TTbar
    #'TTJets_DiLept',

    # tW
    #'SingleTop',

    # Diboson
    #'Diboson',

    # QCD
    #'QCD_EMEnriched',
    #'QCD_bcToE',
    
    # Signal
    #'DisplacedSUSYSignal',
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    datasets.append(    
        # Data
        'DoubleEG_2016_postHIP',
        #'DoubleEG_2016B',
        #'DoubleEG_2016C',
        #'DoubleEG_2016D',
        #'DoubleEG_2016E',
        #'DoubleEG_2016F',
        #'DoubleEG_2016G',
        #'DoubleEG_2016H',
        )
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    datasets.append(
        # Data 
        'DoubleEG_2017',
        )


from ROOT import kRed
colors['DisplacedSUSYSignal'] = kRed +1
labels['DisplacedSUSYSignal'] = "Signal"
types['DisplacedSUSYSignal'] = "bgMC"



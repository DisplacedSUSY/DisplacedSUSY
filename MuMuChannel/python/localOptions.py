#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# choose luminosity used for MC normalization and set default samples to run over
# lumi and samples vary from channel to channel, so define locally
# units: 1/pb
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):

    intLumi = 16146.2 # 2016G,H only

    default_datasets = [
        'DoubleMu_2016_postHIP',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'DisplacedSUSYSignal',
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):

    intLumi = 36733.6 #Nov17 rereco 2017 golden json AND mu-mu trigger

    default_datasets = [
        'DoubleMu_2017_withoutB',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'DisplacedSUSYSignal',
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):

    intLumi = 59740 #17Sept early rereco 2018 golden json, with approved PHYSICS normtag

    default_datasets = [
        'DoubleMu_2018',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'DisplacedSUSYSignal',
        ]

# Define background MC composite datasets for plotting
composite_dataset_definitions['Background'] = [x for x in default_datasets if not (x.startswith('DoubleMu') or x.startswith('DisplacedSUSYSignal'))]
composite_dataset_definitions['NonQcdBackground'] = [x for x in composite_dataset_definitions['Background'] if not x.startswith('QCD')]

composite_dataset_definitions['Background_noDYTauTau'] = ["DYJetsToLL_noDYTauTau" if x == "DYJetsToLL" else x for x in composite_dataset_definitions['Background']]

# Define combined-across-years data datasets
composite_dataset_definitions['DoubleMu_2017_2018'] = [
    'DoubleMu_2017_withoutB',
    'DoubleMu_2018'
]
composite_dataset_definitions['DoubleMu_2016_2017_2018'] = [
    'DoubleMu_2016_postHIP',
    'DoubleMu_2017_withoutB',
    'DoubleMu_2018'
]

composite_dataset_definitions['DYJetsToLL_2017_2018'] = [
    'DYJetsToLL_2017_withoutB',
    'DYJetsToLL_2018'
]

composite_dataset_definitions['Background_noDYTauTau_2017_2018'] = [
    'Background_noDYTauTau_2017',
    'Background_noDYTauTau_2018'
]

analysisChannel = "mumu"

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}

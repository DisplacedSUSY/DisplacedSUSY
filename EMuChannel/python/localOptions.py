#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# choose luminosity used for MC normalization and set default samples to run over
# lumi and samples vary from channel to channel, so define locally
# units: 1/pb
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):

    intLumi = 16146.2 # 2016G,H only

    default_datasets = [
        'MuonEG_2016_postHIP',
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'QCD_EMEnriched',
        'DisplacedSUSYSignal',
        ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):

    intLumi = 36733.6 #Nov17 rereco 2017 golden json AND e-mu trigger

    default_datasets = [
        'MuonEG_2017_withoutB',
        'DYJetsToLL',
        'TTJets_Lept',
        'TTJets_inclusive',
        'SingleTop',
        'Diboson',
        'QCD_MuEnriched',
        'QCD_EMEnriched',
        'DisplacedSUSYSignal',
        ]

# Define background MC composite dataset for plotting
composite_dataset_definitions['Background'] = [x for x in default_datasets if not (x.startswith('MuonEG') or x.startswith('DisplacedSUSYSignal'))]

print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}

#!/usr/bin/env python
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

datasets = [
    'Diboson',
    'WJetsToLNu',
    'DYJetsToLL_50',
    'SingleTop',
    'TTJets_Lept',
#    'QCD_MuEnriched',
#    'MuonEG_2015D',
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

systematic_name = "muonSF100um"
condor_dir = "APR3_16_LeptonSFSystematics"

central_channel = "CentralValue100um"
minus_channel = "MuDown100um"
plus_channel = "MuUp100um"

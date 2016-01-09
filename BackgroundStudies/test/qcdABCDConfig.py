#!/usr/bin/env python

#from DisplacedSUSY.Configuration.systematicsDefinitions import *

#external_systematics_directory = 'DisplacedSUSY/Configuration/data/'


# for the ABCD method and the signal region
region_names = {
    'A' : 'SSIso',
    'B' : 'OSIso',
    'C' : 'SSAntiIso',
    'D' : 'OSAntiIso',
    'signal' : 'OSIso',
    'signal_antiIso' : 'OSAntiIso'
}

backgrounds = [
    'Diboson_MiniAOD',
    'WJetsToLNu_MiniAOD',
    'DYJetsToLL_50_MiniAOD',
    'SingleTop_MiniAOD',
    'TTJets_Lept_MiniAOD',
]

# the data dataset to be used when constructing the data-driven QCD sample
data_dataset = 'MuonEG_2015D'




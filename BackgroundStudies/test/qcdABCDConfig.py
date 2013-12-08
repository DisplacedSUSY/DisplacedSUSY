#!/usr/bin/env python

from DisplacedSUSY.Configuration.systematicsDefinitions import *

# for the ABCD method and the signal region
region_names = {
    'A' : 'Preselection_100um_SS',
    'B' : 'Preselection_100um',
    'C' : 'Preselection_100um_AntiIso_SS',
    'D' : 'Preselection_100um_AntiIso',
    'signal' : 'Preselection_100um',
    'signal_antiIso' : 'Preselection_100um_AntiIso'
}

# these are the distributinos that will be fit in region A to extract the QCD yield
distributions_to_fit = [
    {'name' : 'electronAbsD0BeamspotM', 
     #'lowerLimit' : 0.02,     #you can define upper or lower limits here.
     #'upperLimit' : 0.05
    },
    {'name' : 'muonAbsD0BeamspotM'     },   
    {'name' : 'electronEta'            },
    {'name' : 'muonEta'                },
    {'name' : 'electronMetMt'          },
    {'name' : 'muonMetMt'              }
]

# other contributions in region A that will be held constant in the fitting
fitting_backgrounds = [
    #'Background'
    'WNjets',
    'Diboson',
    'SingleTop',
    'TTbar',
    'DY',
]

# other contributions in regions C & D that should be subtracted off
impurities = [
    #'Background'
    'WNjets',
    'Diboson',
    'SingleTop',
    'TTbar',
    'DY',
]

# the data dataset to be used when constructing the data-driven QCD sample
data_dataset = 'MuEG_22Jan2013'




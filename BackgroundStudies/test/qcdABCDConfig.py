#!/usr/bin/env python

# for the ABCD method and the signal region
region_names = {
    'A' : 'Preselection_SS',
    'B' : 'Preselection',
    'C' : 'Preselection_AntiIso_SS',
    'D' : 'Preselection_AntiIso',
    'signal' : 'Signal_Selection_200um',
    'signal_antiIso' : 'Signal_Selection_AntiIso_200um'
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
    'Background'
]

# other contributions in regions C & D that should be subtracted off
impurities = [
    'Background'
]

# the data dataset to be used when constructing the data-driven QCD sample
data_dataset = 'MuEG_22Jan2013'




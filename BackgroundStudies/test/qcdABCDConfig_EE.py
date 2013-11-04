#!/usr/bin/env python

# for the ABCD method and the signal region
region_names = {
    'A' : 'Preselection_EE_SS',
    'B' : 'Preselection_EE',
    'C' : 'Preselection_EE_AntiIso_SS',
    'D' : 'Preselection_EE_AntiIso',
    'signal' : 'Signal_Selection_EE_200um',
    'signal_antiIso' : 'Signal_Selection_EE_AntiIso_200um'
}

# these are the distributinos that will be fit in region A to extract the QCD yield
distributions_to_fit = [
    'electronAbsD0BeamspotM',
    'secondaryElectronAbsD0BeamspotM',    
    'electronEta',
    'secondaryElectronEta',
    'electronMetMt',
    'secondaryElectronMetMt'
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
data_dataset = 'DoubleElectron_22Jan2013'




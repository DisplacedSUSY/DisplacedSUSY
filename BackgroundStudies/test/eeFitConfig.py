#!/usr/bin/env python

intLumi = 19330.  # DoubleElectron 22Jan Re-Reco


input_distributions = [
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'electronAbsD0BeamspotL',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'secondaryElectronAbsD0BeamspotL',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'electronEta',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'secondaryElectronEta',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'electronMetMt',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleElectron_22Jan2013',
        'channel' : 'Preselection_EE_SS',
        'name' : 'secondaryElectronMetMt',
        'iterations' : 10,
    },

]

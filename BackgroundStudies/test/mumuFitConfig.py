#!/usr/bin/env python

intLumi = 19423.  # DoubleMu 22Jan Re-Reco


input_distributions = [
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'muonAbsD0BeamspotM',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'secondaryMuonAbsD0BeamspotM',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'muonEta',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'secondaryMuonEta',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'muonMetMt',
        'iterations' : 10,
    },
    {
        'datasets' : ['Background', 'QCDFromData'],   
        'fixed_datasets' : ['Background'],
        'target_dataset' : 'DoubleMu_22Jan2013',
        'channel' : 'Preselection_MuMu_SS',
        'name' : 'secondaryMuonMetMt',
        'iterations' : 10,
    },

]

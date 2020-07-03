#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

blinded = True # sets observed events equal to bg estimate

# full run 2 background estimates are loaded from a json that also defines the signal regions
background = {
    'name' : 'bg_estimate',
    'dir'  : 'EMuPreselection_FullAnalysis_3Dhists_30July2019',
    'file' : 'standard_background_estimate.json',
}

# fixme: populate fields with full run2 unblinded results when we're ready to unblind
data = {
    'name' : '',
    'dir'  : '',
    'file' : '',
    'hist' : '',
}

# fixme: temporary fudge factor to scale 2018 signal yield to Run II signal yield
lumi_factor = 112.8/59.7

# a separate datacard will be produced for each signal point
if arguments.era == "2016":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_12Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]',
    }
elif arguments.era == "2017":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_12Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]',
    }
elif arguments.era == "2018":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_12Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]',
    }

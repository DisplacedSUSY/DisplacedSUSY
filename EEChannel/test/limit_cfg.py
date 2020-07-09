#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

blinded = True # sets observed events equal to bg estimate

# full run 2 background estimates are loaded from a json that also defines the signal regions
background = {
    'name' : 'bg_estimate',
    'dir'  : 'ee_runII_estimates_07July2020',
    'file' : 'runII_standardSR_background_estimate.json',
}

# fixme: populate fields with full run2 unblinded results when we're ready to unblind
data = {
    'name' : '',
    'dir'  : '',
    'file' : '',
    'hist' : '',
    'var_bins' : '',
}

# fixme: temporary fudge factor to scale 2018 signal yield
lumi_factor = 117.6/59.7 # 2018 --> 2016-18
#lumi_factor = (59.7+36.7)/59.7 # 2018 --> 2017-18

# a separate datacard will be produced for each signal point
if arguments.era == "2016":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2017":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2018":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EEAdditionalPreselection_signal_2018Analysis_01July2020',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um',
        'var_bins' : True,
    }

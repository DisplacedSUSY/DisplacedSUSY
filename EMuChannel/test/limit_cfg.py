#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

blinded = True # sets observed events equal to bg estimate

# full run 2 background estimates are loaded from a json that also defines the signal regions
background = {
    'name' : 'bg_estimate',
    'dir'  : 'emu_runII_ptBinned_estimates_15July2020',
    'file' : 'emu_2018_100um_500um_200GeV_3dHist_background_estimate.json',
}

# fixme: populate fields with full run2 unblinded results when we're ready to unblind
data = {
    'name'     : '',
    'dir'      : '',
    'file'     : '',
    'hist'     : '',
    'var_bins' : '',
}

# fixme: temporary fudge factor to scale 2018 signal yield
#lumi_factor = 1 # 2018 --> 2018
#lumi_factor = (59.7+36.7)/59.7 # 2018 --> 2017-18
lumi_factor = 112.8/59.7 # 2018 --> 2016-18

# a separate datacard will be produced for each signal point
if arguments.era == "2016":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_12Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2017":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuPreselection_2018Analysis_Signal_12Aug2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2018":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'EMuAdditionalPreselection_2018Analysis_signal_coarse3DHists_10July2020',
        'file' : '', # will be automatically generated for each signal point
        #'hist' : 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um',
        'hist' : 'AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]',
        'var_bins' : True,
    }

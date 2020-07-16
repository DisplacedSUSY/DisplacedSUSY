#!/usr/bin/env python
from DisplacedSUSY.Configuration.limitOptions import *

blinded = True # sets observed events equal to bg estimate

# full run 2 background estimates are loaded from a json that also defines the signal regions
background = {
    'name' : 'bg_estimate',
    'dir'  : 'mumu_runII_ptBinned_estimates_15July2020',
    'file' : 'mumu_runII_100um_500um_150GeV_3dhist_background_estimate.json',
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
#lumi_factor = 1
#lumi_factor = (59.7+36.7)/59.7 # 2018 --> 2017-18
lumi_factor = 112.8/59.7 # 2018 --> 2016-18

# a separate datacard will be produced for each signal point
if arguments.era == "2016":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'MuMuPreselection_2018Analysis_Signal_16Aug2019',
        #'dir' : 'MuMuPreselection_2018Analysis_SignalHToXX_justXS_15Nov2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2017":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'MuMuPreselection_2018Analysis_Signal_16Aug2019',
        #'dir' : 'MuMuPreselection_2018Analysis_SignalHToXX_justXS_15Nov2019',
        'file' : '', # will be automatically generated for each signal point
        'hist' : 'AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um',
        'var_bins' : True,
    }
elif arguments.era == "2018":
    signal = {
        'name' : '', # will be automatically generated for each signal point
        'dir'  : 'MuMuAdditionalPreselection_2018Analysis_signal_coarse3DHists_9July2020',
        'file' : '', # will be automatically generated for each signal point
        #'hist' : 'AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um',
        'hist' : 'AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um_vs_muonPt[0]',
        'var_bins' : True,
    }

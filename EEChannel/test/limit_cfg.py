#!/usr/bin/env python

blinded = True # sets observed events equal to bg estimate

# first background estimate hist will be used to define signal regions
backgrounds = {
    'name' : 'bg_estimate',
    'dir'  : 'EEPreselection_FullAnalysis_3Dhists_30July2019',
    'file' : '', # insert json file here
}

# fixme: populate fields when we're ready to unblind
data = {
    'name' : '',
    'dir'  : '',
    'file' : '',
    'hist' : '',
}

# fixme: temporary fudge factor to scale 2018 signal yield to Run II signal yield
lumi_factor = 112.8/59.7

processes = ['stopToLB']
masses = [m for m in range(200, 1801, 100)]
lifetimes = [10**e for e in range(-1, 4)]
signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]

# a separate datacard will be produced for each signal point
# fixme: handle multiple signals (to combine years)
signal = {
    'name' : '', # will be automatically generated for each signal point
    'dir'  : 'EEPreselection_2018Analysis_Signal_15Aug2019',
    'file' : '', # will be automatically generated for each signal point
    'hist' : 'PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]',
}

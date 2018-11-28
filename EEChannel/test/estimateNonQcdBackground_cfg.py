#!/usr/bin/env python

plot = "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

samples = [
    'DYJetsToLL',
    'TTJets_inclusive',
    'SingleTop',
    'Diboson',
]

closure_test_bins = [
    (60,200),
    (80,200),
    (100,200),
    (120,200),
    (140,200),
    (160,200),
]

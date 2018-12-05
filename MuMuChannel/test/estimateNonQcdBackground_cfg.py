#!/usr/bin/env python
import os

plot = "PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    samples = [
        'DYJetsToLL',
        'TTJets_Lept',
        'SingleTop',
        'Diboson',
    ]

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
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

#!/usr/bin/env python

samples = [
    'DYJetsToLL',
    'TTJets_Lept',
    'SingleTop',
    'Diboson',
    'QCD_MuEnriched',
]

# specifify which channel will be used for each region of d = c * b / a
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'DisplacedLowPtControlRegion',
    'c' : 'PromptHighPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion',
}

input_hist = "Muon Plots/muonLeadingPt"
fit_function = "[0] + [1]/x" # |d0| resolution as a function of pT
fit_range = (40, 100)

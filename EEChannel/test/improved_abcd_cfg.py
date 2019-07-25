#!/usr/bin/env python
import os

samples = [
    #'DYJetsToLL',
    #'TTJets_Lept',
    #'SingleTop',
    #'Diboson',
    #'QCD_EMEnriched',
    'NonQcdBackground',
    #'Background',
]

# fit assumes composite samples have two components
composite_samples = {
    #'Background' : ['NonQcdBackground', 'QCD_MuEnriched']
}

# specifify which channel will be used for each region of d = c * b / a
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'DisplacedLowPtControlRegion',
    'c' : 'PromptHighPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion', # signal region
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 65 #electron pt cut at 65 GeV in 2016 ee
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 75 #electron pt cut at 75 GeV in 2017 and 2018 ee

input_hist = "PreselectionPlotter/Electron Plots/electronLeadingPt"
fit_ranges = [(x, 100) for x in range(fitMin, 81, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

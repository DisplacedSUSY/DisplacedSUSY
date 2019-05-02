#!/usr/bin/env python
import os

samples = [
    #'DYJetsToLL',
    #'TTJets_Lept',
    #'SingleTop',
    #'Diboson',
    #'QCD_EMEnriched',
    'NonQcdBackground',
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
    'd' : 'DisplacedHighPtControlRegion',
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 65 #electron pt cut at 65 GeV in 2016 ee
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 75 #electron pt cut at 75 GeV in 2017 and 2018 ee

input_hist = "Electron Plots/electronLeadingPt"
bin_edges = [0] + [x for x in range(fitMin, 105, 2)] + [105,125,150,200,250,500]
fit_ranges = [(x, 100) for x in range(fitMin, 81, 2)]
#bin_edges = [0,65,70,75,80,85,90,95,100,150,200,250,500]
#bin_edges = [0,65,70,75,80,85,90,95,100,110,120,130,140,150,200,300,400,500]
#fit_range = (65, 100)
component_model = "[0] + [1]/x" # |d0| resolution as a function of pT
composite_model = "[0] * ([1] + [2]/x) + (1 - [0]) * ([3] + [4]/x)"

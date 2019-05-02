#!/usr/bin/env python
import os

# composite samples must be listed after component samples
samples = [
    #'DYJetsToLL',
    #'TTJets_Lept',
    #'SingleTop',
    #'Diboson',
    #'QCD_MuEnriched',
    'NonQcdBackground',
    #'Background',
]

# fit assumes composite samples have two components
composite_samples = {
    #'Background' : ['NonQcdBackground', 'QCD_MuEnriched']
}

# specifify which channel will be used for each region b=a*f(x), d=c*f(x)
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'DisplacedLowPtControlRegion',
    'c' : 'PromptHighPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion', # signal region
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 40 #muon pt cut at 40 GeV in 2016 mumu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 50 #muon pt cut at 50 GeV in 2017 and 2018 mumu

input_hist = "Muon Plots/muonLeadingPt"
bin_edges = [0] + [x for x in range(fitMin, 100, 2)] + [100,125,150,200,250,500]
fit_ranges = [(x, 100) for x in range(fitMin, 71, 2)]
component_model = "[0] + [1]/x" # |d0| resolution as a function of pT
composite_model = "[0] * ([1] + [2]/x) + (1 - [0]) * ([3] + [4]/x)"

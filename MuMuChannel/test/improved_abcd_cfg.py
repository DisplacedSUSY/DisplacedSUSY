#!/usr/bin/env python

# composite samples must be listed after component samples
samples = [
    'DYJetsToLL',
    'TTJets_Lept',
    'SingleTop',
    'Diboson',
    'QCD_MuEnriched',
    'NonQcdBackground',
    'Background',
]

# fit assumes composite samples have two components
composite_samples = {
    'Background' : ['NonQcdBackground', 'QCD_MuEnriched']
}

# specifify which channel will be used for each region b=a*f(x), d=c*f(x)
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'DisplacedLowPtControlRegion',
    'c' : 'PromptHighPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion', # signal region
}

input_hist = "Muon Plots/muonLeadingPt"
bin_edges = [0,40,50,60,70,80,90,100,150,200,300,400,500]
component_model = "[0] + [1]/x" # |d0| resolution as a function of pT
composite_model = "[0] * ([1] + [2]/x) + (1 - [0]) * ([3] + [4]/x)"
fit_range = (40, 100)

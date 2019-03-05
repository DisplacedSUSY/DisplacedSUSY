#!/usr/bin/env python

samples = [
    'DYJetsToLL',
    'TTJets_Lept',
    'SingleTop',
    'Diboson',
    #'QCD_EMEnriched', # not enough statistics
]

# specifify which channel will be used for each region of d = c * b / a
channels = {
    'a' : 'PromptLowPtControlRegion',
    'b' : 'PromptHighPtControlRegion',
    'c' : 'DisplacedLowPtControlRegion',
    'd' : 'DisplacedHighPtControlRegion',
}

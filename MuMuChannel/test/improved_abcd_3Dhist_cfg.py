#!/usr/bin/env python
import os

# composite samples must be listed after component samples
samples = [
    'DYJetsToLL',
    #'TTJets_Lept',
    #'SingleTop',
    #'Diboson',
    #'QCD_MuEnriched',
    #'NonQcdBackground',
    #'Background',
]

# fit assumes composite samples have two components
composite_samples = {
    #'Background' : ['NonQcdBackground', 'QCD_MuEnriched']
}

d0_0_cut = 50.
d0_1_cut = 50.
pt_cut = 100.

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 40 #muon pt cut at 40 GeV in 2016 mumu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 50 #muon pt cut at 50 GeV in 2017 and 2018 mumu

input_hist = "Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonPt[0]"
fit_ranges = [(x, 100) for x in range(fitMin, 71, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

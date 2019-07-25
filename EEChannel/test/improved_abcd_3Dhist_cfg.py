#!/usr/bin/env python
import os

# composite samples must be listed after component samples
samples = [
    'DoubleEG_2017F',
    #'DYJetsToLL',
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

# the following parameters only take effect when using the -t option
# 1st sideband tried:
#d0_0_cut = 15.
#d0_1_cut = 15.
#pt_cut = 120.
#d0_0_max = 30 # set to 0 to remove upper limit
#d0_1_max = 30 # set to 0 to remove upper limit
#pt_max = 0 # set to 0 to remove upper limit

# 2nd sideband tried:
d0_0_cut = 30.
d0_1_cut = 30.
pt_cut = 120.
d0_0_max = 100 # set to 0 to remove upper limit
d0_1_max = 100 # set to 0 to remove upper limit
pt_max = 300 # set to 0 to remove upper limit

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 65 #electron pt cut at 65 GeV in 2016 ee
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 75 #electron pt cut at 75 GeV in 2017 and 2018 ee

input_hist = "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]"
fit_ranges = [(x, pt_cut) for x in range(fitMin, 91, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

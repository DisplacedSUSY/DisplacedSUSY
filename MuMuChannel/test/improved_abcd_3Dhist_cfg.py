#!/usr/bin/env python
import os

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    # samples must be listed before composite samples
    samples = [
        'DoubleMu_2016_postHIP',
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

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    # samples must be listed before composite samples
    samples = ['DoubleMu_2017_withoutB']

    # fit assumes composite samples have two components
    composite_samples = { }

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    # samples must be listed before composite samples
    #samples = ['DoubleMu_2018']
    samples = ['DoubleMu_2016_2017_2018']

    # fit assumes composite samples have two components
    composite_samples = { }

# the following parameters only take effect when using the -t option
# 1st sideband tried:
d0_0_cut = 15.
d0_1_cut = 15.
pt_cut = 100.
d0_0_max = 30 # set to 0 to remove upper limit
d0_1_max = 30 # set to 0 to remove upper limit
pt_max = 0 # set to 0 to remove upper limit

# 2nd sideband tried:
#d0_0_cut = 30.
#d0_1_cut = 30.
#pt_cut = 100.
#d0_0_max = 100 # set to 0 to remove upper limit
#d0_1_max = 100 # set to 0 to remove upper limit
#pt_max = 300 # set to 0 to remove upper limit

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 40 #muon pt cut at 40 GeV in 2016 mumu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 50 #muon pt cut at 50 GeV in 2017 and 2018 mumu

input_hist = "PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonPt[0]"
fit_ranges = [(x, pt_cut) for x in range(fitMin, 91, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

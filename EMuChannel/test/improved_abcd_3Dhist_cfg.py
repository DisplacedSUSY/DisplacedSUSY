#!/usr/bin/env python
import os

#vsElectronPt = False #use this if you want to plot/compute vs muon pt
vsElectronPt = True #use this if you want to plot/compute vs electron pt

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    # samples must be listed before composite samples
    samples = [
        'MuonEG_2016_postHIP',
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
    samples = ['MuonEG_2017_withoutB']

    # fit assumes composite samples have two components
    composite_samples = { }

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    # samples must be listed before composite samples
    samples = ['MuonEG_2018']

    # fit assumes composite samples have two components
    composite_samples = { }

# the following block of parameters only take effect when using the -t option
# these parameters are the default setup (not particularily motivated)
d0_0_cut = 15.
d0_1_cut = 15.
#pt_cut = 120.
pt_cut = 100.
d0_0_max = 30 # set to 0 to remove upper limit
d0_1_max = 30 # set to 0 to remove upper limit
pt_max = 0 # set to 0 to remove upper limit

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    if vsElectronPt: fitMin = 42 #electron pt cut at 42 GeV in emu
    else: fitMin = 40 #muon pt cut at 40 GeV in 2016 emu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 50 #both electron and muon pt cut at 50 GeV in 2017 and 2018 emu

if vsElectronPt: input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_electronPt[0]"
else: input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]"

fit_ranges = [(x, pt_cut) for x in range(fitMin, 71, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

#!/usr/bin/env python
import os

#vs_electon_pt = False #use this if you want to plot/compute vs muon pt
vs_electon_pt = True #use this if you want to plot/compute vs electron pt

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    template_sample = 'DYJetsToTauTauLeptonic'
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

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    template_sample = 'DYJetsToTauTauLeptonic'
    samples = ['MuonEG_2017_withoutB']

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    template_sample = 'DYJetsToTauTauLeptonic'
    samples = ['DYJetsToLL_50']

# 1st sideband tried:
#d0_0_cuts = [10]
#d0_1_cuts = [10]
#pt_cuts   = [100]
#d0_0_max  = 30 # set to 0 to remove upper limit
#d0_1_max  = 30 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

# 2nd sideband tried:
#d0_0_cuts = [30]
#d0_1_cuts = [30]
#pt_cuts   = [100]
#d0_0_max  = 100 # set to 0 to remove upper limit
#d0_1_max  = 100 # set to 0 to remove upper limit
#pt_max    = 300 # set to 0 to remove upper limit

# 1st background estimate (DON'T UNBLIND UNLESS YOU MEAN TO!!):
d0_0_cuts = [100, 500, 1000]
d0_1_cuts = [100, 500, 1000]
pt_cuts   = [100, 400]
d0_0_max  = 0 # set to 0 to remove upper limit
d0_1_max  = 0 # set to 0 to remove upper limit
pt_max    = 0 # set to 0 to remove upper limit

# prompt muon, displaced electron sideband:
#d0_0_cuts = [10, 10,  10, 10]
#d0_1_cuts = [10, 100, 500, 1000]
#pt_cuts   = [100]
#d0_0_max  = 40 # set to 0 to remove upper limit
#d0_1_max  = 0 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

# prompt electron, displaced muon sideband:
#d0_0_cuts = [10, 100, 500, 1000]
#d0_1_cuts = [10, 10,  10,  10]
#pt_cuts   = [100]
#d0_0_max  = 0 # set to 0 to remove upper limit
#d0_1_max  = 40 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    if vs_electon_pt: fit_min = 42 #electron pt cut at 42 GeV in emu
    else: fit_min = 40 #muon pt cut at 40 GeV in 2016 emu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fit_min = 50 #both electron and muon pt cut at 50 GeV in 2017 and 2018 emu

if vs_electon_pt: input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_electronPt[0]"
else: input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]"

fit_range = (fit_min, pt_cuts[0])
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

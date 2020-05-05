#!/usr/bin/env python
import os

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    template_sample = 'DYJetsToTauTauLeptonic'
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

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    template_sample = 'DYJetsToTauTauLeptonic'
    samples = ['DoubleMu_2017_withoutB']

elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    template_sample = 'DYJetsToTauTauLeptonic'
    samples = [#'DoubleMu_2016_2017_2018',
               'DoubleMu_2018'
    ]

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

# prompt leading, displaced subleading sideband:
#d0_0_cuts = [10, 10,  10,  10]
#d0_1_cuts = [10, 100, 1000, 2000]
#pt_cuts   = [100]
#d0_0_max  = 40 # set to 0 to remove upper limit
#d0_1_max  = 0 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

# prompt subleading, displaced leading sideband:
#d0_0_cuts = [10, 100, 1000, 2000]
#d0_1_cuts = [10, 10,  10,  10]
#pt_cuts   = [100]
#d0_0_max  = 0 # set to 0 to remove upper limit
#d0_1_max  = 40 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit


# both slightly displaced sideband (as in elog 1548):
#d0_0_cuts = [50]
#d0_1_cuts = [50]
#pt_cuts   = [100]
#d0_0_max  = 100 # set to 0 to remove upper limit
#d0_1_max  = 100 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

# displaced leading muon, prompt subleading muon sideband:
#d0_0_cuts = [100]
#d0_1_cuts = [20]
#pt_cuts   = [100]
#d0_0_max  = 500 # set to 0 to remove upper limit
#d0_1_max  = 100 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit

# displaced subleading muon, prompt leading muon sideband:
#d0_0_cuts = [20]
#d0_1_cuts = [100]
#pt_cuts   = [100]
#d0_0_max  = 100 # set to 0 to remove upper limit
#d0_1_max  = 500 # set to 0 to remove upper limit
#pt_max    = 0 # set to 0 to remove upper limit


if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fit_min = 60 #muon pt cut at 40 GeV in 2016 mumu, but set to 60 GeV to avoid z peak
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fit_min = 60 #muon pt cut at 50 GeV in 2017 and 2018 mumu, but set to 60 GeV to avoid z peak

input_hist = "PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonLeadingPt[0]"
#input_hist = "PreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonSubleadingPt[0]"
fit_range = (fit_min, pt_cuts[0])
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

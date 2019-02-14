#!/usr/bin/env python

distributions = [
    # e-e channel
    {
        'name' : "EE2016_meanEleAbsD0_vs_pt_BackgroundMC",
        'file' : "/uscms/home/cardwell/nobackup/condor/EEPreselection_2016Analysis_30January2019/Diboson.root",
        'hist' : "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_1000um_vs_electronPt_500",
        'fit_range' : (65, 500), # optional parameter; comment out to fit full range
    },
]

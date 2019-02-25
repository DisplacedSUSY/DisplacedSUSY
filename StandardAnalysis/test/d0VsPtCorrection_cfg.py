#!/usr/bin/env python

distributions = [
    # e-e 2016 channel
    {
        'name' : "EE2016_meanEleAbsD0_vs_pt_DYJetsToLL",
        'file' : "/uscms/home/cardwell/nobackup/condor/EEPreselection_2016Analysis_30January2019/DYJetsToLL.root",
        'hist' : "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_1000um_vs_electronPt_500",
        'fit_rangeA' : (65, 99), # optional parameter; comment out to fit full range
        'fit_rangeB' : (100, 500), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE2016_meanEleAbsD0_vs_pt_TTJets_Lept",
        'file' : "/uscms/home/cardwell/nobackup/condor/EEPreselection_2016Analysis_30January2019/TTJets_Lept.root",
        'hist' : "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_1000um_vs_electronPt_500",
        'fit_rangeA' : (65, 215), # optional parameter; comment out to fit full range
        'fit_rangeB' : (216, 500), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE2016_meanEleAbsD0_vs_pt_SingleTop",
        'file' : "/uscms/home/cardwell/nobackup/condor/EEPreselection_2016Analysis_30January2019/SingleTop.root",
        'hist' : "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_1000um_vs_electronPt_500",
        'fit_rangeA' : (65, 199), # optional parameter; comment out to fit full range
        'fit_rangeB' : (200, 500), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE2016_meanEleAbsD0_vs_pt_Diboson",
        'file' : "/uscms/home/cardwell/nobackup/condor/EEPreselection_2016Analysis_30January2019/Diboson.root",
        'hist' : "PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_1000um_vs_electronPt_500",
        'fit_rangeA' : (65, 199), # optional parameter; comment out to fit full range
        'fit_rangeB' : (200, 500), # optional parameter; comment out to fit full range
    },
    #not enough points in the distribution for QCD_EMEnriched to work in fit
]

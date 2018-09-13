#!/usr/bin/env python

distributions = [
    # e-e channel
    {
        'name' : "EE_e_BackgroundMC",
        'file' : "~/nobackup/condor/EEPromptControlRegion_2017Analysis_02August2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE_e_Data",
        'file' : "~/nobackup/condor/EEPromptControlRegion_2017Analysis_02August2018/DoubleEG_2017.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # e-mu channel
    {
        'name' : "EMu_e_BackgroundMC",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_2017Analysis_6Aug2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_e_Data",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_2017Analysis_6Aug2018/MuonEG_2017_withoutB.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_mu_BackgroundMC",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_2017Analysis_6Aug2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_mu_Data",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_2017Analysis_6Aug2018/MuonEG_2017_withoutB.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # mu-mu channel
]

#!/usr/bin/env python

distributions = [
    # e-e channel
    {
        'name' : "EE_eD0_BackgroundMC",
        'file' : "~/nobackup/condor/EEPromptControlRegion_testD0Smearing_2017Analysis_13September2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE_eD0_Data",
        'file' : "~/nobackup/condor/EEPromptControlRegion_testD0Smearing_2017Analysis_13September2018/DoubleEG_2017.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # e-mu channel
    {
        'name' : "EMu_eD0_BackgroundMC",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_eD0_Data",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/MuonEG_2017_withoutB.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_muD0_BackgroundMC",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_muD0_Data",
        'file' : "~/nobackup/condor/EMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/MuonEG_2017_withoutB.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # mu-mu channel
    {
        'name' : "MuMu_muD0_BackgroundMC",
        'file' : "~/nobackup/condor/MuMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "MuMu_muD0_Data",
        'file' : "~/nobackup/condor/MuMuPromptControlRegion_testD0Smearing_2017Analysis_13September2018/DoubleMu_2017_withoutB.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
]

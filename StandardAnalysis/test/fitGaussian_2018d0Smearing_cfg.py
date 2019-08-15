#!/usr/bin/env python

distributions = [
    # e-e channel
    {
        'name' : "EE_eD0_BackgroundMC",
        'file' : "/uscms_data/d3/cardwell/condor/EEPromptControlRegion_2018Analysis_13Aug2019/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EE_eD0_Data",
        'file' : "/uscms_data/d3/cardwell/condor/EEPromptControlRegion_2018Analysis_13Aug2019/EGamma_2018.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # e-mu channel
    {
        'name' : "EMu_eD0_BackgroundMC",
        'file' : "/uscms_data/d3/cardwell/condor/EMuPromptControlRegion_2018Analysis_12Aug2019/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_eD0_Data",
        'file' : "/uscms_data/d3/cardwell/condor/EMuPromptControlRegion_2018Analysis_12Aug2019/MuonEG_2018.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_muD0_BackgroundMC",
        'file' : "/uscms_data/d3/cardwell/condor/EMuPromptControlRegion_2018Analysis_12Aug2019/Background.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "EMu_muD0_Data",
        'file' : "/uscms_data/d3/cardwell/condor/EMuPromptControlRegion_2018Analysis_12Aug2019/MuonEG_2018.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    # mu-mu channel
    {
        'name' : "MuMu_muD0_BackgroundMC",
        'file' : "/uscms_data/d3/cardwell/condor/MuMuPromptControlRegion_2018Analysis_12Aug2019/Background.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
    {
        'name' : "MuMu_muD0_Data",
        'file' : "/uscms_data/d3/cardwell/condor/MuMuPromptControlRegion_2018Analysis_12Aug2019/DoubleMu_2018.root",
        'hist' : "PromptControlRegionPlotter/Muon-beamspot Plots/muonUnsmearedD0_50um",
        'fit_range' : (-20, 20), # optional parameter; comment out to fit full range
    },
]

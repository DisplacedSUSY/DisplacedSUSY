#!/usr/bin/env python

distributions = [
    {
        'name' : "Background MC",
        'file' : "~/nobackup/condor/EEPromptControlRegion_2017Analysis_02August2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter. comment out to fit full range
    },
    {
        'name' : "Smeared Background MC",
        'file' : "~/nobackup/condor/EEPromptControlRegion_testD0Smearing_2017Analysis_22August2018/Background.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0Smeared_50um",
        'fit_range' : (-20, 20), # optional parameter. comment out to fit full range
    },
    {
        'name' : "DoubleEG_2017",
        'file' : "~/nobackup/condor/EEPromptControlRegion_testD0Smearing_2017Analysis_22August2018/DoubleEG_2017.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter. comment out to fit full range
    },
]

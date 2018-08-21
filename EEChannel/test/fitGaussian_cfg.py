#!/usr/bin/env python

distributions = [
    {
        'name' : "dy_jets",
        'file' : "~/nobackup/condor/EEPromptControlRegion_2017Analysis_02August2018/DYJetsToLL.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter. comment out to fit full range
    },
    {
        'name' : "data",
        'file' : "~/nobackup/condor/EEPromptControlRegion_2017Analysis_02August2018/DoubleEG_2017.root",
        'hist' : "PromptControlRegionPlotter/Electron-beamspot Plots/electronD0_50um",
        'fit_range' : (-20, 20), # optional parameter. comment out to fit full range
    },
]

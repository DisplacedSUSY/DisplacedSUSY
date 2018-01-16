#!/usr/bin/env python

# output info
channel = "BackgroundEstimate"
emu_dir = "Electron-muon Plots"
fit_dir = "Sideband Fits"
th2_name = "electronAbsD0_vs_muonAbsD0_10cm"
regions = {
    # "name"  : (low, high, num_bins) note: bin edges must line up with edges in input hist
    "prompt"  : (0.00,   0.02,  1),
    "signal1" : (0.02,   0.05,  1),
    "signal2" : (0.05,   0.10,  1),
    "signal3" : (0.10,  10.00,  1),
}

# input info
sidebands = [
    {
        "name" : "electron",
        "prompt" : {
            "file" : "/data/users/bcardwell/condor/EE_ZCR_17_11_02/DoubleEG_2016_postHIP.root",
            "hist" : "ZControlRegionPlotter/Electron Plots/electronAbsD0_10cm",
            "name" : "Prompt Electron Background",
        },
        "displaced" : {
            "file" : "/data/users/bcardwell/condor/QCDElectronCR_El27_17_12_12/SingleEle_2016_postHIP.root",
            "hist" : "QCDElectronControlRegionPlotter/Electron Plots/electronAbsD0_10cm",
            "name" : "Displaced Electron Background",
        },
        "sideband" : {
            "file" : "/data/users/bcardwell/condor/EMu_Sidebands_18_01_15/MuonEG_2016_postHIP.root",
            "hist" : "PreselectionPromptMuonPlotter/Electron Plots/electronLeadingAbsD0_10cm",
            "name" : "Electron Sideband",
        },
    },
    {
        "name" : "muon",
        "prompt" : {
            "file" : "/data/users/bcardwell/condor/MuMu_ZCR_17_11_02/DoubleMu_2016_postHIP.root",
            "hist" : "ZControlRegionPlotter/Muon Plots/muonAbsD0_10cm",
            "name" : "Prompt Muon Background",
        },
        "displaced" : {
            "file" : "/data/users/bcardwell/condor/QCDMuonCR_17_11_02/SingleMu_2016_postHIP.root",
            "hist" : "QCDMuonControlRegionPlotter/Muon Plots/muonAbsD0_10cm",
            "name" : "Displaced Muon Background",
        },
        "sideband" : {
            "file" : "/data/users/bcardwell/condor/EMu_Sidebands_18_01_15/MuonEG_2016_postHIP.root",
            "hist" : "PreselectionPromptElectronPlotter/Muon Plots/muonLeadingAbsD0_10cm",
            "name" : "Muon Sideband",
        },
    },
]

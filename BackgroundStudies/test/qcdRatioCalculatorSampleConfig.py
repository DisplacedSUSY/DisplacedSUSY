#!/usr/bin/env python

# to be used with 'calculateQCDfakerate.py' script

# it will calculate and print the lepton isolation fake-rates for QCD for 3 cases:
# 1: MC in the analysis region
# 2: MC in the control region
# 3: data in the control region

# it will do this for both electrons and muons, and multiply the two to get an event fake-rate

#finally, it will calculate directly the event fake-rate using the 2D isolation histogram for the MC in the analysis region


# 1: MC in the analysis region
analysis_condor_dir = "AUG28__QCD_PRESELECTIONS"
analysis_channel = "Preselection_NoIso"
analysis_dataset = "QCD_MuEnriched"

# 2 & 3: MC & data in the control region
control_electron_condor_dir = "FULL_ANALYSIS_AUG14__QCD_ELECTRON_CONTROL_REGION"
control_electron_channel = "QCD_Electron_ControlRegion"
control_MC_electron_dataset = "QCD_ElectronEnriched"
control_data_electron_dataset = "DoubleElectron_22Jan2013"
#-----------------------------
control_muon_condor_dir = "FULL_ANALYSIS_AUG14__QCD_MUON_CONTROL_REGION"
control_muon_channel = "QCD_Muon_ControlRegion"
control_MC_muon_dataset = "QCD_MuEnriched"
control_data_muon_dataset = "DoubleMu_22Jan2013"

# histogram names for the isolation variables
electron_iso_histogram = "electronPFrhoIso"
muon_iso_histogram = "muonPFdBetaIso"
electron_muon_iso_histogram = "electronPFrhoIsoVsMuonPFdBetaIso"

# value below which a lepton is considered isolated
electron_iso_threshold = 0.1
muon_iso_threshold = 0.12

# values for anti-isolated box
electron_iso_minimum = 0.2
electron_iso_maximum = 1
muon_iso_minimum = 0.24
muon_iso_maximum = 1.5



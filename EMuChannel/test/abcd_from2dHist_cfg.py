#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/alimena/condor/EMuPreselection_2016Analysis_27July2018/Background.root"
#input_file = "/uscms_data/d3/cardwell/condor/EMuPreselectionMuFromWorZandMuFromTau_2018Analysis_30Mar2020/TTJets_DiLept.root"

#input_file = "/uscms_data/d3/alimena/condor/EMuPreselection_2016Analysis_27July2018/MuonEG_2016_postHIP.root" #DATA! HANDLE WITH CARE!
#input_file = "/uscms_data/d3/alimena/condor/EMuPreselection_2017Analysis_28July2018/MuonEG_2017_withoutB.root" #DATA! HANDLE WITH CARE!
input_file = "/uscms_data/d3/cardwell/condor/EMuPreselection_2018Analysis_30Mar2020/MuonEG_2018.root" #DATA! HANDLE WITH CARE!

input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/electronAbsD0_vs_muonAbsD0_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

# output info
output_file  = "data_displacedMu_test.root"
x_axis_title = "Leading muon |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# prompt-e/displaced-mu sideband
bins_x = [0, 100, 200, 400, 2000]
bins_y = [0, 10, 20, 40, 60, 80]

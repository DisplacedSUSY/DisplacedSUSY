#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/uscms_data/d3/cardwell/condor/EMuAdditionalPreselection_2018Analysis_03June2020/MuonEG_2018.root"

input_hist = "AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um"

# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

# output info
output_file  = "BackgroundABCDClosureTestData_startAt20mum_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTestData_startAt20mum_DisplacedMuRegion.root"
#output_file  = "BackgroundABCDClosureTestData_startAt20mum_DisplacedEleRegion.root"
x_axis_title = "Leading muon |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# prompt-sub mu/prompt-lead mu region
bins_x = [20, 40, 100]
bins_y = [20, 40, 100]

# prompt-leading-ele/displaced-leading-mu region
#bins_x = [20, 100,  100000]
#bins_y = [20, 40, 100]

# displaced-leading-ele/prompt-leading-mu region
#bins_x = [20, 40,   100]
#bins_y = [20, 100,  100000]

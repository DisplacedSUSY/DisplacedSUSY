#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/uscms_data/d3/cardwell/condor/emu_runII_ptBinned_estimates_15July2020/MuonEG_2016_2017_2018.root"

#input_hist = "AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um"
#input_hist = "AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_electronPt[0]"
input_hist = "AdditionalPreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]"

# Is the sample data? If so, the script will use poisson uncertainty instead of normal approximation
data = True
# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True
# systematic uncertainty on estimate (e.g. 0.5 = 50% uncertainty"
systematic_uncertainty = 0.30
# do pol0 (False) or pol1 (True) fit for extrapolation?
pol1 = False

# output info
output_file  = "BackgroundABCDClosureTestData_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedMuRegion.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedEleRegion.root"
x_axis_title = "Leading muon |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# set last bin to -1 on any axis to include overflow along that axis
# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# actual signal regions (don't unblind!)
#bins_x = [20, 100, 500, 100000]
#bins_y = [20, 100, 500, 100000]
#bins_z = [0, 200, -1]

# prompt-sub mu/prompt-lead mu region
bins_x = [20, 40, 100]
bins_y = [20, 40, 100]
bins_z = [0, -1]

# prompt-leading-ele/displaced-leading-mu region
#bins_x = [20, 100,  100000]
#bins_y = [20, 30, 40, 50, 60, 70, 100]
#bins_z = [0, -1]

# displaced-leading-ele/prompt-leading-mu region
#bins_x = [20, 30, 40, 50, 60, 70, 100]
#bins_y = [20, 100,  100000]
#bins_z = [0, -1]

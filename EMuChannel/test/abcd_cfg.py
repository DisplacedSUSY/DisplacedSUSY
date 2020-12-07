#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
input_file = "/uscms_data/d3/cardwell/condor/emu_closureTests_02Dec2020/Background_2016.root"
#input_file = "/uscms_data/d3/cardwell/condor/emu_closureTests_02Dec2020/Background_2017_2018.root"

#input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um"
#input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_electronPt[0]"
input_hist = "PreselectionPlotter/Electron-muon-beamspot Plots/muonAbsD0[0]_vs_electronAbsD0[0]_100000um_vs_muonPt[0]"

# Is the sample data? If so, the script will use poisson uncertainty instead of normal approximation
data = False
# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True
# do pol0 (False) or pol1 (True) fit for extrapolation?
pol1 = False

# uncertainty info
# mutliplicative correction to the estimate in the most-prompt signal region to account for correlation
# correlation factor is only applied if not None
correlation_factor = None # needed for closure tests
#correlation_factor = 1.82 # 2016 bg MC
#correlation_factor = 3.10 # 2017+18 bg MC

# uncertainty on correlation factor (actual value, e.g. 2 implies +-2, not +-200%)
correlation_factor_uncertainty = None # needed for closure tests
#correlation_factor_uncertainty = 0.46 # 2016 bg MC
#correlation_factor_uncertainty = 1.10 # 2017+18 bg MC

# output info
output_file  = "BackgroundABCDClosureTestData_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedMuRegion.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedEleRegion.root"

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

# displaced-leading-ele/prompt-leading-mu region
#bins_x = [20, 100,  100000]
#bins_y = [20, 30, 40, 50, 60, 70, 80, 100]
#bins_z = [0, -1]

# prompt-leading-ele/displaced-leading-mu region
#bins_x = [20, 30, 40, 50, 60, 70, 80, 100]
#bins_y = [20, 100,  100000]
#bins_z = [0, -1]

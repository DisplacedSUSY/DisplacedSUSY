#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2016Analysis_24July2018/Background.root"
#input_file = "/uscms_data/d3/cardwell/condor/EEPreselection_2017Analysis_26July2018/Background.root"
input_file = "/uscms_data/d3/cardwell/condor/ee_runII_ptBinned_estimates_15July2020/DoubleEG_2016_2017_2018.root"
#input_file = "/uscms_data/d3/alimena/condor/EEAdditionalPreselection_2018Analysis_2June2020/DYJetsToLL.root"
#input_file = "/uscms_data/d3/alimena/condor/EEAdditionalPreselection_2018Analysis_2June2020/Background.root"

#input_hist = "AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um"
input_hist = "AdditionalPreselectionPlotter/Electron-beamspot Plots/electronAbsD0[0]_vs_electronAbsD0[1]_100000um_vs_electronPt[0]"

# Is the sample data? If so, the script will use poisson uncertainty instead of normal approximation
data = True
# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True
# systematic uncertainty on estimate (e.g. 0.5 = 50% uncertainty"
systematic_uncertainty = 0.30
# do pol0 (False) or pol1 (True) fit for extrapolation?
pol1 = False

# output info
#output_file  = "BackgroundABCDEstimate_Data.root"
output_file  = "BackgroundABCDClosureTest_Data_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTest_Data_DisplacedSubleadingEleRegion.root"
#output_file  = "BackgroundABCDClosureTest_Data_DisplacedLeadingEleRegion.root"
x_axis_title = "Subleading electron |d_{0}| [#mum]"
y_axis_title = "Leading electron |d_{0}| [#mum]"

# set last bin to -1 on any axis to include overflow along that axis
# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# actual signal regions (don't unblind!)
#bins_x = [0, 100, 500, 1000, 100000]
#bins_y = [0, 100, 500, 1000, 100000]
#bins_z = [0, 300, -1]

# prompt-e/prompt-e region
bins_x = [20, 50, 100]
bins_y = [20, 50, 100]
bins_z = [0, -1]

# prompt-leading-e/displaced-subleading-e region
#bins_x = [20,  100,  100000]
#bins_y = [20,  30, 40, 50, 60, 70,   100]
#bins_z = [0, -1]

# displaced-leading-e/prompt-subleading-e region
#bins_x = [20,  30, 40, 50, 60, 70,   100]
#bins_y = [20, 100,  100000]
#bins_z = [0, -1]

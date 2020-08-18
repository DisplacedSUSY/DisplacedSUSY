#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/manunezo/condor/MuMuPreselection_2016Analysis_25July2018/Background.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuPreselection_2017Analysis_27July2018/Background.root"
input_file = "/uscms_data/d3/cardwell/condor/mumu_runII_ptBinned_estimates_15July2020/DoubleMu_2016_2017_2018.root"
#input_file = "/uscms_data/d3/cardwell/condor/MuMuAdditionalPreselection_2018Analysis_09July2020/DoubleMu_2018.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuAdditionalPreselection_2018Analysis_03June2020/DYJetsToLL.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuAdditionalPreselection_2018Analysis_03June2020/Background.root"
#input_file = "/uscms_data/d3/alimena/condor/MuMuAdditionalPreselection_2018Analysis_MoreHists_22June2020/DYJetsToLL.root"

#input_hist = "AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um"
input_hist = "AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um_vs_muonPt[0]"

# Is the sample data? If so, the script will use poisson uncertainty instead of normal approximation
data = True
# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True
# systematic uncertainty on estimate (e.g. 0.5 = 50% uncertainty"
systematic_uncertainty = 1.00
# do pol0 (False) or pol1 (True) fit for extrapolation?
pol1 = True

# output info
#output_file  = "BackgroundABCDEstimate.root"
output_file  = "BackgroundABCDClosureTestData_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedSubleadingMuRegion_100To500um.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedSubleadingMuRegion_500umTo10cm.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedLeadingMuRegion_100To500um.root"
#output_file  = "BackgroundABCDClosureTestData_DisplacedLeadingMuRegion_500umTo10cm.root"
x_axis_title = "Subleading muon |d_{0}| [#mum]"
y_axis_title = "Leading muon |d_{0}| [#mum]"

# set last bin to -1 on any axis to include overflow along that axis
# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data

# actual signal regions (don't unblind!)
#bins_x = [20, 100, 500, 100000]
#bins_y = [20, 100, 500, 100000]
#bins_z = [0, 150, -1]

# prompt-sub mu/prompt-lead mu region
bins_x = [20, 50, 100]
bins_y = [20, 50, 100]
bins_z = [0, -1]

# prompt-leading-mu/displaced-subleading-mu region, 100 um to 500 um
#bins_x = [20,  100,  500]
#bins_y = [20, 30, 40, 50, 60, 70, 100]
#bins_z = [0, -1]

# prompt-leading-mu/displaced-subleading-mu region, 500 um to 10 cm
#bins_x = [20,  500,  100000]
#bins_y = [20, 30, 100]
#bins_z = [0, -1]

# displaced-leading-mu/prompt-subleading-mu region, 100 um to 500 um
#bins_x = [20, 30, 40, 50, 60, 70,  100]
#bins_y = [20, 100,  500]
#bins_z = [0, -1]

# displaced-leading-mu/prompt-subleading-mu region, 500 um to 10 cm
#bins_x = [20, 30, 100]
#bins_y = [20, 500,  100000]
#bins_z = [0, -1]

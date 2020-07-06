#!/usr/bin/env python

# input info - be careful if running over preselection data while still blinded
#input_file = "/uscms_data/d3/manunezo/condor/MuMuPreselection_2016Analysis_25July2018/Background.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuPreselection_2017Analysis_27July2018/Background.root"
input_file = "/uscms_data/d3/manunezo/condor/MuMuAdditionalPreselection_2018Analysis_03June2020/DoubleMu_2018.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuAdditionalPreselection_2018Analysis_03June2020/DYJetsToLL.root"
#input_file = "/uscms_data/d3/manunezo/condor/MuMuAdditionalPreselection_2018Analysis_03June2020/Background.root"
#input_file = "/uscms_data/d3/alimena/condor/MuMuAdditionalPreselection_2018Analysis_MoreHists_22June2020/DYJetsToLL.root"
input_hist = "AdditionalPreselectionPlotter/Muon-beamspot Plots/muonAbsD0[0]_vs_muonAbsD0[1]_100000um"

# Is the sample data? If so, the script will use poisson uncertainty instead of normal approximation
data = True
# Was the histogram constructed with the variable bin constructor? i.e. TH2(name,title,nbinsx,xbins,nbinsy,ybins)
variable_bins = True

# output info
#output_file  = "BackgroundABCDEstimate.root"
output_file  = "BackgroundABCDClosureTestData_startAt20mum_PromptRegion.root"
#output_file  = "BackgroundABCDClosureTestData_startAt20mum_DisplacedSubleadingMuRegion.root"
#output_file  = "BackgroundABCDClosureTestData_startAt20mum_DisplacedLeadingMuRegion.root"
x_axis_title = "Subleading muon |d_{0}| [#mum]"
y_axis_title = "Leading muon |d_{0}| [#mum]"

# bin edges must line up with bin edges in input histograms
# be careful not to accidently unblind if running over preselection data
#bins_x = [50, 60, 100, 760, 1860, 100000] #Bartsch and Quast |d0| optimization, starting at 50 microns
#bins_y = [50, 60, 100, 760, 1860, 100000]

# prompt-sub mu/prompt-lead mu region
bins_x = [20, 50, 100]
bins_y = [20, 50, 100]

# prompt-leading-mu/displaced-subleading-mu region
#bins_x = [20,  100,  100000]
#bins_y = [20,  40,  100]

# displaced-leading-mu/prompt-subleading-mu region
#bins_x = [20, 40,   100]
#bins_y = [20, 100,  100000]

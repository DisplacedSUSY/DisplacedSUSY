import os

# composite samples must be listed after component samples
samples = [
    'ParkingBPH4_Run2018A',
]

composite_samples = {
}

# specifify which channel will be used for each region b=a*f(x), d=c*f(x)
channels = {
    'a' : 'promptLowPtJPsi',
    'b' : 'displacedLowPtJPsi',
    'c' : 'promptHighPtJPsi',
    'd' : 'displacedHighPtJPsi', # signal region
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    fitMin = 40 #muon pt cut at 40 GeV in 2016 mumu
elif (os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_")):
    fitMin = 9 #muon pt cut at 9 GeV from trigger

input_hist = "PreselectionPlotter/Muon Plots/muonLeadingPt"
fit_ranges = [(x, 15) for x in range(fitMin, 17, 2)]
error_tolerance = 0.1 # maximum error/bin content ratio for b/a plot

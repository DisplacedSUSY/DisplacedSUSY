import os
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.genSim_102X_Samples import *

# specify which config file to pass to cmsRun
config_file = "stopRHadronSimAnalyzer_cfg.py"

#units = 1/pb
intLumi = 59740

# create list of datasets to process
datasets = [
    "stopToLB1000_0p1mm",
    "stopToLB1000_1mm",
    "stopToLB1000_10mm",
    "stopToLB1000_100mm",
    "stopToLB1000_1000mm",
    "stopToLB1000_10000mm",
]

colors["stopToLB1000_0p1mm"] = 1
colors["stopToLB1000_1mm"] = 2
colors["stopToLB1000_10mm"] = 4
colors["stopToLB1000_100mm"] = 6
colors["stopToLB1000_1000mm"] = 7
colors["stopToLB1000_10000mm"] = 8


labels["stopToLB1000_0p1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=0.1 mm, with cloud model"
labels["stopToLB1000_1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1 mm, with cloud model"
labels["stopToLB1000_10mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10 mm, with cloud model"
labels["stopToLB1000_100mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=100 mm, with cloud model"
labels["stopToLB1000_1000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1000 mm, with cloud model"
labels["stopToLB1000_10000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10000 mm, with cloud model"

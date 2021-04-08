import os
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.genSim_102X_Samples import *

# specify which config file to pass to cmsRun
config_file = "stopRHadronSimAnalyzer_cfg.py"

#units = 1/pb
intLumi = 59740

# create list of datasets to process
datasets = [
    "stopToLB1000_0p1mm_withCloudModel",
    "stopToLB1000_1mm_withCloudModel",
    "stopToLB1000_10mm_withCloudModel",
    "stopToLB1000_100mm_withCloudModel",
    "stopToLB1000_1000mm_withCloudModel",
    "stopToLB1000_10000mm_withCloudModel",
]

colors["stopToLB1000_0p1mm_withCloudModel"] = 1
colors["stopToLB1000_1mm_withCloudModel"] = 2
colors["stopToLB1000_10mm_withCloudModel"] = 4
colors["stopToLB1000_100mm_withCloudModel"] = 6
colors["stopToLB1000_1000mm_withCloudModel"] = 7
colors["stopToLB1000_10000mm_withCloudModel"] = 8


labels["stopToLB1000_0p1mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=0.1 mm, with cloud model"
labels["stopToLB1000_1mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1 mm, with cloud model"
labels["stopToLB1000_10mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10 mm, with cloud model"
labels["stopToLB1000_100mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=100 mm, with cloud model"
labels["stopToLB1000_1000mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1000 mm, with cloud model"
labels["stopToLB1000_10000mm_withCloudModel"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10000 mm, with cloud model"

import os
from OSUT3Analysis.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_102X_Samples import *

# specify which config file to pass to cmsRun
config_file = "stopRHadronGenAnalyzer_cfg.py"

#units = 1/pb
intLumi = 59740

# create list of datasets to process
datasets = [
    #"stopToLB200_0p1mm",
    #"stopToLB200_1mm",
    #"stopToLB200_10mm",
    #"stopToLB200_100mm",
    #"stopToLB200_1000mm",
    #"stopToLB200_10000mm",

    "stopToLB1000_0p1mm",
    "stopToLB1000_1mm",
    "stopToLB1000_10mm",
    "stopToLB1000_100mm",
    "stopToLB1000_1000mm",
    "stopToLB1000_10000mm",

    #"stopToLB1800_0p1mm",
    #"stopToLB1800_1mm",
    #"stopToLB1800_10mm",
    #"stopToLB1800_100mm",
    #"stopToLB1800_1000mm",
    #"stopToLB1800_10000mm",
]

colors["stopToLB200_0p1mm"] = 1
colors["stopToLB200_1mm"] = 2
colors["stopToLB200_10mm"] = 4
colors["stopToLB200_100mm"] = 6
colors["stopToLB200_1000mm"] = 7
colors["stopToLB200_10000mm"] = 8

colors["stopToLB1000_0p1mm"] = 1
colors["stopToLB1000_1mm"] = 2
colors["stopToLB1000_10mm"] = 4
colors["stopToLB1000_100mm"] = 6
colors["stopToLB1000_1000mm"] = 7
colors["stopToLB1000_10000mm"] = 8

colors["stopToLB1800_0p1mm"] = 1
colors["stopToLB1800_1mm"] = 2
colors["stopToLB1800_10mm"] = 4
colors["stopToLB1800_100mm"] = 6
colors["stopToLB1800_1000mm"] = 7
colors["stopToLB1800_10000mm"] = 8


labels["stopToLB200_0p1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=0.1 mm"
labels["stopToLB200_1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=1 mm"
labels["stopToLB200_10mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=10 mm"
labels["stopToLB200_100mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=100 mm"
labels["stopToLB200_1000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=1000 mm"
labels["stopToLB200_10000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=200 GeV, c#tau=10000 mm"

labels["stopToLB1000_0p1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=0.1 mm"
labels["stopToLB1000_1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1 mm"
labels["stopToLB1000_10mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10 mm"
labels["stopToLB1000_100mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=100 mm"
labels["stopToLB1000_1000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=1000 mm"
labels["stopToLB1000_10000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1000 GeV, c#tau=10000 mm"

labels["stopToLB1800_0p1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=0.1 mm"
labels["stopToLB1800_1mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=1 mm"
labels["stopToLB1800_10mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=10 mm"
labels["stopToLB1800_100mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=100 mm"
labels["stopToLB1800_1000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=1000 mm"
labels["stopToLB1800_10000mm"] = "#tilde{t}#tilde{t}#rightarrow lb lb, M=1800 GeV, c#tau=10000 mm"

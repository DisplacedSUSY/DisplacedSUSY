import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "pu_cfg.py"

# create list of datasets to process
# add datasets as lists instead of the usual dict keys so mergeOutputHadd.py can handle them
datasets = []
datasets.extend(composite_dataset_definitions['all_bg_mc'])
datasets.extend(composite_dataset_definitions['DisplacedSUSYSignal'])

#processes = ['HToSSTo4L']
#massesH = ["110","125","150","200","300","400","450","500","600","750","800","900","1000"]
#massesS = ["10","20","30","50"] #minimum list of S masses that exist for every H mass
#lifetimes = [10**e for e in range(0, 6)]
#datasets = ["{}{}_{}_{}mm".format(p, mH, mS, l) for p in processes for mH in massesH for mS in massesS for l in lifetimes]
#for mH in massesH:
#  if int(mH)>=300:
#    for ctau in lifetimes:
#      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#  if int(mH)>=750:
#    for ctau in lifetimes:
#      datasets.append("HToSSTo4L"+mH+"_350_"+str(ctau)+"mm")
#datasets = [lt.replace(".", "p") for lt in datasets]

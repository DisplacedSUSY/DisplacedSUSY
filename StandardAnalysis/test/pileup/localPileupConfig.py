import os
from DisplacedSUSY.StandardAnalysis.Options import *

# specify which config file to pass to cmsRun
config_file = "pu_cfg.py"

# create list of datasets to process
# add datasets as lists instead of the usual dict keys so mergeOutputHadd.py can handle them
#datasets = [
#    'Cosmics'
#]
#datasets.extend(composite_dataset_definitions['all_bg_mc'])
#datasets.extend(composite_dataset_definitions['DisplacedSUSYSignal'])

processes = ['HToSSTo4L']
massesH = ["125","300","400","600","800","1000"]
massesS = []#minimum list of S masses that exist for every H mass
lifetimes = [10**e for e in range(0, 5)]
datasets = ["{}{}_{}_{}mm".format(p, mH, mS, l) for p in processes for mH in massesH for mS in massesS for l in lifetimes]
for mH in massesH:
  if int(mH)==125:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
  elif int(mH)==300:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_20_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
  elif int(mH)==400:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
  elif int(mH)==600:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
  elif int(mH)==800:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_250_"+str(ctau)+"mm")
  elif int(mH)==1000:
    for ctau in lifetimes:
      #datasets.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_350_"+str(ctau)+"mm")

# gmsb
#processes = ['sleptons']
#masses = [50] + [m for m in range(100, 901, 100)]
#lifetimes = [10**e for e in range(-2, 5)]
#datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]

datasets = [lt.replace(".", "p") for lt in datasets]

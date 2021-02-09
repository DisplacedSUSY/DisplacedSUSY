#!/usr/bin/env python
from DisplacedSUSY.MuMuChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"

# create list of datasets to process
datasets = default_datasets
datasets.remove('DisplacedSUSYSignal')
#datasets.append()

#datasets = [
    #'Cosmics',
    #'NoBPTX_2016_postHIP',
    #'NoBPTX_2017',
    #'NoBPTX_2018',
    #'DoubleMu_2016_postHIP',
#]

# full list of signal jobs we need to run,
# now that lifetime reweighting is in trees
#processes = ['stopToLB','stopToLD']
#masses = [m for m in range(100, 1801, 100)]
#lifetimes = [10**e for e in range(-1, 4)]
#datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
#datasets = [lt.replace(".", "p") for lt in datasets]

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

#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    #datasets = [
    #'HTo4Mu125_50_50mm',
    #'HTo4Mu125_50_500mm',
    #'HTo4Mu125_50_5000mm',
    #'HTo4Mu125_20_13mm',
    #'HTo4Mu125_20_130mm',
    #'HTo4Mu125_20_1300mm',
    #]

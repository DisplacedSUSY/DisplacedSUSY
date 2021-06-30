#!/usr/bin/env python
from DisplacedSUSY.EEChannel.localOptions import *

# specify which config file to pass to cmsRun
config_file = "Preselection_cfg.py"


# create list of datasets to process
#datasets = default_datasets
#datasets.remove('DisplacedSUSYSignal')
#datasets.remove('DoubleEG_2017')
#datasets.append()

#datasets = [
    #'Background',
    #'DoubleEG_2016_postHIP',
    #'DoubleEG_2017',
    #'DoubleEG_2017B',
    #'DoubleEG_2017C',
    #'DoubleEG_2017E',
    #'DoubleEG_2017F',
    #'EGamma_2018',
    #'DoubleEG_2016_2017_2018',

#'DYJetsToLL_10to50',
#'DYJetsToLL_50',
#'QCD_DoubleEMEnriched_HighMass_30to40',
#'QCD_DoubleEMEnriched_HighMass_40toInf',
#'QCD_DoubleEMEnriched_LowMass_30toInf',
#'QCD_EMEnriched_120to170',
#'QCD_EMEnriched_15to20',
#'QCD_EMEnriched_170to300',
#'QCD_EMEnriched_20to30',
#'QCD_EMEnriched_300toInf',
#'QCD_EMEnriched_30to50',
#'QCD_EMEnriched_50to80',
#'QCD_EMEnriched_80to120',
#'SingleTop_s_channel',
#'SingleTop_tW',
#'SingleTop_t_channel_antitop',
#'SingleTop_t_channel_top',
#'SingleTop_tbarW',
#'TTJets_DiLept',
#'TTJets_SingleLeptFromT',
#'TTJets_SingleLeptFromTbar',
#'WG',
#'WWToLNuLNu',
#'WWToLNuQQ',
#'WZToLLLNu',
#'WZToLNu2QorQQ2L',
#'WZToLNuNuNu',
#'ZG',
#'ZZToLLLL',
#'ZZToLLNuNu',
#'ZZToLLQQ',
#'ZZToNuNuQQ',

#]

# full list of signal jobs we need to run,
# now that lifetime reweighting is in trees
#processes = ['stopToLB','stopToLD']
#masses = [m for m in range(100, 1801, 100)]
#lifetimes = [10**e for e in range(-1, 4)]
#datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
#datasets = [lt.replace(".", "p") for lt in datasets]

processes = ['HToSSTo4L']
massesH = ["125","300","400","600","800","1000"]
massesS = []#minimum list of S masses that exist for every H mass
lifetimes = [10**e for e in range(0, 5)]
datasets = ["{}{}_{}_{}mm".format(p, mH, mS, l) for p in processes for mH in massesH for mS in massesS for l in lifetimes]
for mH in massesH:
  if int(mH)==125:
    for ctau in lifetimes:
      datasets.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
      datasets.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
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
datasets = [lt.replace(".", "p") for lt in datasets]

# gmsb
#processes = ['sleptons']
#masses = [50] + [m for m in range(100, 901, 100)]
#lifetimes = [10**e for e in range(-2, 5)]

#processes = ['staus']
#masses = [50] + [m for m in range(100, 501, 100)]
#lifetimes = [10**e for e in range(-1, 4)]

#datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
#datasets = [lt.replace(".", "p") for lt in datasets]

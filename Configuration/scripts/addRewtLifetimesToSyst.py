#!/usr/bin/env python

# Add reweighted lifetime points to systematic files
# Usage:
# $ python addRewtLifetimesToSyst.py
# If mistake is made, revert the changes with, e.g.:
# $ git checkout HEAD data/systematic_values__pileup.txt


import sys
import math
import functools
from DisplacedSUSY.StandardAnalysis.Options import *



if HToSS:
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
        datasets.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
        datasets.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
        datasets.append("HToSSTo4L"+mH+"_350_"+str(ctau)+"mm")
  datasets = [lt.replace(".", "p") for lt in datasets]

elif stops:
  processes = ['stopToLB','stopToLD']
  masses = [m for m in range(100, 1801, 100)]
  lifetimes = [10**e for e in range(-1, 4)]     #now with reweighting in trees
  datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
  datasets = [lt.replace(".", "p") for lt in datasets]

elif GMSB and not GMSBstaus:
  processes = ['sleptons']
  masses = [50] + [m for m in range(100, 1001, 100)]
  lifetimes = [10**e for e in range(-1, 5)]     #now with reweighting in trees, should eventually be extended

elif GMSBstaus:
  processes = ['staus']
  masses = [50] + [m for m in range(100, 501, 100)]
  lifetimes = [10**e for e in range(-1, 4)]     #now with reweighting in trees
  datasets = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
  datasets = [lt.replace(".", "p") for lt in datasets]

lifetimes = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
lifetimes0p1 = ['0p01', '0p02', '0p03', '0p04', '0p05', '0p06', '0p07', '0p08', '0p09', '0p1']
if HToSS:
  lifetimes1 = ['0p1', '0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1'] #HtoSS
else:
  lifetimes1 = ['0p2', '0p3', '0p4', '0p5', '0p6', '0p7', '0p8', '0p9', '1'] #stops and GMSB


systs = [
    'pileup',
    'electronD0Smearing',
    'muonD0Smearing',
    'electronIDandIso',
    'muonIDandIso',
    'muonPixelHitEff',
    'muonPixelHitEff16',
]

analysisChannels = [
    'emu',
    'ee',
    'mumu',
]

years = [
    '2016',
    '2017',
    '2018',
]

for syst in systs:
    for analysisChannel in analysisChannels:
        for year in years:
            if year == '2016' and (syst == 'electronD0Smearing' or syst == 'muonD0Smearing' or syst == 'muonPixelHitEff'):
                continue #no d0 smearing in 2016
            elif (year == '2017' or year == '2018') and syst == 'muonPixelHitEff16':
                continue #muonPixelHitEff16 in 2016 only, muonPixelHitEff in 2017 and 2018
            elif analysisChannel == 'ee' and (syst == 'muonD0Smearing' or syst == 'muonIDandIso' or syst == 'muonPixelHitEff' or syst == 'muonPixelHitEff16'):
                continue #no muon systematics in ee channel
            elif analysisChannel == 'mumu' and (syst == 'electronD0Smearing' or syst == 'electronIDandIso'):
                continue #no electron systs in mumu channel
            else:
              #read in original text file, split into 3 "words": original dataset name, down error, up error
              if HToSS:
                infile = "../data/systematic_values__HToSS__" + syst + "_" + analysisChannel + "_" + year + ".txt"
              elif GMSB and not GMSBstaus:
                infile = "../data/systematic_values__sleptons__" + syst + "_" + analysisChannel + "_" + year + ".txt"
              elif GMSBstaus:
                infile = "../data/systematic_values__staus__" + syst + "_" + analysisChannel + "_" + year + ".txt"
              else:
                infile = "../data/systematic_values__" + syst + "_" + analysisChannel + "_" + year + ".txt"
              fin = open(infile, "r")
              contentOld = fin.read()
              words = contentOld.split()
              for dataset in datasets:
                  idx = words.index(dataset)
                  errDn = float(words[idx+1])
                  errUp = float(words[idx+2])
                  contentNew = ""

                  #find original lifetime from dataset name
                  if HToSS:
                    oldLifetime = dataset.split("_")[2] #H to SS
                  else:
                    oldLifetime = dataset.split("_")[1] #stops and GMSB
                  #print "oldLifetime is: " + oldLifetime

                  #change original lifetime to the list of new lifetimes
                  #for each new lifetime, add a new line to the new text file
                  #need several categories because original lifetimes are things like 0p1, etc
                  if oldLifetime.find("0p1mm")>=0:
                      for l in range(10):
                          newLifetime0p1 = oldLifetime.replace("0p1",lifetimes0p1[l])
                          newDataset = dataset.replace(oldLifetime,newLifetime0p1)
                          line = '{0: <40}'.format(str(newDataset)) + " " + '{0: <8}'.format(errDn) + " " + str(errUp) + "\n"
                          contentNew += line
                  else:
                      newLifetimes = []
                      if oldLifetime.find("10")>=0:
                        for l in range(9):
                          newLifetimes.append(oldLifetime.replace("10",lifetimes[l]))
                          newDataset = dataset.replace(oldLifetime,newLifetimes[l])
                          line = '{0: <40}'.format(str(newDataset)) + " " + '{0: <8}'.format(errDn) + " " + str(errUp) + "\n"
                          contentNew += line
                      elif oldLifetime.find("1mm")>=0:
                        if HToSS:
                          for l in range(10): #H to SS
                            newLifetimes.append(oldLifetime.replace("1",lifetimes1[l]))
                            newDataset = dataset.replace(oldLifetime,newLifetimes[l])
                            line = '{0: <40}'.format(str(newDataset)) + " " + '{0: <8}'.format(errDn) + " " + str(errUp) + "\n"
                            contentNew += line
                        else:
                          for l in range(9): #stops and GMSB
                            newLifetimes.append(oldLifetime.replace("1",lifetimes1[l]))
                            newDataset = dataset.replace(oldLifetime,newLifetimes[l])
                            line = '{0: <40}'.format(str(newDataset)) + " " + '{0: <8}'.format(errDn) + " " + str(errUp) + "\n"
                            contentNew += line
                      elif oldLifetime.find("1000mm")>=0:
                        for l in range(9):
                          newLifetime1000mm = oldLifetime.replace("1",lifetimes[l])
                          newDataset = dataset.replace(oldLifetime,newLifetime1000mm)
                          line = '{0: <40}'.format(str(newDataset)) + " " + '{0: <8}'.format(errDn) + " " + str(errUp) + "\n"
                          contentNew += line

                  #replace old line with new content
                  oldLine = dataset + " " + words[idx+1] + " " + words[idx+2] + "\n"
                  contentOld = contentOld.replace(oldLine, contentNew)

              #replace old text file with new one
              outputFile = infile

              #another option would be to save a new file: good to use if you're not sure yet
              #outputFile = infile.replace(".txt", "_add.txt")

              fout = open (outputFile, "w")
              fout.write(contentOld)
              fout.close()
              print "Finished writing " + outputFile + " using as input: " + infile

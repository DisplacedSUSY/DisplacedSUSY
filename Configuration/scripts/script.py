#!/usr/bin/env python
import subprocess
import sys
import os
import re
import math
import glob
from array import *
from decimal import *


#inputDir1= "/data/users/lantonel/condor/MuMu_Skim_syncTest"
#inputDir2= "/data/users/bcardwell/condor/MuMuSkim_17_02_03"

#inputDir1= "/data/users/lantonel/condor/EE_Skim_syncTest"
#inputDir2= "/data/users/bcardwell/condor/EESkim_17_02_03"

inputDir1 = "/data/users/lantonel/condor/MuMu_PRC_Skim"
inputDir2 = "/data/users/bcardwell/condor/MuMu_PromptControlRegion+Trig_17_03_02"

#inputDir1 = "/data/users/lantonel/condor/EE_PRC_Skim_wGoodTrigger"
#inputDir2 = "/data/users/bcardwell/condor/EE_PromptControlRegion_17_03_20"

datasets1 = filter(lambda x: os.path.isdir(os.path.join(inputDir1, x)), os.listdir(inputDir1))

#datasets1 = ["DoubleMu_2016B"]

datasets1.remove("CMSSW_8_0_21")
#datasets2.remove("CMSSW_8_0_21")

for sample in datasets1:
    print
    print '----------------------------------',sample
    print
    print
    dir1 = inputDir1+"/"+sample+"/"
    dir2 = inputDir2+"/"+sample+"/"
    files = [path.split("/")[-1] for path in glob.glob(dir1+"*err")]
#    print files




    total1 = 0
    total2 = 0
    evtList1= [-1] * 2000
    evtList2= [-1] * 2000
    for file_ in files:
        job = int(file_.split("_")[-1].split(".")[0])

#        print file_.split("condor_")[-1].split('.')[0],
        if not os.path.isfile(dir1+file_):
            print "!!!"
        else:
            file1 = subprocess.Popen(['tail','-4',dir1+file_], stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()
#            print file1
#            file1 = open(dir1+file_).readlines()
            found = False
            for line in reversed(file1):
                if line.startswith('----------'):
                    found = True
                    continue
                if found:
#                    print line
                    if len(filter(None,line.split(' '))) > 5:
                        evtList1[job] += int(filter(None,line.split(' '))[5].split('.')[0])+1
                    else:
                        evtList1[job] += -1
#                    print "jamie", evtList1[job]
                    break


        if not os.path.isfile(dir2+file_):
            print "!!!!!!"
        else:
            top = subprocess.Popen(['head','-1',dir2+file_], stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()
            index = int(top[0].split("skim_")[-1].split('.')[0])
            file2 = subprocess.Popen(['tail','-4',dir2+file_], stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()
#            file2 = open(dir2+file_).readlines()
            found = False
            for line in reversed(file2):
                if line.startswith('----------'):
                    found = True
                    continue
                if found:                    
#                    print index
                    if len(filter(None,line.split(' '))) > 5:
                        evtList2[index] += int(filter(None,line.split(' '))[5].split('.')[0])+1
                    else:
                        evtList2[index] += -1
#                    print "bryan", evtList2[index]
                    break

#        if 'nan' not in evts1[2]:
#            total1 += float(evts1[2])
#        if 'nan' not in evts2[2]:
#            total2 += float(evts2[2])

#        print evts1[5], evts2[5]

#        if float(evts1[5]) != float(evts2[5]):
#            print file_

#        if len(evts1) > 5:
#            total1 += float(evts1[5])
#        if len(evts2) > 5:
#            total2 += float(evts2[5])



#        print total1 - total2

#        if evts1 != evts2:
#        if len(evts1) < 6 or :
#        if 0:
#            print "------------"
#            print dir1+file_
#            print "\t",evts1
#            print "-----"
 #           print dir2+file_
##            print "\t",evts2
 #           print "------------"


#    print total1, total2


    print len(evtList1)
    for job in range(len(evtList1)):
        if evtList1[job] != evtList2[job]:
            print sample, job, evtList1[job], evtList2[job]

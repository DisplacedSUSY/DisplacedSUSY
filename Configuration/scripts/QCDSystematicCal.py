#!/usr/bin/env python
from decimal import *
import sys
import os
import re
from math import *
from array import *
from ROOT import *  
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.miniAODV2Samples import *

parser = OptionParser()
parser = set_commandline_arguments(parser)

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

def getDivError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)/pow(b,2) + pow(deltab,2)*pow(a,2)/pow(b,4))
def getMulError(a,b,deltaa,deltab):
    return sqrt(pow(deltaa,2)*pow(b,2) + pow(deltab,2)*pow(a,2))

scaleFactors = {}
def getScaleFactor(muSFSets, eleSFSets):
    totalSFSR1s = []
    totalSFSR2s = []
    totalSFSR3s = []
    for muSFSet in muSFSets:
        for eleSFSet in eleSFSets:
            totalSFSR1s.append(abs(float(muSFSet['SR1'])*float(eleSFSet['SR1']) - 1.34375 * 1.48546296162))           
            totalSFSR2s.append(abs(float(muSFSet['SR2'])*float(eleSFSet['SR2']) - 0.46875*0.627076344124))            
            totalSFSR3s.append(abs(float(muSFSet['SR3'])*float(eleSFSet['SR3']) - 0.046875*0.227408007911))         
    totalSFSR1s.sort()
    totalSFSR2s.sort()
    totalSFSR3s.sort()
    print "Systematic uncertainty in SR1: " + str(totalSFSR1s[len(totalSFSR1s) - 1]/(1.34375 * 1.48546296162))
    print "Systematic uncertainty in SR2: " + str(totalSFSR2s[len(totalSFSR2s) - 1]/(0.46875*0.627076344124))
    print "Systematic uncertainty in SR3: " + str(totalSFSR3s[len(totalSFSR3s) - 1]/(0.046875*0.227408007911))

getScaleFactor(muSFSets, eleSFSets)

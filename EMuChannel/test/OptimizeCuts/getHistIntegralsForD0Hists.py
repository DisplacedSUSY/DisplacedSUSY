#run with a command like this:
#python getHistIntegralsForD0Hists.py -l options.py -w DisplacedLeptons2016/Preselection_D0CutOptimization
import time
import os
import sys
import math
import copy
import re
from math import *
from array import *
from optparse import OptionParser
from operator import itemgetter
from ROOT import *

from DisplacedSUSY.Configuration.configurationOptions import *
from DisplacedSUSY.Configuration.miniAODV2_80X_Samples import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.histogramUtilities import *

parser = OptionParser()
parser = set_commandline_arguments(parser)
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)

if arguments.condorDir:
    condor_dir = arguments.condorDir
else:
    print "No condor output directory specified, shame on you"
    sys.exit(0)

xloValues = [0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045, 0.050] #cm
#xloValues = [0.010, 0.020, 0.030, 0.040, 0.050, 0.060, 0.070, 0.080, 0.090, 0.100, 0.110, 0.120, 0.130, 0.140, 0.150]#cm
#xloValues = [0.050, 0.100, 0.150, 0.200, 0.250, 0.300, 0.350, 0.400, 0.450, 0.500, 0.550, 0.600, 0.650, 0.700, 0.750, 0.800, 0.850, 0.900] #cm
#xloValues = [1] #cm
#xloValues = [50,100,150,300] #um
xhi = 10 #cm
#xhi = 400 #um

bkgdEleInts = []
bkgdMuInts = []
signalEleInts = []
signalMuInts = []

for dataset in datasets:
    for xlo in xloValues:
        histEle = "Electron Plots/electronAbsD0_10cm"
        #hist = "Electron Plots/electronAbsD0_200um"
        histMu = "Muon Plots/muonAbsD0_10cm"
        (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histEle,xlo,xhi)
        (muInt, muIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",histMu,xlo,xhi)
        if dataset=="Background": 
            bkgdEleInts.append(eleInt)
            bkgdMuInts.append(muInt)
        else:
            signalEleInts.append(eleInt)
            signalMuInts.append(muInt)

        print "for " + dataset + ", " + "in " + condor_dir 
        print "    electron integral from " + str(xlo) + " cm to 10 cm is: " + str("%.1f" % eleInt) + " +/- " + str("%.1f" % eleIntError)
        print "    muon integral from " + str(xlo) + " cm to 10 cm is: " + str("%.1f" % muInt) + " +/- " + str("%.1f" % muIntError)

print "/////////////////////////////////////////////////////////////////////"
for bkgdEleInt,signalEleInt in zip(bkgdEleInts,signalEleInts):
    #print "bkgdEleInt is: " + str(bkgdEleInt) + ", signalEleInt is: " + str(signalEleInt)
    SoverSqrtBEle = signalEleInt/sqrt(bkgdEleInt)
    print "S/sqrt(B) for electrons is: " + str("%.1f" % SoverSqrtBEle) 

print "/////////////////////////////////////////////////////////////////////"
for bkgdMuInt,signalMuInt in zip(bkgdMuInts,signalMuInts):
    SoverSqrtBMu = signalMuInt/sqrt(bkgdMuInt)
    print "S/sqrt(B) for muons is: " + str("%.1f" % SoverSqrtBMu) 
    

print "done"

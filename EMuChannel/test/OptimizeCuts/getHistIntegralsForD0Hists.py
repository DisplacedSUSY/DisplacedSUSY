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

#xloValues = [0.005, 0.010, 0.015, 0.020, 0.025, 0.030] #cm
xloValues = [50,100,150,300] #um
#xhi = 10 #cm
xhi = 400 #um

bkgdEleInts = []
signalEleInts = []

for dataset in datasets:
    for xlo in xloValues:
        #hist = "Electron Plots/electronAbsD0_10cm"
        hist = "Electron Plots/electronAbsD0_200um"
        (eleInt, eleIntError) = getHistIntegral(dataset,condor_dir,"PreselectionPlotter",hist,xlo,xhi)
        if dataset=="Background": 
            bkgdEleInts.append(eleInt)
        else:
            signalEleInts.append(eleInt)

        print "for " + dataset + ", " + "in " + condor_dir 
        print "     electron integral from " + str(xlo) + " cm to 10 cm is: " + str("%.1f" % eleInt) + " +/- " + str("%.1f" % eleIntError)

print "/////////////////////////////////////////////////////////////////////"
for bkgdEleInt,signalEleInt in zip(bkgdEleInts,signalEleInts):
    #print "bkgdEleInt is: " + str(bkgdEleInt) + ", signalEleInt is: " + str(signalEleInt)
    SoverSqrtB = signalEleInt/sqrt(bkgdEleInt)
    print "S/sqrt(B) is: " + str("%.1f" % SoverSqrtB) 
    

print "done"

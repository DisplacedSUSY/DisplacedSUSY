#!/usr/bin/env python
import os
from DisplacedSUSY.StandardAnalysis.Options import *

# choose luminosity used for MC normalization
# units: 1/pb
# lumi varies from channel to channel, so define locally
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    intLumi = 16146.2 # 2016G,H only
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    intLumi = 41527.5 #Nov17 rereco 2017 golden json AND e-e triggers
print "normalizing MC to " + str(intLumi) + " 1/pb"

InputCondorArguments = {}

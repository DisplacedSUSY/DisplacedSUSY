#!/usr/bin/env python

import time
import os
import sys
import math
import copy
from array import *
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                                    help="output directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.rstrip('.py') + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)

###looping over signal models and writing a datacard for each
for mass in masses:
    for lifetime in lifetimes:
        for branching_ratio in branching_ratios:

            signal_name = "stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio
            datacard_name = "limits/"+arguments.outputDir+"/datacard_"+signal_name+".txt"
            combine_options = "-M Asymptotic -s -1 --minimizerStrategy 1 --picky --minosAlgo stepping -H ProfileLikelihood"

            command = "combine "+datacard_name+" "+combine_options+" --name "+signal_name+" > limits/"+arguments.outputDir+"/combine_log_"+signal_name+".log"
            print command
            os.system(command)
            command = "mv higgsCombine"+signal_name+"*.root limits/"+arguments.outputDir+"/limits_"+signal_name+".root"
            os.system(command)
            os.system("rm -f roostats*")



                                

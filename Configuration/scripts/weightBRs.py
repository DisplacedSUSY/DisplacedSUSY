#!/usr/bin/env python
import os
import sys
from optparse import OptionParser

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *



parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--condorDir", dest="condorDir",
                  help="condor output directory")
    
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.rstrip('.py') + " import *")
else:
    print "No local config specified, shame on you"
    exit

if arguments.condorDir:
    condor_dir = set_condor_output_dir(arguments)    
else:
    print "No condor directory specified, how could you?"
    exit

from ROOT import TFile, TH1D

for mass in masses:
    for lifetime in lifetimes:
        for branching_ratio in branching_ratios:

            print "creating output file for:"
            print "   stop mass   =",mass,"GeV"
            print "   lifetime    =",lifetime,"mm"
            print "   stop->Bl BR =",branching_ratio,"percent" 

            BR = float(branching_ratio)/100
            Bl_weight = BR * BR
            Tnu_weight = (1-BR) * (1-BR)
            BT_weight = 2 * BR * (1-BR) 
                
            input_file_name = "%s/stop%stoBl_%smm" % (condor_dir,mass,lifetime)
            output_file_name_Bl = "%s_BR%s_tmp" % (input_file_name,branching_ratio)
            command = "mergeTFileServiceHistograms -i %s.root -o %s.root -w %s" % (input_file_name, output_file_name_Bl, Bl_weight)
            os.system(command)

            input_file_name = "%s/stop%stoTnu_%smm" % (condor_dir,mass,lifetime)
            output_file_name_Tnu = "%s_BR%s_tmp" % (input_file_name,branching_ratio)
            command = "mergeTFileServiceHistograms -i %s.root -o %s.root -w %s" % (input_file_name, output_file_name_Tnu, Tnu_weight)
            os.system(command)

            input_file_name = "%s/stop%stoBT_%smm" % (condor_dir,mass,lifetime)
            output_file_name_BT = "%s_BR%s_tmp" % (input_file_name,branching_ratio)
            command = "mergeTFileServiceHistograms -i %s.root -o %s.root -w %s" % (input_file_name, output_file_name_BT, BT_weight)
            os.system(command)

            input_file_list = "%s.root %s.root %s.root" % (output_file_name_Bl,output_file_name_Tnu,output_file_name_BT)
            command = "hadd -v 0 -f %s/stop%s_%smm_br%s.root %s" % (condor_dir,mass,lifetime,branching_ratio,input_file_list)
            os.system(command)

            command = "rm %s/*tmp*" % (condor_dir)
            os.system(command)

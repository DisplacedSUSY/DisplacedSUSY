#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
import shutil
from array import *
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                                    help="output directory")
parser.add_option("-M", "--method", dest="method", default="Asymptotic",
                                    help="which method of combine to use: currently supported options are Asymptotic (default), MarkovChainMC and HybridNew")
parser.add_option("-t", "--toys", dest="Ntoys", default="1",
                  help="how many toy MC to throw, default = 1")
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                                    help="run on the condor queue")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)

def output_condor(command, options):
    script = "#!/usr/bin/env bash\n\n"
    script += command+" "+options+"\n"
    f = open ("condor.sh", "w")
    f.write (script)
    f.close ()
    os.chmod ("condor.sh", 0775)
    command = os.getcwd () + "/condor.sh"

    sub_file = ""
    if os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/data/condor.sub"):
        f = open (os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/data/condor.sub", "r")
        sub_file = f.read ()
        f.close ()
        sub_file = re.sub (r"\$combine", command, sub_file)
    else:
        sub_file += "Executable              = "+command+"\n"
        sub_file += "Universe                = vanilla\n"
        sub_file += "Getenv                  = True\n"
        sub_file += "\n"
        sub_file += "Output                  = condor_$(Process).out\n"
        sub_file += "Error                   = condor_$(Process).err\n"
        sub_file += "Log                     = condor_$(Process).log\n"
        sub_file += "\n"
        sub_file += "+IsLocalJob             = true\n"
        sub_file += "Rank                    = TARGET.IsLocalSlot\n"
        sub_file += "\n"
        sub_file += "Queue 1\n"

    f = open ("condor.sub", "w")
    f.write (sub_file)
    f.close ()


### create a file to keep track of which combine method was used
### (since extracting the limits is different for each one)
methodFile = open(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/test/limits/"+arguments.outputDir+"/method.txt", "w")
methodFile.write(arguments.method)
methodFile.close()

### looping over signal models and running a combine job for each one
for mass in masses:
    for lifetime in lifetimes:
        for branching_ratio in branching_ratios:

            signal_name = "stop"+mass+"_"+lifetime+"mm_"+"br"+branching_ratio
            condor_dir = "limits/"+arguments.outputDir+"/"+signal_name
            datacard_name = "datacard_"+signal_name+".txt"
            datacard_src_name = "limits/"+arguments.outputDir+"/"+datacard_name
            datacard_dst_name = condor_dir+"/"+datacard_name
            combine_options = "-s -1 -H ProfileLikelihood "
            if arguments.method == "HybridNew" or arguments.method == "MarkovChainMC":
                combine_options += "-M " + arguments.method + " "
                combine_options = combine_options + "-t " + arguments.Ntoys + " "
            else:
                combine_options += "-M Asymptotic --minimizerStrategy 1 --picky --minosAlgo stepping "

            combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
            combine_command = combine_command.rstrip()

            shutil.rmtree(condor_dir, True)
            os.mkdir(condor_dir)
            shutil.copy(datacard_src_name, datacard_dst_name)
            os.chdir(condor_dir)

            if not arguments.batchMode:
                command = "(combine "+datacard_name+" "+combine_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
                print command
                os.system(command)

            else:
                print "combine "+datacard_name+" "+combine_options+" --name "+signal_name
                output_condor(combine_command, datacard_name+" "+combine_options+" --name "+signal_name+" | tee /dev/null")
                os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

            os.chdir("../../..")

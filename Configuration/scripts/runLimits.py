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
parser.add_option("-w", "--workDir", dest="condorDir",
                  help="condor working directory")
parser.add_option("-M", "--method", dest="method", default="AsymptoticLimits",
                  help="which method of combine to use: currently supported options are AsymptoticLimits (default), BayesianSimple, MarkovChainMC, BayesianToyMC, and HybridNew")
parser.add_option("-i", "--iterations", dest="Niterations", default="10000",
                  help="how many points are proposed to fill a single Markov chain, default = 10k")
parser.add_option("-r", "--tries", dest="Ntries", default="10",
                  help="how many times the algorithm will run for observed limits, default = 10")
parser.add_option("-t", "--toys", dest="Ntoys", default="1",
                  help="how many toy MC to throw for expected limits, default = 1")
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                                    help="run on the condor queue")
parser.add_option("-s", "--scaleSignalRate", dest="maxSignalRate", default="0.1",
                  help="scale all signal rates so the maximum is MAXSIGNALRATE, default = 0.1; negative values turn off scaling")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if not arguments.condorDir:
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
        sub_file += "request_memory            = 2048MB\n"
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

def scaleSignal(src, dst):
    f = open (src, "r")
    processLine = ""
    rateLine = ""
    gammaLines = []
    for line in f:
      if re.search (r"^\s*process\s", line) and not processLine:
          processLine = line.split ()
      if re.search (r"^\s*rate\s", line) and not rateLine:
          rateLine = line.split ()
      if re.search (r"\sgmN\s", line):
          gammaLines.append (line.split ())
    f.close ()

    signalRate = []
    signalAlpha = []
    for process in range (0, len (processLine)):
        if re.search (r"^stop", processLine[process]):
            signalRate.append (float (rateLine[process]))
    signalSF = 1.0
    if len (signalRate) > 0:
        largestSignalRate = sorted (signalRate)[-1]
        signalSF = float (arguments.maxSignalRate) / largestSignalRate if largestSignalRate > 0 else 0.0
    for process in range (0, len (processLine)):
        if re.search (r"^stop", processLine[process]):
            rateLine[process] = str (signalSF * float (rateLine[process]))
            for gammaLine in gammaLines:
                try:
                    gammaLine[process + 2] = str (signalSF * float (gammaLine[process + 2]))
                except ValueError:
                    pass

    fin = open (src, "r")
    fout = open (dst, "w")
    for line in fin:
      if re.search (r"^\s*rate\s", line):
          fout.write (" ".join (rateLine) + "\n")
      elif re.search (r"\sgmN\s", line):
          fout.write (" ".join (gammaLines[0]) + "\n")
          del gammaLines[0]
      else:
          fout.write (line)
    fin.close ()
    fout.close ()

    dst = re.sub (r"^(.*)\.[^./]*$", r"\1.sf", dst)
    f = open (dst, "w")
    f.write (str (signalSF) + "\n")
    f.close ()

# create a file to keep track of which combine method was used
outputDirPath = os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/test/limits/"+arguments.condorDir
methodFile = open(outputDirPath+"/method.txt", "w")
methodFile.write(arguments.method)
methodFile.close()

# loop over signal models and run a combine job for each one
for signal_name in signal_points:
    # rename sub-mm samples to match sample names
    signal_name = signal_name.replace('.', 'p')

    condor_expected_dir = "limits/"+arguments.condorDir+"/"+signal_name+"_expected"
    condor_observed_dir = "limits/"+arguments.condorDir+"/"+signal_name+"_observed"
    datacard_name = "datacard_"+signal_name+".txt"
    datacard_src_name = "limits/"+arguments.condorDir+"/"+datacard_name
    datacard_dst_expected_name = condor_expected_dir+"/"+datacard_name
    datacard_dst_observed_name = condor_observed_dir+"/"+datacard_name

    combine_expected_options = combine_observed_options = "-M " + arguments.method
    if arguments.method == "HybridNew":
        combine_expected_options = combine_expected_options + "-T " + arguments.Ntoys + " --frequentist --expectedFromGrid=0.5 --saveToys --fullBToys --testStat LHC --saveHybridResult --saveGrid"
    elif arguments.method == "MarkovChainMC":
        combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " --tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
        combine_observed_options = combine_observed_options + "--tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
    elif arguments.method == "BayesianSimple":
        combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " "
    elif arguments.method == "BayesianToyMC":
        combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " "
    else:
        print "Defaulting to AsymptoticLimits"
        combine_expected_options += " --picky "
        combine_observed_options += " --picky "

    combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
    combine_command = combine_command.rstrip()

    shutil.rmtree(condor_expected_dir, True)
    os.mkdir(condor_expected_dir)
    if arguments.maxSignalRate < 0.0:
        shutil.copy(datacard_src_name, datacard_dst_expected_name)
    else:
        scaleSignal(datacard_src_name, datacard_dst_expected_name)
    os.chdir(condor_expected_dir)

    if not arguments.batchMode:
        command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
        print command
        os.system(command)

    else:
        print "combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name
        output_condor(combine_command, datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
        os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
    os.chdir("../../..")

    # for everything other than Asymptotic, we need to also run observed limits
    if arguments.method != "AsymptoticLimits":

        shutil.rmtree(condor_observed_dir, True)
        os.mkdir(condor_observed_dir)
        if arguments.maxSignalRate < 0.0:
            shutil.copy(datacard_src_name, datacard_dst_observed_name)
        else:
            scaleSignal(datacard_src_name, datacard_dst_observed_name)
        os.chdir(condor_observed_dir)

        if not arguments.batchMode:
            command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
            print command
            os.system(command)

        else:
            print "combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name
            output_condor(combine_command, datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null")
            os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

        os.chdir("../../..")

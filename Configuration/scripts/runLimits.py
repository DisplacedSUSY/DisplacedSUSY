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

from DisplacedSUSY.Configuration.limitOptions import *

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
    cmssw_tarball = os.environ["CMSSW_VERSION"] + '.tar.gz'
    script = "#!/usr/bin/env bash\n\n"
    script += 'source /cvmfs/cms.cern.ch/cmsset_default.sh\n'
    script += 'source /cvmfs/cms.cern.ch/crab3/crab.sh\n'
    script += 'tar -xzf '+cmssw_tarball+'\n'
    script += 'rm -f '+cmssw_tarball+'\n'
    script += 'SCRAM_ARCH=' + os.environ["SCRAM_ARCH"] + '\n'
    script += 'cd ' + os.environ["CMSSW_VERSION"] + '/src/\n'
    script += 'scramv1 b ProjectRename\n'
    script += 'eval `scramv1 runtime -sh`\n'
    script += 'cd -\n\n'
    script += command+" "+options+"\n"
    f = open ("condor.sh", "w")
    f.write (script)
    f.close ()
    os.chmod ("condor.sh", 0775)
    command = os.getcwd () + "/condor.sh"

    sub_file = ""
    sub_file += "Executable              = "+command+"\n"
    sub_file += "Universe                = vanilla\n"
    sub_file += "Getenv                  = True\n"
    sub_file += "request_memory          = 2048MB\n"
    sub_file += "Should_Transfer_Files   = YES\n"
    sub_file += "Transfer_Input_Files    = "+combine_command+", "+cmssw_tarball+", "+datacard_name+"\n"
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
        if (re.search (r"^stop", processLine[process]) or re.search (r"^HTo", processLine[process])):
            signalRate.append (float (rateLine[process]))
    signalSF = 1.0
    if len (signalRate) > 0:
        largestSignalRate = sorted (signalRate)[-1]
        signalSF = float (arguments.maxSignalRate) / largestSignalRate if largestSignalRate > 0 else 0.0
    for process in range (0, len (processLine)):
        if (re.search (r"^stop", processLine[process]) or re.search (r"^HTo", processLine[process])):
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
outputDirPath = "limits/"+arguments.condorDir
methodFile = open(outputDirPath+"/method.txt", "w")
methodFile.write(arguments.method)
methodFile.close()


# fixme: update to only make one tarball per directory (instead of one per signal point)
if arguments.batchMode:
    os.system('tar -zc --exclude="*git*" --exclude="test" --exclude="tmp" -C $CMSSW_BASE/../ -f limits/'+arguments.condorDir+'/$CMSSW_VERSION.tar.gz $CMSSW_VERSION')

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

    if arguments.method == "AsymptoticLimits":
        print "Defaulting to AsymptoticLimits"
        common_options = ""
        method_options = ""
        expected_only_options = "--noFitAsimov"
    elif arguments.method == "Significance":
        common_options = ""
        method_options = ""
        expected_only_options = ""
        #expected_only_options = "-t -1 --expectSignal=1"
    else:
        common_options = "-H AsymptoticLimits"

        # fixme: do we need something fancier for blinded expected limits?
        if arguments.method == "HybridNew":
            method_options = "--LHCmode LHC-limits --cminDefaultMinimizerStrategy 0 --fork 4"
            #method_options = ""
            expected_only_options = "-t -1 --expectedFromGrid 0.500"
        else:
            raise RuntimeError("Unrecognized method:", arguments.method)

    combine_observed_options = "-M {} {} {}".format(arguments.method, common_options, method_options)
    combine_expected_options = combine_observed_options + " " + expected_only_options

    combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
    combine_command = combine_command.rstrip()

    shutil.rmtree(condor_expected_dir, True)
    os.mkdir(condor_expected_dir)
    if float(arguments.maxSignalRate) < 0.0:
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
        os.symlink ("../"+os.environ["CMSSW_VERSION"]+".tar.gz",os.environ["CMSSW_VERSION"]+".tar.gz")
        output_condor("combine", datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
        os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
    os.chdir("../../..")

    # for everything other than Asymptotic, we need to also run observed limits
    if arguments.method != "AsymptoticLimits" and not arguments.expectedOnly:

        shutil.rmtree(condor_observed_dir, True)
        os.mkdir(condor_observed_dir)
        if float(arguments.maxSignalRate) < 0.0:
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

    if arguments.quick:
        sys.exit("Finished running one point.")

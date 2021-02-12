#!/usr/bin/env python

# Calculate expected hybridNew limits using input grid of test-statistic distributions. This script
# assumes the naming conventions of Configuration/scripts/runLimitsGrid.py and runs over signal
# points defined in Configuaration/python/limitOptions.py.

# usage: calculateLimits.py -w WORKING_DIR [--batchMode]

import os
import subprocess
import glob
from DisplacedSUSY.Configuration.limitOptions import *

if arguments.condorDir:
    output_dir = "limits/" + arguments.condorDir
    if not os.path.exists(output_dir):
        os.system("mkdir " + output_dir)
else:
    raise RuntimeError("No output directory specified")

def output_condor(name, commands, inputs):
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
    for command in commands:
        script += command+"\n"
    with open(name+".sh", "w") as f:
        f.write(script)
    os.chmod (name+".sh", 0775)

    command = "{}/{}".format(os.getcwd(), name+".sh")
    input_list = ", ".join(inputs)
    sub_file = ""
    sub_file += "Executable              = "+command+"\n"
    sub_file += "Universe                = vanilla\n"
    sub_file += "Getenv                  = True\n"
    sub_file += "request_memory          = 2048MB\n"
    sub_file += "Should_Transfer_Files   = YES\n"
    sub_file += "Transfer_Input_Files    = "+input_list+"\n"
    sub_file += "\n"
    sub_file += "Output                  = "+name+".out\n"
    sub_file += "Error                   = "+name+".err\n"
    sub_file += "Log                     = "+name+".log\n"
    sub_file += "\n"
    sub_file += "+IsLocalJob             = true\n"
    sub_file += "Rank                    = TARGET.IsLocalSlot\n"
    sub_file += "\n"
    sub_file += "Queue 1\n"
    with open(name+".sub", "w") as f:
        f.write(sub_file)

def link_tarball(tarball_name):
    try:
        os.symlink("../" + tarball_name, tarball_name)
    except OSError as e:
        # suppress exception if symlink already exists
        if e.errno != 17:
            raise RuntimeError("Something is wrong with the cmssw tarball symlink")

####################################################################################################

quantiles = [0.025, 0.160, 0.500, 0.840, 0.975]
combine_template = ("combine {datacard} -M HybridNew --LHCmode LHC-limits --grid grid.root "
                    "--readHybridResults --expectedFromGrid {quantile} --plot cls_{quantile}.pdf")

if arguments.batchMode:
    combine_executable = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE)
    combine_executable = combine_executable.communicate()[0].rstrip()
    tarball_name = os.environ["CMSSW_VERSION"] + ".tar.gz"

for signal_name in signal_points:
    # rename sub-mm samples to match sample names
    signal_name = signal_name.replace('.', 'p')
    print "\nCalculating limits for " + signal_name

    expected_dir = "{}/{}_expected".format(output_dir, signal_name)
    try:
        os.chdir(expected_dir)
    except OSError:
        print expected_dir + " does not exist; skipping."
        continue

    # build set of commands to merge input, calculate limits, and merge output
    commands = []
    commands.append("hadd -f grid.root higgsCombine.{}*.root".format(signal_name))
    datacard_name = "datacard_{}.txt".format(signal_name)
    for q in quantiles:
        commands.append(combine_template.format(datacard=datacard_name, quantile=q))
    commands.append("hadd -f merged.root higgsCombineTest.*quant0*.root")

    # run commands
    if arguments.batchMode:
        # prepare inputs
        link_tarball(tarball_name)
        inputs = [combine_executable, tarball_name, datacard_name]
        inputs.extend(glob.glob("higgsCombine.{}*.root".format(signal_name)))
        name = "condor_calculateLimits"
        # launch condor jobs
        output_condor(name, commands, inputs)
        os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit "+name+".sub")
    else:
        for command in commands:
            subprocess.call(command, shell=True)

    os.chdir("../../../")

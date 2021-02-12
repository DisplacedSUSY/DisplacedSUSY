#!/usr/bin/env python

import os
import shutil
import glob
import subprocess
from DisplacedSUSY.Configuration.limitOptions import *
from ROOT import TFile

if arguments.inputDir:
    input_dir = "limits/" + arguments.inputDir
    if not os.path.exists(input_dir):
        raise RuntimeError("Could not find input directory: " + input_dir)
else:
    raise RuntimeError("No input directory specified")

if arguments.condorDir:
    output_dir = "limits/" + arguments.condorDir
    if not os.path.exists(output_dir):
        os.system("mkdir " + output_dir)
else:
    raise RuntimeError("No output directory specified")

if arguments.add and arguments.rerun:
    raise RuntimeError("Cannot apply --add and --rerun flags simultaneously")

def output_condor(name, options, inputs, toys):
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
    script += "combine "+options+"\n"
    script_name = "condor_{}.sh".format(name)
    with open(script_name, "w") as f:
        f.write(script)
    os.chmod(script_name, 0775)

    command = "{}/{}".format(os.getcwd(), script_name)
    input_list = ", ".join(inputs)
    sub_file = ""
    sub_file += "Executable              = "+command+"\n"
    sub_file += "Universe                = vanilla\n"
    sub_file += "Getenv                  = True\n"
    sub_file += "request_memory          = "+str(int(3*toys))+"MB\n" # empirically determined
    sub_file += "Should_Transfer_Files   = YES\n"
    sub_file += "Transfer_Input_Files    = "+input_list+"\n"
    sub_file += "\n"
    sub_file += "Output                  = condor_{}.out\n".format(name)
    sub_file += "Error                   = condor_{}.err\n".format(name)
    sub_file += "Log                     = condor_{}.log\n".format(name)
    sub_file += "\n"
    sub_file += "+IsLocalJob             = true\n"
    sub_file += "Rank                    = TARGET.IsLocalSlot\n"
    sub_file += "\n"
    sub_file += "Queue 1\n"
    with open("condor_{}.sub".format(name), "w") as f:
        f.write (sub_file)

def ceil_div(a, b):
    if a/b == float(a)/float(b):
        return a/b
    else:
        return int(float(a)/float(b)) + 1

def first_half(l):
    return l[:ceil_div(len(l), 2)]

def get_asymptotic_limits(in_dir, signal_point):
    file_name_template = "{0}/{1}_expected/higgsCombine{1}.AsymptoticLimits.mH120.root"
    file_name = file_name_template.format(in_dir, signal_point)
    try:
        f = TFile(file_name)
        limit_tree = f.Get('limit').Clone()
        limit_tree.SetDirectory(0)
        f.Close()
    except ReferenceError:
        return False

    limits = {q : None for q in (0.025, 0.160, 0.500, 0.840, 0.975)}
    for i in range(limit_tree.GetEntries()):
        limit_tree.GetEntry(i)
        quantile = round(limit_tree.quantileExpected, 3)
        limits[quantile] = limit_tree.limit

    # check that combine results exist and are at least vaguely reasonable
    if not all(limits.values()):
        return False
    if not (limits[0.025] < limits[0.500] < limits[0.975]):
        return False

    return limits

# use expected asymptotic results to determine set of r-values to use for a particular signal point
def get_r_vals(limits, n_points, lower_half):
    # set r range from approximately -3 to +2 sigma around asymptotic mean because, empirically,
    # hybridNew r-values tend to be slightly lower and more toys are needed for the lower quantiles
    n_points = int(n_points)
    r_min = max(0.0001, limits[0.025] - (limits[0.500] - limits[0.025])/2.)
    r_max = limits[0.975]
    step = (r_max - r_min) / (n_points - 1)
    r_vals = [r_min + step*n for n in range(n_points)]

    # round to 3 sig figs
    r_vals = [float("{:.3g}".format(r)) for r in r_vals]

    # discard upper half of r values if user wants to build up toys for lower quantiles
    r_vals = r_vals if not lower_half else first_half(r_vals)

    return r_vals

def set_toys(toys, near_curve):
    if arguments.toys > 0:
        return arguments.toys
    # default to 2000 toys in region near limit curve and 500 toys elsewhere
    else:
        return 2000 if near_curve else 500

def check_log(log_file):
    with open(log_file, 'r') as f:
        return "Normal termination (return value 0)" in f.read()

def link_tarball(tarball_name):
    try:
        os.symlink("../" + tarball_name, tarball_name)
    except OSError as e:
        # suppress exception if symlink already exists
        if e.errno != 17:
            raise RuntimeError("Something is wrong with the cmssw tarball symlink")

####################################################################################################

options_template = ("{datacard} -M HybridNew --LHCmode LHC-limits --fork 4 --clsAcc 0 -s -1 "
                    "--saveHybridResult --singlePoint {r} --rMax {r_max} -n {name} -T {toys}")

# make cmssw tarball for condor
os.system('tar -zc --exclude="*git*" --exclude="test" --exclude="tmp" -C $CMSSW_BASE/../ '
          '-f {}/$CMSSW_VERSION.tar.gz $CMSSW_VERSION'.format(output_dir))

# prepare common inputs
combine_executable = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE)
combine_executable = combine_executable.communicate()[0].rstrip()
tarball_name = os.environ["CMSSW_VERSION"] + ".tar.gz"

for signal_name in signal_points:
    # rename sub-mm samples to match sample names
    signal_name = signal_name.replace('.', 'p')

    # set up output directory
    expected_dir = "{}/{}_expected".format(output_dir, signal_name)
    # handle cases where directory doesn't yet exist
    if not os.path.exists(expected_dir):
        if arguments.rerun:
            continue
        else:
            os.mkdir(expected_dir)
            first_ix = 0
    # handle cases where directory already exists
    else:
        print expected_dir + " already exists"

        # skip existing points when not in rerun or add mode
        if not arguments.rerun and not arguments.add:
            print "skipping"
            continue

        # check existing log files
        previous_logs = glob.glob(expected_dir + "/condor_[0-9]*.log")
        successful_logs = filter(check_log, previous_logs)
        failed_logs = [l for l in previous_logs if l not in successful_logs]
        log_labels = [name.split(".")[0].split("_")[-1] for name in previous_logs]
        last_ix = max(int(l) for l in log_labels if l.isdigit())
        print "contains {} successes and {} failures".format(len(successful_logs), len(failed_logs))

        if arguments.add:
            print "running w/o removing previous results to add more toys and/or r values"
            first_ix = last_ix + 1
        elif arguments.rerun:
            # skip points without failues
            if not failed_logs:
                print "skipping"
                continue
            # when all previous jobs have failed, just start fresh
            elif not successful_logs:
                print "recreating directory and starting over"
                shutil.rmtree(expected_dir, True)
                os.mkdir(expected_dir)
                first_ix = 0
            # when failures and successes coexist, remove failures and launch new jobs
            # fixme: check that this doesn't harm currently running jobs
            else:
                for log in failed_logs:
                    os.remove(log)
                first_ix = last_ix + 1

    # get asymptotic limits
    limits = get_asymptotic_limits(input_dir, signal_name)
    if not limits:
        print "Couldn't read input combine results for {}; skipping.".format(signal_name)
        continue

    # check if signal point is near expected limit curve
    datacard_name = "datacard_{}.txt".format(signal_name)
    datacard_path = "{}/{}_expected/{}".format(input_dir, signal_name, datacard_name)
    if not os.path.isfile(datacard_path):
        print "Can't find input datacard for {}; skipping.". format(signal_name)
        continue
    sf_file_path = datacard_path.replace('.txt', '.sf')
    try:
        with open(sf_file_path) as sf_file:
            sf = float(sf_file.readline().rstrip())
    except IOError:
        print "No input signal SF found. Defaulting to 1"
        sf = 1.0
    true_r = sf * limits[0.500]
    near_curve = 0.1 < true_r < 10
    if arguments.nearCurveOnly and not near_curve:
        print "{} too far from limit curve; skipping".format(signal_name)
        continue

    # copy over scaled datacard and scale-factor file
    shutil.copy(datacard_path, expected_dir)
    shutil.copy(sf_file_path, expected_dir)

    # run one job for each r value
    os.chdir(expected_dir)
    link_tarball(tarball_name)
    toys = set_toys(arguments.toys, near_curve)
    inputs = [combine_executable, tarball_name, datacard_name]
    r_vals = get_r_vals(limits, arguments.nPoints, arguments.lowerHalf)
    for ix, r in enumerate(r_vals):
        output_name = ".{}.{}".format(signal_name, r)
        options = options_template.format(datacard=datacard_name, r=r, r_max=2*r, name=output_name,
                                          toys = toys)
        print "combine " + options
        current_ix = first_ix + ix
        output_condor(current_ix, options, inputs, toys)
        os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH "
                  "condor_submit condor_{}.sub".format(current_ix))

    os.chdir("../../../")

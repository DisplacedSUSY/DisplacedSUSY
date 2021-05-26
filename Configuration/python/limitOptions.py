import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDir", dest="condorDir",
                  help="condor working directory")
parser.add_option("-E", "--era", dest="era", default="",
                  help="data-taking era for which to create cards")
parser.add_option("-M", "--method", dest="method", default="AsymptoticLimits",
                  help="which method of combine to use")
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                  help="run on the condor queue")
parser.add_option("-s", "--scaleSignalRate", dest="maxSignalRate", default="-1",
                  help="scale all signal rates so the maximum is MAXSIGNALRATE, default = -1; negative values turn off scaling")
parser.add_option("-e", "--expectedOnly", action="store_true", dest="expectedOnly", default=False,
                  help="only run expected limits (skip observed)")
parser.add_option("-q", "--quick", action="store_true", dest="quick", default=False,
                  help="run only a single sample, for testing")
parser.add_option("--separateFileQuantiles", action="store_true", dest="separateFileQuantiles", default=False,
                  help="Fetch quantiles from separate root files")
parser.add_option("-i", "--inputDir", dest="inputDir", default=None,
                  help="input directory containing asymptotic results to guide grid production")
parser.add_option("-n", "--nPoints", dest="nPoints", default=5,
                  help="number of r values to use when producing grid")
parser.add_option("-r", "--rerun", action="store_true", dest="rerun", default=False,
                  help="rerun signal points that already have an output directory")
parser.add_option("-a", "--add", action="store_true", dest="add", default=False,
                  help="run more toys and/or r-values in already existant output directories")
parser.add_option("-t", "--toys", dest="toys", default=-1,
                  help="number of toys to run for each r value. default is 2000 near limit curve and 500 otherwise")
parser.add_option("--lowerHalf", action="store_true", dest="lowerHalf", default=False,
                  help="only run jobs for lower half of r values, generally used to build up toys for lower uncertainty bands")
parser.add_option("--nearCurveOnly", action="store_true", dest="nearCurveOnly", default=False,
                  help="only run signal points w/ 0.1 < asymptotic expected r < 10")
parser.add_option("--doBR", action="store_true", dest="doBR", default=False,
                  help="make 1D branching ratio limit plots")
parser.add_option("--mm", action="store_true", dest="mm", default=False,
                  help="make limit plots vs ctau in mm rather than cm")
parser.add_option("--ns", action="store_true", dest="ns", default=False,
                  help="make limit plots vs lifetime in ns rather than ctau in cm")
parser.add_option("--fillGaps", action="store_true", dest="fillGaps", default=False,
                  help="plot expected limit value for points where observed has not converged")

(arguments, args) = parser.parse_args()

validEras = [
    "2016",
    "2017",
    "2018",
    "2017_18",
    "run2",
]

datacardCombinations = {
    '2017_18' : [
        '2017',
        '2018',
    ],
    'run2' : [
        '2016',
        '2017',
        '2018',
    ],
}

#stops
processes = [
   'stopToLB',
   #'stopToLD',
]
masses = [m for m in range(100, 1801, 100)]
#lifetimes = [10**e for e in range(-1, 5)] #just major decades
lifetimes = [b*10**e for e in range(-1, 4) for b in range(1, 10)] + [10000] #all lifetimes
signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]


# gmsb
#processes = ['sleptons']
#processes = ['gmsb']
#masses = [50] + [m for m in range(100, 1001, 100)]
#lifetimes = [b*10**e for e in range(-1, 4) for b in range(1, 10)] + [10000] #all lifetimes
#signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]

#processes = ['staus']
#masses = [m for m in range(100, 501, 100)]
#lifetimes = [b*10**e for e in range(-1, 3) for b in range(1, 10)] + [1000]  #all lifetimes
#signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]



#processes = ['HToSSTo4L']
#massesH = ["125","300","400","600","800","1000"]
#massesS = []#minimum list of S masses that exist for every H mass
#lifetimes = [b*10**e for e in range(0, 4) for b in range(1, 10)] + [10000] #all lifetimes
#signal_points = ["{}{}_{}_{}mm".format(p, mH, mS, l) for p in processes for mH in massesH for mS in massesS for l in lifetimes]
#for mH in massesH:
#  if int(mH)==125:
#    for ctau in lifetimes:
#      signal_points.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
#  elif int(mH)==300:
#    for ctau in lifetimes:
#      signal_points.append("HToSSTo4L"+mH+"_20_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#  elif int(mH)==400:
#    for ctau in lifetimes:
#      signal_points.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#  elif int(mH)==600:
#    for ctau in lifetimes:
#      signal_points.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#  elif int(mH)==800:
#    for ctau in lifetimes:
#      signal_points.append("HToSSTo4L"+mH+"_50_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_250_"+str(ctau)+"mm")
#  elif int(mH)==1000:
#    for ctau in lifetimes:
#      #signal_points.append("HToSSTo4L"+mH+"_30_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_150_"+str(ctau)+"mm")
#      signal_points.append("HToSSTo4L"+mH+"_350_"+str(ctau)+"mm")
#signal_points = [lt.replace(".", "p") for lt in signal_points]

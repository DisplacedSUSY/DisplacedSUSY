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
parser.add_option("-e", "--expectedOnly", action="store_true", dest="expectedOnly", default=False,
                                    help="only run expected limits (skip observed)")
parser.add_option("-q", "--quick", action="store_true", dest="quick", default=False,
                  help="run only a single sample, for testing")

(arguments, args) = parser.parse_args()

validEras = ["2016",
             "2017",
             "2018",
             "run2"]

datacardCombinations = {
    'run2' : ['2016',
              '2017',
              '2018'],
}

processes = ['stopToLB']
masses = [m for m in range(100, 1801, 100)]
lifetimes = [10**e for e in range(-2, 5)]
#lifetimes = [b*10**e for e in range(-2, 5) for b in range(1, 10)] + [10000]
signal_points = ["{}{}_{}mm".format(p, m, l) for p in processes for m in masses for l in lifetimes]
#signal_points = [
#        'HTo4Mu125_50_50mm',
#        'HTo4Mu125_50_500mm',
#        'HTo4Mu125_50_5000mm',
#        'HTo4Mu125_20_13mm',
#        'HTo4Mu125_20_130mm',
#        'HTo4Mu125_20_1300mm',
#]

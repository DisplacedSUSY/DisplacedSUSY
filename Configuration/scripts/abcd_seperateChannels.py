#!/usr/bin/env python

import sys
import os
import re
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TH1F, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-c", "--doClosureTest", action="store_true", dest="doClosureTest",
                  default=False, help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)

if arguments.condorDir:
    output_path = "condor/" + arguments.condorDir + "/"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
else:
    print "you forgot to specify a condor directory with -w"
    sys.exit(1)

for sample in samples:
    yields = {}
    errors = {}
    in_file = TFile(output_path + sample + ".root")

    # get yields and statistical uncertainties for all channels
    for region, channel in channels.iteritems():
        # use numPV plot b/c it is filled once per event
        in_hist = in_file.Get(channel + "Plotter/Eventvariable Plots/numPV")
        if not in_hist:
            print "Warning: did not find input hist " + channel + "Plotter/Eventvariable Plots/numPV"
        error = Double(0.0)
        events = in_hist.IntegralAndError(0, in_hist.GetNbinsX()+1, error)
        yields[region] = events
        errors[region] = error

    # estimate yield as d = c * b / a
    if yields['b'] == 0 or yields['c'] == 0:
        abcd_yield = abcd_error = 0
        ratio = ratio_error = 0
    else:
        cb_yield, cb_error = propagateError("product", yields['c'], errors['c'],
                                            yields['b'], errors['b'])
        abcd_yield, abcd_error = propagateError("quotient", cb_yield, cb_error,
                                                yields['a'], errors['a'])
        ratio, ratio_error = propagateError("quotient", abcd_yield, abcd_error,
                                                yields['d'], errors['d'])

    print sample
    print 'estimate: {:.3g} +- {:.3g}'.format(abcd_yield, abcd_error)
    print 'counting: {:.3g} +- {:.3g}'.format(yields['d'], errors['d'])
    print 'ratio: {:.3g} +- {:.3g}'.format(ratio, ratio_error)

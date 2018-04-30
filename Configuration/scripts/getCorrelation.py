#!/usr/bin/env python
import sys
import os
import re
from ROOT import TFile, TH2
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "you forgot to specify a config file with -l"
    sys.exit(1)


for i in inputs:
    in_file = TFile(i["file"])
    print
    print i["file"]

    for h in i["hists"]:
        hist = in_file.Get(h).Clone()
        print h
        print round(hist.GetCorrelationFactor(), 3)


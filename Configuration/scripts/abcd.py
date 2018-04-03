#!/usr/bin/env python
import sys
import os
import re
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from array import array
from optparse import OptionParser
from ROOT import TFile, TCanvas, TH2F, gROOT, Double

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")

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


def get_yields_and_errors(h, x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi):
    error = Double(0.0)
    integral = h.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, error)
    return (integral, error)


gROOT.SetBatch()
e_yields_and_errors = {}
mu_yields_and_errors = {}

in_file = TFile(input_file)
e_hist  = in_file.Get(electron_hist).Clone()
mu_hist = in_file.Get(muon_hist).Clone()

# get electron sideband yields and errors
for edge_low, edge_high in zip(bin_edges_e[:-1], bin_edges_e[1:]):
    e_yields_and_errors[edge_low] = get_yields_and_errors(
                            e_hist,
                            0,
                            e_hist.GetXaxis().FindBin(bin_edges_mu[1])-1,
                            e_hist.GetYaxis().FindBin(edge_low),
                            e_hist.GetYaxis().FindBin(edge_high)-1 )

# get muon sideband yields and errors
for edge_low, edge_high in zip(bin_edges_mu[:-1], bin_edges_mu[1:]):
    mu_yields_and_errors[edge_low] = get_yields_and_errors(
                            mu_hist,
                            mu_hist.GetXaxis().FindBin(edge_low),
                            mu_hist.GetXaxis().FindBin(edge_high)-1,
                            0,
                            mu_hist.GetYaxis().FindBin(bin_edges_e[1])-1 )

out_hist = TH2F(out_hist, out_hist,len(bin_edges_mu)-1, array('d',bin_edges_mu),
                len(bin_edges_e)-1, array('d',bin_edges_e))

# get yield in prompt region
if e_yields_and_errors[bin_edges_e[0]] is not mu_yields_and_errors[bin_edges_mu[0]]:
    print "e and mu sideband yields don't match in 'a' (prompt) region"
    print "using e yield in 'a' region, but you should make sure this is expected"
(a_yield, a_error) = e_yields_and_errors[bin_edges_e[0]]

# fill TH2 using abcd method
for e_d0, (e_yield, e_error) in e_yields_and_errors.iteritems():
    for mu_d0, (mu_yield, mu_error) in mu_yields_and_errors.iteritems():
        bin_num = out_hist.FindBin(mu_d0, e_d0)

        if mu_d0 is bin_edges_mu[0] and e_d0 is bin_edges_e[0]: # prompt region; use input yield
            yield_temp = a_yield
            error_temp = a_error
        elif e_d0 is bin_edges_e[0]: # muon sideband; use input yield
            yield_temp = mu_yield
            error_temp = mu_error
        elif mu_d0 is bin_edges_mu[0]: # electron sideband; use input yield
            yield_temp = e_yield
            error_temp = e_error
        else: # signal region; use d = c*b/a
            (cb_yield, cb_error) = propagateError("product", mu_yield, mu_error,
                                                    e_yield, e_error)
            (yield_temp, error_temp) = propagateError("quotient", cb_yield, cb_error,
                                                      a_yield, a_error)

        out_hist.SetBinContent(bin_num, yield_temp)
        out_hist.SetBinError(bin_num, error_temp)

out_file = TFile(output_path + out_file, "recreate")
out_hist.SetOption("colz texte")
out_hist.GetXaxis().SetTitle("muon |d0| [cm]")
out_hist.GetYaxis().SetTitle("electron |d0| [cm]")
out_hist.Draw()
out_hist.Write()
out_file.Close()

#!/usr/bin/env python

# Given a 2D histogram and a set of x and y bin edges, this script will estimate
# the number of events in the given target regions using an abcd method.
#
# usage: abcd_from2dHist.py -l CONFIG -w CONDOR_DIR
# sample config: EEChannel/test/abcd_from2dHist_cfg.py

import sys
import os
import re
import copy
import json
import itertools
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, TH1D, TH2D, TH3D, gROOT, Double, gStyle

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-c", "--doClosureTest", action="store_true", dest="doClosureTest", default=False,
                  help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")
parser.add_option("-t", "--makeTables", action="store_true", dest="makeTables", default=False,
                  help="print table of abcd and counting yields; table is formatted for elog")

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


gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('.2f')
gROOT.ForceStyle()


# fixme: what about overflow?
def get_th2(th3, z_lo, z_hi, variable_bins):
    z_bin_lo = th3.GetZaxis().FindBin(z_lo)
    z_bin_hi = th3.GetZaxis().FindBin(z_hi)-1
    th3.GetZaxis().SetRange(z_bin_lo, z_bin_hi)
    th2 = th3.Project3D("xy")
    if variable_bins: # scale events and eror to account for bin size in z
        nBins = th3.GetZaxis().GetNbins()
        th2.Scale(th3.GetZaxis().GetBinWidth(nBins))
    return th2

def get_poisson_uncertainty(counts):
    dummy_hist = TH1D("dummy", "dummy", 1, 0, 1)
    dummy_hist.SetBinErrorOption(1) # one-sigma poisson interval
    dummy_hist.SetBinContent(1, counts)
    return (dummy_hist.GetBinErrorLow(1), dummy_hist.GetBinErrorUp(1))

def get_yields_and_errors(h, x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, variable_bins, data):
    err = Double(0.0)
    integral = h.IntegralAndError(x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi, err)
    # multiply by area of last bin if histogram was made with variable-width bins
    # assume input histograms have symmetric binning
    if variable_bins:
        nBins = h.GetXaxis().GetNbins()
        area = h.GetXaxis().GetBinWidth(nBins) ** 2
        integral *= area
        err *= area
    # replace normal approxmation uncertainty with poisson uncertainty for unweighted hists
    (err_lo, err_hi) = get_poisson_uncertainty(integral) if data else (err, err)
    return {'val':integral, 'err_lo':err_lo, 'err_hi':err_hi}

# separately propagate lo and hi uncertaintanties
def propagate_asymm_err(func, a, a_err_lo, a_err_hi, b, b_err_lo, b_err_hi):
    (result, err_lo) = propagateError(func, a, a_err_lo, b, b_err_lo)
    (result, err_hi) = propagateError(func, a, a_err_hi, b, b_err_hi)
    return {'val':result, 'err_lo':err_lo, 'err_hi':err_hi}

# sum events from different regions while accounting for asymmetric uncertainties
def sum_regions(r1, r2):
    return propagate_asymm_err("sum", r1['val'], r1['err_lo'], r1['err_hi'],
                                      r2['val'], r2['err_lo'], r2['err_hi'])


out_file = TFile(output_path + output_file, "recreate")
in_file = TFile(input_file)
in_hist = in_file.Get(input_hist).Clone()

if type(in_hist) is TH2D and len(bins_z) != 2:
    print
    print "The input hist is a TH2, but you are trying to bin in pT."
    print "Please define 'z_bins' to correspond to the full selection pT range."
    print
    sys.exit(1)

abcd_yields = {}
count_yields = {}
bg_estimate_output = {'background' : []} # strange structure to match makeDataCards expectation

regions = lambda bins: zip(bins[:-1], bins[1:])
x_regions = regions(bins_x)
y_regions = regions(bins_y)
z_regions = regions(bins_z)

for z_lo, z_hi in z_regions:
    abcd_yields[z_lo]  = {}
    count_yields[z_lo] = {}

    if type(in_hist) is TH3D:
        print "input hist is th3; converting to th2..."
        in_th2 = get_th2(in_hist, z_lo, z_hi, variable_bins)
    else:
        in_th2 = in_hist

    title = lambda x: output_file.replace(".root", "{} {}GeV".format(x, z_lo))
    abcd_hist  = TH2D(title("ABCD Estimates"), title("ABCD Estimates"), len(bins_x)-1,
                      array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
    count_hist = TH2D(title("Counting Yields"), title("Counting Yields"), len(bins_x)-1,
                      array('d',bins_x), len(bins_y)-1, array('d',bins_y) )
    ratio_hist  = TH2D(title("Ratio"), title("Ratio"),  len(bins_x)-1,
                      array('d',bins_x), len(bins_y)-1, array('d',bins_y) )

    # Get yield and error in prompt region
    prompt_bin_x_lo = in_th2.GetXaxis().FindBin(bins_x[0])
    prompt_bin_x_hi = in_th2.GetXaxis().FindBin(bins_x[1])-1
    prompt_bin_y_lo = in_th2.GetYaxis().FindBin(bins_y[0])
    prompt_bin_y_hi = in_th2.GetYaxis().FindBin(bins_y[1])-1

    prompt = get_yields_and_errors(in_th2, prompt_bin_x_lo, prompt_bin_x_hi, prompt_bin_y_lo,
                                   prompt_bin_y_hi, variable_bins, data)

    if arguments.makeTables:
        print
        if not arguments.doClosureTest:
            print "Blinded: actual yields set equal to estimate."
        print "[B]", title(""), "[/B]"
        print '[TABLE border="1"]'
        print "mu d0 range (#mum)|e d0 range (#mum)|A|B|C|D Estimate|D Actual|D Actual/Estimate"

    for (x_lo, x_hi), (y_lo, y_hi) in itertools.product(x_regions[1:], y_regions[1:]):
        if not x_lo in abcd_yields[z_lo]:
            abcd_yields[z_lo][x_lo]  = {}
            count_yields[z_lo][x_lo] = {}
        abcd_yields[z_lo][x_lo][y_lo]  = {}
        count_yields[z_lo][x_lo][y_lo] = {}

        x_bin_lo = in_th2.GetXaxis().FindBin(x_lo)
        x_bin_hi = in_th2.GetXaxis().FindBin(x_hi)-1
        y_bin_lo = in_th2.GetYaxis().FindBin(y_lo)
        y_bin_hi = in_th2.GetYaxis().FindBin(y_hi)-1
        out_bin = count_hist.FindBin(x_lo, y_lo)

        # Get yield and error in x sideband
        x = get_yields_and_errors(in_th2, x_bin_lo, x_bin_hi, prompt_bin_y_lo, prompt_bin_y_hi,
                                  variable_bins, data)

        # Get yield and error in y sideband
        y = get_yields_and_errors(in_th2, prompt_bin_x_lo, prompt_bin_x_hi, y_bin_lo, y_bin_hi,
                                  variable_bins, data)

        # calculate abcd yield as d = c * b / a
        if x['val'] == 0 or y['val'] == 0:
            abcd['val'] = 0
            abcd['err_lo'] = abcd['err_hi'] = 0
        else:
            cb = propagate_asymm_err("product", x['val'], x['err_lo'], x['err_hi'],
                                                y['val'], y['err_lo'], y['err_hi'])
            abcd = propagate_asymm_err("quotient", cb['val'], cb['err_lo'], cb['err_hi'],
                                       prompt['val'], prompt['err_lo'], prompt['err_hi'])

        # store abcd estimate in hist and dictionary
        abcd_hist.SetBinContent(out_bin, abcd['val'])
        # set error to larger of err_lo and err_hi
        larger_abcd_err = abcd['err_lo'] if abcd['err_lo'] > abcd['err_hi'] else abcd['err_hi']
        abcd_hist.SetBinError(out_bin, larger_abcd_err)

        abcd_yields[z_lo][x_lo][y_lo]['val']  = abcd['val']
        abcd_yields[z_lo][x_lo][y_lo]['err_lo'] = abcd['err_lo']
        abcd_yields[z_lo][x_lo][y_lo]['err_hi'] = abcd['err_hi']

        # if unblinded, get count yields
        if arguments.doClosureTest:
            count = get_yields_and_errors(in_th2, x_bin_lo, x_bin_hi, y_bin_lo, y_bin_hi,
                                          variable_bins, data)

        else: # if blinded, set count yields equal to abcd estimate
            count = copy.deepcopy(abcd)

        # store actual yield in hist and dictionary
        count_hist.SetBinContent(out_bin, count['val'])
        # set error to larger of err_lo and err_hi
        larger_count_err = count['err_lo'] if count['err_lo'] > count['err_hi'] else count['err_hi']
        count_hist.SetBinError(out_bin, larger_count_err)

        count_yields[z_lo][x_lo][y_lo]['val']  = count['val']
        count_yields[z_lo][x_lo][y_lo]['err_lo'] = count['err_lo']
        count_yields[z_lo][x_lo][y_lo]['err_hi'] = count['err_hi']

        # calculate ratio of actual yield to estimate
        if abcd['val'] == 0:
            print "estimate is 0, setting ratio to 100 +/- 100"
            ratio['val'] = 100
            ratio['err_lo'] = ratio['err_hi'] = 100
        elif count['val'] == 0:
            print "count_yield is 0, setting ratio uncertainty to 100"
            ratio['val'] = 1.*count['val']/abcd['val']
            ratio['lo'] = 0
            ratio['hi'] = 100
        else:
            ratio = propagate_asymm_err("quotient", count['val'], count['err_lo'], count['err_hi'],
                                        abcd['val'], abcd['err_lo'], abcd['err_hi'])

        ratio_hist.SetBinContent(out_bin, ratio['val'])
        # set error to larger of err_lo and err_hi
        larger_ratio_err = ratio['err_lo'] if ratio['err_lo'] > ratio['err_hi'] else ratio['err_hi']
        ratio_hist.SetBinError(out_bin, larger_ratio_err)

        if arguments.makeTables:
            print "|-"
            if data: # use asymmetric errors on estimate and no uncertainty on actual count
                format_string = ("{:d}-{:d} | {:d}-{:d}" + 3 * " | {:.0f}" +
                                 " | {:.2f}+{:.2f}-{:.2f} | {:.0f} | {:.2f}+{:.2f}-{:.2f}")
                print format_string.format(x_lo, x_hi, y_lo, y_hi, prompt['val'], x['val'],
                                           y['val'], abcd['val'], abcd['err_hi'], abcd['err_lo'],
                                           count['val'], ratio['val'], ratio['err_hi'], ratio['err_lo'])
            else: # use normal errors on estimate and actual count
                format_string = ("{:d}-{:d} | {:d}-{:d}" + 3 * " | {:.0f}" +
                                 2 * " | {:.2f}+-{:.2f}" + " | {:.2f}+-{:.2f}")
                print format_string.format(x_lo, x_hi, y_lo, y_hi, prompt['val'], x['val'],
                                           y['val'], abcd['val'], abcd['err_hi'], count['val'],
                                           count['err_hi'], ratio['val'], ratio['val'], ratio['err_hi'])

    # finish table
    if arguments.makeTables:
        print "[/TABLE]"
        print

    # get estimated and actual yields in L-shaped signal regions
    if len(bins_x) != len(bins_y):
        print
        print "Not making L-shaped signal regions because x and y have different numbers of bins"
    else:
        # begin summary table
        if arguments.makeTables:
            print "[B]", title(" summary"), "[/B]"
            print '[TABLE border="1"]'
            print "Signal Region|Estimate|Actual"

        for sr in range(0, len(bins_x)-2):
            sr_count = {'val':0, 'err_lo':0, 'err_hi':0}
            sr_abcd  = {'val':0, 'err_lo':0, 'err_hi':0}
            for x_lo in bins_x[sr+1:-1]:
                y_lo = bins_y[sr+1]
                sr_count = sum_regions(sr_count, count_yields[z_lo][x_lo][y_lo])
                sr_abcd = sum_regions(sr_abcd, abcd_yields[z_lo][x_lo][y_lo])
            for y_lo in bins_y[sr+2:-1]: # +2 to not double count corner of L
                x_lo = bins_x[sr+1]
                sr_count = sum_regions(sr_count, count_yields[z_lo][x_lo][y_lo])
                sr_abcd = sum_regions(sr_abcd, abcd_yields[z_lo][x_lo][y_lo])

            # print summary table row
            if arguments.makeTables:
                print "|-"
                if data:
                    print "Region {} | {:.2f}+{:.2f}-{:.2f} | {:.0f}".format(
                           sr, sr_abcd['val'], sr_abcd['err_hi'], sr_abcd['err_lo'], sr_count['val'])
                else:
                    print "Region {} | {:.2f}+-{:.2f} | {:.2f}+-{:.2f}".format(
                           sr, sr_abcd['val'], sr_abcd['err_hi'], sr_count['val'], sr_abcd['err_hi'])

            # store estimated and actual yields with signal region info for json output
            bg_estimate_output['background'].append(
                {
                    'pt'   : (z_lo, z_hi),
                    'd0_0' : (bins_x[sr+1], bins_x[sr+2]),
                    'd0_1' : (bins_y[sr+1], bins_y[sr+2]),
                    'd0_max' : bins_x[-1], # assume symmetric max d0 values
                    'estimate' : sr_abcd['val'],
                    # store uncertainties as multiplicative factors for makeDataCards
                    'err_lo' : (sr_abcd['val'] - sr_abcd['err_lo']) / sr_abcd['val'],
                    'err_hi' : (sr_abcd['val'] + sr_abcd['err_hi']) / sr_abcd['val'],
                    'sys_err_lo' : 1 - systematic_uncertainty,
                    'sys_err_hi' : 1 + systematic_uncertainty,
                }
            )

        # end summary table
        if arguments.makeTables:
            print "[/TABLE]"
            print

    # Format and export histograms
    out_file.cd()

    abcd_hist.SetMarkerSize(2)
    abcd_hist.SetOption("colz text45 e")
    abcd_hist.GetXaxis().SetTitle(x_axis_title)
    abcd_hist.GetYaxis().SetTitle(y_axis_title)
    abcd_hist.GetXaxis().SetTitleOffset(1.2)
    abcd_hist.GetYaxis().SetTitleOffset(1.1)
    abcd_hist.Write()
    CanvasAbcd = TCanvas("CanvasAbcd"+str(z_lo), "CanvasAbcd"+str(z_lo), 100, 100, 700, 600)
    #CanvasAbcd.SetLogx()
    #CanvasAbcd.SetLogy()
    CanvasAbcd.SetLogz()
    CanvasAbcd.cd()

    abcd_hist.Draw("colz text45 e")
    CanvasAbcd.SaveAs(output_path+output_file.replace(".root", "_abcd.pdf"))
    CanvasAbcd.SaveAs(output_path+output_file.replace(".root", "_abcd.png"))

    if arguments.doClosureTest:
        count_hist.SetMarkerSize(2)
        count_hist.SetOption("colz text45 e")
        count_hist.GetXaxis().SetTitle(x_axis_title)
        count_hist.GetYaxis().SetTitle(y_axis_title)
        count_hist.GetXaxis().SetTitleOffset(1.2)
        count_hist.GetYaxis().SetTitleOffset(1.1)
        count_hist.Write()
        CanvasCount = TCanvas("CanvasCount"+str(z_lo), "CanvasCount"+str(z_lo), 100, 100, 700, 600)
        #CanvasCount.SetLogx()
        #CanvasCount.SetLogy()
        CanvasCount.SetLogz()
        CanvasCount.cd()
        count_hist.Draw("colz text45 e")
        CanvasCount.SaveAs(output_path+output_file.replace(".root", "_count.pdf"))
        CanvasCount.SaveAs(output_path+output_file.replace(".root", "_count.png"))

        ratio_hist.SetMarkerSize(2)
        ratio_hist.SetOption("colz text45 e")
        ratio_hist.GetXaxis().SetTitle(x_axis_title)
        ratio_hist.GetYaxis().SetTitle(y_axis_title)
        ratio_hist.GetXaxis().SetTitleOffset(1.2)
        ratio_hist.GetYaxis().SetTitleOffset(1.1)
        ratio_hist.SetMinimum(0)
        ratio_hist.SetMaximum(2)
        ratio_hist.Write()
        CanvasRatio = TCanvas("CanvasRatio"+str(z_lo), "CanvasRatio"+str(z_lo), 100, 100, 700, 600)
        #CanvasRatio.SetLogx()
        #CanvasRatio.SetLogy()
        CanvasRatio.cd()
        ratio_hist.Draw("colz text45 e")
        CanvasRatio.SaveAs(output_path+output_file.replace(".root", "_ratio.pdf"))
        CanvasRatio.SaveAs(output_path+output_file.replace(".root", "_ratio.png"))

out_file.Close()

# export estimates as json for limit setting
json_name = output_file.replace(".root", "_background_estimate.json")
output_estimates = open(output_path+json_name, "w")
json = json.dump(bg_estimate_output, output_estimates, sort_keys=True, indent=2)
print "Storing estimates in", output_path+json_name

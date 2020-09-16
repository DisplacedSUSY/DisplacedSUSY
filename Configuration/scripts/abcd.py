#!/usr/bin/env python

# Given a 2D or 3D histogram and a set of bin edges, this script will estimate the number of
# events in the given targets regions using an abcd method. When given a 3D hist, this script
# will perform the abcd estimate separately for each given z range.
#
# usage: abcd.py -l CONFIG -w CONDOR_DIR
# sample config: EEChannel/test/abcd.py

import sys
import os
import re
import copy
import json
import itertools
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TCanvas, TF1, TH1D, TH2D, TH3D, TGraphErrors, TGraphAsymmErrors, TVirtualFitter, gROOT, Double, gStyle

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-c", "--doClosureTest", action="store_true", dest="doClosureTest", default=False,
                  help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")
parser.add_option("-x", "--doExtrapolation", action="store_true", dest="doExtrapolation", default=False,
                  help="extrapolate closure tests to signal region; DON'T RUN OVER DATA IF BLINDED!")
parser.add_option("-T", "--makeTables", action="store_true", dest="makeTables", default=False,
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

#### deal with conflicting arguments
if arguments.doExtrapolation and not arguments.doClosureTest:
    print
    print "You have requested to extrapolate the closure tests without calling for the closure tests. This is a very strange request. Will skip doing the extrapolation."
    print
    arguments.doExtrapolation = False

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('.2f')
gROOT.ForceStyle()

# make output histogram with bins for each ABCD region
def make_output_hist(title, template_hist, x_bins, y_bins):
    #  include overflow in outermost bins if applicable
    x_edges = array('d', [template_hist.GetXaxis().GetXmax() if x == -1 else x for x in bins_x])
    y_edges = array('d', [template_hist.GetYaxis().GetXmax() if y == -1 else y for y in bins_y])

    return TH2D(title, title, len(x_bins)-1, x_edges, len(y_bins)-1, y_edges)

# get bin numbers associated with given values; account for possible overflow inclusion
def get_bins(hist, axis_name, lo, hi):
    if axis_name is "x":
        axis = hist.GetXaxis()
    elif axis_name is "y":
        axis = hist.GetYaxis()
    elif axis_name is "z":
        axis = hist.GetZaxis()
    else:
        print axis_name, "is not a recognized axis name. Try 'x', 'y', or 'z'."

    lo_bin = axis.FindBin(lo)
    if hi is -1:
        hi_bin = axis.GetNbins()+1
    else:
        hi_bin = axis.FindBin(hi)-1

    return (lo_bin, hi_bin)

def get_th2(th3, z_lo, z_hi, variable_bins):
    (z_bin_lo, z_bin_hi) = get_bins(th3, 'z', z_lo, z_hi)
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

def get_yields_and_errors(h, x_lo, x_hi, y_lo, y_hi, variable_bins, data):
    (x_bin_lo, x_bin_hi) = get_bins(h, "x", x_lo, x_hi)
    (y_bin_lo, y_bin_hi) = get_bins(h, "y", y_lo, y_hi)
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

def linear_extrapolation(pol1,nPoints,d0Points,ratios,d0_err_lo,d0_err_hi,ratio_err_lo,ratio_err_hi,extrapolatedD0Point):
    graph = TGraphAsymmErrors(nPoints, array('f',d0Points), array('f',ratios), array('f',d0_err_lo), array('f',d0_err_hi), array('f',ratio_err_lo), array('f',ratio_err_hi))
    if pol1 is True:
        fit = TF1("fit","pol1",0,extrapolatedD0Point)
        graph.Fit(fit,"R")
        print "pol1 chisq is: {:.2f}".format(fit.GetChisquare())
        print "pol1 y-intercept is: {:.2f}".format(fit.GetParameter(0))+" +/- {:.2f}".format(fit.GetParError(0))
        print "pol1 slope is: {:.2f}".format(fit.GetParameter(1))+" +/- {:.2f}".format(fit.GetParError(1))

    else:
        fit = TF1("fit","pol0")
        graph.Fit(fit)
        print "pol0 chisq is: {:.2f}".format(fit.GetChisquare())
        print "pol0 y-intercept is: {:.2f}".format(fit.GetParameter(0))+" +/- {:.2f}".format(fit.GetParError(0))

    grConfInt1Sig = TGraphErrors(graph.GetN()+1)
    for i in range(graph.GetN()):
        grConfInt1Sig.SetPoint(i, graph.GetX()[i], 0 )
    grConfInt1Sig.SetPoint(nPoints,extrapolatedD0Point, 0)
    grConfInt2Sig = grConfInt1Sig.Clone()

    #Compute the 68% and 95% confidence intervals at the x points of the created graph
    TVirtualFitter.GetFitter().GetConfidenceIntervals(grConfInt1Sig, 0.68)
    TVirtualFitter.GetFitter().GetConfidenceIntervals(grConfInt2Sig, 0.95)
    #Now the "grConfInt" graphs contains function values as its y-coordinates
    #and confidence intervals as the errors on these coordinates

    return (fit.Eval(extrapolatedD0Point),graph,grConfInt1Sig,grConfInt2Sig)



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

# perform abcd estimate separately for each region in z
for z_lo, z_hi in z_regions:
    abcd_yields[z_lo]  = {}
    count_yields[z_lo] = {}

    if type(in_hist) is TH3D:
        print "input hist is th3; converting to th2..."
        in_th2 = get_th2(in_hist, z_lo, z_hi, variable_bins)
    else:
        in_th2 = in_hist

    abcd_hist  = make_output_hist(str(z_lo)+"GeV ABCD Estimates",        in_th2, bins_x, bins_y)
    count_hist = make_output_hist(str(z_lo)+"GeV Counting Yields",       in_th2, bins_x, bins_y)
    ratio_hist = make_output_hist("", in_th2, bins_x, bins_y)

    prompt = get_yields_and_errors(in_th2, bins_x[0], bins_x[1], bins_y[0], bins_y[1],
                                   variable_bins, data)

    if arguments.doExtrapolation:
        ratios = []
        ratios_err_lo = []
        ratios_err_hi = []
        x_mids = []
        x_halfRanges = []
        y_mids = []
        y_halfRanges = []

    if arguments.makeTables:
        print
        if not arguments.doClosureTest:
            print "Blinded: actual yields set equal to estimate."
        print "[B]", output_file.replace(".root", ""), "[/B]"
        print '[TABLE border="1"]'
        print "mu d0 range (#mum)|e d0 range (#mum)|A|B|C|D Estimate|D Actual|D Actual/Estimate"

    # iterate through all target regions and perform abcd estimate
    for (x_lo, x_hi), (y_lo, y_hi) in itertools.product(x_regions[1:], y_regions[1:]):
        if not x_lo in abcd_yields[z_lo]:
            abcd_yields[z_lo][x_lo]  = {}
            count_yields[z_lo][x_lo] = {}
        abcd_yields[z_lo][x_lo][y_lo]  = {}
        count_yields[z_lo][x_lo][y_lo] = {}

        # Get yield and error in x and y sidebands
        x = get_yields_and_errors(in_th2, x_lo, x_hi, bins_y[0], bins_y[1], variable_bins, data)
        y = get_yields_and_errors(in_th2, bins_x[0], bins_x[1], y_lo, y_hi, variable_bins, data)

        # calculate abcd yield as d = c * b / a
        if x['val'] == 0 or y['val'] == 0:
            abcd['val'] = 0
            abcd['err_lo'] = abcd['err_hi'] = 0
        else:
            cb = propagate_asymm_err("product", x['val'], x['err_lo'], x['err_hi'],
                                                y['val'], y['err_lo'], y['err_hi'])
            abcd = propagate_asymm_err("quotient", cb['val'], cb['err_lo'], cb['err_hi'],
                                       prompt['val'], prompt['err_lo'], prompt['err_hi'])

        # get count yields if unblinded; otherwise, set count yields equal to estimate
        if arguments.doClosureTest:
            count = get_yields_and_errors(in_th2, x_lo, x_hi, y_lo, y_hi, variable_bins, data)
        else:
            count = copy.deepcopy(abcd)

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

        # store results in dictionaries
        abcd_yields[z_lo][x_lo][y_lo]['val']    = abcd['val']
        abcd_yields[z_lo][x_lo][y_lo]['err_lo'] = abcd['err_lo']
        abcd_yields[z_lo][x_lo][y_lo]['err_hi'] = abcd['err_hi']

        count_yields[z_lo][x_lo][y_lo]['val']    = count['val']
        count_yields[z_lo][x_lo][y_lo]['err_lo'] = count['err_lo']
        count_yields[z_lo][x_lo][y_lo]['err_hi'] = count['err_hi']

        # fill output hists
        out_bin = count_hist.FindBin(x_lo, y_lo)
        abcd_hist.SetBinContent(out_bin, abcd['val'])
        abcd_hist.SetBinError(out_bin, max(abcd['err_lo'], abcd['err_hi']))

        count_hist.SetBinContent(out_bin, count['val'])
        count_hist.SetBinError(out_bin, max(count['err_lo'], count['err_hi']))

        ratio_hist.SetBinContent(out_bin, ratio['val'])
        ratio_hist.SetBinError(out_bin, max(ratio['err_lo'], ratio['err_hi']))

        # fill arrays for extrapolation
        if arguments.doExtrapolation:
            ratios.append(float(ratio['val']))
            ratios_err_lo.append(float(ratio['err_lo']))
            ratios_err_hi.append(float(ratio['err_hi']))

            x_halfRange = 0.5*(x_hi-x_lo)
            x_mid = x_halfRange+x_lo
            x_halfRanges.append(float(x_halfRange))
            x_mids.append(float(x_mid))

            y_halfRange = 0.5*(y_hi-y_lo)
            y_mid = y_halfRange+y_lo
            y_halfRanges.append(float(y_halfRange))
            y_mids.append(float(y_mid))

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
                                       count['err_hi'], ratio['val'], ratio['err_hi'])

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
            print "[B]", output_file.replace(".root", " summary"), "[/B]"
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

    #do linear extrapolation to estimate systematic uncertainty
    if arguments.doExtrapolation:
        #find if x's or y's are changing: the ones that change are the d0 values we want
        d0_mids = array('f',[])
        d0_halfRanges = array('f',[])

        if x_mids.count(x_mid) > 1:
            d0_mids = y_mids
            d0_halfRanges = y_halfRanges
        elif y_mids.count(y_mid) > 1:
            d0_mids = x_mids
            d0_halfRanges = x_halfRanges
        else:
            print "problem with d0_mids"

        #extrapolate using the middle of each d0 bin as the d0 points
        extrapolatedD0Point = 300
        (ratioProj_start, graph_middle, grConfInt1Sig, grConfInt2Sig) = linear_extrapolation(pol1,len(ratios),d0_mids,ratios,d0_halfRanges,d0_halfRanges,ratios_err_lo,ratios_err_hi,extrapolatedD0Point)
        if pol1 is True:
            line = "line with slope "
        else:
            line = "horizontal line "
        print "The projected ratio is {:.2f}".format(ratioProj_start) + " +/- {:.2f}".format(grConfInt1Sig.GetErrorY(len(ratios))) +" when extrapolating with "+line+"at the start of the d0 bins to |d0|=" + str(extrapolatedD0Point)+ "um"
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

    if arguments.doExtrapolation:
        graph_middle.SetTitle("")
        grConfInt1Sig.SetTitle("")
        grConfInt2Sig.SetTitle("")
        graph_middle.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        graph_middle.GetYaxis().SetTitle("Actual/estimate ratios")
        grConfInt1Sig.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        grConfInt1Sig.GetYaxis().SetTitle("Actual/estimate ratios")
        grConfInt2Sig.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        grConfInt2Sig.GetYaxis().SetTitle("Actual/estimate ratios")
        graph_middle.GetXaxis().SetTitleOffset(1.2)
        graph_middle.GetYaxis().SetTitleOffset(1.1)
        grConfInt1Sig.GetXaxis().SetTitleOffset(1.2)
        grConfInt1Sig.GetYaxis().SetTitleOffset(1.1)
        grConfInt2Sig.GetXaxis().SetTitleOffset(1.2)
        grConfInt2Sig.GetYaxis().SetTitleOffset(1.1)
        if pol1 is True:
            graph_middle.GetYaxis().SetRangeUser(0.,13.0)
            grConfInt1Sig.GetYaxis().SetRangeUser(0.,13.0)
            grConfInt2Sig.GetYaxis().SetRangeUser(0.,13.0)
        else:
            graph_middle.GetYaxis().SetRangeUser(0.6,2.0)
            grConfInt1Sig.GetYaxis().SetRangeUser(0.6,2.0)
            grConfInt2Sig.GetYaxis().SetRangeUser(0.6,2.0)
        graph_middle.SetMarkerSize(2)
        grConfInt1Sig.SetFillColor(3)
        grConfInt2Sig.SetFillColor(5)
        CanvasGraphMiddle = TCanvas("CanvasGraphMiddle"+str(z_lo), "CanvasGraphMiddle"+str(z_lo), 100, 100, 700, 600)
        CanvasGraphMiddle.cd()
        grConfInt1Sig.Draw("A3")
        grConfInt2Sig.Draw("3same")
        grConfInt1Sig.Draw("3same")
        graph_middle.Draw("Psame")
        CanvasGraphMiddle.SaveAs(output_path+output_file.replace(".root", "_ratiosVsPromptD0.pdf"))
        CanvasGraphMiddle.SaveAs(output_path+output_file.replace(".root", "_ratiosVsPromptD0.png"))
        graph_middle.Write("graph_middle")
        grConfInt1Sig.Write("grConfInt1Sig")
        grConfInt2Sig.Write("grConfInt2Sig")

out_file.Close()

# export estimates as json for limit setting
json_name = output_file.replace(".root", "_background_estimate.json")
output_estimates = open(output_path+json_name, "w")
json = json.dump(bg_estimate_output, output_estimates, sort_keys=True, indent=2)
print "Storing estimates in", output_path+json_name

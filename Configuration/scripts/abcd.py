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
gStyle.SetOptFit(1111)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('.2f')
gROOT.ForceStyle()


def make_array(l):
    return array('d', l)

# make output histogram with bins for each ABCD region
def make_output_hist(title, template_hist, x_bins, y_bins):
    #  include overflow in outermost bins if applicable
    x_edges = make_array([template_hist.GetXaxis().GetXmax() if x == -1 else x for x in bins_x])
    y_edges = make_array([template_hist.GetYaxis().GetXmax() if y == -1 else y for y in bins_y])

    x_axis_title = template_hist.GetXaxis().GetTitle()
    y_axis_title = template_hist.GetYaxis().GetTitle()
    title_string = "{};{};{}".format(title, x_axis_title, y_axis_title)

    return TH2D(title, title_string, len(x_bins)-1, x_edges, len(y_bins)-1, y_edges)

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

    # replace normal approxmation uncertainty with poisson uncertainty
    if data:
        (err_lo, err_hi) = get_poisson_uncertainty(integral)
    else:
        try:
            eff_evts = (integral/err)**2
        except ZeroDivisionError:
            if integral == 0.0:
                return {'val':integral, 'err_lo':err, 'err_hi':err}
            else:
                print "Actual event count is nonzero while error is 0. Something is wrong."
        eff_evts = round(eff_evts)
        avg_weight = integral/eff_evts
        (err_lo, err_hi) = get_poisson_uncertainty(eff_evts)
        (err_lo, err_hi) = (err_lo * avg_weight, err_hi * avg_weight)
    return {'val':integral, 'err_lo':err_lo, 'err_hi':err_hi}

# separately propagate lo and hi uncertaintanties
def propagate_asymm_err(func, a, b):
    (result, err_lo) = propagateError(func, a['val'], a['err_lo'], b['val'], b['err_lo'])
    (result, err_hi) = propagateError(func, a['val'], a['err_hi'], b['val'], b['err_hi'])
    return {'val':result, 'err_lo':err_lo, 'err_hi':err_hi}

# sum events from different regions while accounting for asymmetric uncertainties
def sum_regions(r1, r2):
    return propagate_asymm_err("sum", r1, r2)

def extrapolate(fit_func, d0s, ratios, d0_err_lo, d0_err_hi, ratio_err_lo, ratio_err_hi,
                extrapolated_d0):
    if fit_func not in ["pol0", "pol1", "expo"]:
        raise RuntimeError("Unrecognized fit function: {}".format(fit_func))

    # perform fit
    tgraph_arrays = map(make_array, [d0s, ratios, d0_err_lo, d0_err_hi, ratio_err_lo, ratio_err_hi])
    graph = TGraphAsymmErrors(len(d0s), *tgraph_arrays)
    fit = TF1("fit", fit_func, 0, extrapolated_d0)
    fit_result = graph.Fit(fit, "SFEM")

    # report fit results
    print "Performing fit with f = {}".format(fit.GetExpFormula())
    print "chisq/dof: {:.2f}".format(fit.GetChisquare()/fit.GetNDF())
    print "p-value: {:.2f}".format(fit.GetProb())
    par_names = [fit.GetParName(i) for i in range(fit.GetNpar())]
    for name, val, err in zip(par_names, fit.GetParameters(), fit.GetParErrors()):
        print "{}: {:.2f} +- {:.2f}".format(name, val, err)

    # compute the 1- and 2-sigma confidence intervals of the fit at the x points of the ratio graph
    # use 1-sigma intervals to construct 2-sigma intervals to avoid GetConfidenceIntervals bug
    # see https://root-forum.cern.ch/t/fitresult-getconfidenceintervals-correction-factor/42552
    all_d0s = make_array(range(int(d0s[0]), extrapolated_d0+1))
    num_points = len(all_d0s)
    confInt1Sig = make_array([0.0]*len(all_d0s))
    fit_result.GetConfidenceIntervals(num_points, 1, 1, all_d0s, confInt1Sig, Double(0.683), False)

    # create tgraphs w/ y-values set by fit values and y-errors set by confidence intervals
    grConfInt1Sig = TGraphErrors()
    grConfInt2Sig = TGraphErrors()
    for i, (d0, ci) in enumerate(zip(all_d0s, confInt1Sig)):
        grConfInt1Sig.SetPoint(i, d0, fit.Eval(d0))
        grConfInt1Sig.SetPointError(i, 0, ci)
        grConfInt2Sig.SetPoint(i, d0, fit.Eval(d0))
        grConfInt2Sig.SetPointError(i, 0, 2*ci) # 2-sigma ci width is twice 1-sigma ci width

    return (fit, graph, grConfInt1Sig, grConfInt2Sig)

####################################################################################################

out_file = TFile(output_path + output_file, "recreate")
in_file = TFile(input_file)
in_hist = in_file.Get(input_hist).Clone()

if type(in_hist) is TH2D and len(bins_z) != 2:
    print
    print "The input hist is a TH2, but you are trying to bin in pT."
    print "Please define 'z_bins' to correspond to the full selection pT range."
    print
    sys.exit(1)

count_totals = {}
bg_estimate_output = {'background' : []} # strange structure to match makeDataCards expectation

regions = lambda bins: zip(bins[:-1], bins[1:])
x_regions = regions(bins_x)
y_regions = regions(bins_y)
z_regions = regions(bins_z)

# combine systematics that apply to the most-prompt signal region
if prompt_sys is not None and extrapolation_sys is not None:
    prompt_sys = propagate_asymm_err("product", prompt_sys, extrapolation_sys)

# perform abcd estimate separately for each region in z
for z_lo, z_hi in z_regions:
    count_totals[z_lo] = {}

    if type(in_hist) is TH3D:
        print "input hist is th3; converting to th2..."
        in_th2 = get_th2(in_hist, z_lo, z_hi, variable_bins)
    else:
        in_th2 = in_hist

    abcd_hist  = make_output_hist(str(z_lo)+"GeV ABCD Estimates", in_th2, bins_x, bins_y)
    count_hist = make_output_hist(str(z_lo)+"GeV Counting Yields", in_th2, bins_x, bins_y)
    ratio_hist = make_output_hist("", in_th2, bins_x, bins_y)

    prompt = get_yields_and_errors(in_th2, bins_x[0], bins_x[1], bins_y[0], bins_y[1],
                                   variable_bins, data)

    if arguments.doExtrapolation:
        ratios = []
        ratios_err_lo = []
        ratios_err_hi = []
        x_mids = []
        y_mids = []

    if arguments.makeTables:
        print
        print "[B]", output_file.replace(".root", ""), "[/B]"
        if not arguments.doClosureTest:
            print "Blinded: actual yields set equal to estimate."
        if prompt_sys is not None:
            print ("Most-prompt SR estimate is scaled by {:.2f}+{:.2f}-{:.2f} to account for "
                "correlation").format(prompt_sys['val'], prompt_sys['err_hi'], prompt_sys['err_lo'])
        if displaced_sys is not None:
            print ("Estimates in more-displaced SRs include systematic uncertainty of "
                   "+{:.2f}-{:.2f}").format(displaced_sys['err_hi'], displaced_sys['err_lo'])
        print '[TABLE border="1"]'
        x_label = in_th2.GetXaxis().GetTitle().replace("|", "\|")
        y_label = in_th2.GetYaxis().GetTitle().replace("|", "\|")
        print "{0}|{1}|A|displaced {0}|displaced {1}|D Estimate|D Actual|D Actual/Estimate".format(
                                                                                   x_label, y_label)

    # iterate through all target regions and perform abcd estimate
    for (x_lo, x_hi), (y_lo, y_hi) in itertools.product(x_regions[1:], y_regions[1:]):

        # Get yield and error in x and y sidebands
        x = get_yields_and_errors(in_th2, x_lo, x_hi, bins_y[0], bins_y[1], variable_bins, data)
        y = get_yields_and_errors(in_th2, bins_x[0], bins_x[1], y_lo, y_hi, variable_bins, data)

        # calculate abcd yield as d = c * b / a
        if x['val'] == 0 or y['val'] == 0:
            abcd = {}
            abcd['val'] = 0
            abcd['err_lo'] = abcd['err_hi'] = 0
        else:
            cb = propagate_asymm_err("product", x, y)
            abcd = propagate_asymm_err("quotient", cb, prompt)

        # account for correction and/or systematic uncertainty on estimate
        prompt_region = x_lo is x_regions[1][0] and y_lo is y_regions[1][0]
        sys = prompt_sys if prompt_region else displaced_sys
        if sys is not None:
            abcd = propagate_asymm_err("product", abcd, sys)

        # get count yields if unblinded; otherwise, set count yields equal to estimate
        if arguments.doClosureTest:
            count = get_yields_and_errors(in_th2, x_lo, x_hi, y_lo, y_hi, variable_bins, data)
        else:
            count = copy.deepcopy(abcd)

        # print low-stats warning if bin contains less than 5 (effective) events
        try:
            lo_err_ratio = count['err_lo']/count['val']
        except ZeroDivisionError:
            lo_err_ratio = 0.0
            print "Warning: the following bin contains zero unweighted events"
        (five_evt_err_lo, _) = get_poisson_uncertainty(5)
        if lo_err_ratio > five_evt_err_lo/5:
            print "Warning: the following bin contains less than five unweighted events"

        # calculate ratio of actual yield to estimate
        if abcd['val'] == 0:
            print "estimate is 0, setting ratio to 100 +/- 100"
            ratio = {}
            ratio['val'] = 100
            ratio['err_lo'] = ratio['err_hi'] = 100
        elif count['val'] == 0:
            print "count_yield is 0, setting ratio uncertainty to 100"
            ratio = {}
            ratio['val'] = 1.*count['val']/abcd['val']
            ratio['err_lo'] = 0
            ratio['err_hi'] = 100
        else:
            ratio = propagate_asymm_err("quotient", count, abcd)

        if 'val' not in count_totals[z_lo]:
            count_totals[z_lo] = copy.deepcopy(count)
        else:
            count_totals[z_lo] = propagate_asymm_err("sum", count_totals[z_lo], count)

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
            x_mids.append(float(x_mid))
            y_halfRange = 0.5*(y_hi-y_lo)
            y_mid = y_halfRange+y_lo
            y_mids.append(float(y_mid))

        if arguments.makeTables:
            print "|-"
            if data: # display asymmetric errors on estimate and no uncertainty on actual count
                format_string = ("{:d}-{:d} | {:d}-{:d}" + 3 * " | {:.0f}" +
                                 " | {:.2f}+{:.2f}-{:.2f} | {:.0f} | {:.2f}+{:.2f}-{:.2f}")
                print format_string.format(x_lo, x_hi, y_lo, y_hi, prompt['val'], x['val'],
                                       y['val'], abcd['val'], abcd['err_hi'], abcd['err_lo'],
                                       count['val'], ratio['val'], ratio['err_hi'], ratio['err_lo'])
            else: # display asymmetric errors on estimate and actual count
                format_string = ("{:d}-{:d} | {:d}-{:d}" + 3 * " | {:.0f}" +
                                 3 * " | {:.2f}+{:.2f}-{:.2f}")
                print format_string.format(x_lo, x_hi, y_lo, y_hi, prompt['val'], x['val'],
                                           y['val'], abcd['val'], abcd['err_hi'], abcd['err_lo'],
                                           count['val'], count['err_hi'], count['err_lo'],
                                           ratio['val'], ratio['err_hi'], ratio['err_lo'])

    # finish table
    if arguments.makeTables:
        print "[/TABLE]"
        print

    # print total count yields
    print "Total test region yield is {:.2f} +{:.2f}/-{:.2f}\n".format(count_totals[z_lo]['val'],
                                         count_totals[z_lo]['err_hi'], count_totals[z_lo]['err_lo'])

    # do linear extrapolation to estimate systematic uncertainty
    if arguments.doExtrapolation:
        # find if x's or y's are changing: the ones that change are the d0 values we want
        d0_mids = make_array([])
        d0_0s = [0.] * len(ratios)
        if x_mids.count(x_mid) > 1:
            d0_mids = y_mids
        elif y_mids.count(y_mid) > 1:
            d0_mids = x_mids
        else:
            print "problem with d0_mids"

        # should really extrapolate using the center of gravity of each bin, but stats committee
        # suggests using small bins to avoid the issue and the bin center, so we use the bin center
        # take no x-axis error bars because we assume the width of the bin center of gravity is
        # small compared to the width of the bin
        extrapolated_d0 = 200

        extrapolation_result = extrapolate(fit_func, d0_mids, ratios, d0_0s, d0_0s, ratios_err_lo,
                                           ratios_err_hi, extrapolated_d0)
        (ratio_fit, ratio_graph, grConfInt1Sig, grConfInt2Sig) = extrapolation_result
        projected_ratio = ratio_fit.Eval(extrapolated_d0)
        projected_err = grConfInt1Sig.GetErrorY(grConfInt1Sig.GetN()-1)
        print "The projected ratio is {:.2f} +/- {:.2f} when extrapolating to |d0|={}".format(
                                                    projected_ratio, projected_err, extrapolated_d0)
        print

    # Format and export histograms
    out_file.cd()

    abcd_hist.SetMarkerSize(2)
    abcd_hist.SetOption("colz text45 e")
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
        ratio_graph.SetTitle("")
        grConfInt1Sig.SetTitle("")
        grConfInt2Sig.SetTitle("")
        ratio_graph.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        ratio_graph.GetYaxis().SetTitle("Actual/estimate ratios")
        grConfInt1Sig.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        grConfInt1Sig.GetYaxis().SetTitle("Actual/estimate ratios")
        grConfInt2Sig.GetXaxis().SetTitle("Prompt lepton |d_{0}| [#mum]")
        grConfInt2Sig.GetYaxis().SetTitle("Actual/estimate ratios")
        ratio_graph.GetXaxis().SetTitleOffset(1.2)
        ratio_graph.GetYaxis().SetTitleOffset(1.1)
        grConfInt1Sig.GetXaxis().SetTitleOffset(1.2)
        grConfInt1Sig.GetYaxis().SetTitleOffset(1.1)
        grConfInt2Sig.GetXaxis().SetTitleOffset(1.2)
        grConfInt2Sig.GetYaxis().SetTitleOffset(1.1)
        if projected_ratio > 5.0:
            y_min = 0.0
            y_max = projected_ratio + projected_err
        elif fit_func in ["pol1", "expo"]:
            y_min = 0.0
            y_max = 6.0
        else:
            y_min = 0.6
            y_max = 2.0
        ratio_graph.GetYaxis().SetRangeUser(y_min, y_max)
        grConfInt1Sig.GetYaxis().SetRangeUser(y_min, y_max)
        grConfInt2Sig.GetYaxis().SetRangeUser(y_min, y_max)
        ratio_graph.SetMarkerStyle(20)
        grConfInt1Sig.SetFillColor(3)
        grConfInt2Sig.SetFillColor(5)
        title = "CanvasRatioGraph"+str(z_lo)
        CanvasRatioGraph = TCanvas(title, title, 100, 100, 700, 600)
        CanvasRatioGraph.cd()
        grConfInt2Sig.Draw("A3")
        grConfInt1Sig.Draw("3same")
        ratio_graph.Draw("Psame")
        ratio_fit.Draw("same")
        CanvasRatioGraph.SaveAs(output_path+output_file.replace(".root", "_ratiosVsPromptD0.pdf"))
        CanvasRatioGraph.SaveAs(output_path+output_file.replace(".root", "_ratiosVsPromptD0.png"))
        ratio_graph.Write("ratio_graph")
        grConfInt1Sig.Write("grConfInt1Sig")
        grConfInt2Sig.Write("grConfInt2Sig")

out_file.Close()

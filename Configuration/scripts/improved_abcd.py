#!/usr/bin/env python

import sys
import os
import re
import json
from math import pi, atan, sqrt, log
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TF1, TCanvas, Double, gStyle, gPad, gROOT, TLine, TGraph,TGraphErrors, TGraphAsymmErrors, TMultiGraph, TLegend, TPaveText, TMatrixDSymEigen, TEllipse, TFormula

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-u", "--unblind", action="store_true", dest="unblind",
                  default=False, help="perform closure test; DON'T RUN OVER DATA IF BLINDED!")
parser.add_option("-p", "--savePlots", action="store_true", dest="savePlots",
                  default=False, help="save summary plots as pdfs and pngs")

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

gROOT.SetBatch(True)
gStyle.SetOptStat(1)
gStyle.SetOptFit(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetPaintTextFormat('6.4f')
gStyle.SetStatFormat('6.4f')
gStyle.SetFitFormat('6.4f')
gROOT.ForceStyle()
# select high contrast TColors for summary plots
colors = [x for x in range(1, 10)] + [11, 12, 28, 29, 33, 38, 41, 42, 43, 45, 46]

def make_estimate_hist(c_hist, fit):
    transfer_factor_hist = c_hist.Clone()
    # use fit value at upper edge of plot as transfer factor for overflow entries
    for b in range(1, transfer_factor_hist.GetNbinsX()+2):
        transfer_factor_hist.SetBinContent(b, fit.Eval(transfer_factor_hist.GetBinCenter(b)))
        transfer_factor_hist.SetBinError(b, 0) # fixme: account for fit uncertainty
    d_estimate_hist = c_hist.Clone()
    d_estimate_hist.Multiply(transfer_factor_hist)
    return d_estimate_hist

def do_closure_test(estimate_hist, d_hist, pt_lo=0, pt_hi=0):
    # use full pT range if pt_lo or pt_hi are unspecified
    lo_bin = estimate_hist.GetXaxis().FindBin(pt_lo) if pt_lo else 1
    if 0 < pt_hi < estimate_hist.GetXaxis().GetXmax():
        hi_bin = estimate_hist.GetXaxis().FindBin(pt_hi) - 1
    else:
        hi_bin = estimate_hist.GetNbinsX() + 1

    estimate = estimate_hist.Integral(lo_bin, hi_bin)
    if arguments.unblind:
        actual_yield = d_hist.Integral(lo_bin, hi_bin)
    else:
        actual_yield = 0.0
    return (estimate, actual_yield)

def setup_plot(plot, title, x_title, y_title):
    plot.SetTitle(title)
    plot.SetName(title)
    plot.GetXaxis().SetTitle(x_title)
    plot.GetYaxis().SetTitle(y_title)
    plot.GetYaxis().SetTitleOffset(1.4)
    plot.GetYaxis().SetLabelSize(0.025)

def draw_lines(x_values):
    line = TLine()
    line.SetLineWidth(2)
    line.SetLineColor(4)
    line.SetLineStyle(9)
    gPad.Update()
    for x in x_values:
        line.DrawLine(x, 0, x, gPad.GetUymax())

def make_default_canvas(name):
    return TCanvas(name, name, 100, 100, 700, 600)

# make 1D pT hist from 3D |d0|-|d0|-pT hist
def make_pt_hist(h, name, d0_0_lo, d0_0_hi, d0_1_lo, d0_1_hi, pt_lo, pt_hi):

    # get bins whose lower edge is equal to the given value
    lo_bin_x = h.GetXaxis().FindBin(d0_0_lo)
    hi_bin_x = h.GetXaxis().FindBin(d0_0_hi)
    lo_bin_y = h.GetYaxis().FindBin(d0_1_lo)
    hi_bin_y = h.GetYaxis().FindBin(d0_1_hi)
    lo_bin_z = h.GetZaxis().FindBin(pt_lo)
    hi_bin_z = h.GetZaxis().FindBin(pt_hi)

    # increment hi bins to include overflow bin if desired max is input hist max
    if d0_0_hi == h.GetXaxis().GetXmax():
       hi_bin_x += 1
    if d0_1_hi == h.GetYaxis().GetXmax():
        hi_bin_y += 1
    if pt_hi == h.GetZaxis().GetXmax():
        hi_bin_z += 1

    # extract 1D pT hist
    pt_hist = h.ProjectionZ(name, lo_bin_x, hi_bin_x-1, lo_bin_y, hi_bin_y-1, "eo")

    # set bin content to zero in all but desired pT range
    for b in range(1, lo_bin_z) + range(hi_bin_z, in_hist.GetNbinsZ()+2):
        pt_hist.SetBinContent(b,0)
        pt_hist.SetBinError(b,0)
    pt_hist.ResetStats()

    return pt_hist

class ErrorEllipse():
    # create one-sigma error ellipse for an arbitrary 2D tgraph,
    def __init__(self, par_vals, covariance_matrix):
        eigen_covariance_matrix = TMatrixDSymEigen(covariance_matrix)
        eigenvalues = eigen_covariance_matrix.GetEigenValues()
        eigenvectors = eigen_covariance_matrix.GetEigenVectors()
        self.par_vals = par_vals
        self.radii = (sqrt(eigenvalues(0)), sqrt(eigenvalues(1)))
        if eigenvalues(0) >= eigenvalues(1):
            self.angle = 180/pi*atan(eigenvectors(1,0)/eigenvectors(0,0))
        else:
            self.angle = 180/pi*atan(eigenvectors(0,1)/eigenvectors(1,1))
        self.ellipse = TEllipse(self.par_vals[0], self.par_vals[1], self.radii[0], self.radii[1],
                                0, 360, self.angle)
        self.ellipse.SetFillStyle(0)
        self.ellipse.SetLineColor(2)
        self.points = self.generate_sample_points()

    # generate list of 360 points sampled from the error ellipse
    def generate_sample_points(self):
        x = TFormula("err_ellipse", "[0] + [1]*cos(x)*cos([2]) + [3]*sin(x)*(-sin([2]))")
        y = TFormula("err_ellipse", "[0] + [1]*cos(x)*sin([2]) + [3]*sin(x)*cos([2])")
        x.SetParameter(0, self.par_vals[0])
        y.SetParameter(0, self.par_vals[1])
        x.SetParameter(1, self.radii[0])
        y.SetParameter(1, self.radii[0])
        x.SetParameter(2, self.angle*pi/180) # TFormula wants radians
        y.SetParameter(2, self.angle*pi/180) # TFormula wants radians
        x.SetParameter(3, self.radii[1])
        y.SetParameter(3, self.radii[1])

        points = []
        min_x = min_y = 100 # this is a little irresponsible
        max_x = max_y = 0
        for t in range(0, 360):
            x_val = x.Eval(t*pi/180) if x.Eval(t*pi/180) > 0 else 0.0
            y_val = y.Eval(t*pi/180) if y.Eval(t*pi/180) > 0 else 0.0
            points.append((x_val, y_val))
            min_x = x_val if x_val < min_x else min_x
            min_y = y_val if y_val < min_y else min_y
            max_x = x_val if x_val > max_x else max_x
            max_y = y_val if y_val > max_y else max_y

        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

        return points

    # estimate background using each pair of fit parameters on ellipse
    def find_estimate_bounds(self, fit_func, pt_hists):
        for pars in self.points:
            # estimate background
            fit_func.FixParameter(0, pars[0])
            fit_func.FixParameter(1, pars[1])
            estimate_hist = make_estimate_hist(pt_hists['c'].Clone(), fit_func)
            estimate, _ = do_closure_test(estimate_hist, pt_hists['d'])
            # save max and min estimate and corresponding fits
            if pars == self.points[0]:
                self.min_estimate = self.max_estimate = estimate
                self.min_fit = self.max_fit = fit_func.Clone()
            else:
                if estimate > self.max_estimate:
                    self.max_estimate = estimate
                    self.max_fit = fit_func.Clone()
                elif estimate < self.min_estimate:
                    self.min_estimate = estimate
                    self.min_fit = fit_func.Clone()

class RatioPlot:
    def __init__(self, num_hist, den_hist):
        self.num = num_hist
        self.den = den_hist
        self.tgraph = TGraphAsymmErrors(self.num, self.den, "pois")

    def get_plot(self):
        return self.tgraph.Clone()

    def rebin(self, bin_edges):
        num_hist = self.num.Rebin(len(bin_edges)-1, self.num.GetName(), array('d', bin_edges))
        den_hist = self.den.Rebin(len(bin_edges)-1, self.den.GetName(), array('d', bin_edges))
        self.tgraph = TGraphAsymmErrors(num_hist, den_hist, "pois")

    # rebin so that error / bin content is below specified tolerance for all bins
    def improve_binning(self, err_tolerance, upper_edge, min_bins=4):
        # create list of initial bin edges
        bin_edges = []
        found_first_filled_bin = False
        # store bin edges from first filled bin until upper edge
        for b in range(1, self.den.GetNbinsX()+1):
            if not found_first_filled_bin and self.den.GetBinContent(b) > 0:
                found_first_filled_bin = True
            if found_first_filled_bin and self.den.GetXaxis().GetBinLowEdge(b) < upper_edge:
                bin_edges.append(self.den.GetXaxis().GetBinLowEdge(b))
        bin_edges.append(upper_edge)
        self.rebin(bin_edges)

        # iteratively rebin until all bins are filled
        bin_ix = 0
        while bin_ix < len(bin_edges)-1:
            content = Double()
            x = Double()
            self.tgraph.GetPoint(bin_ix, x, content)
            if content == 0:
                if bin_ix < len(bin_edges)-2:
                    del bin_edges[bin_ix+1] # combine current and next bins
                else:
                    del bin_edges[bin_ix] # combine final and penultimate bins
                self.rebin(bin_edges)
            else:
                bin_ix += 1 # go to next bin if current bin is filled

        # iteratively rebin until bin error / bin content is below tolerance for each bin
        if len(bin_edges)-1 < min_bins:
            return
        original_edges = list(bin_edges)
        original_tolerance = err_tolerance
        bin_ix = 0
        while bin_ix < len(bin_edges)-1:
            self.tgraph.GetPoint(bin_ix, x, content)
            error = self.tgraph.GetErrorY(bin_ix)
            if error/content > err_tolerance:
                if bin_ix < len(bin_edges)-2:
                    del bin_edges[bin_ix+1] # combine current and next bins
                else:
                    del bin_edges[bin_ix] # combine final and penultimate bins
                self.rebin(bin_edges)
            else:
                bin_ix += 1 # go to next bin if current error is below tolerance

            # if there are fewer than min_bins bins, increase the tolerance and try again
            if len(bin_edges)-1 < min_bins:
                bin_edges = list(original_edges)
                self.rebin(bin_edges)
                bin_ix = 0
                err_tolerance += original_tolerance


####################################################################################################

output_plots = TFile(output_path + "improved_abcd_results.root", "recreate")
bg_estimates = {}
ctrl_region_evts = {}
estimate_upper_bounds = {}
estimate_lower_bounds = {}

for sample in samples:
    print "\n" + sample
    bg_estimates[sample] = {}
    ctrl_region_evts[sample] = {}
    estimate_upper_bounds[sample] = {}
    estimate_lower_bounds[sample] = {}

    # get histograms and statistical uncertainties for all regions
    in_file = TFile(output_path + sample + ".root")
    in_hist = in_file.Get(input_hist)
    if not in_hist:
        print "Warning: could not load " + input_hist

    in_hist_d0_0_max = in_hist.GetXaxis().GetXmax()
    in_hist_d0_1_max = in_hist.GetYaxis().GetXmax()
    in_hist_pt_max   = in_hist.GetZaxis().GetXmax()
    d0_0_max = d0_0_max if 0 < d0_0_max < in_hist_d0_0_max else in_hist_d0_0_max
    d0_1_max = d0_1_max if 0 < d0_1_max < in_hist_d0_1_max else in_hist_d0_1_max
    pt_max   = pt_max   if 0 < pt_max   < in_hist_pt_max   else in_hist_pt_max

    # get pT hist for prompt, low-pT region
    pt_hists = {}
    pt_hists['a'] = make_pt_hist(in_hist, "A", 0, d0_0_cuts[0], 0, d0_1_cuts[0], fit_min, pt_cuts[0])

    # do bg estimate in each non-overlapping |d0| signal region
    # loop from most displaced to least displaced to simplify creation of L-shaped signal regions
    for (d0_0_cut, d0_1_cut) in reversed(zip(d0_0_cuts, d0_1_cuts)):
        bg_estimates[sample][d0_0_cut] = {}
        ctrl_region_evts[sample][d0_0_cut] = {}
        estimate_upper_bounds[sample][d0_0_cut] = {}
        estimate_lower_bounds[sample][d0_0_cut] = {}
        fit_summary_plot = TMultiGraph()
        fit_summary_legend = TLegend(0.4, 0.5, 0.89, 0.87)
        fit_summary_legend.AddEntry(None, "", "") # add blank entry for spacing
        fit_parameters_plot = TGraph()
        color_ix = 0

        # get pT hists for displaced and/or high-pt regions
        # don't subdivide signal region in pT at this point -- will do so after fitting etc
        pt_hists['b'] = make_pt_hist(in_hist, "B", d0_0_cut, d0_0_max,
                                                   d0_1_cut, d0_1_max,
                                                   fit_min, pt_cuts[0])
        pt_hists['c'] = make_pt_hist(in_hist, "C", 0, d0_0_cuts[0],
                                                   0, d0_1_cuts[0],
                                                   pt_cuts[0], pt_max)
        pt_hists['d'] = make_pt_hist(in_hist, "D", d0_0_cut, d0_0_max,
                                                   d0_1_cut, d0_1_max,
                                                   pt_cuts[0], pt_max)

        inclusive_pt_hists = {}
        inclusive_pt_hists['b'] = pt_hists['b'].Clone()
        inclusive_pt_hists['d'] = pt_hists['d'].Clone()

        # subtract previous displaced pt hists from current ones to create L-shaped regions in |d0|
        if d0_0_cut != d0_0_cuts[-1] and d0_1_cut != d0_0_cuts[-1]:
            pt_hists['b'].Add(previous_pt_hists['b'], -1)
            pt_hists['d'].Add(previous_pt_hists['d'], -1)

        previous_pt_hists = {}
        previous_pt_hists['b'] = inclusive_pt_hists['b'].Clone()
        previous_pt_hists['d'] = inclusive_pt_hists['d'].Clone()

        # set up fit model
        model = "[0] + [1]/x" # |d0| resolution as a function of pT
        fit_func = TF1(sample + "_fit", model, 0, pt_max)
        fit_func.SetParLimits(0, 0, 100)
        fit_func.SetParLimits(1, 0, 100)

        # fit B/A
        b_over_a = RatioPlot(pt_hists['b'], pt_hists['a'])
        b_over_a.improve_binning(error_tolerance, fit_range[1])
        b_over_a_plot = b_over_a.get_plot()
        fit_results = b_over_a_plot.Fit(fit_func, "S", "", fit_range[0], fit_range[1])
        fit = b_over_a_plot.GetFunction(sample+"_fit")
        try:
            print "Chi2/NDF: {}".format(fit.GetChisquare()/fit.GetNDF())
        except ZeroDivisionError:
            print "NDF is {}; you might need to increase statistics in region B".format(fit.GetNDF())

        # calculate d(pT) = c(pT) * model(pT) and do closure test
        d_estimate_hist = make_estimate_hist(pt_hists['c'].Clone(), fit)
        estimate, actual_yield = do_closure_test(d_estimate_hist, pt_hists['d'])

        # make plots
        output_plots.cd()
        sample_and_d0_region = "{}_{}_{}".format(sample, d0_0_cut, d0_1_cut)

        # input hists
        a_canvas = make_default_canvas(sample_and_d0_region + "_A")
        pt_hists['a'].Draw()
        a_canvas.Write()
        b_canvas = make_default_canvas(sample_and_d0_region + "_B")
        pt_hists['b'].Draw()
        b_canvas.Write()
        c_canvas = make_default_canvas(sample_and_d0_region + "_C")
        pt_hists['c'].Draw()
        c_canvas.Write()

        # fit parameters plot
        fit_parameters_canvas = make_default_canvas(sample_and_d0_region+"_fit_pars")
        fit_covariance = fit_results.GetCovarianceMatrix()
        fit_parameters = (fit.GetParameter(0), fit.GetParameter(1))
        err_ellipse = ErrorEllipse(fit_parameters, fit_covariance)
        fit_parameters_plot = TGraph()
        fit_parameters_plot.SetMarkerColor(4)
        fit_parameters_plot.SetMarkerStyle(8)
        fit_parameters_plot.SetPoint(0, fit_parameters[0], fit_parameters[1])
        par_mg = TMultiGraph()
        par_mg.Add(fit_parameters_plot, "P")
        par_mg.Draw("A")
        setup_plot(par_mg, "Fit parameters and uncertainty for "+model,
                   "Parameter [0]", "Parameter [1]")
        par_mg.GetXaxis().SetLimits(0.5*err_ellipse.min_x, 1.5*err_ellipse.max_x)
        par_mg.SetMinimum(0.5*err_ellipse.min_y)
        par_mg.SetMaximum(1.5*err_ellipse.max_y)
        err_ellipse.ellipse.Draw("same")
        par_legend = TLegend(0.5, 0.7, 0.89, 0.89)
        par_legend.AddEntry(fit_parameters_plot, "Fit parameters", "P")
        par_legend.AddEntry(err_ellipse.ellipse, "One-sigma uncertainty ellipse", "L")
        par_legend.SetBorderSize(0)
        par_legend.Draw()
        fit_parameters_canvas.Write()
        if arguments.savePlots:
            fit_parameters_canvas.SaveAs("fit_parameters_"+sample_and_d0_region+".pdf", "recreate")
            fit_parameters_canvas.SaveAs("fit_parameters_"+sample_and_d0_region+".png", "recreate")

        # fit plot
        fit_canvas = make_default_canvas(sample_and_d0_region+"_fit")
        fit_plot = TMultiGraph()
        fit_plot.Add(b_over_a_plot, "P")
        if arguments.unblind:
            d_over_c = RatioPlot(pt_hists['d'], pt_hists['c'])
            d_over_c.improve_binning(error_tolerance, pt_max)
            fit_plot.Add(d_over_c.get_plot(), "P")
        fit_plot.Draw("A")
        fit_plot.GetXaxis().SetLimits(0, pt_max)
        setup_plot(fit_plot, sample+" fit", str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
        fit.SetRange(0, pt_max)
        fit_plot.Draw("same") # draw again so points aren't covered by fit lines
        fit_plot.GetYaxis().SetRangeUser(0, 1.5*fit_plot.GetYaxis().GetXmax())
        err_ellipse.find_estimate_bounds(fit_func, pt_hists)
        err_ellipse.min_fit.Draw("same")
        err_ellipse.max_fit.Draw("same")
        err_ellipse.min_fit.SetRange(fit_range[1], d_estimate_hist.GetXaxis().GetXmax())
        err_ellipse.max_fit.SetRange(fit_range[1], d_estimate_hist.GetXaxis().GetXmax())
        draw_lines([fit_range[0], fit_range[1]])
        # add text with closure test results
        results_pave = TPaveText(0.3, 0.75, 0.85, 0.85, "NDC")
        results_pave.AddText("Actual yield for entire pT range: {} events".format(
                              round(actual_yield, 1)))
        err_up = round(err_ellipse.max_estimate - estimate, 2)
        err_down = round(estimate - err_ellipse.min_estimate, 2)
        if err_up == err_down:
            uncertainty_string = " +- {}".format(err_up)
        else:
            uncertainty_string = " +{}/-{}".format(err_up, err_down)
        results_pave.AddText("Estimated yield for entire pT range: {}{} events".format(
                              round(estimate, 2), uncertainty_string))
        results_pave.SetTextSize(0.025)
        results_pave.SetFillColor(0)
        results_pave.SetBorderSize(0)
        results_pave.SetTextAlign(11)
        results_pave.Draw()
        fit_canvas.Write()
        if arguments.savePlots:
            fit_canvas.SaveAs("fit_"+sample_and_d0_region+".pdf","recreate")
            fit_canvas.SaveAs("fit_"+sample_and_d0_region+".png","recreate")

        # divide bg estimate into non-overlapping pT bins
        for pt_lo, pt_hi in zip(pt_cuts, pt_cuts[1:]+[int(pt_max)]):
            estimate, _ = do_closure_test(d_estimate_hist, pt_hists['d'] , pt_lo, pt_hi)
            bg_estimates[sample][d0_0_cut][pt_lo] = estimate
            # also divide upper and lower bounds on bg estimate to estimate uncertainty
            estimate_up_hist   = make_estimate_hist(pt_hists['c'].Clone(), err_ellipse.max_fit)
            estimate_down_hist = make_estimate_hist(pt_hists['c'].Clone(), err_ellipse.min_fit)
            estimate_up, _   = do_closure_test(estimate_up_hist, pt_hists['d'] , pt_lo, pt_hi)
            estimate_down, _ = do_closure_test(estimate_down_hist, pt_hists['d'] , pt_lo, pt_hi)
            estimate_upper_bounds[sample][d0_0_cut][pt_lo] = estimate_up
            estimate_lower_bounds[sample][d0_0_cut][pt_lo] = estimate_down
            # store number of events in part of region C that corresponds to each pT range
            lo_bin =  pt_hists['c'].GetXaxis().FindBin(pt_lo)
            if 0 < pt_hi < pt_hists['c'].GetXaxis().GetXmax():
                hi_bin = pt_hists['c'].GetXaxis().FindBin(pt_hi) - 1
            else:
                hi_bin = pt_hists['c'].GetNbinsX() + 1
            ctrl_region_evts[sample][pt_lo] = pt_hists['c'].Integral(lo_bin, hi_bin)

        # print CR stats
        print "Region A contains {} events".format(pt_hists['a'].Integral())
        print "Region B contains {} events".format(pt_hists['b'].Integral())
        for pt in pt_cuts:
            print "Region C contains {} events in pT range starting at {}GeV".format(
                   ctrl_region_evts[sample][pt], pt)

# create output json that contains background estimate results for use in limit setting
bg_estimate_output = {}
d0_cuts = zip(zip(d0_0_cuts, d0_1_cuts),
              zip(d0_0_cuts, d0_1_cuts)[1:] + [(int(d0_0_max), int(d0_1_max))])
for s in samples:
    bg_estimate_output[s] = []
    for pt_lo, pt_hi in zip(pt_cuts, pt_cuts[1:]+[int(pt_max)]):
        for (d0_0_lo, d0_1_lo), (d0_0_hi, d0_1_hi) in d0_cuts:
            sr = {}
            sr['pt'] = (pt_lo, pt_hi)
            sr['d0_0'] = (d0_0_lo, d0_0_hi)
            sr['d0_1'] = (d0_1_lo, d0_1_hi)
            sr['d0_max'] = d0_0_max # assuming d0_0_max == d0_1_max
            sr['estimate'] = bg_estimates[s][d0_0_lo][pt_lo]
            sr['ctrl_region_events'] = ctrl_region_evts[s][pt_lo]
            sr['fit_up_err']   = estimate_upper_bounds[s][d0_0_lo][pt_lo] / sr['estimate']
            sr['fit_down_err'] = estimate_lower_bounds[s][d0_0_lo][pt_lo] / sr['estimate']
            bg_estimate_output[s].append(sr)

            # print estimtates
            err_up   = round(estimate_upper_bounds[s][d0_0_lo][pt_lo] - sr['estimate'], 4)
            err_down = round(sr['estimate'] - estimate_lower_bounds[s][d0_0_lo][pt_lo], 4)
            if err_up == err_down:
                uncertainty_string = " +- {}".format(err_up)
            else:
                uncertainty_string = " +{}/-{}".format(err_up, err_down)
            print "For {}-{}um, {}-{}GeV signal region:".format(d0_0_lo, d0_0_hi, pt_lo, pt_hi)
            print "Estimate: {}{} events".format(round(sr['estimate'], 4), uncertainty_string)

import json
output_estimates = open(output_path + "background_estimate.json", "w")
json = json.dump(bg_estimate_output, output_estimates, sort_keys=True, indent=4)

output_plots.Close()
output_estimates.close()

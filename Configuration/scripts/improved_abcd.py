#!/usr/bin/env python

import sys
import os
import re
import json
from math import pi, atan, sqrt, log
from array import array
from optparse import OptionParser
from DisplacedSUSY.Configuration.helperFunctions import propagateError
from ROOT import TFile, TF1, TCanvas, Double, gStyle, gPad, gROOT, TLine, TGraph,TGraphErrors, TGraphAsymmErrors, TMultiGraph, TLegend, TPaveText, TMatrixD, TMatrixDEigen, TEllipse, TFormula

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")
parser.add_option("-u", "--unblind", action="store_true", dest="unblind",
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
        actual_error = Double()
        actual_yield = d_hist.IntegralAndError(lo_bin, hi_bin, actual_error)
    else:
        actual_yield = actual_error = 0.0
    return (estimate, actual_yield, actual_error)

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
    pt_hist = h.ProjectionZ(name, lo_bin_x, hi_bin_x, lo_bin_y, hi_bin_y, "eo")

    # set bin content to zero in all but desired pT range
    for b in range(1, lo_bin_z) + range(hi_bin_z, in_hist.GetNbinsZ()+2):
        pt_hist.SetBinContent(b,0)
        pt_hist.SetBinError(b,0)
    pt_hist.ResetStats()

    if arguments.unblind or name in ("A", "B", "C"):
        error = Double()
        print "number of events in {} is: {} +- {}".format(name,
            pt_hist.IntegralAndError(1, pt_hist.GetNbinsX()+1, error), error)

    return pt_hist

class ErrorEllipse():
    # create one-sigma error ellipse for an arbitrary 2D tgraph,
    def __init__(self, tgraph):
        covariance_matrix = TMatrixD(2, 2, array('d', [tgraph.GetRMS(1)**2, tgraph.GetCovariance(),
                                                       tgraph.GetCovariance(), tgraph.GetRMS(2)**2]))
        eigen_covariance_matrix = TMatrixDEigen(covariance_matrix)
        eigenvalues = eigen_covariance_matrix.GetEigenValues()
        eigenvectors = eigen_covariance_matrix.GetEigenVectors()
        self.mean = (tgraph.GetMean(1), tgraph.GetMean(2))
        self.radii = (sqrt(eigenvalues(0,0)), sqrt(eigenvalues(1,1)))
        if eigenvalues(0,0) >= eigenvalues(1,1):
            self.angle = 180/pi*atan(eigenvectors(1,0)/eigenvectors(0,0))
        else:
            self.angle = 180/pi*atan(eigenvectors(0,1)/eigenvectors(1,1))
        self.ellipse = TEllipse(self.mean[0], self.mean[1], self.radii[0], self.radii[1],
                                0, 360, self.angle)
        self.ellipse.SetFillStyle(0)
        self.ellipse.SetLineColor(2)

    # generate list of 360 points sampled from the error ellipse
    def sample_points(self):
        x = TFormula("err_ellipse", "[0] + [1]*cos(x)*cos([2]) + [3]*sin(x)*(-sin([2]))")
        y = TFormula("err_ellipse", "[0] + [1]*cos(x)*sin([2]) + [3]*sin(x)*cos([2])")
        x.SetParameter(0, self.mean[0])
        y.SetParameter(0, self.mean[1])
        x.SetParameter(1, self.radii[0])
        y.SetParameter(1, self.radii[0])
        x.SetParameter(2, self.angle*pi/180) # TFormula wants radians
        y.SetParameter(2, self.angle*pi/180) # TFormula wants radians
        x.SetParameter(3, self.radii[1])
        y.SetParameter(3, self.radii[1])
        points = []
        for t in range(0, 360):
            points.append((x.Eval(t*pi/180), y.Eval(t*pi/180)))
        return points

    # estimate background using each pair of fit parameters on ellipse
    def find_estimate_bounds(self, fit_func, in_hists):
        self.points = self.sample_points()
        for pars in self.points:
            # estimate background
            fit_func.FixParameter(0, pars[0])
            fit_func.FixParameter(1, pars[1])
            estimate_hist = make_estimate_hist(in_hists['c'].Clone(), fit_func)
            estimate, _, _ = do_closure_test(estimate_hist, in_hists['d'])
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
    def improve_binning(self, err_tolerance, upper_edge):
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

        # iteratively rebin until bin error / bin content is below tolerance for each bin
        bin_ix = 0
        while bin_ix < len(bin_edges)-1 and len(bin_edges) > 2:
            content = Double()
            x = Double()
            self.tgraph.GetPoint(bin_ix, x, content)
            error = self.tgraph.GetErrorY(bin_ix)
            if content == 0 or error/content > err_tolerance:
                if bin_ix < len(bin_edges)-2:
                    del bin_edges[bin_ix+1] # combine current and next bins
                else:
                    del bin_edges[bin_ix] # combine final and penultimate bins
                self.rebin(bin_edges)
            else:
                bin_ix += 1 # go to next bin if current error is below tolerance


####################################################################################################

output_plots = TFile(output_path + "improved_abcd_results.root", "recreate")
bg_estimates = {}

for sample in samples:
    print "\n" + sample
    bg_estimates[sample] = {}

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
    in_hists = {}
    in_hists['a'] = make_pt_hist(in_hist, "A", 0, d0_0_cuts[0], 0, d0_1_cuts[0], fit_min, pt_cuts[0])

    # do bg estimate in each inclusive d0 signal region
    for (d0_0_cut, d0_1_cut) in zip(d0_0_cuts, d0_1_cuts):
        bg_estimates[sample][d0_0_cut] = {}
        fit_summary_plot = TMultiGraph()
        fit_summary_legend = TLegend(0.4, 0.5, 0.89, 0.87)
        fit_summary_legend.AddEntry(None, "", "") # add blank entry for spacing
        fit_parameters_plot = TGraph()
        color_ix = 0

        # get pT hists for displaced and/or high-pt regions
        # don't subdivide signal region in pT at this point  -- will do so after fitting etc
        in_hists['b'] = make_pt_hist(in_hist, "B", d0_0_cut, d0_0_max,
                                                   d0_1_cut, d0_1_max,
                                                   fit_min, pt_cuts[0])
        in_hists['c'] = make_pt_hist(in_hist, "C", 0, d0_0_cuts[0],
                                                   0, d0_1_cuts[0],
                                                   pt_cuts[0], pt_max)
        in_hists['d'] = make_pt_hist(in_hist, "D", d0_0_cut, d0_0_max,
                                                   d0_1_cut, d0_1_max,
                                                   pt_cuts[0], pt_max)

        # set up fit model
        model = "[0] + [1]/x" # |d0| resolution as a function of pT
        fit_func = TF1(sample + "_fit", model, 0, pt_max)
        fit_func.SetParLimits(0, 0, 100)
        fit_func.SetParLimits(1, 0, 100)

        # fit B/A once per fit range
        for fit_range in fit_ranges:
            # don't perform fit if fit range is empty
            get_bin = lambda x: in_hists['b'].GetXaxis().FindBin(x)
            if not in_hists['b'].Integral(get_bin(fit_range[0]), get_bin(fit_range[1])-1) > 0:
                print "No events in fit range {}-{}. Skipping.".format(fit_range[0], fit_range[1])
                # fixme: will skipping empty fit ranges lead to overestimate?
                # maybe rebinning to avoid empty ranges would be better?
                continue

            b_over_a = RatioPlot(in_hists['b'], in_hists['a'])
            b_over_a_plot = b_over_a.get_plot()
            b_over_a_plot.Fit(fit_func, "", "", fit_range[0], fit_range[1])
            fit = b_over_a_plot.GetFunction(sample+"_fit")
            chisq_per_dof = fit.GetChisquare()/fit.GetNDF()

            # calculate d(pT) = c(pT) * model(pT) and do closure test
            d_estimate_hist = make_estimate_hist(in_hists['c'].Clone(), fit)
            estimate, actual_yield, actual_error = do_closure_test(d_estimate_hist, in_hists['d'])

            # add fit plots to fit summary plot
            fit.SetRange(0, pt_max)
            fit.SetLineColor(colors[color_ix])
            b_over_a_plot.SetLineColor(colors[color_ix])
            fit_summary_plot.Add(b_over_a_plot, "X")
            fit_summary_legend.AddEntry(b_over_a_plot, str(fit_range[0]) + " GeV --> " +
                                        str(round(estimate, 2)) + " events; chisq/dof is "
                                        + str(round(chisq_per_dof,2)))
            color_ix = (color_ix + 1) % len(colors)

            # add point to fit parameter plot
            fit_parameters_plot.SetPoint(fit_parameters_plot.GetN(),
                                        fit.GetParameter(0), fit.GetParameter(1))

        # save once-per-sample plots
        output_plots.cd()
        sample_and_d0_region = "{}_{}_{}".format(sample, d0_0_cut, d0_1_cut)

        # input hists
        a_canvas = make_default_canvas(sample_and_d0_region + "_A")
        in_hists['a'].Draw()
        a_canvas.Write()
        b_canvas = make_default_canvas(sample_and_d0_region + "_B")
        in_hists['b'].Draw()
        b_canvas.Write()
        c_canvas = make_default_canvas(sample_and_d0_region + "_C")
        in_hists['c'].Draw()
        c_canvas.Write()

        # fit summary plot
        fit_summary_canvas = make_default_canvas(sample_and_d0_region+"_fit_summary")
        fit_summary_plot.Draw("A")
        fit_summary_plot.GetXaxis().SetLimits(0, pt_max)
        setup_plot(fit_summary_plot, sample_and_d0_region+" fit summary",
                   str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
        fit_summary_legend.SetHeader(
            "#splitline{Fit Range Lower Bound --> Corresponding BG Estimate}{(Actual yield is "
            + str(round(actual_yield, 1)) + " +- " + str(round(actual_error, 1)) + " events)}")
        fit_summary_legend.SetTextSize(0.025)
        fit_summary_legend.SetBorderSize(0)
        fit_summary_legend.Draw()
        draw_lines([fit_range[1]])
        fit_summary_canvas.Write()
        fit_summary_canvas.SaveAs("fit_summary_"+sample_and_d0_region+".pdf", "recreate")
        fit_summary_canvas.SaveAs("fit_summary_"+sample_and_d0_region+".png", "recreate")

        # fit parameters plot
        fit_parameters_canvas = make_default_canvas(sample_and_d0_region+"_fit_pars")
        fit_parameters_plot.SetMarkerStyle(8)
        err_ellipse = ErrorEllipse(fit_parameters_plot)
        fit_parameters_mean = TGraph()
        fit_parameters_mean.SetMarkerColor(4)
        fit_parameters_mean.SetMarkerStyle(8)
        fit_parameters_mean.SetPoint(0, err_ellipse.mean[0], err_ellipse.mean[1])
        par_mg = TMultiGraph()
        par_mg.Add(fit_parameters_plot, "P")
        par_mg.Add(fit_parameters_mean, "P")
        par_mg.Draw("A")
        setup_plot(par_mg, "Fit parameters for "+model, "Parameter [0]", "Parameter [1]")
        err_ellipse.ellipse.Draw("same")
        par_legend = TLegend(0.5, 0.7, 0.89, 0.89)
        par_legend.AddEntry(fit_parameters_plot, "Individual fit parameters", "P")
        par_legend.AddEntry(fit_parameters_mean, "Mean fit parameters", "P")
        par_legend.AddEntry(err_ellipse.ellipse, "One-sigma uncertainty ellipse", "L")
        par_legend.SetBorderSize(0)
        par_legend.Draw()
        fit_parameters_canvas.Write()
        fit_parameters_canvas.SaveAs("fit_parameters_"+sample_and_d0_region+".pdf", "recreate")
        fit_parameters_canvas.SaveAs("fit_parameters_"+sample_and_d0_region+".png", "recreate")

        # mean fit plot
        mean_fit_canvas = make_default_canvas(sample_and_d0_region+"_mean_fit")
        # estimate background using mean fit parameters
        fit_func.FixParameter(0, err_ellipse.mean[0])
        fit_func.FixParameter(1, err_ellipse.mean[1])
        b_over_a.improve_binning(error_tolerance, fit_ranges[0][1])
        b_over_a_plot = b_over_a.get_plot()
        b_over_a_plot.Fit(fit_func, "", "", fit_ranges[0][0], fit_ranges[0][1])
        mean_fit = b_over_a_plot.GetFunction(sample+"_fit")
        print "mean fit chisq/dof is: "+ str(mean_fit.GetChisquare()/mean_fit.GetNDF())
        mean_estimate_hist = make_estimate_hist(in_hists['c'].Clone(), mean_fit)
        mean_estimate, _, _ = do_closure_test(mean_estimate_hist, in_hists['d'])
        # make plot
        mean_fit_plot = TMultiGraph()
        mean_fit_plot.Add(b_over_a_plot, "P")
        if arguments.unblind:
            d_over_c_plot = d_over_c.get_plot() # get new instance of plot so pyroot doesn't get confused
            mean_fit_plot.Add(d_over_c_plot, "P")
        mean_fit_plot.Draw("A")
        mean_fit_plot.GetXaxis().SetLimits(0, pt_max)
        setup_plot(mean_fit_plot, sample+" mean fit",
                   str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
        mean_fit.SetRange(0, pt_max)
        mean_fit_plot.Draw("same") # draw again so points aren't covered by fit lines
        mean_fit_plot.GetYaxis().SetRangeUser(0, mean_fit_plot.GetYaxis().GetXmax())
        err_ellipse.find_estimate_bounds(fit_func, in_hists)
        err_ellipse.min_fit.Draw("same")
        err_ellipse.max_fit.Draw("same")
        err_ellipse.min_fit.SetRange(fit_ranges[0][1], d_estimate_hist.GetXaxis().GetXmax())
        err_ellipse.max_fit.SetRange(fit_ranges[0][1], d_estimate_hist.GetXaxis().GetXmax())
        draw_lines([fit_ranges[0][0], fit_ranges[0][1]])
        # add text with closure test results
        results_pave = TPaveText(0.5, 0.7, 0.8, 0.8, "NDC")
        results_pave.AddText("Actual yield: " + str(round(actual_yield, 1)) + " +- "
                             + str(round(actual_error, 1)) + " events")
        # fixme: cosmetic cleanup needed
        err_up = round(err_ellipse.max_estimate - mean_estimate, 1)
        err_down = round(mean_estimate - err_ellipse.min_estimate, 1)
        if err_up == err_down:
            estimate_uncertainty_string = " +- {}".format(err_up)
        else:
            estimate_uncertainty_string = " +{}/-{}".format(err_up, err_down)
        results_pave.AddText("Mean fit estimated yield: {}{} events".format(
                             round(mean_estimate, 1), estimate_uncertainty_string))
        results_pave.SetTextSize(0.025)
        results_pave.SetFillColor(0)
        results_pave.SetBorderSize(0)
        results_pave.SetTextAlign(11)
        results_pave.Draw()
        mean_fit_canvas.Write()
        mean_fit_canvas.SaveAs("mean_fit_"+sample_and_d0_region+".pdf","recreate")
        mean_fit_canvas.SaveAs("mean_fit_"+sample_and_d0_region+".png","recreate")

        # divide bg estimate into non-overlapping pT bins
        for pt_lo, pt_hi in zip(pt_cuts, pt_cuts[1:]+[int(pt_max)]):
            estimate, _, _ = do_closure_test(mean_estimate_hist, in_hists['d'] , pt_lo, pt_hi)
            bg_estimates[sample][d0_0_cut][pt_lo] = estimate
            # fixme: add uncertainties

    # in |d0|-|d0| plane, subtract estimate from more displaced signal regions
    # to create non-overlapping L-shaped signal regions
    for d0_0, next_d0_0 in zip(d0_0_cuts[:-1], d0_0_cuts[1:]):
        for pt in pt_cuts:
            bg_estimates[sample][d0_0][pt] -= bg_estimates[sample][next_d0_0][pt]
            # fixme: propagate uncertainty

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
            sr['d0_max'] = d0_0_max # fixme: assuming d0_0_max == d0_1_max
            sr['estimate'] = bg_estimates[s][d0_0_lo][pt_lo]
            sr['stat_err'] = 0 # fixme
            sr['sys_err'] = 0 # fixme
            bg_estimate_output[s].append(sr)

import json
output_estimates = open(output_path + "background_estimate.json", "w")
json = json.dump(bg_estimate_output, output_estimates, sort_keys=True, indent=4)

output_plots.Close()
output_estimates.close()

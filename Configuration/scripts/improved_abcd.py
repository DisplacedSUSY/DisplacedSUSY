#!/usr/bin/env python

import sys
import os
import re
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
gStyle.SetOptFit(0) # fixme: ideally this would be set on a plot-by-plot basis
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
    for b in range(1, transfer_factor_hist.GetNbinsX()+1):
        transfer_factor_hist.SetBinContent(b, fit.Eval(transfer_factor_hist.GetBinCenter(b)))
        transfer_factor_hist.SetBinError(b, 0) # fixme: account for fit uncertainty
    d_estimate_hist = c_hist.Clone()
    d_estimate_hist.Multiply(transfer_factor_hist)
    return d_estimate_hist

def do_closure_test(estimate_hist, d_hist):
    estimate = estimate_hist.Integral(0, estimate_hist.GetNbinsX())
    #print "estimate:", round(estimate, 2)
    if arguments.unblind:
        actual_error = Double()
        actual_yield = d_hist.IntegralAndError(0, d_hist.GetNbinsX(), actual_error)
        #print "actual:", round(actual_yield, 2), "+-", round(actual_error, 2)
    else:
        #print "actual: BLINDED"
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

out_file = TFile(output_path + "improved_abcd_results.root", "recreate")

for sample in samples:
    fit_summary_plot = TMultiGraph()
    fit_summary_legend = TLegend(0.4, 0.5, 0.89, 0.87)
    fit_summary_legend.AddEntry(None, "", "") # add blank entry for spacing
    fit_parameters_plot = TGraph()
    color_ix = 0
    print "\n" + sample

    # get histograms and statistical uncertainties for all regions
    in_hists = {}
    in_file = TFile(output_path + sample + ".root")
    in_hist = in_file.Get(input_hist)
    if not in_hist:
        print "Warning: could not load " + input_hist
    xaxis = in_hist.GetXaxis()
    yaxis = in_hist.GetYaxis()
    zaxis = in_hist.GetZaxis()
    d0_0_max = d0_0_max if d0_0_max else in_hist.GetXaxis().GetXmax()
    d0_1_max = d0_1_max if d0_1_max else in_hist.GetYaxis().GetXmax()
    pt_max   = pt_max if pt_max else in_hist.GetZaxis().GetXmax()
    cut_bin_x = xaxis.FindBin(d0_0_cut)
    cut_bin_y = yaxis.FindBin(d0_1_cut)
    cut_bin_z = zaxis.FindBin(pt_cut)
    min_bin_z = zaxis.FindBin(fit_min)
    max_bin_x = xaxis.FindBin(d0_0_max)
    max_bin_y = yaxis.FindBin(d0_1_max)
    max_bin_z = zaxis.FindBin(pt_max)

    #in below: cut_bin_x, or cut_bin_x-1, or cut_bin_x+1 ?
    #also: check underflow/overflow
    in_hists['a'] = in_hist.ProjectionZ("a", #PromptLowPtControlRegion
                                   1,#x min bin
                                   cut_bin_x,#x max bin
                                   1,#ymin
                                   cut_bin_y,#ymax
                                   "eo")
    for b in range(1, min_bin_z) + range(cut_bin_z, in_hist.GetNbinsZ()+1):
        in_hists['a'].SetBinContent(b,0)
        in_hists['a'].SetBinError(b,0)
    error = Double()
    print "number of events in A is: "+str(in_hists['a'].IntegralAndError(0,in_hists['a'].GetNbinsX(),error))+" +/- "+str(error)

    in_hists['b'] = in_hist.ProjectionZ("b", #DisplacedLowPtControlRegion
                                   cut_bin_x,#x min bin
                                   max_bin_x,#x max bin
                                   cut_bin_y,#ymin
                                   max_bin_y,#ymax
                                   "eo")
    for b in range(1, min_bin_z) + range(cut_bin_z, in_hist.GetNbinsZ()+1):
        in_hists['b'].SetBinContent(b,0)
        in_hists['b'].SetBinError(b,0)
    print "number of events in B is: "+str(in_hists['b'].IntegralAndError(0,in_hists['b'].GetNbinsX(),error))+" +/- "+str(error)

    in_hists['c'] = in_hist.ProjectionZ("c", #PromptHighPtControlRegion
                                   1,#x min bin
                                   cut_bin_x,#x max bin
                                   1,#ymin
                                   cut_bin_y,#ymax
                                   "eo")
    for b in range(1, cut_bin_z) + range(max_bin_z, in_hist.GetNbinsZ()+1):
        in_hists['c'].SetBinContent(b,0)
        in_hists['c'].SetBinError(b,0)
    print "number of events in C is: "+str(in_hists['c'].IntegralAndError(0,in_hists['c'].GetNbinsX(),error))+" +/- "+str(error)

    in_hists['d'] = in_hist.ProjectionZ("d", #DisplacedHighPtControlRegion (signal region)
                                   cut_bin_x,#x min bin
                                   max_bin_x,#x max bin
                                   cut_bin_y,#ymin
                                   max_bin_y,#ymax
                                   "eo")
    for b in range(1, cut_bin_z) + range(max_bin_z, in_hist.GetNbinsZ()+1):
        in_hists['d'].SetBinContent(b,0)
        in_hists['d'].SetBinError(b,0)
    if arguments.unblind:
        print "number of events in D is: "+str(in_hists['d'].IntegralAndError(0,in_hists['d'].GetNbinsX(),error))+" +/- "+str(error)

    # set up fit model
    model = "[0] + [1]/x" # |d0| resolution as a function of pT
    fit_func = TF1(sample + "_fit", model, 0, in_hists['a'].GetXaxis().GetXmax())
    fit_func.SetParLimits(0, 0, 100)
    fit_func.SetParLimits(1, 0, 100)

    # fit B/A once per fit range
    for fit_range in fit_ranges:
        b_over_a = RatioPlot(in_hists['b'], in_hists['a'])
        b_over_a_plot = b_over_a.get_plot()
        b_over_a_plot.Fit(fit_func, "", "", fit_range[0], fit_range[1])
        fit = b_over_a_plot.GetFunction(sample+"_fit")
        chisq_per_dof = fit.GetChisquare()/fit.GetNDF()

        # calculate d(pT) = c(pT) * model(pT) and do closure test
        d_estimate_hist = make_estimate_hist(in_hists['c'].Clone(), fit)
        estimate, actual_yield, actual_error = do_closure_test(d_estimate_hist, in_hists['d'])

        # save once-per-fit plots
        out_file.cd()
        sample_and_range = sample + "_" + str(fit_range[0])

        # estimated and actual pT distribution in region D
        d_canvas = make_default_canvas(sample_and_range+"_d")
        d_estimate_hist.SetTitle(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetName(sample_and_range + " d estimate and actual")
        d_estimate_hist.SetLineColor(2)
        d_estimate_hist.Draw()
        if arguments.unblind:
            in_hists['d'].Draw("sames")
        d_canvas.Write()

        # fits and combined B/A and D/C plot
        fit_canvas = make_default_canvas(sample_and_range+"_fit")
        b_over_a_plot.PaintStats(fit)
        fit_plot = TMultiGraph()
        fit_plot.Add(b_over_a_plot, "P")
        if arguments.unblind:
            d_over_c = RatioPlot(in_hists['d'], in_hists['c'])
            upper_edge = pt_max
            # use 2*error_tolerance due to lower stats in c and d regions
            d_over_c.improve_binning(error_tolerance*2, upper_edge)
            d_over_c_plot = d_over_c.get_plot()
            fit_plot.Add(d_over_c_plot, "P")
        fit_plot.Draw("A")
        setup_plot(fit_plot, sample_and_range+" fit",
                    str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
        fit.SetRange(0, 500)
        draw_lines([fit_range[0], fit_range[1]])
        fit_canvas.Write()

        # add fit plots to fit summary plot
        fit.SetLineColor(colors[color_ix])
        b_over_a_plot = b_over_a_plot.Clone() # get new instance of plot with fit information
        b_over_a_plot.SetMarkerStyle(6)
        b_over_a_plot.SetMarkerColor(colors[color_ix])
        b_over_a_plot.SetLineColor(colors[color_ix])
        fit_summary_plot.Add(b_over_a_plot, "PX")
        fit_summary_legend.AddEntry(b_over_a_plot, str(fit_range[0]) + " GeV --> " +
                                    str(round(estimate, 2)) + " events; chisq/dof is "
                                    + str(round(chisq_per_dof,2)))
        if arguments.unblind:
            d_over_c_plot = d_over_c.get_plot() # get new instance of plot so pyroot doesn't get confused
            d_over_c_plot.SetMarkerStyle(6)
            d_over_c_plot.SetMarkerColor(colors[color_ix])
            d_over_c_plot.SetLineColor(colors[color_ix])
            fit_summary_plot.Add(d_over_c_plot, "PX")
        color_ix = (color_ix + 1) % len(colors)

        # add point to fit parameter plot
        fit_parameters_plot.SetPoint(fit_parameters_plot.GetN(),
                                    fit.GetParameter(0), fit.GetParameter(1))

    # save once-per-sample plots
    # input hists
    a_canvas = make_default_canvas(sample+"_a")
    in_hists['a'].Draw()
    a_canvas.Write()
    b_canvas = make_default_canvas(sample+"_b")
    in_hists['b'].Draw()
    b_canvas.Write()
    c_canvas = make_default_canvas(sample+"_c")
    in_hists['c'].Draw()
    c_canvas.Write()

    # fit summary plot
    fit_summary_canvas = make_default_canvas(sample+"_fit_summary")
    fit_summary_plot.Draw("A")
    setup_plot(fit_summary_plot, sample+" fit summary",
               str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
    fit_summary_legend.SetHeader(
        "#splitline{Fit Range Lower Bound --> Corresponding BG Estimate}{(Actual yield is "
        + str(round(actual_yield, 1)) + " +- " + str(round(actual_error, 1)) + " events)}")
    fit_summary_legend.SetTextSize(0.025)
    fit_summary_legend.SetBorderSize(0)
    fit_summary_legend.Draw()
    draw_lines([fit_range[1]])
    fit_summary_canvas.Write()
    fit_summary_canvas.SaveAs("fit_summary.pdf", "recreate")
    fit_summary_canvas.SaveAs("fit_summary.png", "recreate")

    # fit parameters plot
    fit_parameters_canvas = make_default_canvas(sample+"_fit_pars")
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
    fit_parameters_canvas.SaveAs("fit_parameters.pdf", "recreate")
    fit_parameters_canvas.SaveAs("fit_parameters.png", "recreate")

    # mean fit plot
    mean_fit_canvas = make_default_canvas(sample+"_mean_fit")
    # estimate background using mean fit parameters
    fit_func.FixParameter(0, err_ellipse.mean[0])
    fit_func.FixParameter(1, err_ellipse.mean[1])
    b_over_a.improve_binning(error_tolerance, fit_ranges[0][1])
    b_over_a_plot = b_over_a.get_plot()
    b_over_a_plot.Fit(fit_func, "", "", fit_ranges[0][0], fit_ranges[0][1]) # use initial fit range
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
    setup_plot(mean_fit_plot, sample+" mean fit",
               str(d_estimate_hist.GetXaxis().GetTitle()), "B/A or D/C")
    mean_fit.SetRange(0, 500)
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
    if round(err_ellipse.max_estimate-mean_estimate, 1) == round(mean_estimate-err_ellipse.min_estimate, 1):
        estimate_uncertainty_string = " +- " + str(round(err_ellipse.max_estimate-mean_estimate, 1))
    else:
        estimate_uncertainty_string = (" +" + str(round(err_ellipse.max_estimate-mean_estimate, 1)) +
                                       "/-" + str(round(mean_estimate-err_ellipse.min_estimate, 1)))
    results_pave.AddText("Mean fit estimated yield: " + str(round(mean_estimate, 1)) +
                                                      estimate_uncertainty_string + " events")
    results_pave.SetTextSize(0.025)
    results_pave.SetFillColor(0)
    results_pave.SetBorderSize(0)
    results_pave.SetTextAlign(11)
    results_pave.Draw()
    mean_fit_canvas.Write()
    mean_fit_canvas.SaveAs("mean_fit.pdf","recreate")
    mean_fit_canvas.SaveAs("mean_fit.png","recreate")

    # 3D mean estimate histogram
    estimate_hist = in_hist.Clone()
    estimate_hist.SetName(sample + "_estimate")
    estimate_hist.SetTitle(sample + "_estimate")
    # create bins for each signal region
    x_edges = [d0_0_cut, d0_0_max]
    y_edges = [d0_1_cut, d0_1_max]
    z_edges = [pt_cut, pt_max]
    estimate_hist.SetBins(len(x_edges)-1, array('d', x_edges),
                          len(y_edges)-1, array('d', y_edges),
                          len(z_edges)-1, array('d', z_edges))
    # fill hist with mean estimate and statistical uncertainty
    for x in x_edges[:-1]:
        x_bin = estimate_hist.GetXaxis().FindBin(x)
        for y in y_edges[:-1]:
            y_bin = estimate_hist.GetYaxis().FindBin(y)
            for z in z_edges[:-1]:
                z_bin = estimate_hist.GetZaxis().FindBin(z)
                bin_num = estimate_hist.GetBin(x_bin, y_bin, z_bin)
                estimate_hist.SetBinContent(bin_num, mean_estimate)
                estimate_hist.ResetStats()
                # fixme: add statistical uncertainty from abcd
    estimate_hist.Write()


out_file.Close()

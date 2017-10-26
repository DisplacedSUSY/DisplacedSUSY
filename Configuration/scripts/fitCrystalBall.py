#!/usr/bin/env python

import sys
import glob
import re
import os
from array import *
from ROOT import *
from math import fabs, exp, floor, log10

#lepton = "muon"
lepton = "electron"
fname = 'stacked_histograms.root'
fin = TFile(fname)
fout = TFile(lepton+"_fits.root","RECREATE")

def round_sig(x):
    return round(x, -int(floor(log10(abs(x))))++2)

def doubleCrystalBall(input, params):

#    print "inputs", params
    x = input[0]
    N = params[0]
    mu = params[1]
    sig = params[2]
    if not sig:
        sig = 1
   
    a = fabs(params[3])
    n = params[4]
    if n <= 1:
        n = 1.01

#    print N,mu,sig,a,n

    u = (x-mu)/sig
    A = ((n/a)**n)*exp(-a*a/2)
    B = n/a - a

    result = N
    if   u < -a:   result *= A*(B-u)**-n
    elif u < a:    result *= exp(-u*u/2)
    else:           result *= A*(B+u)**-n


    return result

#dir = "ZControlRegionPlotter/" + lepton.capitalize() + "-beamspot Plots/"
dir = "ZControlRegionPlotter/" + lepton.capitalize() + " Plots/"


plot_names = []

plot_limits = ["100um","200um","500um","1mm","2mm","5mm","1cm","2cm","5cm"]
plot_names.extend(lepton+"D0_"+limit for limit in plot_limits)
plot_names.extend(lepton+"AbsD0_"+limit for limit in plot_limits)
plot_limits = ["100um_variableBins","200um_variableBins","500um_variableBins","1mm_variableBins","2mm_variableBins","5mm_variableBins","1cm_variableBins","2cm_variableBins","5cm_variableBins"]
plot_names.extend(lepton+"AbsD0_"+limit for limit in plot_limits)
plot_limits = ["5","10","20","50","100","200","500"]
plot_names.extend(lepton+"D0Sig_"+limit for limit in plot_limits)
plot_names.extend(lepton+"AbsD0Sig_"+limit for limit in plot_limits)

for plot_name in plot_names:
    print "fitting", plot_name
    canvas = fin.Get(dir+plot_name)
    canvas.cd()
    canvas.SetLogy()
    mc = canvas.FindObject("stack").GetStack().Last()
    data = canvas.FindObject(plot_name)

    list = []
    for item in canvas.GetListOfPrimitives():
        if item.InheritsFrom("TPave"):
            list.append(item.GetName())
    for item in list:
        canvas.GetListOfPrimitives().Remove(canvas.FindObject(item))

    min = mc.GetXaxis().GetXmin()
    max = mc.GetXaxis().GetXmax()

    fit_mc = TF1("fit_mc",doubleCrystalBall,min,max,5);
    fit_data = TF1("fit_data",doubleCrystalBall,min,max,5);

    if "Sig" in plot_name:

        # good parameters for d0_sig distributions
        
        fit_mc.SetParameter(0,1000000)  # N
        fit_mc.SetParLimits(0,0,100000000)
        fit_mc.SetParameter(1,0)  # mean
        fit_mc.SetParLimits(1,-0.5,0.5)
        fit_mc.SetParameter(2,10) # sigma
        fit_mc.SetParLimits(2,1,30)
        fit_mc.SetParameter(3,2)  # a
        fit_mc.SetParLimits(3,0.1,5)
        fit_mc.SetParameter(4,2)  # n
        fit_mc.SetParLimits(4,1.01,20)
        
        fit_data.SetParameter(0,1000000)  # N
        fit_data.SetParLimits(0,0,100000000)
        fit_data.SetParameter(1,0)  # mean
        fit_data.SetParLimits(1,-0.5,0.5)
        fit_data.SetParameter(2,10) # sigma
        fit_data.SetParLimits(2,1,30)
        fit_data.SetParameter(3,2)  # a
        fit_data.SetParLimits(3,0.1,5)
        fit_data.SetParameter(4,2)  # n
        fit_data.SetParLimits(4,1.01,20)

    else:

        fit_mc.SetParameter(0,1000000)  # N
        fit_mc.SetParLimits(0,0,100000000)
        fit_mc.SetParameter(1,0)  # mean
        fit_mc.SetParLimits(1,-10,10)
        fit_mc.SetParameter(2,15) # sigma
        fit_mc.SetParLimits(2,10,100)
        fit_mc.SetParameter(3,3)  # a
        fit_mc.SetParLimits(3,0.1,10)
        fit_mc.SetParameter(4,2)  # n
        fit_mc.SetParLimits(4,1.01,20)
    
        fit_data.SetParameter(0,1000000)  # N
        fit_data.SetParLimits(0,0,100000000)
        fit_data.SetParameter(1,0)  # mean
        fit_data.SetParLimits(1,-1,1)
        fit_data.SetParameter(2,15) # sigma
        fit_data.SetParLimits(2,10,100)
        fit_data.SetParameter(3,3)  # a
        fit_data.SetParLimits(3,0.1,10)
        fit_data.SetParameter(4,2)  # n
        fit_data.SetParLimits(4,1.01,20)
    



    mc.Fit(fit_mc,"LNQRB")
    data.Fit(fit_data,"LNQRB")

    fit_data.SetLineColor(kCyan+1)
    fit_data.SetLineWidth(5)
    fit_mc.SetLineWidth(5)
    fit_mc.Draw("same")
    fit_data.Draw("same")

    names = ['N','#mu','#sigma','a','n']

    legend_data = TLegend(0.65,0.7,0.8,0.9)
    legend_data.SetBorderSize(0)
    legend_data.SetFillColor(0)
    legend_data.SetFillStyle(0)
    legend_data.AddEntry(fit_data,"data fit","L")
    for i in range(5):
        value = str(round_sig(fit_data.GetParameter(i)))
        toprint = value.rstrip('0').rstrip('.') if '.' in value else value
        legend_data.AddEntry(0, names[i] + ": " + toprint,"H")
    legend_data.Draw("same")

    legend_mc = TLegend(0.8,0.7,0.95,0.9)
    legend_mc.SetBorderSize(0)
    legend_mc.SetFillColor(0)
    legend_mc.SetFillStyle(0)
    legend_mc.AddEntry(fit_mc,"MC fit","L")
    for i in range(5):
        value = str(round_sig(fit_mc.GetParameter(i)))
        toprint = value.rstrip('0').rstrip('.') if '.' in value else value
        legend_mc.AddEntry(0, names[i] + ": " + toprint,"H")
    legend_mc.Draw("same")


    fout.cd()
    gPad.Update()
    gPad.Modified()
    gPad.RedrawAxis()
    canvas.Write()


fout.Close()

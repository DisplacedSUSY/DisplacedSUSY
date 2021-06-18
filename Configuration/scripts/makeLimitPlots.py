#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
import glob
import numpy as np
from array import *
from operator import itemgetter

from DisplacedSUSY.Configuration.limitOptions import *
from DisplacedSUSY.StandardAnalysis.Options import *

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if arguments.condorDir:
    if not os.path.exists("limits/"+arguments.condorDir):
        os.system("mkdir limits/"+arguments.condorDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)

from DisplacedSUSY.Configuration.systematicsDefinitions import signal_cross_sections_13TeV, signal_cross_sections_sleptons_13TeV, signal_cross_sections_staus_13TeV, signal_cross_sections_HToSS_13TeV
signal_cross_sections = {}

from ROOT import TFile, TGraph,TH2F, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel, TH2D, TPave, Double, TTree, TGaxis

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.20)
gStyle.SetPadBottomMargin(0.20)
gStyle.SetPadLeftMargin(0.20)
gStyle.SetPadRightMargin(0.20)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.05, "XYZ")
gStyle.SetTitleXSize(0.04)
gStyle.SetTitleXOffset(1.25)
gStyle.SetTitleYSize(0.04)
gStyle.SetTitleYOffset(1.5)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.005, "XYZ")
gStyle.SetLabelSize(0.04, "YZ")
gStyle.SetLabelSize(0.033, "X")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetPadTickX(1)
if not arguments.ns:
    gStyle.SetPadTickY(1)
gROOT.ForceStyle()

#bestest place for lumi. label, in top left corner
topLeft_x_left    = 0.2
y_bottom  = 0.8
topLeft_x_right   = 0.6
y_top     = 0.85

#position for header
header_x_left    = 0.45
header_x_right   = 0.81

colorSchemes = {
    'susy_pag' : {
        'obs' : 1,
        'exp' : 632,
        'oneSigma' : 632,
        'twoSigma' : 632,
    },
    'brazilian' : {
        'obs' : 1,
        'exp' : 4,
        'oneSigma' : 417,
        'twoSigma' : 800,
    },
    'theory' : {
        'obs' : 1,
        'exp' : 1,
        'oneSigma' : 921,
        'twoSigma' : 920,
    },
    'red' : {
        'obs' : 632,
        'exp' : 632,
        'oneSigma' : 632,
        'twoSigma' : 632,
    },
    'blue' : {
        'obs' : 600,
        'exp' : 600,
        'oneSigma' : 600,
        'twoSigma' : 600,
    },
    'green' : {
        'obs' : 413,
        'exp' : 413,
        'oneSigma' : 413,
        'twoSigma' : 413,
    },
    'purple' : {
        'obs' : 882,
        'exp' : 882,
        'oneSigma' : 882,
        'twoSigma' : 882,
    },
    'yellow' : {
        'obs' : 402,
        'exp' : 402,
        'oneSigma' : 402,
        'twoSigma' : 402,
    },
    'orange' : {
        'obs' : 806,
        'exp' : 806,
        'oneSigma' : 806,
        'twoSigma' : 806,
    },
    'magenta' : {
        'obs' : 616,
        'exp' : 616,
        'oneSigma' : 616,
        'twoSigma' : 616,
    },
    'black' : {
        'obs' : 1,
        'exp' : 1,
        'oneSigma' : 1,
        'twoSigma' : 1,
    },
}

#set the text for the luminosity label
if isinstance(intLumi, list):
    LumiInFb = [l/1000. for l in intLumi]
    LumiInFb = [int(round(l)) for l in LumiInFb]
    LumiText = "{:d}-{:d} fb^{{-1}}".format(*LumiInFb)
else:
    LumiInFb = intLumi/1000.
    LumiText = "{:d} fb^{{-1}}".format(int(round(LumiInFb)))

HeaderText = LumiText + " (" + energy + " TeV)"

if(HToSS):
    massesNames = []
    for H, S in zip(bareMasses.keys(),bareMasses.values()):
        for i in S:
            massesNames.append(str(H)+"_"+str(i))
else:
    massesNames = masses

def moveFile(old_name, new_name):
    if glob.glob(old_name):
        os.system("mv -f {} {}".format(old_name, new_name))
    return new_name if os.path.isfile(new_name) else False

def makeSignalName(process, mass, lifetime):
    name = process + str(mass) + "_" + str(lifetime) + "mm"
    # rename sub-mm samples to match sample names
    name = name.replace('.', 'p')
    return name

def makeSignalRootFileName(process, mass, lifetime, directory, limit_type):
    signal_name = makeSignalName(process, mass, lifetime)
    base_path = "limits/"+directory+"/"+signal_name+"_"+limit_type
    old_name = base_path+"/higgsCombine"+signal_name+".*.root"
    new_name = base_path+"/limits_"+signal_name+".root"
    # fixme: why change file name?
    return moveFile(old_name, new_name)

def makeSignalLogFileName(process, mass, lifetime, directory, limit_type):
    signal_name = makeSignalName(process, mass, lifetime)
    old_name = "limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0*.out"
    new_name = "limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".log"
    # fixme: why change file name?
    return moveFile(old_name, new_name)

def getSignalSF(mass, lifetime, directory, type_):
    signal_name = makeSignalName(process, mass, lifetime)
    signalSFFile = glob.glob("limits/"+directory+"/"+signal_name+"_"+type_+"/*.sf")
    if not signalSFFile:
        return 1.0
    f = open(signalSFFile[0], "r")
    signalSF = f.readline().rstrip()
    return float(signalSF)

def setCrossSections():
    global signal_cross_sections
    if energy == '8':
        signal_cross_sections = signal_cross_sections_8TeV
    elif energy == '13':
        if(HToSS):
            signal_cross_sections = signal_cross_sections_HToSS_13TeV
        elif(GMSBstaus):
            signal_cross_sections = signal_cross_sections_staus_13TeV
        elif(GMSB):
            signal_cross_sections = signal_cross_sections_sleptons_13TeV
        else:
            signal_cross_sections = signal_cross_sections_13TeV #stops
    else:  # use run2 by default
        print "invalid energy = " + energy + " -- using default stop 13 TeV cross sections"
        signal_cross_sections = signal_cross_sections_13TeV

    # convert all values and uncertainties to floats
    for mass in signal_cross_sections.keys():
        d = signal_cross_sections[mass]
        d.update((k, float(v)) for k, v in d.iteritems())

def getTheoryGraph():
    x = [ ]
    y = [ ]
    if HToSS:
        for mass in masses.keys():
            xSection = signal_cross_sections[str(mass)]['value']
            x.append(float(mass))
            y.append(xSection)
    else:
        for mass in masses:
            xSection = signal_cross_sections[str(mass)]['value']
            x.append(float(mass))
            y.append(xSection)

    graph = TGraph(len(x), array('d', x), array('d', y))
    graph.SetLineWidth(3)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes['theory']['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes['theory']['exp'])
    return graph

def makeTGraphAsymmErrors(x, y, x_lo, x_hi, y_lo, y_hi):
    graph_arrays = [array('d', arg) for arg in [x, y, x_lo, x_hi, y_lo, y_hi]]
    return TGraphAsymmErrors(len(x), *graph_arrays)

def getTheoryOneSigmaGraph():
    x = []
    y = []
    up = []
    down = []
    if HToSS:
        for mass in masses.keys():
            xSection = signal_cross_sections[str(mass)]['value']
            xSectionError = signal_cross_sections[str(mass)]['error']
            x.append(float(mass))
            y.append(xSection)
            up.append((xSectionError - 1.0)*xSection)
            down.append((xSectionError - 1.0)*xSection)
    else:
        for mass in masses:
            xSection = signal_cross_sections[str(mass)]['value']
            xSectionError = signal_cross_sections[str(mass)]['error']
            x.append(float(mass))
            y.append(xSection)
            up.append((xSectionError - 1.0)*xSection)
            down.append((xSectionError - 1.0)*xSection)

    graph = makeTGraphAsymmErrors(x, y, [0]*len(x), [0]*len(x), down, up)
    graph.SetFillColor(colorSchemes['theory']['oneSigma'])
    graph.SetFillStyle(0)
    graph.SetLineColor(colorSchemes['theory']['oneSigma'])
    graph.SetMarkerColor(colorSchemes['theory']['oneSigma'])
    return graph

def getGraph(limits, x_key, y_key):
    x = []
    y = []
    for limit in limits:
        if not limit.has_key(x_key) or not limit.has_key(y_key):
            continue
        x.append(float(limit[x_key]))
        y.append(float(limit[y_key]))

    graph = TGraph(len(x), array('d', x), array('d', y))
    return graph

def getBRGraph(limits, x_key, y_key): #branching ratio 1D graph
    x = []
    y = []
    for limit in limits:
        if not limit.has_key(x_key) or not limit.has_key(y_key):
            continue
        if(HToSS):
            end = str(limit['mass']).find("_")
            mass = int(limit['mass'][:end])
        else:
            mass = int(limit['mass'])
        xSection = signal_cross_sections[str(mass)]['value']

        if arguments.mm:
            x.append(10.*float(limit[x_key])) #convert lifetimes from cm to mm
        else:
            x.append(float(limit[x_key])) #convert lifetimes from cm to mm
        y.append(float(limit[y_key])/xSection) #exp or obs limit divided by theory cross section

    graph = TGraph(len(x), array('d', x), array('d', y))
    return graph

def getBinArray(key, dictionaries):
    if(HToSS):
        bins = []
        for d in dictionaries:
            end = str(d[key]).find("_")
            bins.append(float(str(d[key])[:end]))
    else:
        bins = [float(d[key]) for d in dictionaries]
    bins = sorted(list(set(bins)))
    bins.append(bins[-1] + 100.0)
    return array("d", bins)

def getTH2F(limits, x_key, y_key, experiment_key, theory_key):
    x_bins = getBinArray('mass', limits)
    y_bins = getBinArray('lifetime', limits)
    gridPlot = TH2F("", "", len(x_bins)-1, x_bins, len(y_bins)-1, y_bins)
    gridPlot.SetContour(500)
    bin_content = []
    limit_dict = {}
    for limit in limits:
        if(HToSS):
            end = str(limit['mass']).find("_")
            mass = float(limit['mass'][:end])
        else:
            mass = float(limit['mass'])
        lifetime = float(limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_val = limit[experiment_key]
        if experiment_key == 'up1' or experiment_key == 'up2':
            limit_val += limit['expected']
        elif experiment_key == 'down1' or experiment_key == 'down2':
            limit_val = limit['expected'] - limit_val
        limit_dict[lifetime][mass]['experiment'] = limit_val
        for theory_mass in signal_cross_sections:
            if abs(float(theory_mass) - mass) < 1.0e-3:
                theory_val = signal_cross_sections[theory_mass]['value']
                theory_error = signal_cross_sections[theory_mass]['error']
                if theory_key == 'up2' or theory_key == 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                elif theory_key == 'up1' or theory_key == 'up2':
                    theory_val *= theory_error
                elif theory_key == 'down1' or theory_key == 'down2':
                    theory_val *= (2.0 - theory_error)
                limit_dict[lifetime][mass]['theory'] = theory_val
    for lifetime in sorted(limit_dict.keys()):
        ordered_masses = sorted(limit_dict[lifetime].keys())
        for mass in ordered_masses:
            limit_point = limit_dict[lifetime][mass]['experiment']
            bin_content.append(limit_point)
            gridPlot.Fill(mass, lifetime, limit_point)
    th2f = gridPlot
    th2f.SetDirectory(0)
    th2f.SetMaximum(th2f.GetMaximum())
    min_val = 0.9*min(c for c in bin_content if c > 0)
    th2f.SetMinimum(min_val)
    print "maximum bin content of th2f is: "+str(th2f.GetBinContent(th2f.GetMaximumBin()))
    print "minimum bin content of th2f is: "+str(th2f.GetBinContent(th2f.GetMinimumBin()))
    th2f.GetZaxis().SetRangeUser(0.0001,10) #based on max and min, need to always check! the point is to normalize all similar 2D histograms
    return th2f

def getGraph2D(limits, x_key, y_key, experiment_key, theory_key):
    x = array('d')
    y = array('d')
    limit_dict = {}
    for limit in limits:
        if(HToSS):
            end = str(limit['mass']).find("_")
            mass = float(limit['mass'][:end])
        else:
            mass = float(limit['mass'])
        lifetime = float(limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_val = limit[experiment_key]
        if experiment_key == 'up1' or experiment_key == 'up2':
            limit_val += limit['expected']
        if experiment_key == 'down1' or experiment_key == 'down2':
            limit_val = limit['expected'] - limit_val
        limit_dict[lifetime][mass]['experiment'] = limit_val
        for theory_mass in signal_cross_sections:
            if abs(float(theory_mass) - mass) < 1.0e-3:
                theory_val = signal_cross_sections[theory_mass]['value']
                theory_error = signal_cross_sections[theory_mass]['error']
                if theory_key == 'up2' or theory_key == 'down2':
                    theory_error = 1.0 + 2.0*(theory_error - 1.0)
                if theory_key == 'up1' or theory_key == 'up2':
                    theory_val *= theory_error
                if theory_key == 'down1' or theory_key == 'down2':
                    theory_val *= (2.0 - theory_error)
                limit_dict[lifetime][mass]['theory'] = theory_val
    for lifetime in sorted(limit_dict.keys()):
        ordered_masses = sorted(limit_dict[lifetime].keys())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] < limit_dict[lifetime][mass]['experiment']:
                first_allowed_mass = mass
                break
            previous_mass = mass
        mass_limit = 0.0
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass
            x3 = previous_mass
            x2 = first_allowed_mass
            x4 = first_allowed_mass
            try:
                y1 = math.log10(limit_dict[lifetime][previous_mass]['theory'])
                y3 = math.log10(limit_dict[lifetime][previous_mass]['experiment'])
                y2 = math.log10(limit_dict[lifetime][first_allowed_mass]['theory'])
                y4 = math.log10(limit_dict[lifetime][first_allowed_mass]['experiment'])
            except ValueError:
                print limit_dict[lifetime][previous_mass]['theory']
                print limit_dict[lifetime][previous_mass]['experiment']
                print limit_dict[lifetime][first_allowed_mass]['theory']
                print limit_dict[lifetime][first_allowed_mass]['experiment']
            mass_limit = (x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)
            mass_limit /= (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
            if math.isnan(mass_limit):
                mass_limit = 0.0

        x.append(mass_limit)
        y.append(lifetime)

        if x_key == 'lifetime' and y_key == 'mass':
            x[-1], y[-1] = y[-1], x[-1]

    graph = TGraph(len(x), x, y)
    return graph

def getObservedGraph(limits, xAxisType, colorScheme, lineStyle=1):
    if(arguments.doBR):
        graph = getBRGraph(limits, xAxisType, 'observed')
    else:
        graph = getGraph(limits, xAxisType, 'observed')
    graph.SetLineWidth(4)
    graph.SetLineStyle(lineStyle)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getObservedGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key, colorScheme,
                       lineStyle=1):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(4)
    graph.SetLineStyle(lineStyle)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getExpectedGraph(limits, xAxisType, colorScheme, lineStyle=7):
    if(arguments.doBR):
        graph = getBRGraph(limits, xAxisType, 'expected')
    else:
        graph = getGraph(limits, xAxisType, 'expected')
    graph.SetLineWidth(4)
    graph.SetLineStyle(lineStyle)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph

def getExpectedGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key, colorScheme,
                       lineStyle=7):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(4)
    graph.SetLineStyle(lineStyle)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph

def getGraphAsymmErrors(limits, x_key, y_key, up_key, down_key):
    x = []
    up = []
    down = []
    y = []
    for limit in limits:
        if not all(k in limit for k in [x_key, y_key, up_key, down_key]):
            continue
        if any(limit[k] < 0 for k in [x_key, y_key, up_key, down_key]):
            continue
        x.append(float(limit[x_key]))
        up.append(float(limit[up_key]))
        down.append(float(limit[down_key]))
        y.append(float(limit[y_key]))
    graph = makeTGraphAsymmErrors(x, y, [0]*len(x), [0]*len(x), down, up)
    return graph

def getBorderGraph(graph, errorType):
    N = graph.GetN()
    otherSideX = []
    otherSideY = []
    x = array('d')
    y = array('d')
    for i in range(N):
        xPoint = Double(0.0)
        yPoint = Double(0.0)
        graph.GetPoint(i, xPoint, yPoint)
        if errorType == 'horizontal':
            eHigh = graph.GetErrorXhigh(i)
            eLow = graph.GetErrorXlow(i)
            otherSideX.append(xPoint - eLow)
            otherSideY.append(yPoint)
            x.append(xPoint + eHigh)
            y.append(yPoint)
        if errorType == 'vertical':
            eHigh = graph.GetErrorYhigh(i)
            eLow = graph.GetErrorYlow(i)
            otherSideX.append(xPoint)
            otherSideY.append(yPoint - eLow)
            x.append(xPoint)
            y.append(yPoint + eHigh)
    for i in range(0, -N, -1):
        x.append(otherSideX[i - 1])
        y.append(otherSideY[i - 1])

    borderGraph = TGraph(len(x), x, y)
    return borderGraph

def getGraphAsymmErrors2D(limits, x_key, y_key, experiment_key, up_key, down_key):
    central = getGraph2D(limits, x_key, y_key, experiment_key, 'theory')
    up = TGraph()
    down = TGraph()
    if experiment_key == 'expected':
        up = getGraph2D(limits, x_key, y_key, down_key, 'theory')
        down = getGraph2D(limits, x_key, y_key, up_key, 'theory')
    if experiment_key == 'observed':
        up = getGraph2D(limits, x_key, y_key, 'observed', up_key)
        down = getGraph2D(limits, x_key, y_key, 'observed', down_key)
    x = []
    y = []
    eXLow = []
    eXHigh = []
    eYLow = []
    eYHigh = []
    for i in range(central.GetN()):
        xPoint = Double(0.0)
        yPoint = Double(0.0)
        upXPoint = Double(0.0)
        upYPoint = Double(0.0)
        downXPoint = Double(0.0)
        downYPoint = Double(0.0)
        central.GetPoint(i, xPoint, yPoint)
        up.GetPoint(i, upXPoint, upYPoint)
        down.GetPoint (i, downXPoint, downYPoint)
        x.append(xPoint)
        y.append(yPoint)
        if y_key == 'lifetime':
            eXHigh.append(upXPoint)
            eXLow.append(downXPoint)
            eYHigh.append(0.0)
            eYLow.append(0.0)
        elif x_key == 'lifetime':
            eXHigh.append(0.0)
            eXLow.append(0.0)
            eYHigh.append(upYPoint)
            eYLow.append(downYPoint)

    for i in range(len(x)):
        if x_key == 'lifetime':
            eYHigh[i] -= y[i]
            eYLow[i] = y[i] - eYLow[i]
        elif y_key == 'lifetime':
            eXHigh[i] -= x[i]
            eXLow[i] = x[i] - eXLow[i]

    graph = makeTGraphAsymmErrors(x, y, eXLow, eXHigh, eYLow, eYHigh)
    borderGraph = TGraphAsymmErrors()
    if x_key == 'lifetime':
        borderGraph = getBorderGraph(graph, 'vertical')
    elif y_key == 'lifetime':
        borderGraph = getBorderGraph(graph, 'horizontal')
    return borderGraph

def getOneSigmaGraph(limits, xAxisType, colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(0)
    graph.SetLineStyle(2)
    graph.SetLineWidth(2)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getOneSigmaGraph2D(limits, xAxisType, yAxisType, colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(0)
    graph.SetLineStyle(2)
    graph.SetLineWidth(2)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getTwoSigmaGraph(limits, xAxisType, colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(0)
    graph.SetLineStyle(2)
    graph.SetLineWidth(1)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph

def getTwoSigmaGraph2D(limits, xAxisType, yAxisType, colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(0)
    graph.SetLineStyle(2)
    graph.SetLineWidth(1)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph

def fetchLimits(process, mass, m, lifetime, directory, limits_to_include):
    print "fetching limits for mass = " + mass + " GeV, ctau = " + lifetime + " mm"
    limit_types = {
        'obs' : ['observed'],
        'exp' : ['expected'],
        'oneSigma' : ['down1', 'up1'],
        'twoSigma' : ['down2', 'up2'],
    }
    quantile_names = {
       -1.000 : 'observed',
        0.025 : 'down2',
        0.160 : 'down1',
        0.500 : 'expected',
        0.840 : 'up1',
        0.975 : 'up2',
    }

    # initialize dictionary with large default values for each desired limit type
    limit = {t : 1e12 for l in limits_to_include for t in limit_types[l]}
    if arguments.fillGaps and 'exp' not in limits_to_include:
        limit.update({t : 1e12 for t in limit_types['exp']})

    # get method used to compute limits
    fname = "limits/"+directory+"/method.txt"
    try:
        with open(fname) as method_file:
            method = method_file.readline()
    except IOError:
        method = "HybridNew"
        print fname + " doesn't exist"
        print "defaulting to HybridNew"

    # handle case where quantiles are stored in separate root files
    # fixme: kill duplicate code
    if method == "HybridNew" and arguments.separateFileQuantiles:
        for t in limit.keys():
            limit_type = t if t in ['expected', 'observed'] else 'expected_'+t
            fname = makeSignalRootFileName(process, mass, lifetime, directory, limit_type)
            if not fname:
                continue
            try:
                f = TFile(fname)
                limit_tree = f.Get('limit').Clone()
                limit_tree.SetDirectory(0)
                f.Close()
            except ReferenceError:
                print "couldn't get ttree from " + fname
                continue

            # update limit values for relevant limit types
            for i in range(limit_tree.GetEntries()):
                limit_tree.GetEntry(i)
                quantile = round(limit_tree.quantileExpected, 3)
                quantile_name = quantile_names.get(quantile)
                if quantile_name in limit:
                    limit[quantile_name] = limit_tree.limit

    # for AsymptoticLimits or HybridNew, get the limits from the root file
    elif method in ["AsymptoticLimits", "HybridNew", "Significance"]:
        # fixme: check that 'expected' is right in every case
        signal_name = makeSignalName(process, mass, lifetime)
        if method == "HybridNew":
            fname = "limits/{}/{}_expected/merged.root".format(directory, signal_name)
        elif method == "AsymptoticLimits":
            fname = makeSignalRootFileName(process, mass, lifetime, directory, "expected")
            #fname = "limits/{0}/{1}_expected/higgsCombine{1}.{2}.mH120.root".format(directory, signal_name, method)

        if not fname:
            return -1
        try:
            f = TFile(fname)
            limit_tree = f.Get('limit').Clone()
            #limit_tree.SetDirectory(0)
            #f.Close()
        except ReferenceError:
            print "couldn't get ttree from " + fname
            return -1

        # update limit values for relevant limit types
        for i in range(limit_tree.GetEntries()):
            limit_tree.GetEntry(i)
            quantile = round(limit_tree.quantileExpected, 3)
            quantile_name = quantile_names.get(quantile)
            if quantile_name in limit:
                limit[quantile_name] = limit_tree.limit

        f.Close() # fixme: why can't I do this in try clause?

    # fixme: for other methods, get the ranges from the log file
    else:
        print method + " not supported"
        return -1

    # check that at least one type of limit has been updated
    #if all(v == 1e12 for v in limit.values()):
    #    return -1
    # check that all limits have been updated
    if any(v == 1e12 for v in limit.values()):
        print [k for k, v in limit.iteritems() if v == 1e12]
        return -1

    # define up and down as distance from central value
    for q in ['down2', 'down1', 'up1', 'up2']:
        if q in limit and 'expected' in limit:
            limit[q] = abs(limit[q] - limit['expected'])

    # optionally replace observed limit with expected when observed does not converge
    if arguments.fillGaps and 'observed' in limit:
        if round(limit['observed'], 5) == round(2.00613, 5): # empirical value
            print "Warning: observed limit did not converge; subsituting expected limit"
            limit['observed'] = limit['expected']
        # remove expected from limit if not otherwise desired
        if 'exp' not in limits_to_include:
            for t in limit_types['exp']:
                limit.pop(t, None)

    if method != "Significance":
        # scale by xsection
        x_section = signal_cross_sections[str(m)]['value']
        limit.update((k, v*x_section) for k, v in limit.iteritems())
        # scale by signal scale factor introduced by runLimits
        signal_sf = getSignalSF(mass, lifetime, directory, 'expected')
        limit.update((k, v*signal_sf) for k, v in limit.iteritems())
    limit['lifetime'] = 0.1*float(lifetime) # convert to cm
    limit['mass'] = mass
    return limit

def printMassLifetimeExclusion(graph, xs, legendEntry):
    allXPoints = []
    allYPoints = []
    x1Points = []
    x2Points = []
    y1Points = []
    y2Points = []
    for i in range(graph.GetN()):
        xPoint = Double(0.0)
        yPoint = Double(0.0)
        graph.GetPoint(i, xPoint, yPoint)
        allXPoints.append(xPoint)
        allYPoints.append(yPoint)

    #in the tgraph parabola of cross section vs lifetime, find the "falling" and "rising" points,
    #separated by the minimum of the parabola
    npAllYPoints = np.array(allYPoints)
    index_minYPoints=np.argmin(npAllYPoints)
    fallingYPoints=npAllYPoints[:index_minYPoints+1]
    risingYPoints=npAllYPoints[index_minYPoints:]

    #get the x and y values for the y points on either side of the 1000 GeV cross section
    y1Points.append(fallingYPoints[fallingYPoints<xs].max())
    y2Points.append(fallingYPoints[fallingYPoints>xs].min())
    y1Points.append(risingYPoints[risingYPoints<xs].max())
    y2Points.append(risingYPoints[risingYPoints>xs].min())

    for i, y in enumerate(allYPoints):
        for y1 in y1Points:
            if y==y1:
                x1Points.append(allXPoints[i])
        for y2 in y2Points:
            if y==y2:
                x2Points.append(allXPoints[i])

    #find the intersection of the lines:
    #in y=mx+b, b=xs, m=dY/dX
    #print "For 1000 GeV observed curve, exclude lifetimes between: "
    #print "For 300 GeV observed curve, exclude lifetimes between: "
    #500 GeV
    print "For " +legendEntry +", exclude lifetimes between: "
    for i in range(len(y2Points)):
        dY = y2Points[i]-y1Points[i]
        dX = x2Points[i]-x1Points[i]
        lifetime = (xs - y2Points[i] + x2Points[i]*dY/dX)*(dX/dY)
        print "  " +str(lifetime)+"cm"

def drawPlot(plot):
    is2D = 'yAxisType' in plot
    outputFile.cd()
    canvas = TCanvas(plot['title'])
    canvases = []
    canvases.append(canvas)
    for source in plot.get('th2fs', []):
        for th2f in source['th2fsToInclude']:
            print th2f
            if th2f == 'obs':
                canvasName = plot['title'] + '_with_observed_limits'
            elif th2f == 'exp':
                canvasName = plot['title'] + '_with_expected_limits'
            tmp_canvas = TCanvas(canvasName)
            canvases.append(tmp_canvas)

    # set up axes and legend
    for canvas in canvases:
        canvas.cd()
        xAxisBins = array('d')
        yAxisBins = array('d')
        if plot['xAxisType'] == 'mass':
            #xAxisMin = float(masses[0])
            xAxisMin = 0.0
            if(HToSS):
                xAxisMax = float(masses.keys()[-1])
            else:
                xAxisMax = float(masses[-1])
        elif plot['xAxisType'] == 'lifetime':
            canvas.SetLogx()
            if arguments.mm:
                xAxisMin = float(lifetimes[0])
                xAxisMax = float(lifetimes[-1])
            else:
                # convert lifetime to cm
                xAxisMin = 0.1*float(lifetimes[0])
                xAxisMax = 0.1*float(lifetimes[-1])
        if is2D:
            canvas.SetLogz()
            if plot['yAxisType'] == 'mass':
                xAxisBins.extend([0.1*float(lifetime) for lifetime in lifetimes])
                xAxisBins.append(0.1*2.0*float(lifetimes[-1]))
                if(HToSS):
                    yAxisMin = float(masses.keys()[0])
                    yAxisMax = float(masses.keys()[-1])
                    yAxisBins.extend([float(mass) for mass in masses.keys()])
                    yAxisBins.append(2.0*float(masses.keys()[-1]) - float(masses.keys()[-2]))
                    yAxisBins.append(8.0*float(masses.keys()[-1]) - 4.0*float(masses.keys()[-2]))
                else:
                    yAxisMin = float(masses[0])
                    yAxisMax = float(masses[-1])
                    yAxisBins.extend([float(mass) for mass in masses])
                    yAxisBins.append(2.0*float(masses[-1]) - float(masses[-2]))
                    yAxisBins.append(8.0*float(masses[-1]) - 4.0*float(masses[-2]))
            elif plot['yAxisType'] == 'lifetime':
                canvas.SetLogy()
                yAxisMin = 0.1*float(lifetimes[0])
                yAxisMax = 0.1*float(lifetimes[-1])
                yAxisBins.extend([0.1*float(lifetime) for lifetime in lifetimes])
                yAxisBins.append(0.1*2.0*float(lifetimes[-1]))
                yAxisBins.append(0.1*8.0*float(lifetimes[-1]))

                if arguments.ns:
                    rightAxisMin = yAxisMin/30
                    rightAxisMax = yAxisMax/30
                    rightAxis = TGaxis(xAxisMax, yAxisMin, xAxisMax, yAxisMax, rightAxisMin, rightAxisMax, 510, "+LG")
                    rightAxis.SetTitle("#tau_{0} [ns]")
                    rightAxis.SetTitleFont(42)
                    rightAxis.SetLabelFont(42)

                if(HToSS):
                    xAxisBins.extend([float(mass) for mass in masses.keys()])
                    xAxisBins.append(2.0*float(masses.keys()[-1]) - float(masses.keys()[-2]))
                else:
                    xAxisBins.extend([float(mass) for mass in masses])
                    xAxisBins.append(2.0*float(masses[-1]) - float(masses[-2]))
            if process == 'gmsb':
                legend = TLegend(0.45, 0.53, 0.75, 0.78) #legend on the top right for stau 2D plot
            else:
                legend = TLegend(topLeft_x_left+0.05, 0.35, 0.55, 0.6) #legend in the middle of the y-axis for 2D plot
        else:
            canvas.SetLogy()
            legend = TLegend(topLeft_x_left+0.05, 0.48, 0.55, 0.77) #legend at the top for 1D plot
        legend.SetTextSize(0.04)
        legend.SetBorderSize(0)
        legend.SetFillColor(0)
        legend.SetFillStyle(0)
        processText = ""
        if process in ['stopToLB', 'stopToLD']:
            quark = 'b' if process == 'stopToLB' else 'd'
            processText = "#tilde{{t}}#tilde{{t}} #rightarrow l{0} l{0}".format(quark)
        elif GMSB and channel == 'ee':
            processText = "#tilde{e}#tilde{e} #rightarrow e#tilde{G} e#tilde{G}"
        elif GMSB and channel == '#mu#mu':
            processText = "#tilde{#mu}#tilde{#mu} #rightarrow #mu#tilde{G} #mu#tilde{G}"
        elif GMSB and channel == None: # co-nlsp or several channels on the same plot
            processText = "#tilde{l}#tilde{l} #rightarrow l#tilde{G} l#tilde{G} (co-NLSP)"
        elif GMSBstaus:
            processText = "#tilde{#tau}#tilde{#tau}#rightarrow #tau#tilde{G} #tau#tilde{G}"
        elif process == 'HToSSTo4L':
            processText = "H #rightarrow SS #rightarrow 4l, l = e, #mu"
        legend.SetHeader("#splitline{"+processText+"}{95% CL upper limits}")

        # construct TGraph objects for all curves and draw them
        tGraphs = []
        tTh2fs = []
        plotDrawn = False

        if not is2D or not plot.get('th2fs', []):
            legend.SetTextSize(0.035)
            expEntry = legend.AddEntry("","Median expected","l",)
            obsEntry = legend.AddEntry("","Observed","l")
            legend.AddEntry("","","")

            expEntry.SetLineStyle(7)
            expEntry.SetLineWidth(4)
            obsEntry.SetLineWidth(4)

        # draw theory curve
        if (not is2D) and plot.get('showTheory') and plot.get('showTheoryError'):
            if plot['xAxisType'] == 'mass':
                tGraphs.append(getTheoryOneSigmaGraph())
                draw_args = 'L' if plotDrawn else 'AL'
                tGraphs[-1].Draw(draw_args)
                plotDrawn = True
                legend.AddEntry(tGraphs[-1], "#pm 1 #sigma: theory", 'L')
                tGraphs.append(getTheoryGraph())
                draw_args = 'L' if plotDrawn else 'AL'
                tGraphs[-1].Draw(draw_args)
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')

        for graph in plot.get('graphs', []):
            colorScheme = graph.get('colorScheme', 'brazilian')
            # draw 1D graphs
            if not is2D:
                for graphName in graph['graphsToInclude']:
                    # draw uncertainty bands
                    if graphName == 'twoSigma':
                        g = getTwoSigmaGraph(graph['limits'], plot['xAxisType'], colorScheme)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = '95% expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    elif graphName == 'oneSigma':
                        g = getOneSigmaGraph(graph['limits'], plot['xAxisType'], colorScheme)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = '68% expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')

                    # draw expected limit
                    elif graphName == 'exp':
                        lineStyle = graph.get('lineStyle', 7)
                        g = getExpectedGraph(graph['limits'], plot['xAxisType'], colorScheme,
                                             lineStyle)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = 'Median expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        #don't draw expected in legend for 1D hists

                    # draw observed limit
                    elif graphName == 'obs':
                        lineStyle = graph.get('lineStyle', 1)
                        g = getObservedGraph(graph['limits'], plot['xAxisType'], colorScheme,
                                             lineStyle)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = 'Observed'
                        if 'legendEntry' in graph:
                            legendEntry = graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')

                        #print summary of limits for paper Summary section:
                        #find lifetime exclusion range for 1000 GeV mass point
                        if stops and legendEntry=='Observed: 1000 GeV':
                            xs = 0.00615134 #1000 GeV stop cross section in pb
                            printMassLifetimeExclusion(tGraphs[-1], xs, legendEntry)
                        elif GMSBstaus and legendEntry=='Observed: 300 GeV':
                            xs = 0.0007755 #300 GeV stau cross section in pb
                            printMassLifetimeExclusion(tGraphs[-1], xs, legendEntry)
                        elif GMSB and not GMSBstaus and legendEntry=='Observed: 500 GeV':
                            xs = 0.0006736 #500 GeV slepton cross section in pb
                            printMassLifetimeExclusion(tGraphs[-1], xs, legendEntry)
                    tGraphs[-1].SetName("h_"+legendEntry)

            # draw 2D graphs
            else:
                for graphName in graph['graphsToInclude']:
                    if graphName == 'twoSigma':
                        g = getTwoSigmaGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], colorScheme)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = '95% expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    if graphName == 'oneSigma':
                        g = getOneSigmaGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], colorScheme)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = '68% expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    if graphName == 'exp':
                        lineStyle = graph.get('lineStyle', 7)
                        g = getExpectedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'expected', 'theory', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = 'Median expected'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                            #legendEntry = graph['legendEntry']
                            #legend.SetHeader("Expected limits")
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    if graphName == 'twoSigmaTheory':
                        lineStyle = graph.get('lineStyle', 1)
                        g = getObservedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'observed', 'down2', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        lineWidth = tGraphs[-1].GetLineWidth()
                        tGraphs[-1].SetLineWidth(1)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        g = getObservedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'observed', 'up2', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        tGraphs[-1].SetLineWidth(1)
                        tGraphs[-1].Draw('L')
                        legendEntry = '#pm 2 #sigma_{theory}'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    if graphName == 'oneSigmaTheory':
                        lineStyle = graph.get('lineStyle', 1)
                        g = getObservedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'observed', 'down1', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        lineWidth = tGraphs[-1].GetLineWidth()
                        tGraphs[-1].SetLineWidth(2)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        g = getObservedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'observed', 'up1', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        tGraphs[-1].SetLineWidth(2)
                        tGraphs[-1].Draw('L')
                        legendEntry = '#pm 1 #sigma_{theory}'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    if graphName == 'obs':
                        lineStyle = graph.get('lineStyle', 1)
                        g = getObservedGraph2D(graph['limits'], plot['xAxisType'],
                                               plot['yAxisType'], 'observed', 'theory', colorScheme,
                                               lineStyle)
                        tGraphs.append(g)
                        draw_args = 'L' if plotDrawn else 'AL'
                        tGraphs[-1].Draw(draw_args)
                        plotDrawn = True
                        legendEntry = 'Observed'
                        if 'legendEntry' in graph:
                            legendEntry = graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                    tGraphs[-1].SetName("h_"+legendEntry)

        for th2f in plot.get('th2fs', []):
            for limit_type in th2f['th2fsToInclude']:
                if limit_type == 'exp':
                    print th2f['limits']
                    g = getTH2F(th2f['limits'], plot['xAxisType'], plot['yAxisType'], 'expected',
                                'theory')
                    tTh2fs.append(g)
                    if 'exp' in canvas.GetName():
                        tTh2fs[-1].Draw('colz')
                        for tGraph in tGraphs:
                            drawOption = tGraph.GetName() + ' same'
                            tGraph.Draw(drawOption)
                elif limit_type == 'obs':
                    g = getTH2F(th2f['limits'], plot['xAxisType'], plot['yAxisType'], 'observed',
                                'theory')
                    tTh2fs.append(g)
                    if 'obs' in canvas.GetName():
                        tTh2fs[-1].Draw('colz')
                        for tGraph in tGraphs:
                            drawOption = tGraph.GetName() + ' same'
                            tGraph.Draw(drawOption)
                tTh2fs[-1].SetName("h_"+canvas.GetName())

        if (not is2D) and plot.get('showTheory') and (not plot.get('showTheoryError')):
            if plot['xAxisType'] == 'mass':
                tGraphs.append(getTheoryGraph())
                draw_args = 'L' if plotDrawn else 'AL'
                tGraphs[-1].Draw(draw_args)
                plotDrawn = True
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')

        #get the min and max of all 1D graphs so the y axis can be set appropriately
        if not is2D:
            absMin = min(tg.GetHistogram().GetMinimum() for tg in tGraphs)
            absMax = max(tg.GetHistogram().GetMaximum() for tg in tGraphs)

        # set axis limits
        for tGraph in tGraphs:
            tGraph.SetTitle("")
            tGraph.GetXaxis().SetTitle(plot['xAxisLabel'])
            tGraph.GetXaxis().SetTitleOffset(1.2)
            tGraph.GetXaxis().SetLimits(0.9*xAxisMin, 1.1*xAxisMax)
            tGraph.GetXaxis().SetRangeUser(xAxisMin, xAxisMax)
            if not is2D:
                if(arguments.doBR):
                    tGraph.GetYaxis().SetTitle('95% CL upper limit on #bf{#it{#Beta}}(H #rightarrow SS)')
                else:
                    tGraph.GetYaxis().SetTitle('#sigma_{95%CL} [pb]')
                tGraph.GetYaxis().SetTitleOffset(1.4)
                if 'yAxis' in plot:
                    tGraph.GetYaxis().SetRangeUser(plot['yAxis'][0], plot['yAxis'][1])
                else:
                    tGraph.GetYaxis().SetRangeUser(0.9*absMin, 1000.1*absMax)
            else:
                tGraph.GetYaxis().SetTitle(plot['yAxisLabel'])
                tGraph.GetYaxis().SetTitleOffset(1.5)
                tGraph.GetYaxis().SetLimits(0.9*yAxisMin, 1.1*yAxisMax)
                tGraph.GetYaxis().SetRangeUser(yAxisMin, yAxisMax)
            tGraph.Write()
        legend.Draw()
        canvas.SetTitle('')
        for th2f in tTh2fs:
            th2f.SetTitle("")
            th2f.GetXaxis().SetTitle(plot['xAxisLabel'])
            th2f.GetXaxis().SetLimits(0.9*xAxisMin, 1.1*xAxisMax)
            th2f.GetXaxis().SetRangeUser(xAxisMin, xAxisMax)
            th2f.GetYaxis().SetTitle(plot['yAxisLabel'])
            th2f.GetXaxis().SetTitleOffset(1.2)
            th2f.GetYaxis().SetTitleOffset(1.5)
            th2f.GetYaxis().SetLimits(0.9*yAxisMin, 1.1*yAxisMax)
            th2f.GetYaxis().SetRangeUser(yAxisMin, yAxisMax)
            if 'exp' in canvas.GetName():
                th2f.GetZaxis().SetTitle('Expected #sigma_{95%CL} [pb]')
            elif 'obs' in canvas.GetName():
                th2f.GetZaxis().SetTitle('Observed #sigma_{95%CL} [pb]')
            th2f.GetZaxis().SetTitleOffset(1.5)
            th2f.Write()

        if arguments.ns:
            rightAxis.Draw()

        # draw header label
        HeaderLabel = TPaveLabel(header_x_left,y_bottom,header_x_right,y_top,HeaderText,"NDC")
        HeaderLabel.SetTextAlign(32)
        HeaderLabel.SetTextFont(42)
        HeaderLabel.SetTextSize(0.697674)
        HeaderLabel.SetBorderSize(0)
        HeaderLabel.SetFillColor(0)
        HeaderLabel.SetFillStyle(0)
        HeaderLabel.Draw()

        #LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS","NDC")
        LumiLabel = TPaveLabel(topLeft_x_left,y_bottom,topLeft_x_right,y_top,"CMS Preliminary","NDC")
        LumiLabel.SetTextFont(62)
        LumiLabel.SetTextSize(0.8)
        LumiLabel.SetTextAlign(12)
        LumiLabel.SetBorderSize(0)
        LumiLabel.SetFillColor(0)
        LumiLabel.SetFillStyle(0)
        LumiLabel.Draw()

        if channel and not GMSB and not GMSBstaus:
            channelLabel = TPaveLabel(0.7, 0.65, 0.9, 0.75, channel+" channel", "NDC")
            channelLabel.SetTextFont(52)
            channelLabel.SetTextSize(0.4)
            channelLabel.SetTextAlign(12)
            channelLabel.SetBorderSize(0)
            channelLabel.SetFillColor(0)
            channelLabel.SetFillStyle(0)
            channelLabel.Draw()
        if 'massLabel' in plot:
            MassLabel = TPaveLabel(0.163793, 0.822034, 0.362069, 0.891949, plot['massLabel'], "NDC")
            MassLabel.SetTextSize(0.5454546)
            MassLabel.SetTextAlign(12)
            MassLabel.SetBorderSize(0)
            MassLabel.SetFillColor(0)
            MassLabel.SetFillStyle(0)
            MassLabel.Draw()
        if 'brLabel' in plot:
            BRLabel = TPaveLabel(0.160920, 0.779661, 0.501437, 0.836864, plot['brLabel'], "NDC")
            BRLabel.SetTextSize(0.6666667)
            BRLabel.SetTextAlign(12)
            BRLabel.SetBorderSize(0)
            BRLabel.SetFillColor(0)
            BRLabel.SetFillStyle(0)
            BRLabel.Draw()

        canvas.Update()
        canvas.RedrawAxis('g')
        canvas.Write()
        canvas.Close()

def add_limit(limit, l, mass, lifetime):
    if limit != -1:
        l.append(limit)
        print "limit is: " +str(limit)
    else:
        print "WARNING: not plotting {}GeV, {}mm point".format(mass, lifetime)

####################################################################################################

outputFileName = "limits/"+arguments.condorDir+"/limit_plot.root"
outputFile = TFile(outputFileName, "RECREATE")

setCrossSections()

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    #fetch all the limits needed for this plot
    for th2f in plot.get('th2fs', []):
        th2f['limits'] = []
        if 'xAxisType' not in plot or 'yAxisType' not in plot:
            print "You want to draw a 2D plot but either X or Y axis is not defined."
            continue
        if(HToSS):
            for mass, m in zip(massesNames, masses.keys()):
                for lifetime in lifetimes:
                    limit = fetchLimits(process, mass, m, lifetime, th2f['source'], th2f['th2fsToInclude'])
                    add_limit(limit, th2f['limits'], mass, lifetime)
        else:
            for mass in masses:
                for lifetime in lifetimes:
                    limit = fetchLimits(process, mass, mass, lifetime, th2f['source'], th2f['th2fsToInclude'])
                    add_limit(limit, th2f['limits'], mass, lifetime)


    for graph in plot.get('graphs', []):
        graph['limits'] = []
        if plot['xAxisType'] == 'lifetime' and 'yAxisType' not in plot:
            for lifetime in lifetimes:
                if(HToSS):
                    limit = fetchLimits(process, graph['mass'], graph['m'], lifetime, graph['source'], graph['graphsToInclude'])
                else:
                    limit = fetchLimits(process, graph['mass'], graph['mass'], lifetime, graph['source'], graph['graphsToInclude'])
                add_limit(limit, graph['limits'], graph['mass'], lifetime)
        elif plot['xAxisType'] == 'mass' and 'yAxisType' not in plot:
            if(HToSS):
                for mass, m in zip(massesNames, masses.keys()):
                    limit = fetchLimits(process, mass, m, graph['lifetime'], graph['source'],
                                        graph['graphsToInclude'])
                    add_limit(limit, graph['limits'], mass, graph['lifetime'])
            else:
                for mass in masses:
                    limit = fetchLimits(process, mass, mass, graph['lifetime'], graph['source'],
                                        graph['graphsToInclude'])
                    add_limit(limit, graph['limits'], mass, graph['lifetime'])
        elif 'yAxisType' in plot:
            if(HToSS):
                for mass, m in zip(massesNames, masses.keys()):
                    for lifetime in lifetimes:
                        limit = fetchLimits(process, mass, m, lifetime, graph['source'],
                                            graph['graphsToInclude'])
                        add_limit(limit, graph['limits'], mass, lifetime)
            else:
                for mass in masses:
                    for lifetime in lifetimes:
                        limit = fetchLimits(process, mass, mass, lifetime, graph['source'],
                                            graph['graphsToInclude'])
                        add_limit(limit, graph['limits'], mass, lifetime)


    #now that all the limits are in place, draw the plot
    if all(g['limits'] for g in plot['graphs']):
        drawPlot(plot)
    else:
        print "WARNING: empty plot found, skipping"


outputFile.Close()

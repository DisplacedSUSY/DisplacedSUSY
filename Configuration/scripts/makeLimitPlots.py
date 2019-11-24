#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
import glob
from array import *
from operator import itemgetter
from optparse import OptionParser



parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)


from DisplacedSUSY.Configuration.systematicsDefinitions import signal_cross_sections_8TeV, signal_cross_sections_13TeV
signal_cross_sections = {}

from ROOT import TFile, TGraph,TH2F, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel, TH2D, TPave, Double, TTree

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetTextFont(42)
gStyle.SetOptTitle(0)
gROOT.ForceStyle()

topLeft_x_left    = 0.127333
topLeft_y_bottom  = 0.840805
topLeft_x_right   = 0.479333
topLeft_y_top     = 0.900483
topLeft_y_offset  = 0.04
topLeft_x_left_extra    = 0.127333
topLeft_y_bottom_extra  = 0.795724
topLeft_x_right_extra  = 0.479333
topLeft_y_top_extra     = 0.85599
topLeft_y_offset_extra  = 0.04
colorSchemes = {
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
        'obs' : 633,
        'exp' : 633,
        'oneSigma' : 625,
        'twoSigma' : 623,
    },
    'blue' : {
        'obs' : 601,
        'exp' : 601,
        'oneSigma' : 594,
        'twoSigma' : 591,
    },
    'green' : {
        'obs' : 418,
        'exp' : 418,
        'oneSigma' : 410,
        'twoSigma' : 407,
    },
    'purple' : {
        'obs' : 882,
        'exp' : 882,
        'oneSigma' : 872,
        'twoSigma' : 871,
    },
    'yellow' : {
        'obs' : 402,
        'exp' : 402,
        'oneSigma' : 397,
        'twoSigma' : 393,
    },
}

#set the text for the luminosity label
if(intLumi < 1000.):
    LumiInPb = intLumi
    LumiText = str(intLumi) + " pb^{-1}"
    LumiText = str.format('{0:.1f}', LumiInPb) + " pb^{-1}"
else:
    LumiInFb = intLumi/1000.
    LumiText = str.format('{0:.1f}', LumiInFb) + " fb^{-1}"

HeaderText = LumiText + " (" + energy + " TeV)"


def makeSignalName(process, mass, lifetime, use_miniAOD):
    name = process + str(mass) + "_" + str(lifetime) + "mm"
    if use_miniAOD:
        name = name + "_MiniAOD"
    # rename sub-mm samples to match sample names
    name = name.replace('.', 'p')
    return name

def makeSignalRootFileName(process,mass,lifetime,directory,limit_type,use_miniAOD):
    signal_name = makeSignalName(process, mass,lifetime,use_miniAOD)
    if glob.glob("limits/"+directory+"/"+signal_name+"_"+limit_type+"/higgsCombine"+signal_name+".*.root"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"_"+limit_type+"/higgsCombine"+signal_name+".*.root limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root")
#    print "limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root"
    fname = "limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root"
    if os.path.isfile(fname):
        return fname
    else:
        return False

def makeSignalLogFileName(process,mass,lifetime,directory,limit_type,use_miniAOD):
    signal_name = makeSignalName(process, mass,lifetime,use_miniAOD)
    if glob.glob("limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0*.out"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0.out limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".log")
#    print "limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".log"
    fname = "limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".log"
    if os.path.isfile(fname):
        return fname
    else:
        return False

def getSignalSF(mass,lifetime,directory,type_,use_miniAOD):
    signal_name = makeSignalName(process, mass,lifetime,use_miniAOD)
    signalSFFile = glob.glob("limits/"+directory+"/"+signal_name+"_"+type_+"/*.sf")
    if not signalSFFile:
        return 1.0
    f = open (signalSFFile[0], "r")
    signalSF = f.readline ().rstrip ()
    return float (signalSF)

def setCrossSections(inputPlot):
    global signal_cross_sections
    if 'energy' not in inputPlot:  # use run2 by default
        signal_cross_sections = signal_cross_sections_13TeV
    else:
        if inputPlot['energy'] == '8':
#            print "using 8 TeV cross sections"
            signal_cross_sections = signal_cross_sections_8TeV
        elif inputPlot['energy'] == '13':
#            print "using 13 TeV cross sections"
            signal_cross_sections = signal_cross_sections_13TeV
        else:  # use run2 by default
            print "invalid energy = " + inputPlot['energy'] + " - using default cross sections"
            signal_cross_sections = signal_cross_sections_13TeV

def getTheoryGraph():
    x = [ ]
    y = [ ]
    for mass in masses:
        xSection = float(signal_cross_sections[str(mass)]['value'])
        x.append(float(mass))
        y.append(float(xSection))

    graph = TGraph(len(x), array('d', x), array('d', y))
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes['theory']['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes['theory']['exp'])
    return graph

def getTheoryOneSigmaGraph():
    x = [ ]
    y = [ ]
    up = [ ]
    down = [ ]
    for mass in masses:
        xSection = float(signal_cross_sections[str(mass)]['value'])
        xSectionError = float(signal_cross_sections[str(mass)]['error'])
        x.append(float(mass))
        y.append(float(xSection))
        up.append(float((xSectionError - 1.0) * xSection))
        down.append(float((xSectionError - 1.0) * xSection))

    graph = TGraphAsymmErrors(
        len(x),
        array('d', x),
        array('d', y),
        array('d', [0 for i in range(0, len(x))]),
        array('d', [0 for i in range(0, len(x))]),
        array('d', down),
        array('d', up)
    )
    graph.SetFillColor(colorSchemes['theory']['oneSigma'])
    graph.SetFillStyle(0)
    graph.SetLineColor(colorSchemes['theory']['oneSigma'])
    graph.SetMarkerColor(colorSchemes['theory']['oneSigma'])

    return graph

def getGraph(limits, x_key, y_key):
    x = [ ]
    y = [ ]
    for limit in limits:
        if not limit.has_key(x_key) or not limit.has_key(y_key):
            continue
        x.append(float(limit[x_key]))
        y.append(float(limit[y_key]))

    graph = TGraph(len(x), array('d', x), array('d', y))
    return graph

def getTH2F(limits,x_key,y_key,experiment_key,theory_key):
    BinContent = []
    xBin_tmp = []
    yBin_tmp = []
    limit_dict = {}
    for limit in limits:
	xBin_tmp.append(float(limit['mass']))
        yBin_tmp.append(float(limit['lifetime']))
    xBin = list(set(xBin_tmp))
    yBin = list(set(yBin_tmp))
    xBin.sort()
    yBin.sort()
    xBin.append(xBin[len(xBin)-1] + float(100))
    yBin.append(yBin[len(yBin)-1] + float(100))
    yBinArray = array("d", yBin)
    xBinArray = array("d", xBin)
    RatioPlot = TH2F("","",int(len(xBin)-1),xBinArray,int(len(yBin)-1),yBinArray)
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key is 'up1' or experiment_key is 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key is 'down1' or experiment_key is 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key is 'up2' or theory_key is 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key is 'up1' or theory_key is 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key is 'down1' or theory_key is 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
		BinContent.append(limit_dict[lifetime][mass]['experiment']/limit_dict[lifetime][mass]['theory'])
		RatioPlot.Fill(mass,lifetime, limit_dict[lifetime][mass]['experiment']/limit_dict[lifetime][mass]['theory'])
    BinContent.sort()
    Min = 0
    for bin in BinContent:
	if bin is not 0.0:
		Min = bin
		break
    th2f = RatioPlot
    th2f.SetDirectory(0)
    #th2f.SetTitleOffset(1.2)
    th2f.SetMaximum(th2f.GetMaximum())
    th2f.SetMinimum(Min)
    #th2f.GetYaxis().SetTitleOffset(1.5)
    #th2f.GetXaxis().SetTitle(x_key)
    #th2f.GetYaxis().SetTitle(y_key)
    return th2f

def getGraph2D(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key is 'up1' or experiment_key is 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key is 'down1' or experiment_key is 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key is 'up2' or theory_key is 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key is 'up1' or theory_key is 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key is 'down1' or theory_key is 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
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
            y1 = math.log10(limit_dict[lifetime][previous_mass]['theory'])
            y3 = math.log10(limit_dict[lifetime][previous_mass]['experiment'])
            y2 = math.log10(limit_dict[lifetime][first_allowed_mass]['theory'])
            y4 = math.log10(limit_dict[lifetime][first_allowed_mass]['experiment'])
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0

        x.append (mass_limit)
        y.append (lifetime)
        if x_key is 'lifetime' and y_key is 'mass':
            x[-1], y[-1] = y[-1], x[-1]

    graph = TGraph (len (x), x, y)
    return graph

def getObservedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'observed')
    graph.SetLineWidth(5)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getObservedGraph2D(limits,xAxisType,yAxisType,experiment_key,theory_key,colorScheme):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(5)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getExpectedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'expected')
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph

def getExpectedGraph2D(limits,xAxisType,yAxisType,experiment_key,theory_key,colorScheme):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph

def getGraphAsymmErrors(limits, x_key, y_key, up_key, down_key):
    x = [ ]
    up = [ ]
    down = [ ]
    y = [ ]
    for limit in limits:
        if not limit.has_key(x_key) or not limit.has_key(up_key) or not limit.has_key(down_key) or not limit.has_key(y_key):
            continue
        x.append(float(limit[x_key]))
        up.append(float(limit[up_key]))
        down.append(float(limit[down_key]))
        y.append(float(limit[y_key]))
    graph = TGraphAsymmErrors(
        len(x),
        array('d', x),
        array('d', y),
        array('d', [0 for i in range(0, len(x))]),
        array('d', [0 for i in range(0, len(x))]),
        array('d', down),
        array('d', up)
        )
    return graph

def getBorderGraph(graph, errorType):
    N = graph.GetN ()
    otherSideX = []
    otherSideY = []
    x = array ('d')
    y = array ('d')
    for i in range (0, N):
        xPoint = Double (0.0)
        yPoint = Double (0.0)
        graph.GetPoint (i, xPoint, yPoint)
        if errorType is 'horizontal':
            eHigh = graph.GetErrorXhigh (i)
            eLow = graph.GetErrorXlow (i)
            otherSideX.append (xPoint - eLow)
            otherSideY.append (yPoint)
            x.append (xPoint + eHigh)
            y.append (yPoint)
        if errorType is 'vertical':
            eHigh = graph.GetErrorYhigh (i)
            eLow = graph.GetErrorYlow (i)
            otherSideX.append (xPoint)
            otherSideY.append (yPoint - eLow)
            x.append (xPoint)
            y.append (yPoint + eHigh)
    for i in range (0, -N, -1):
        x.append (otherSideX[i - 1])
        y.append (otherSideY[i - 1])

    borderGraph = TGraph (len (x), x, y)
    return borderGraph

def getGraphAsymmErrors2D(limits, x_key, y_key, experiment_key, up_key, down_key):
    central = getGraph2D (limits, x_key, y_key, experiment_key, 'theory')
    up = TGraph ()
    down = TGraph ()
    if experiment_key is 'expected':
        up = getGraph2D (limits, x_key, y_key, down_key, 'theory')
        down = getGraph2D (limits, x_key, y_key, up_key, 'theory')
    if experiment_key is 'observed':
        up = getGraph2D (limits, x_key, y_key, 'observed', up_key)
        down = getGraph2D (limits, x_key, y_key, 'observed', down_key)
    x = []
    y = []
    eXLow = []
    eXHigh = []
    eYLow = []
    eYHigh = []
    for i in range (0, central.GetN ()):
        xPoint = Double (0.0)
        yPoint = Double (0.0)
        upXPoint = Double (0.0)
        upYPoint = Double (0.0)
        downXPoint = Double (0.0)
        downYPoint = Double (0.0)
        central.GetPoint (i, xPoint, yPoint)
        up.GetPoint (i, upXPoint, upYPoint)
        down.GetPoint (i, downXPoint, downYPoint)
        x.append (xPoint)
        y.append (yPoint)
        if y_key is 'lifetime':
            eXHigh.append (upXPoint)
            eXLow.append (downXPoint)
            eYHigh.append (0.0)
            eYLow.append (0.0)
        if x_key is 'lifetime':
            eXHigh.append (0.0)
            eXLow.append (0.0)
            eYHigh.append (upYPoint)
            eYLow.append (downYPoint)

    for i in range (0, len (x)):
        if y_key is 'lifetime':
            eXHigh[i] -= x[i]
            eXLow[i] = x[i] - eXLow[i]
        if x_key is 'lifetime':
            eYHigh[i] -= y[i]
            eYLow[i] = y[i] - eYLow[i]

    graph = TGraphAsymmErrors (len (x),
                               array ('d', x),
                               array ('d', y),
                               array ('d', eXLow),
                               array ('d', eXHigh),
                               array ('d', eYLow),
                               array ('d', eYHigh))
    borderGraph = TGraphAsymmErrors ()
    if y_key is 'lifetime':
        borderGraph = getBorderGraph (graph, 'horizontal')
    if x_key is 'lifetime':
        borderGraph = getBorderGraph (graph, 'vertical')
    return borderGraph

def getOneSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getOneSigmaGraph2D(limits,xAxisType,yAxisType,colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getTwoSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph

def getTwoSigmaGraph2D(limits,xAxisType,yAxisType,colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph

def fetchLimits(process,mass,lifetime,directories,use_miniAOD):
    print "fetching limits for mass = " + mass + " GeV, ctau = " + lifetime + " mm"
    limit = { }
    limit['expected'] = 1.0e12

    for directory in directories:
        if not os.path.exists("limits/"+directory+"/method.txt"):
            print "limits/"+directory+"/method.txt doesn't exist"
            return -1

        with open("limits/"+directory+"/method.txt", 'r') as methodFile:
            method = methodFile.readline()

        #########################################################

        tmp_limit = { }

        # for AsymptoticLimits CLs, get the limits from the root file
        if method == "AsymptoticLimits":
            fname = makeSignalRootFileName(process,mass,lifetime,directory,"expected",use_miniAOD)
            if not fname:
                print "not fname"
                continue
            f = TFile(fname)
            if not f.GetNkeys():
                print "not f.GetNkeys()"
                return -1
            limit_tree = f.Get('limit')
            if not limit_tree:
                print "not limit_tree"
                return -1
            if limit_tree.GetEntries() < 6:
                print "limit_tree.GetEntries() < 6"
                continue
            for i in range(0,limit_tree.GetEntries()):
                limit_tree.GetEntry(i)
                quantileExpected = limit_tree.quantileExpected
                if quantileExpected == 0.5:
                    tmp_limit['expected'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.025) < 0.001:
                    tmp_limit['down2'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.16) < 0.001:
                    tmp_limit['down1'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.84) < 0.001:
                    tmp_limit['up1'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.975) < 0.001:
                    tmp_limit['up2'] = limit_tree.limit
                if math.fabs(quantileExpected - (-1)) < 0.001:
                    tmp_limit['observed'] = limit_tree.limit
            f.Close()

        #########################################################

        # for other methods, get the ranges from the log file
        else:
            fname = makeSignalLogFileName(process,mass,lifetime,directory,"expected",use_miniAOD)
            if not fname:
                continue
            file = open(fname)
            for line in file:
                line = line.rstrip("\n").split(":")
                if line[0] == "median expected limit":
                    tmp_limit['expected'] = float(line[1].split(" ")[3])
                elif line[0] == "   68% expected band ":
                    tmp_limit['down1'] = float(line[1].split(" ")[1])
                    tmp_limit['up1'] = float(line[1].split(" ")[5])
                elif line[0] == "   95% expected band ":
                    tmp_limit['down2'] = float(line[1].split(" ")[1])
                    tmp_limit['up2'] = float(line[1].split(" ")[5])
            file.close()
            if len(tmp_limit) != 5:
                fname = makeSignalRootFileName(process,mass,lifetime,directory,"expected",use_miniAOD)
                if not fname:
                    continue
                file = TFile(fname)
                if not file.GetNkeys():
                    return -1
                limit_tree = file.Get('limit')
                if not limit_tree:
                    return -1
                hist = TH1F("limithist","limithist",200,0,200)
                limit_tree.Draw("limit>>limithist")
                xq = array('d',[0.0,0.0,0.0,0.0,0.0])
                ql = array('d',[0.025,0.16,0.5,0.84,0.975])
                hist.GetQuantiles(5,xq,ql)
                tmp_limit['expected'] = float(xq[2])
                tmp_limit['down1'] = float(xq[1])
                tmp_limit['up1'] = float(xq[3])
                tmp_limit['down2'] = float(xq[0])
                tmp_limit['up2'] = float(xq[4])
                file.Close()

            fname = makeSignalLogFileName(process,mass,lifetime,directory,"expected",use_miniAOD)
            if not fname:
                continue
            file = open(fname)
            for line in file:
                line = line.rstrip("\n").split(":")
                if line[0] =="Limit": #observed limit
                    tmp_limit['observed'] = float(line[1].split(" ")[3])
            file.close()

        if len(tmp_limit) is not 6:
            return -1


        tmp_limit['up2'] = math.fabs(tmp_limit['up2'] - tmp_limit['expected'])
        tmp_limit['up1'] = math.fabs(tmp_limit['up1'] - tmp_limit['expected'])
        tmp_limit['down2'] = math.fabs(tmp_limit['down2'] - tmp_limit['expected'])
        tmp_limit['down1'] = math.fabs(tmp_limit['down1'] - tmp_limit['expected'])
        xSection = float(signal_cross_sections[str(mass)]['value'])
        tmp_limit['up2'] *= xSection
        tmp_limit['up1'] *= xSection
        tmp_limit['observed'] *= xSection
        tmp_limit['expected'] *= xSection
        tmp_limit['down1'] *= xSection
        tmp_limit['down2'] *= xSection
        tmp_limit['mass'] = mass
            # convert lifetime to cm
        tmp_limit['lifetime'] = 0.1 * float(lifetime)
        signalSF = getSignalSF (mass, lifetime, directory, 'expected', use_miniAOD)
        tmp_limit['expected'] *= signalSF
        tmp_limit['up1'] *= signalSF
        tmp_limit['up2'] *= signalSF
        tmp_limit['down1'] *= signalSF
        tmp_limit['down2'] *= signalSF
        if method != "AsymptoticLimits":
            signalSF = getSignalSF (mass, lifetime, directory, 'observed', use_miniAOD)
        tmp_limit['observed'] *= signalSF
#        print tmp_limit['observed']/xSection
        if tmp_limit['expected'] < limit['expected']:
            limit = tmp_limit
    return (limit if limit['expected'] < 9.9e11 else -1)

def drawPlot(plot):
    is2D = 'yAxisType' in plot
    outputFile.cd()
    hasRatioTH2F = False
    canvas = TCanvas(plot['title'])
    generalCanvas = []
    generalCanvas.append(canvas)
    if plot.has_key('th2fs'):
        hasRatioTH2F = True
	for source in plot['th2fs']:
            for th2f in source['th2fsToInclude']:
                if th2f is 'obs':
                    canvasName = plot['title'] + ' with_ratio_of_observed_to_theory_limits'
                elif th2f is 'exp':
                    canvasName = plot['title'] + ' with_ratio_of_expected_to_theory_limits'
                tmp_canvas = TCanvas(canvasName)
                generalCanvas.append(tmp_canvas)
# canvas.SetGridx()
# canvas.SetGridy()
    for canvas in generalCanvas:
        canvas.cd()
        xAxisMin = 1
        yAxisMin = 1
        xAxisMax = 2
        yAxisMax = 2
        xAxisBins = array('d')
        yAxisBins = array('d')
        nBinsX = 1
        nBinsY = 1
        if plot['xAxisType'] is 'mass':
            xAxisMin = float(masses[0])
            xAxisMax = float(masses[-1])
        elif plot['xAxisType'] is 'lifetime':
            canvas.SetLogx()
            # convert lifetime to cm
            xAxisMin = 0.1*float(lifetimes[0])
            xAxisMax = 0.1*float(lifetimes[-1])
        if is2D:
            canvas.SetLogz()
            if plot['yAxisType'] is 'mass':
                yAxisMin = float(masses[0])
                yAxisMax = float(masses[-1])
                xAxisBins.extend ([0.1 * float (lifetime) for lifetime in lifetimes])
                xAxisBins.append (0.1 * 2.0 * float (lifetimes[-1]))
                yAxisBins.extend ([float (mass) for mass in masses])
                yAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
                yAxisBins.append (8.0 * float (masses[-1]) - 4.0 * float (masses[-2]))
            elif plot['yAxisType'] is 'lifetime':
                yAxisMin = 0.1*float(lifetimes[0])
                yAxisMax = 0.1*float(lifetimes[-1])
                canvas.SetLogy()
                xAxisBins.extend ([float (mass) for mass in masses])
                xAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
                yAxisBins.extend ([0.1 * float (lifetime) for lifetime in lifetimes])
                yAxisBins.append (0.1 * 2.0 * float (lifetimes[-1]))
                yAxisBins.append (0.1 * 8.0 * float (lifetimes[-1]))
            nBinsX = len (xAxisBins) - 1
            nBinsY = len (yAxisBins) - 1
        else:
            canvas.SetLogy()
        legend = TLegend(0.5, 0.6, 0.9, 0.88)
        legend.SetBorderSize(0)
        legend.SetFillColor(0)
        legend.SetFillStyle(0)
        #construct tGraph objects for all curves and draw them
        tGraphs = []
        tTh2fs = []
        plotDrawn = False
        if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' in plot and plot['showTheoryError']):
            if plot['xAxisType'] is 'mass':
                tGraphs.append(getTheoryOneSigmaGraph())
                if plotDrawn:
                    tGraphs[-1].Draw('3')
                else:
                    tGraphs[-1].Draw('A3')
                plotDrawn = True
                legend.AddEntry(tGraphs[-1], "#pm 1 #sigma: theory", 'F')
                tGraphs.append(getTheoryGraph())
                if plotDrawn:
                    tGraphs[-1].Draw('L')
                else:
                    tGraphs[-1].Draw('AL')
                plotDrawn = True
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
        if plot.has_key('graphs'):
                   for graph in plot['graphs']:
                       colorScheme = 'brazilian'
                       if 'colorScheme' in graph:
                           colorScheme = graph['colorScheme']
                       if not is2D:
                           for graphName in graph['graphsToInclude']:
                               setCrossSections(graph)
                               if graphName is 'twoSigma':
                                   tGraphs.append(getTwoSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('3')
                                   else:
                                       tGraphs[-1].Draw('A3')
                                   plotDrawn = True
                                   legendEntry = '#pm 2 std. deviation'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                               if graphName is 'oneSigma':
                                   tGraphs.append(getOneSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('3')
                                   else:
                                       tGraphs[-1].Draw('A3')
                                   plotDrawn = True

                                   legendEntry = '#pm 1 std. deviation'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                               if graphName is 'exp':
                                   tGraphs.append(getExpectedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True

                                   legendEntry = 'Expected'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                               if graphName is 'obs':
                                   tGraphs.append(getObservedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True

                                   legendEntry = 'Observed'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                       else:
                           for graphName in graph['graphsToInclude']:
                               setCrossSections(graph)
                               if graphName is 'twoSigma':
                                   tGraphs.append(getTwoSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('F')
                                   else:
                                       tGraphs[-1].Draw('AF')
                                   plotDrawn = True
                                   legendEntry = '#pm 2 std. deviation'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                                   tGraphs[-1].SetName('F')
                               if graphName is 'oneSigma':
                                   tGraphs.append(getOneSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('F')
                                   else:
                                       tGraphs[-1].Draw('AF')
                                   plotDrawn = True
                                   legendEntry = '#pm 1 std. deviation'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                                   tGraphs[-1].SetName('F')
                               if graphName is 'exp':
                                   tGraphs.append(getExpectedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory',colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True
                                   legendEntry = 'Expected'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                                   tGraphs[-1].SetName('L')
                               if graphName is 'twoSigmaTheory':
                                   tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down2',colorScheme))
                                   lineWidth = tGraphs[-1].GetLineWidth ()
                                   tGraphs[-1].SetLineWidth (lineWidth - 4)
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True
                                   tGraphs[-1].SetName('L')
                                   tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up2',colorScheme))
                                   tGraphs[-1].SetLineWidth (lineWidth - 4)
                                   tGraphs[-1].Draw('L')
                                   legendEntry = '#pm 2 #sigma_{theory}'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                                   tGraphs[-1].SetName('L')
                               if graphName is 'oneSigmaTheory':
                                   tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down1',colorScheme))
                                   lineWidth = tGraphs[-1].GetLineWidth ()
                                   tGraphs[-1].SetLineWidth (lineWidth - 2)
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True
                                   tGraphs[-1].SetName('L')
                                   tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up1',colorScheme))
                                   tGraphs[-1].SetLineWidth (lineWidth - 2)
                                   tGraphs[-1].Draw('L')
                                   legendEntry = '#pm 1 #sigma_{theory}'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                                   tGraphs[-1].SetName('L')
                               if graphName is 'obs':
                                   tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','theory',colorScheme))
                                   if plotDrawn:
                                       tGraphs[-1].Draw('L')
                                   else:
                                       tGraphs[-1].Draw('AL')
                                   plotDrawn = True
                                   legendEntry = 'Observed'
                                   if 'legendEntry' in graph:
                                       legendEntry = legendEntry + ": " + graph['legendEntry']
                                   legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                                   tGraphs[-1].SetName('L')
        if hasRatioTH2F:
            for th2f in plot['th2fs']:
                setCrossSections(th2f)
         	for type in th2f['th2fsToInclude']:
                    if type is 'exp':
                        tTh2fs.append(getTH2F(th2f['limits'],plot['xAxisType'],plot['yAxisType'],'expected', 'theory'))
                        if 'exp' in canvas.GetName():
                            tTh2fs[-1].Draw('colz')
                            for tGraph in tGraphs:
                                drawOption = tGraph.GetName() + ' same'
                                tGraph.Draw(drawOption)
                    if type is 'obs':
                        tTh2fs.append(getTH2F(th2f['limits'],plot['xAxisType'],plot['yAxisType'],'observed', 'theory'))
                        if 'obs' in canvas.GetName():
                            tTh2fs[-1].Draw('colz')
                            for tGraph in tGraphs:
                                drawOption = tGraph.GetName() + ' same'
                                tGraph.Draw(drawOption)

        if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' not in plot or not plot['showTheoryError']):
            if plot['xAxisType'] is 'mass':
                tGraphs.append(getTheoryGraph())
                if plotDrawn:
                    tGraphs[-1].Draw('L')
                else:
                    tGraphs[-1].Draw('AL')
                plotDrawn = True
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
        if not is2D:
            #get the min and max of all graphs, so the y-axis can be set appropriately
            absMin = 999
            absMax = -999
            for tGraph in tGraphs:
                histo = tGraph.GetHistogram()
                plotMax = histo.GetMaximum()
                plotMin = histo.GetMinimum()
                if plotMin < absMin:
                    absMin = plotMin
                if plotMax > absMax:
                    absMax = plotMax
        #now set the axis limits
        for tGraph in tGraphs:
            tGraph.SetTitle("")
            tGraph.GetXaxis().SetTitle(plot['xAxisLabel'])
            tGraph.GetXaxis().SetTitleOffset(1.2)
            tGraph.GetXaxis().SetLimits(0.9*xAxisMin,1.1*xAxisMax)
            tGraph.GetXaxis().SetRangeUser(xAxisMin,xAxisMax)
            if not is2D:
                tGraph.GetYaxis().SetTitle('#sigma_{95%CL} [pb]')
                #tGraph.GetYaxis().SetTitle('#sigma_{95%CL}(H #rightarrow XX) B(X #rightarrow #mu#mu) [pb]')
                tGraph.GetYaxis().SetTitleOffset(1.4)
                if 'yAxis' in plot:
                    tGraph.GetYaxis().SetRangeUser(plot['yAxis'][0],plot['yAxis'][1])
                else:
                    tGraph.GetYaxis().SetRangeUser(0.9*absMin,1.1*absMax)
            else:
                tGraph.GetYaxis().SetTitle(plot['yAxisLabel'])
                tGraph.GetYaxis().SetTitleOffset(1.5)
                tGraph.GetYaxis().SetLimits(0.9*yAxisMin,1.1*yAxisMax)
                tGraph.GetYaxis().SetRangeUser(yAxisMin,yAxisMax)
        legend.Draw()
        canvas.SetTitle('')
        for th2f in tTh2fs:
            th2f.SetTitle("")
            th2f.GetXaxis().SetTitle(plot['xAxisLabel'])
            th2f.GetXaxis().SetLimits(0.9*xAxisMin,1.1*xAxisMax)
            th2f.GetXaxis().SetRangeUser(xAxisMin,xAxisMax)
            th2f.GetYaxis().SetTitle(plot['yAxisLabel'])
            th2f.GetXaxis().SetTitleOffset(1.2)
            th2f.GetYaxis().SetTitleOffset(1.5)
            th2f.GetYaxis().SetLimits(0.9*yAxisMin,1.1*yAxisMax)
            th2f.GetYaxis().SetRangeUser(yAxisMin,yAxisMax)


        #draw the header label
        HeaderLabel = TPaveLabel(0.88,0.9,0.90,0.94,HeaderText,"NDC")
        HeaderLabel.SetTextAlign(32)
        HeaderLabel.SetTextFont(42)
        HeaderLabel.SetTextSize(1)
        HeaderLabel.SetBorderSize(0)
        HeaderLabel.SetFillColor(0)
        HeaderLabel.SetFillStyle(0)
        HeaderLabel.Draw()
        LumiLabel = TPaveLabel(topLeft_x_left,topLeft_y_bottom,topLeft_x_right,topLeft_y_top,"CMS","NDC")
        LumiLabel.SetTextFont(61)
        LumiLabel.SetTextSize(0.75)
        LumiLabel.SetTextAlign(12)
        extraLabel = TPaveLabel(topLeft_x_left_extra,topLeft_y_bottom_extra,topLeft_x_right_extra,topLeft_y_top_extra,"Preliminary","NDC")
        extraLabel.SetTextFont(52)
        extraLabel.SetTextSize(0.57)
        extraLabel.SetTextAlign(12)
        LumiLabel.SetBorderSize(0)
        LumiLabel.SetFillColor(0)
        LumiLabel.SetFillStyle(0)
        extraLabel.SetBorderSize(0)
        extraLabel.SetFillColor(0)
        extraLabel.SetFillStyle(0)
        LumiLabel.Draw()
        extraLabel.Draw()
        if 'massLabel' in plot:
            MassLabel = TPaveLabel(0.1637931,0.8220339,0.362069,0.8919492,plot['massLabel'],"NDC")
            MassLabel.SetTextSize(0.5454546)
            MassLabel.SetTextAlign(12)
            MassLabel.SetBorderSize(0)
            MassLabel.SetFillColor(0)
            MassLabel.SetFillStyle(0)
            MassLabel.Draw()
        if 'brLabel' in plot:
            BRLabel = TPaveLabel(0.1609195,0.779661,0.5014368,0.8368644,plot['brLabel'],"NDC")
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
    # canvas.SaveAs("test.pdf")




######################################################################################################


outputFileName = "limits/"+arguments.outputDir+"/limit_plot.root"
outputFile = TFile(outputFileName, "RECREATE")

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    #fetch all the limits needed for this plot
    if plot.has_key('th2fs'):
        for th2f in plot['th2fs']:
            setCrossSections(th2f)
            use_miniAOD = False
            if plot.has_key('add_MiniAOD'):
                use_miniAOD = True
            th2f['limits'] = []
            if 'xAxisType' not in plot or 'yAxisType' not in plot:
                print "You want to draw a 2D plot but either X or Y axis is not defined."
            else:
                for mass in masses:
                    for lifetime in lifetimes:
                        limit = fetchLimits(process,mass,lifetime,th2f['source'],use_miniAOD)
                        if limit is not -1:
                            th2f['limits'].append(limit)
                        else:
                            print "WARNING: not plotting mass " + str (mass) + " GeV, lifetime " + str (lifetime) + " mm"
    if plot.has_key('graphs'):
        for graph in plot['graphs']:
            setCrossSections(graph)
            use_miniAOD = False
            if graph.has_key('add_MiniAOD'):
                use_miniAOD = True
            graph['limits'] = []
            if plot['xAxisType'] is 'lifetime' and 'yAxisType' not in plot:
                for lifetime in lifetimes:
                    limit = fetchLimits(process,graph['mass'],lifetime,graph['source'],use_miniAOD)
                    if limit is not -1:
                        graph['limits'].append(limit)
                    else:
                        print "WARNING: not plotting lifetime " + str (lifetime) + " mm"
            elif plot['xAxisType'] is 'mass' and 'yAxisType' not in plot:
                for mass in masses:
                    limit = fetchLimits(process,mass,graph['lifetime'],graph['source'],use_miniAOD)
                    if limit is not -1:
                        graph['limits'].append(limit)
                    else:
                        print "WARNING: not plotting mass " + str (mass) + " GeV"
            elif 'yAxisType' in plot:
                for mass in masses:
                    for lifetime in lifetimes:
                        limit = fetchLimits(process,mass,lifetime,graph['source'],use_miniAOD)
                        if limit is not -1:
                            graph['limits'].append(limit)
                        else:
                            print "WARNING: not plotting mass " + str (mass) + " GeV, lifetime " + str (lifetime) + " mm"


    #now that all the limits are in place, draw the plot
    validPlot = True
    for graph in plot['graphs']:
        if not graph['limits']:
            validPlot = False
    if validPlot:
        drawPlot(plot)
    else:
        print "WARNING: empty plot found, skipping"


outputFile.Close()

#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
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


from ROOT import TFile, TGraph, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetOptTitle(0)
gROOT.ForceStyle()

colorSchemes = {
    'brazilian' : {
        'obs' : 1,
        'exp' : 1,
        'oneSigma' : 410,
        'twoSigma' : 393,
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


def makeSignalName(mass,lifetime,branching_ratio):
    return "stop"+str(mass)+"_"+str(lifetime)+"mm_"+"br"+str(branching_ratio)

def makeSignalFileName(mass,lifetime,branching_ratio,directory):
    signal_name = makeSignalName(mass,lifetime,branching_ratio)
    if not os.path.exists ("limits/"+directory+"/"+signal_name+"/limits_"+signal_name+".root"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"/higgsCombine"+signal_name+".*.root limits/"+directory+"/"+signal_name+"/limits_"+signal_name+".root")
    return "limits/"+directory+"/"+signal_name+"/limits_"+signal_name+".root"

def getTheoryGraph():
    x = [ ]
    y = [ ]
    for mass in masses:
        xSection = float(signal_cross_sections[str(mass)]['value'])
        x.append(float(mass))
        y.append(float(xSection))

    graph = TGraph(len(x), array('d', x), array('d', y))
    graph.SetLineWidth(4)
    graph.SetLineStyle(3)
    graph.SetFillColor(0)
    graph.SetLineColor(1)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(1)
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

def getObservedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'observed')
    graph.SetLineWidth(4)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getExpectedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'expected')
    graph.SetLineWidth(4)
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
    
def getOneSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up1', 'down1')
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


def fetchLimits(mass,lifetime,branching_ratio,directory):

    file = TFile(makeSignalFileName(mass,lifetime,branching_ratio,directory))
    limit_tree = file.Get('limit')
    limit = { }
    if limit_tree.GetEntries() < 6:
        return -1
    for i in range(0,limit_tree.GetEntries()):
        limit_tree.GetEntry(i)
        quantileExpected = limit_tree.quantileExpected
        if quantileExpected == -1.0:
            limit['observed'] = limit_tree.limit
        if quantileExpected == 0.5:
            limit['expected'] = limit_tree.limit
        if math.fabs(quantileExpected - 0.025) < 0.0001:
            limit['down2'] = limit_tree.limit
        if math.fabs(quantileExpected - 0.16) < 0.0001:
            limit['down1'] = limit_tree.limit
        if math.fabs(quantileExpected - 0.84) < 0.0001:
            limit['up1'] = limit_tree.limit
        if math.fabs(quantileExpected - 0.975) < 0.0001:
            limit['up2'] = limit_tree.limit

    limit['up2'] = math.fabs(limit['up2'] - limit['expected'])
    limit['up1'] = math.fabs(limit['up1'] - limit['expected'])
    limit['down2'] = math.fabs(limit['down2'] - limit['expected'])
    limit['down1'] = math.fabs(limit['down1'] - limit['expected'])

    xSection = float(signal_cross_sections[str(mass)]['value'])
    limit['up2'] *= xSection
    limit['up1'] *= xSection
    limit['observed'] *= xSection
    limit['expected'] *= xSection
    limit['down1'] *= xSection
    limit['down2'] *= xSection

    limit['mass'] = mass
    limit['lifetime'] = lifetime
    limit['branching_ratio'] = branching_ratio
    #print limit
    #print

    return limit
        

def drawPlot(plot):
    outputFile.cd()
    canvas = TCanvas(plot['title'])
#    canvas.SetGridx()
#    canvas.SetGridy()
    xAxisMin = 1
    xAxisMax = 2
    if plot['xAxisType'] is 'mass':
        canvas.SetLogy()
        xAxisMin = float(masses[0])
        xAxisMax = float(masses[-1])
    elif plot['xAxisType'] is 'lifetime':
        canvas.SetLogy()
        canvas.SetLogx()
        xAxisMin = float(lifetimes[0])
        xAxisMax = float(lifetimes[-1])

    legend = TLegend(0.5, 0.6, 0.9, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)

    #construct tGraph objects for all curves and draw them
    tGraphs = []
    plotDrawn = False
    for graph in plot['graphs']:
        colorScheme = 'brazilian'
        if 'colorScheme' in graph:
            colorScheme = graph['colorScheme']
        if 'twoSigma' in graph['graphsToInclude']:
            tGraphs.append(getTwoSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('3')
            else:
                tGraphs[-1].Draw('A3')
            plotDrawn = True
            legendEntry = '#pm 2 #sigma'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'F')
        if 'oneSigma' in graph['graphsToInclude']:
            tGraphs.append(getOneSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('3')
            else:
                tGraphs[-1].Draw('A3')
            plotDrawn = True

            legendEntry = '#pm 1 #sigma'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'F')
        if 'exp' in graph['graphsToInclude']:
            tGraphs.append(getExpectedGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('LP')
            else:
                tGraphs[-1].Draw('ALP')
            plotDrawn = True

            legendEntry = 'exp. limit'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'L')
        if 'obs' in graph['graphsToInclude']:
            tGraphs.append(getObservedGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('LP')
            else:
                tGraphs[-1].Draw('ALP')
            plotDrawn = True

            legendEntry = 'obs. limit'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'L')

    if 'showTheory' in plot:
        if 'showTheory':
            if plot['xAxisType'] is 'mass':
                tGraphs.append(getTheoryGraph())
                if plotDrawn:
                    tGraphs[-1].Draw('LP')
                else:
                    tGraphs[-1].Draw('ALP')

                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')


    #get the min and max of all graphs, so the y-axis can be set appropriately
    absMin =  999
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
        tGraph.GetXaxis().SetRangeUser(xAxisMin,xAxisMax)
        tGraph.GetYaxis().SetTitle('#sigma_{95%CL} [pb]')
        if 'yAxis' in plot:
            tGraph.GetYaxis().SetRangeUser(plot['yAxis'][0],plot['yAxis'][1])
        else:
            tGraph.GetYaxis().SetRangeUser(0.9*absMin,1.1*absMax)

        
    legend.Draw()
    canvas.SetTitle('')
    canvas.Update()
    
    canvas.RedrawAxis('g')
    canvas.Write()
#    canvas.SaveAs("test.pdf")




######################################################################################################


outputFileName = "limits/"+arguments.outputDir+"/limit_plot.root"
outputFile = TFile(outputFileName, "RECREATE")

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    #fetch all the limits needed for this plot

    for graph in plot['graphs']:
        graph['limits'] = []
        if plot['xAxisType'] is 'lifetime':
            for lifetime in lifetimes:
                limit = fetchLimits(graph['mass'],lifetime,graph['br'],graph['source'])
                if limit is not -1:
                    graph['limits'].append(limit)
        elif plot['xAxisType'] is 'mass':
            for mass in masses:
                limit = fetchLimits(mass,graph['lifetime'],graph['br'],graph['source'])
                if limit is not -1:
                    graph['limits'].append(limit)

    #now that all the limits are in place, draw the plot
    drawPlot(plot)


outputFile.Close()

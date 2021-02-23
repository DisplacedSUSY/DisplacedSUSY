#!/usr/bin/env python

# Find average and 1 sigma range of systematic uncertainities, by reading in text files.
# Can be run after lifetime reweighted points added to text files.
# Usage:
# $ python find1sigmaRangeOfSyst.py

from ROOT import TCanvas, TFile, TH1F, TF1

from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *
from OSUT3Analysis.Configuration.cutUtilities import *

systs = [
    'pileup',
    'electronD0Smearing',
    'muonD0Smearing',
    'electronIDandIso',
    'muonIDandIso',
    'muonPixelHitEff',
    'muonPixelHitEff16',
]

analysisChannels = [
    'emu',
    'ee',
    'mumu',
]

years = [
    '2016',
    '2017',
    '2018',
]

for syst in systs:
    for analysisChannel in analysisChannels:
        for year in years:
            if year == '2016' and (syst == 'electronD0Smearing' or syst == 'muonD0Smearing' or syst == 'muonPixelHitEff'):
                continue #no d0 smearing in 2016
            elif (year == '2017' or year == '2018') and syst == 'muonPixelHitEff16':
                continue #muonPixelHitEff16 in 2016 only, muonPixelHitEff in 2017 and 2018
            elif analysisChannel == 'ee' and (syst == 'muonD0Smearing' or syst == 'muonIDandIso' or syst == 'muonPixelHitEff' or syst == 'muonPixelHitEff16'):
                continue #no muon systematics in ee channel
            elif analysisChannel == 'mumu' and (syst == 'electronD0Smearing' or syst == 'electronIDandIso'):
                continue #no electron systs in mumu channel
            else:
                nlines = 0
                sum_fractions = 0.
                lowest_fraction = 1.
                highest_fraction = 0.
                lowerBound = 0

                c1 = TCanvas("c1","c1",100,100,700,550)

                #empirically determined
                if syst == 'pileup':
                    upperBound = 10
                    lowFitRange = 0
                    highFitRange = upperBound
                    fit = "landau"
                elif syst == 'electronD0Smearing' or syst == 'muonD0Smearing': #negligible
                    upperBound = 0.01
                    lowFitRange = 0
                    highFitRange = upperBound
                    fit = "gaus"
                elif syst == 'electronIDandIso':
                    if analysisChannel == 'ee':
                        upperBound = 25
                        lowFitRange = 0
                        highFitRange = upperBound
                    elif analysisChannel == 'emu':
                        upperBound = 10
                        lowFitRange = 0
                        highFitRange = upperBound
                    fit = "gaus"
                elif syst == 'muonIDandIso':
                    upperBound = 1
                    lowFitRange = 0
                    highFitRange = upperBound
                    fit = "gaus"
                elif syst == 'muonPixelHitEff' or syst == 'muonPixelHitEff16':
                    if syst == 'muonPixelHitEff16':
                        if analysisChannel == 'emu':
                            upperBound = 40
                            lowFitRange = 30
                            highFitRange = 33
                        elif analysisChannel == 'mumu':
                            lowerBound = 70
                            upperBound = 80
                            lowFitRange = 72
                            highFitRnage = 76
                    elif syst == 'muonPixelHitEff':
                        if analysisChannel == 'emu':
                            if year == '2017':
                                upperBound = 20
                                lowFitRange = 12
                                highFitRange = 14
                            elif year == '2018':
                                upperBound = 20
                                lowFitRange = 16
                                highFitRange = 18
                        elif analysisChannel == 'mumu':
                            if year == '2017':
                                upperBound = 30
                                lowFitRange = 23
                                highFitRange = 25
                            elif year == '2018':
                                upperBound = 40
                                lowFitRange = 29
                                highFitRange = 32
                    fit = "gaus"

                hist = TH1F("hist","",100,lowerBound,upperBound)
                hist.SetTitle(";Systematic uncertainties [%];Entries")
                hist.SetLineWidth(3)

                #read in original text file, split into 3 "words": original dataset name, down error, up error
                infile = "../data/systematic_values__" + syst + "_" + analysisChannel + "_" + year + ".txt"
                with open(infile) as fin:
                    for line in fin:
                        nlines += 1

                        words = line.split()
                        errDn = float(words[1])
                        errUp = float(words[2])

                        fractionDn = 1.0-errDn if errDn<1.0 else errDn-1.0
                        fractionUp = 1.0-errUp if errUp<1.0 else errUp-1.0

                        sum_fractions += fractionDn
                        sum_fractions += fractionUp

                        if fractionDn < lowest_fraction:
                            lowest_fraction = fractionDn
                        if fractionDn > highest_fraction:
                            highest_fraction = fractionDn
                        if fractionUp < lowest_fraction:
                            lowest_fraction = fractionUp
                        if fractionUp > highest_fraction:
                            highest_fraction = fractionUp

                        hist.Fill(100.*fractionDn)
                        hist.Fill(100.*fractionUp)

                f1 = TF1("f1",fit,lowFitRange,highFitRange)
                hist.Fit("f1","R")
                c1.cd()
                hist.Draw("l")
                c1.SaveAs("systs/" + syst + "_" + analysisChannel + "_" + year + ".pdf")

                mpv = f1.GetParameter(1)
                sigma = f1.GetParameter(2)
                print "for " + syst + " systematic for " + analysisChannel + " and " + year
                print "systematic uncertainty ranges from " + str(100.*lowest_fraction) + " to " + str(100.*highest_fraction) + "%"
                print "arthimetic average syst uncert is " + str(100.*sum_fractions/(2*nlines)) + "%" #need to multiply nlines by 2 because adding down and up fractions together
                print "fitted most probabale value syst uncert is " + str(round_sigfigs(mpv,2)) + "% with sigma " + str(round_sigfigs(sigma,2)) + "%"
                print "so the 1 sigma range is " + str(round_sigfigs(mpv-sigma,2)) + "-" + str(round_sigfigs(mpv+sigma,2)) + "%"
                print "######"

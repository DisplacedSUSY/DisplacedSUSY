import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.cutUtilities import *
from OSUT3Analysis.Configuration.pdgIdBins import *

#####################################
##### Define variable bin lists #####
#####################################

import math
def variableBins(nBins,lower,upper):
    original_bin_size = (upper - lower)/float(nBins)
    number_of_sections = 4
    bins_per_section = math.floor(nBins/number_of_sections)
    multipliers = [2**n for n in range(number_of_sections)]
    last = 0
    variableBins = [0]
    for multiplier in multipliers:
        bins = [last + multiplier*original_bin_size*n for n in range(1,int(math.ceil(bins_per_section/multiplier))+1)]
        last = bins[-1]
        variableBins.extend(bins)
    return variableBins

# create list of bin edges for 10cm d0 TH2s
# 10um bins from 0-2mm, then 100um bins from 2mm to 10cm so TH2 isn't too large
fine_100000um_bins = range(0, 2000, 10) + range(2000, 100001, 100)

###############################################
##### Set up the histograms to be plotted #####
###############################################

ElectronD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("electronTrackD0Error"),
            title = cms.string("Electron track #sigma(d_{0});Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr),
            ),
        cms.PSet (
            name = cms.string("electronDz_500um"),
            title = cms.string("Electron d_{z};Electron d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronDZWRTBeamspot),
            ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronD0_10um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_1000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_2000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_5000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_10000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1, 10000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_20000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2, 20000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5, 50000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -10, 100000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200000um"),
            title = cms.string("Electron d_{0};Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -20, 200000),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),

        ###################################################################
        # d0 smearing histograms
        cms.PSet (
            name = cms.string("electronUnsmearedD0_50um"),
            title = cms.string("Unsmeared Electron d_{0};Unsmeared Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0SmearingVal"),
            title = cms.string("Electron d_{0} Smearing Value;Electron d_{0} Smearing Value [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.d0SmearingVal"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsD0_10um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,1000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_1000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,10000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_10000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Electron |d_{0}|;Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200000um"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200000um_variableBins"),
            title = cms.string("Electron |d_{0}|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200000)),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("electronD0Sig_5"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_10"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_20"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_50"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_100"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_200"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_500"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("electronAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_50um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_200um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_500um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_1000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100000um"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_50um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_200um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_500um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_1000um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10000um_coarse"),
            title = cms.string("Leading electron |d_{0}| vs. Subleading electron |d_{0}|;Subleading electron |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_5"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_10"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_20"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_50"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_100"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_200"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_500"),
            title = cms.string("Leading electron |d_{0}/#sigma(d_{0})| vs. Subleading electron |d_{0}/#sigma(d_{0})|;Subleading electron |d_{0}/#sigma(d_{0})|;Leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_vs_ElectronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|;Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronTrackD0Error_500"),
            title = cms.string("Electron |d_{0}| vs. Electron #sigma(d_{0});Electron #sigma(d_{0}) [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr, "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("electronD0_vs_electronPt"),
            title = cms.string("Electron d_{0} vs. Electron p_{T};Electron p_{T} [GeV];Electron d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D abs(d0) vs. pt
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronPt_200"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronPt_500"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_vs_electronPt_1000"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronPt_200_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 200),
            binsY = cms.untracked.vdouble(20, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronPt_500_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 500),
            binsY = cms.untracked.vdouble(20, 0, 1000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10000um_vs_electronPt_1000_coarse"),
            title = cms.string("Electron |d_{0}| vs. Electron p_{T};Electron p_{T} [GeV];Electron |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 1000),
            binsY = cms.untracked.vdouble(20, 0, 10000),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPt"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron p_{T};Electron p_{T} [GeV];Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.pt", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPt"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron p_{T};Electron p_{T} [GeV];Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("electronD0_vs_electronEta"),
            title = cms.string("Electron d_{0} vs. Electron #eta;Electron #eta;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.eta", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronEta"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #eta;Electron #eta;Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.eta", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronEta"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #eta;Electron #eta;Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.eta", "10000*"+electronD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("electronD0_50um_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;Electron #phi;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;Electron #phi;Electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPhi"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #phi;Electron #phi;Electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.phi", electronD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPhi"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #phi;Electron #phi;Electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.phi", "10000*"+electronD0WRTBeamspotErr),
        ),

        ###################################################################
        # 3D leading electron d0 vs subleading electron d0 vs leading electron pt
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_2000um_vs_electronPt[0]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Electron Leading p_{T};Leading electron |d_{0}| [#mum];Subleading electron |d_{0}| [#mum];Leading electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","electron.pt"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronGenD0_10um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_50um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_100um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_200um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_500um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_5000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_50000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_100000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_200000um"),
            title = cms.string("Generated electron d_{0};Generated electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*electron.genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsGenD0_10um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_50um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_100um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_200um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_500um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_5000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_50000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_100000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_200000um"),
            title = cms.string("Generated electron |d_{0}|;Generated electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_50um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_200um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_500um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_1000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100000um"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_50um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_100um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_200um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_500um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_1000um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0[0]_vs_electronAbsGenD0[1]_10000um_coarse"),
            title = cms.string("Leading gen electron |d_{0}| vs. Subleading gen electron |d_{0}|;Subleading gen electron |d_{0}| [#mum];Leading gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0pull_50um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_100um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_200um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_500um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),

        cms.PSet (
            name = cms.string("electronD0pullAbs_50um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_100um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_200um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_500um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),

        #2D pull vs reco pt
        cms.PSet (
            name = cms.string("electronD0pull_50um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_100um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_200um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_500um_vs_electronPt"),
            title = cms.string("Electron reco d_{0} - gen d_{0} vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*"+electronSmearedD0WRTBeamspot+" - 10000*electron.genD0"),
        ),

        cms.PSet (
            name = cms.string("electronD0pullAbs_50um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_100um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_200um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_500um_vs_electronPt"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}| vs electron reco p_{T}; Electron reco p_{T} [GeV]; Electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", "10000*abs("+electronSmearedD0WRTBeamspot+") - 10000*abs(electron.genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0_10um_vs_electronGenD0_10um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_50um_vs_electronGenD0_50um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_100um_vs_electronGenD0_100um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um_vs_electronGenD0_200um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um_vs_electronGenD0_500um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_1000um_vs_electronGenD0_1000um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("electronD0_5000um_vs_electronGenD0_5000um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; Electron gen d_{0} [#mum]; Electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*electron.genD0", "10000*"+electronSmearedD0WRTBeamspot),
        ),




        cms.PSet (
            name = cms.string("electronAbsD0_10um_vs_electronAbsGenD0_10um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            binsY = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_50um_vs_electronAbsGenD0_50um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um_vs_electronAbsGenD0_100um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_vs_electronAbsGenD0_200um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronAbsGenD0_500um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1000um_vs_electronAbsGenD0_1000um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5000um_vs_electronAbsGenD0_5000um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; Electron gen |d_{0}| [#mum]; Electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(electron.genD0)", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),


    )
)



MuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("muonTrackD0Error"),
            title = cms.string("Muon track #sigma(d_{0});Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr),
        ),
        cms.PSet (
            name = cms.string("muonDz_500um"),
            title = cms.string("Muon d_{z};Muon d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonDZWRTBeamspot),
            ),


        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonD0_10um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_50um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_1000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_2000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_5000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_10000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10000, 10000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_20000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -20000, 20000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_50000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200000um"),
            title = cms.string("Muon d_{0};Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),

        ###################################################################
        # d0 smearing histograms
        cms.PSet (
            name = cms.string("muonUnsmearedD0_50um"),
            title = cms.string("Unsmeared Muon d_{0};Unsmeared Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0SmearingVal"),
            title = cms.string("Muon d_{0} Smearing Value;Muon d_{0} Smearing Value [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*muon.d0SmearingVal"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsD0_10um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,1000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_1000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,10000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_10000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,50000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingAbsD0_100000um_variableBins_coarse"),
            title = cms.string("Muon |d_{0}|;Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(20,0,100000)),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200000um"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200000um_variableBins"),
            title = cms.string("Muon |d_{0}|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200000)),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("muonD0Sig_5"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_10"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_20"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_50"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_100"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_200"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_500"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("muonAbsD0Sig_5"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_10"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_20"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_100"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_200"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_50um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_200um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_500um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_1000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100000um"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_50um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_200um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_500um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_1000um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10000um_coarse"),
            title = cms.string("Leading muon |d_{0}| vs. Subleading muon |d_{0}|;Subleading muon |d_{0}| [#mum];Leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_5"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_10"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_20"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_50"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_100"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_200"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_500"),
            title = cms.string("Leading muon |d_{0}/#sigma(d_{0})| vs. Subleading muon |d_{0}/#sigma(d_{0})|;Subleading muon |d_{0}/#sigma(d_{0})|;Leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+muonD0WRTBeamspotSig+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_vs_MuonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonTrackD0Error_500"),
            title = cms.string("Muon |d_{0}| vs. Muon #sigma(d_{0});Muon #sigma(d_{0}) [#mum];Muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr, "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("muonD0_vs_muonPt"),
            title = cms.string("Muon d_{0} vs. Muon p_{T};Muon p_{T} [GeV];Muon d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D abs(d0) vs. pt
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonPt_200"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonPt_500"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_vs_muonPt_1000"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonPt_200_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 200),
            binsY = cms.untracked.vdouble(20, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonPt_500_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 500),
            binsY = cms.untracked.vdouble(20, 0, 1000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10000um_vs_muonPt_1000_coarse"),
            title = cms.string("Muon |d_{0}| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}| [#mum];"),
            binsX = cms.untracked.vdouble(20, 0, 1000),
            binsY = cms.untracked.vdouble(20, 0, 10000),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPt"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon p_{T};Muon p_{T} [GeV];Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.pt", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D abs( sig(d0) ) vs. pt
        cms.PSet (
            name = cms.string("muonAbsD0Sig_vs_muonPt"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| vs. Muon p_{T};Muon p_{T} [GeV];Muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "abs("+muonD0WRTBeamspotSig+")"),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPt"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon p_{T};Muon p_{T} [GeV];Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("muonD0_vs_muonEta"),
            title = cms.string("Muon d_{0} vs. Muon #eta;Muon #eta;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.eta", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonEta"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #eta;Muon #eta;Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.eta", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonEta"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #eta;Muon #eta;Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.eta", "10000*"+muonD0WRTBeamspotErr),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("muonD0_50um_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;Muon #phi;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;Muon #phi;Muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPhi"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #phi;Muon #phi;Muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.phi", muonD0WRTBeamspotSig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPhi"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #phi;Muon #phi;Muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.phi", "10000*"+muonD0WRTBeamspotErr),
        ),

        ###################################################################
        # 3D leading muon d0 vs subleading muon d0 vs leading muon pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_2000um_vs_muonPt[0]"),
            title = cms.string("Leading |d_{0}| vs Subleading |d_{0}| vs Muon Leading p_{T};Leading muon |d_{0}| [#mum];Subleading muon |d_{0}| [#mum];Leading muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(1),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+muonSmearedD0WRTBeamspot+")","muon.pt"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonGenD0_10um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_50um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_100um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_200um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_500um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_5000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_50000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -50000, 50000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_100000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(1000, -100000, 100000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_200000um"),
            title = cms.string("Generated muon d_{0};Generated muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200000, 200000),
            inputVariables = cms.vstring("10000*muon.genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsGenD0_10um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_50um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_100um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_200um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_500um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_5000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_50000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_100000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_200000um"),
            title = cms.string("Generated muon |d_{0}|;Generated muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_50um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_200um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_500um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_1000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100000um"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),

        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_50um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_100um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_200um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_500um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_1000um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0[0]_vs_muonAbsGenD0[1]_10000um_coarse"),
            title = cms.string("Leading gen muon |d_{0}| vs. Subleading gen muon |d_{0}|;Subleading gen muon |d_{0}| [#mum];Leading gen muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(muon.genD0)"),
        ),

        cms.PSet (
            name = cms.string("muonD0pull_50um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_100um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_200um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_500um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),

        cms.PSet (
            name = cms.string("muonD0pullAbs_50um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_100um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_200um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_500um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),

        #2D pull vs reco pt
        cms.PSet (
            name = cms.string("muonD0pull_50um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_100um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_200um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_500um_vs_muonPt"),
            title = cms.string("Muon reco d_{0} - gen d_{0} vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*"+muonSmearedD0WRTBeamspot+" - 10000*muon.genD0"),
        ),

        cms.PSet (
            name = cms.string("muonD0pullAbs_50um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_100um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_200um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_500um_vs_muonPt"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}| vs muon reco p_{T}; Muon reco p_{T} [GeV]; Muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", "10000*abs("+muonSmearedD0WRTBeamspot+") - 10000*abs(muon.genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonD0_10um_vs_muonGenD0_10um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            binsY = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_100um_vs_muonGenD0_100um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um_vs_muonGenD0_200um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um_vs_muonGenD0_500um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_1000um_vs_muonGenD0_1000um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("muonD0_5000um_vs_muonGenD0_5000um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; Muon gen d_{0} [#mum]; Muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*muon.genD0", "10000*"+muonSmearedD0WRTBeamspot),
        ),




        cms.PSet (
            name = cms.string("muonAbsD0_10um_vs_muonAbsGenD0_10um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            binsY = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_50um_vs_muonAbsGenD0_50um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um_vs_muonAbsGenD0_100um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_vs_muonAbsGenD0_200um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonAbsGenD0_500um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1000um_vs_muonAbsGenD0_1000um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5000um_vs_muonAbsGenD0_5000um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; Muon gen |d_{0}| [#mum]; Muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
    )
)


ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_50um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_1000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,1000),
            binsY = cms.untracked.vdouble(100,0,1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10000),
            binsY = cms.untracked.vdouble(100,0,10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingAbsD0_vs_muonLeadingAbsD0_100000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(fine_100000um_bins),
            binsY = cms.untracked.vdouble(fine_100000um_bins),
            indexX = cms.untracked.int32(0),
            indexy = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200000um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200000),
            binsY = cms.untracked.vdouble(100,0,200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_50um_coare"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_1000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,1000),
            binsY = cms.untracked.vdouble(10,0,1000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10000),
            binsY = cms.untracked.vdouble(10,0,10000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200000um_coarse"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;Muon |d_{0}| [#mum];Electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200000),
            binsY = cms.untracked.vdouble(10,0,200000),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")", "10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;Muon |d_{0}/#sigma(d_{0})|;Electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")", "abs("+electronD0WRTBeamspotSig+")"),
        ),
        ###################################################################
        # 3D leading muon d0 vs leading electron d0 vs leading muon pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_muonPt[0]"),
            title = cms.string("Leading muon |d_{0}| vs Leading electron |d_{0}| vs Muon leading p_{T};Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum];Leading muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","muon.pt"),
        ),
        # 3D leading muon d0 vs leading electron d0 vs leading electron pt
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_electronAbsD0[0]_2000um_vs_electronPt[0]"),
            title = cms.string("Leading muon |d_{0}| vs Leading electron |d_{0}| vs Electron leading p_{T};Leading muon |d_{0}| [#mum];Leading electron |d_{0}| [#mum];Leading electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 2000),
            binsY = cms.untracked.vdouble(200, 0, 2000),
            binsZ = cms.untracked.vdouble(250, 0, 500),
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            indexZ = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")","10000*abs("+electronSmearedD0WRTBeamspot+")","electron.pt"),
        ),

        #gen
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_10um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_50um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_100um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_200um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_500um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_2000um"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(2000,0,2000),
            binsY = cms.untracked.vdouble(2000,0,2000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),

        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_10um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,10),
            binsY = cms.untracked.vdouble(10,0,10),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_50um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,50),
            binsY = cms.untracked.vdouble(10,0,50),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_100um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,100),
            binsY = cms.untracked.vdouble(10,0,100),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_200um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,200),
            binsY = cms.untracked.vdouble(10,0,200),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_500um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,500),
            binsY = cms.untracked.vdouble(10,0,500),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_vs_muonAbsGenD0_2000um_coarse"),
            title = cms.string("Gen electron |d_{0}| vs. Gen muon |d_{0}|;Gen muon |d_{0}| [#mum];Gen electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(10,0,2000),
            binsY = cms.untracked.vdouble(10,0,2000),
            inputVariables = cms.vstring("10000*abs(muon.genD0)", "10000*abs(electron.genD0)"),
        ),
    )
)

BeamspotHistograms = cms.PSet(
    inputCollection = cms.vstring("beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("beamspotV0"),
            title = cms.string("Beamspot v_{0};beamspot v_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*hypot(beamspot.x0, beamspot.y0)"),
        ),
        cms.PSet (
            name = cms.string("beamspotV0Error"),
            title = cms.string("Beamspot #sigma(v_{0});beamspot #sigma(v_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("10000*hypot(beamspot.x0Error, beamspot.y0Error)"),
        ),
        cms.PSet (
            name = cms.string("beamspotVz"),
            title = cms.string("Beamspot v_{z};beamspot v_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50000),
            inputVariables = cms.vstring("10000*beamspot.z0"),
        ),
    )
)


eventHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numPV"),
            title = cms.string("Number of Primary Vertex; #PV"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numPV"),
        ),
        cms.PSet (
            name = cms.string("numTruePV"),
            title = cms.string("Number of True PVs; #True PVs"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numTruePV"),
        ),
        cms.PSet (
            name = cms.string("numPV_vs_numTruePV"),
            title = cms.string("Number of Primary Vertex; #True PVs; #PV"),
            binsX = cms.untracked.vdouble(75, 0, 75),
            binsY = cms.untracked.vdouble(75, 0, 75),
            inputVariables = cms.vstring("numTruePV", "numPV"),
        ),
        cms.PSet (
            name = cms.string("puScalingFactor"),
            title = cms.string("PU Scaling Factor; log(PU Scaling Factor)"),
            binsX = cms.untracked.vdouble(200, -4, 4),
            inputVariables = cms.vstring("log10(puScalingFactor)"),
        ),
        cms.PSet (
            name = cms.string("sumJetPt"),
            title = cms.string("Sum of Jet Transverse Momentum; #Sigma p_{T}_{jet}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("sumJetPt"),
        ),
        cms.PSet (
            name = cms.string("tagMuonPt"),
            title = cms.string("Tag Muon p_{T}; Muon p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("tagMuonPt"),
        ),
        cms.PSet (
            name = cms.string("tagMuonEta"),
            title = cms.string("Tag Muon #eta; Muon #eta"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            inputVariables = cms.vstring("tagMuonEta"),
        ),
        cms.PSet (
            name = cms.string("tagMuonPhi"),
            title = cms.string("Tag Muon #phi; Muon #phi"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            inputVariables = cms.vstring("tagMuonPhi"),
        ),
        cms.PSet (
            name = cms.string("tagMuonCharge"),
            title = cms.string("Tag Muon Charge; Muon Charge"),
            binsX = cms.untracked.vdouble(3, -1, 1),
            inputVariables = cms.vstring("tagMuonCharge"),
        ),
        cms.PSet (
            name = cms.string("passTrigger"),
            title = cms.string("Pass Trigger; Trigger Flag"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("passTrigger"),
        ),
        cms.PSet (
            name = cms.string("triggerScaleFactor"),
            title = cms.string("Trigger Scale Factor; Trigger Scale Factor"),
            binsX = cms.untracked.vdouble(10, 0, 1),
            inputVariables = cms.vstring("triggerScaleFactor"),
        ),
        cms.PSet (
            name = cms.string("electronReco2016"),
            title = cms.string("Electron Reco SF; Electron Reco SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronReco2016"),
        ),
        cms.PSet (
            name = cms.string("electronID2016Tight"),
            title = cms.string("Electron ID SF; Electron ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronID2016Tight"),
        ),
        cms.PSet (
            name = cms.string("muonTracking2016GH"),
            title = cms.string("Muon Tracking SF; Muon Tracking SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonTracking2016GH"),
        ),
        cms.PSet (
            name = cms.string("muonID2016TightGH"),
            title = cms.string("Muon ID SF; Muon ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonID2016TightGH"),
        ),
        cms.PSet (
            name = cms.string("muonIso2016TightTightIDGH"),
            title = cms.string("Muon Iso SF; Muon Iso SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonIso2016TightTightIDGH"),
        ),
        cms.PSet (
            name = cms.string("electronID2017Tight"),
            title = cms.string("Electron ID SF; Electron ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("electronID2017Tight"),
        ),
        cms.PSet (
            name = cms.string("muonID2017Tight"),
            title = cms.string("Muon ID SF; Muon ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonID2017Tight"),
        ),
        cms.PSet (
            name = cms.string("muonIso2017TightTightID"),
            title = cms.string("Muon Iso SF; Muon Iso SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonIso2017TightTightID"),
        ),
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            title = cms.string("Lifetime Scaling Factor; Lifetime Scaling Factor"),
            binsX = cms.untracked.vdouble(200, -4, 4),
            inputVariables = cms.vstring("log10(lifetimeWeight)"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_100um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1mm"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1mm"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_10000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_10000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100000),
            inputVariables = cms.vstring("cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_100000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100000),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1000000um"),
            title = cms.string("Stop 0 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000000),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1000000um"),
            title = cms.string("Stop 1 c#tau;c#tau [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000000),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
    )
)


CosmicMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("MuontimeAtIpInOut"),
            title = cms.string("Muon timeAtIpInOut; timeAtIpInOut"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("time.timeAtIpInOut"),
        ),
        cms.PSet (
            name = cms.string("MuontimeAtIpOutIn"),
            title = cms.string("Muon timeAtIpOutIn; timeAtIpOutIn"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("time.timeAtIpOutIn"),
        ),
        cms.PSet (
            name = cms.string("MuontimeAtIpInOut_vs_MuontimeAtIpOutIn"),
            title = cms.string("Muon timeAtIpInOut vs. Muon timeAtIpOutIn;timeAtIpOutIn;timeAtIpInOut"),
            binsX = cms.untracked.vdouble(100,-200,200),
            binsY = cms.untracked.vdouble(100,-200,200),
            inputVariables = cms.vstring("time.timeAtIpOutIn", "time.timeAtIpInOut"),
        ),
    )
)

eventMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonPt_vs_tagMuonPt"),
            title = cms.string("Muon p_{T} vs tag Muon p_{T}; tag Muon p_{T} [GeV]; Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("eventvariable.tagMuonPt, muon.pt"),
        ),
    )
)

DiMuonHistogramsExtra = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow_100Bins"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),
        cms.PSet (
            name = cms.string("diMuonInvMassJPsiMassWindow_200Bins"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(200, 0, 10),
            inputVariables = cms.vstring("invMass (muon, muon)"),
            ),

    )
)

GenParticleHistograms = cms.PSet(
    inputCollection = cms.vstring("hardInteractionMcparticles"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("GenPdgId"),
            title = cms.string("Gen PdgId;|PDG ID|"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (pdgId)"),
            ),
        cms.PSet (
            name = cms.string("GenStatus"),
            title = cms.string("Gen Status;Status"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("status"),
            ),
        cms.PSet (
            name = cms.string("GenPt"),
            title = cms.string("Gen Transverse Momentum;Gen p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("GenEta"),
            title = cms.string("Gen Eta;Gen #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("GenPhi"),
            title = cms.string("Gen Phi;Gen #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("GenMotherPdgId"),
            title = cms.string("Gen Mother PdgId;Mother |PDG ID|"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (motherPdgId)"),
            ),
        cms.PSet (
            name = cms.string("GenMotherStatus"),
            title = cms.string("Gen Mother Status;Mother Status"),
            binsX = cms.untracked.vdouble(5, 0, 5),
            inputVariables = cms.vstring("motherStatus"),
            ),
        )
    )

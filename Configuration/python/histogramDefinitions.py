import FWCore.ParameterSet.Config as cms

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
    variableBins = []
    for multiplier in multipliers:
        bins = [last + multiplier*original_bin_size*n for n in range(1,int(math.ceil(bins_per_section/multiplier))+1)]
        last = bins[-1]
        variableBins.extend(bins)
    return variableBins

###############################################
##### Set up the histograms to be plotted #####
###############################################


ElectronD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("electronTrackD0Error"),
            title = cms.string("Electron track #sigma(d_{0});electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*gsfTrack.d0Error"),
            ),
        cms.PSet (
            name = cms.string("electronDz_500um"),
            title = cms.string("Electron d_{z};electron d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*dz"),
            ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronD0_100um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_1mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_2mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_5mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_1cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_2cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_5cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_10cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_20cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("d0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsD0_100um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_100um_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1mm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2mm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1cm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_2cm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5cm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10cm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20cm_variableBins"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20)),
            inputVariables = cms.vstring("abs(d0)"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("electronD0Sig_5"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_10"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_20"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_50"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_100"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_200"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_500"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("d0Sig"),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("electronAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_100um"),
            title = cms.string("Leading Electron |d_{0}| vs. Subleading Electron |d_{0}|;subleading electron |d_{0}| [#mum];leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_200um"),
            title = cms.string("Leading Electron |d_{0}| vs. Subleading Electron |d_{0}|;subleading electron |d_{0}| [#mum];leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_500um"),
            title = cms.string("Leading Electron |d_{0}| vs. Subleading Electron |d_{0}|;subleading electron |d_{0}| [#mum];leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        # When  used for limit-setting, make this plot with 100um bins !!!
        cms.PSet (
            name = cms.string("electronAbsD0[0]_vs_electronAbsD0[1]_10cm"),
            title = cms.string("Leading Electron |d_{0}| vs. Subleading Electron |d_{0}|;subleading electron |d_{0}| [#mum];leading electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0)", "abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_5"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_10"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_20"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_50"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_100"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_200"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig[0]_vs_electronAbsD0Sig[1]_500"),
            title = cms.string("Leading Electron |d_{0}/#sigma(d_{0})| vs. Subleading Electron |d_{0}/#sigma(d_{0})|;subleading electron |d_{0}/#sigma(d_{0})|;leading electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs(d0Sig)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm_vs_ElectronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs(d0Sig)", "10000*abs(d0)"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronTrackD0Error_500"),
            title = cms.string("Electron |d_{0}| vs. Electron #sigma(d_{0});electron #sigma(d_{0}) [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*gsfTrack.d0Error", "10000*abs(d0)"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("electronD0_vs_electronPt"),
            title = cms.string("Electron d_{0} vs. Electron p_{T};electron p_{T} [GeV];electron d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("pt", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPt"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron p_{T};electron p_{T} [GeV];electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("pt", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPt"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron p_{T};electron p_{T} [GeV];electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt", "10000*gsfTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("electronD0_vs_electronEta"),
            title = cms.string("Electron d_{0} vs. Electron #eta;electron #eta;electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("eta", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronEta"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #eta;electron #eta;electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("eta", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronEta"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #eta;electron #eta;electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("eta", "10000*gsfTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("electronD0_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;electron #phi;electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("phi", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPhi"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #phi;electron #phi;electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("phi", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPhi"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #phi;electron #phi;electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("phi", "10000*gsfTrack.d0Error"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronGenD0_100um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_200um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_500um"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_5mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_5cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_10cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("genD0"),
        ),
        cms.PSet (
            name = cms.string("electronGenD0_20cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsGenD0_100um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_200um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_500um"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_5mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_5cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_10cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsGenD0_20cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0pull_50um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_100um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_200um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0pull_500um"),
            title = cms.string("Electron reco d_{0} - gen d_{0}; electron d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),

        cms.PSet (
            name = cms.string("electronD0pullAbs_50um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_100um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_200um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0pullAbs_500um"),
            title = cms.string("Electron reco |d_{0}| - gen |d_{0}|; electron |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),


        cms.PSet (
            name = cms.string("electronD0_100um_vs_electronGenD0_100um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; electron gen d_{0} [#mum]; electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um_vs_electronGenD0_200um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; electron gen d_{0} [#mum]; electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um_vs_electronGenD0_500um"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; electron gen d_{0} [#mum]; electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_1mm_vs_electronGenD0_1mm"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; electron gen d_{0} [#mum]; electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("electronD0_5mm_vs_electronGenD0_5mm"),
            title = cms.string("Electron reco d_{0} vs. Electron gen d_{0}; electron gen d_{0} [#mum]; electron reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),




        cms.PSet (
            name = cms.string("electronAbsD0_100um_vs_electronAbsGenD0_100um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; electron gen |d_{0}| [#mum]; electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um_vs_electronAbsGenD0_200um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; electron gen |d_{0}| [#mum]; electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_electronAbsGenD0_500um"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; electron gen |d_{0}| [#mum]; electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_1mm_vs_electronAbsGenD0_1mm"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; electron gen |d_{0}| [#mum]; electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm_vs_electronAbsGenD0_5mm"),
            title = cms.string("Electron reco |d_{0}| vs. Electron gen |d_{0}|; electron gen |d_{0}| [#mum]; electron reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),


    )
)



MuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (

        ###################################################################
        # track d0 error histogram
        cms.PSet (
            name = cms.string("muonTrackD0Error"),
            title = cms.string("Muon track #sigma(d_{0});muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*innerTrack.d0Error"),
        ),
        cms.PSet (
            name = cms.string("muonDz_500um"),
            title = cms.string("Muon d_{z};muon d_{z} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*dz"),
            ),


        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonD0_100um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_1mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_2mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000, 2000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_5mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_1cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_2cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_5cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_10cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_20cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("d0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsD0_100um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_100um_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,100)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,200)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,500)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1mm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2mm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5000)),
            inputVariables = cms.vstring("10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1cm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,1)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_2cm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,2)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5cm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,5)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10cm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,10)),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20cm_variableBins"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(variableBins(100,0,20)),
            inputVariables = cms.vstring("abs(d0)"),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("muonD0Sig_5"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_10"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_20"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_50"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_100"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_200"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("d0Sig"),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_500"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("d0Sig"),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("muonAbsD0Sig_5"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_10"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_20"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_100"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_200"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs(d0Sig)"),
        ),

        ###################################################################
        # 2D plots
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_100um"),
            title = cms.string("Leading Muon |d_{0}| vs. Subleading Muon |d_{0}|;subleading muon |d_{0}| [#mum];leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_200um"),
            title = cms.string("Leading Muon |d_{0}| vs. Subleading Muon |d_{0}|;subleading muon |d_{0}| [#mum];leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_500um"),
            title = cms.string("Leading Muon |d_{0}| vs. Subleading Muon |d_{0}|;subleading muon |d_{0}| [#mum];leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs(d0)", "10000*abs(d0)"),
        ),
        # When  used for limit-setting, make this plot with 100um bins !!!
        cms.PSet (
            name = cms.string("muonAbsD0[0]_vs_muonAbsD0[1]_10cm"),
            title = cms.string("Leading Muon |d_{0}| vs. Subleading Muon |d_{0}|;subleading muon |d_{0}| [#mum];leading muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0)", "abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_5"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_10"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_20"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_50"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_100"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_200"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig[0]_vs_muonAbsD0Sig[1]_500"),
            title = cms.string("Leading Muon |d_{0}/#sigma(d_{0})| vs. Subleading Muon |d_{0}/#sigma(d_{0})|;subleading muon |d_{0}/#sigma(d_{0})|;leading muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            indexX = cms.untracked.int32(1),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs(d0Sig)", "abs(d0Sig)"),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("abs(d0Sig)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm_vs_MuonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("abs(d0Sig)", "10000*abs(d0)"),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonTrackD0Error_500"),
            title = cms.string("Muon |d_{0}| vs. Muon #sigma(d_{0});muon #sigma(d_{0}) [#mum];muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*innerTrack.d0Error", "10000*abs(d0)"),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("muonD0_vs_muonPt"),
            title = cms.string("Muon d_{0} vs. Muon p_{T};muon p_{T} [GeV];muon d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("pt", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPt"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon p_{T};muon p_{T} [GeV];muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("pt", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPt"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon p_{T};muon p_{T} [GeV];muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt", "10000*innerTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("muonD0_vs_muonEta"),
            title = cms.string("Muon d_{0} vs. Muon #eta;muon #eta;muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("eta", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonEta"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #eta;muon #eta;muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("eta", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonEta"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #eta;muon #eta;muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("eta", "10000*innerTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("muonD0_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;muon #phi;muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("phi", "10000*d0"),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPhi"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #phi;muon #phi;muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("phi", "d0Sig"),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPhi"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #phi;muon #phi;muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("phi", "10000*innerTrack.d0Error"),
        ),


        ###################################################################
        ###################################################################
        # begin gen d0 histograms

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonGenD0_100um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_200um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_500um"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_5mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_5cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_10cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("genD0"),
        ),
        cms.PSet (
            name = cms.string("muonGenD0_20cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("genD0"),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsGenD0_100um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_200um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_500um"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_5mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_5cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_10cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsGenD0_20cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonD0pull_50um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_100um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_200um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0pull_500um"),
            title = cms.string("Muon reco d_{0} - gen d_{0}; muon d_{0} pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*d0 - 10000*genD0"),
        ),

        cms.PSet (
            name = cms.string("muonD0pullAbs_50um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_100um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_200um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0pullAbs_500um"),
            title = cms.string("Muon reco |d_{0}| - gen |d_{0}|; muon |d_{0}| pull [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*abs(d0) - 10000*abs(genD0)"),
        ),


        cms.PSet (
            name = cms.string("muonD0_100um_vs_muonGenD0_100um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; muon gen d_{0} [#mum]; muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            binsY = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um_vs_muonGenD0_200um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; muon gen d_{0} [#mum]; muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            binsY = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um_vs_muonGenD0_500um"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; muon gen d_{0} [#mum]; muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_1mm_vs_muonGenD0_1mm"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; muon gen d_{0} [#mum]; muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -1000, 1000),
            binsY = cms.untracked.vdouble(100, -1000, 1000),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),
        cms.PSet (
            name = cms.string("muonD0_5mm_vs_muonGenD0_5mm"),
            title = cms.string("Muon reco d_{0} vs. Muon gen d_{0}; muon gen d_{0} [#mum]; muon reco d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            binsY = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring("10000*genD0", "10000*d0"),
        ),




        cms.PSet (
            name = cms.string("muonAbsD0_100um_vs_muonAbsGenD0_100um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; muon gen |d_{0}| [#mum]; muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um_vs_muonAbsGenD0_200um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; muon gen |d_{0}| [#mum]; muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_muonAbsGenD0_500um"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; muon gen |d_{0}| [#mum]; muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_1mm_vs_muonAbsGenD0_1mm"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; muon gen |d_{0}| [#mum]; muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            binsY = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm_vs_muonAbsGenD0_5mm"),
            title = cms.string("Muon reco |d_{0}| vs. Muon gen |d_{0}|; muon gen |d_{0}| [#mum]; muon reco |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring("10000*abs(genD0)", "10000*abs(d0)"),
        ),
    )
)


ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons"),
    histograms = cms.VPSet (

        ###################################################################
        #
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("10000*abs(muon.d0)", "10000*abs(electron.d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("10000*abs(muon.d0)", "10000*abs(electron.d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("10000*abs(muon.d0)", "10000*abs(electron.d0)"),
        ),
        # When  used for limit-setting, make this plot with 100um bins !!!
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10cm"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [cm];electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("abs(muon.d0)", "abs(electron.d0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_20cm"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [cm];electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring("abs(muon.d0)", "abs(electron.d0)"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("abs(muon.d0Sig)", "abs(electron.d0Sig)"),
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
            name = cms.string("passTrigger"),
            title = cms.string("Pass Trigger; Trigger Flag"),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("passTrigger"),
        ),
        cms.PSet (
            name = cms.string("triggerScalingFactor"),
            title = cms.string("Trigger Scaling Factor; Trigger Scaling Factor"),
            binsX = cms.untracked.vdouble(10, 0, 1),
            inputVariables = cms.vstring("triggerScalingFactor"),
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
            name = cms.string("muonReco2016"),
            title = cms.string("Muon Reco SF; Muon Reco SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonReco2016"),
        ),
        cms.PSet (
            name = cms.string("muonID2016Tight"),
            title = cms.string("Muon ID SF; Muon ID SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonID2016Tight"),
        ),
        cms.PSet (
            name = cms.string("muonIso2016Tight"),
            title = cms.string("Muon Iso SF; Muon Iso SF"),
            binsX = cms.untracked.vdouble(100, 0.5, 1.5),
            inputVariables = cms.vstring("muonIso2016Tight"),
        ),
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            title = cms.string("Lifetime Scaling Factor; Lifetime Scaling Factor"),
            binsX = cms.untracked.vdouble(200, -4, 4),
            inputVariables = cms.vstring("log10(lifetimeWeight)"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100um"),
            title = cms.string("Stop 0 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_100um"),
            title = cms.string("Stop 1 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1mm"),
            title = cms.string("Stop 0 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1mm"),
            title = cms.string("Stop 1 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_1cm"),
            title = cms.string("Stop 0 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_1cm"),
            title = cms.string("Stop 1 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_10cm"),
            title = cms.string("Stop 0 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("cTau_1000006_0"),
            ),
        cms.PSet (
            name = cms.string("ctauStop1_10cm"),
            title = cms.string("Stop 1 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("cTau_1000006_1"),
        ),
        cms.PSet (
            name = cms.string("ctauStop0_100cm"),
            title = cms.string("Stop 0 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("cTau_1000006_0"),
        ),
        cms.PSet (
            name = cms.string("ctauStop1_100cm"),
            title = cms.string("Stop 1 c#tau;c#tau [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
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

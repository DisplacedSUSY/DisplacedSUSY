import FWCore.ParameterSet.Config as cms


# import definitions of d0/dz
from DisplacedSUSY.Configuration.objectDefinitions import *


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
             title = cms.string("Electron track #sigma(d_{0});electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*electron.gsfTrack.d0Error"),
        ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("electronD0_100um"),
             title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(electronD0),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um"),
             title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(electronD0),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um"),
             title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(electronD0),
        ),
        cms.PSet (
            name = cms.string("electronD0_5mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring(electronD0),
        ),
        cms.PSet (
            name = cms.string("electronD0_5cm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500000, 500000),
            inputVariables = cms.vstring(electronD0),
        ),
        cms.PSet (
            name = cms.string("electronD0_20cm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000000, 2000000),
            inputVariables = cms.vstring(electronD0),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsD0_100um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500000),
            inputVariables = cms.vstring(electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000000),
            inputVariables = cms.vstring(electronAbsD0),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("electronD0Sig_5"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(electronD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_10"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(electronD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_20"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(electronD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_50"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(electronD0Sig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("electronAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("electronAbsD0_vs_ElectronAbsD0Sig"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(electronAbsD0Sig, electronAbsD0),
        ),

        ###################################################################
        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("electronD0_vs_electronPt"),
            title = cms.string("Electron d_{0} vs. Electron p_{T};electron p_{T} [GeV];electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", electronD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPt"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron p_{T};electron p_{T} [GeV];electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.pt", electronD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPt"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron p_{T};electron p_{T} [GeV];electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.pt", "10000*electron.gsfTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("electronD0_vs_electronEta"),
            title = cms.string("Electron d_{0} vs. Electron #eta;electron #eta;electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.eta", electronD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronEta"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #eta;electron #eta;electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.eta", electronD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronEta"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #eta;electron #eta;electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.eta", "10000*electron.gsfTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("electronD0_vs_electronPhi"),
            title = cms.string("Electron d_{0} vs. Electron #phi;electron #phi;electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.phi", electronD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("electronD0Sig_vs_electronPhi"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) vs. Electron #phi;electron #phi;electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.phi", electronD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("electronTrackD0Error_vs_electronPhi"),
            title = cms.string("Electron track #sigma(d_{0}) vs. Electron #phi;electron #phi;electron track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("electron.phi", "10000*electron.gsfTrack.d0Error"),
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
             title = cms.string("Muon track #sigma(d_{0});muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*muon.innerTrack.d0Error"),
        ),

        ###################################################################
        # d0 histograms
        cms.PSet (
            name = cms.string("muonD0_100um"),
             title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(muonD0),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um"),
             title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(muonD0),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um"),
             title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(muonD0),
        ),
        cms.PSet (
            name = cms.string("muonD0_5mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring(muonD0),
        ),
        cms.PSet (
            name = cms.string("muonD0_5cm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500000, 500000),
            inputVariables = cms.vstring(muonD0),
        ),
        cms.PSet (
            name = cms.string("muonD0_20cm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -2000000, 2000000),
            inputVariables = cms.vstring(muonD0),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsD0_100um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(muonAbsD0),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(muonAbsD0),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(muonAbsD0),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(muonAbsD0),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500000),
            inputVariables = cms.vstring(muonAbsD0),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 2000000),
            inputVariables = cms.vstring(muonAbsD0),
        ),

        ###################################################################
        # sig(d0) histograms
        cms.PSet (
            name = cms.string("muonD0Sig_5"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(muonD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_10"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(muonD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_20"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(muonD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_50"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring(muonD0Sig),
        ),

        ###################################################################
        # abs(sig(d0)) histograms
        cms.PSet (
            name = cms.string("muonAbsD0Sig_5"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_10"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_20"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("muonAbsD0_vs_MuonAbsD0Sig"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(muonAbsD0Sig, muonAbsD0),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("muonD0_vs_muonPt"),
            title = cms.string("Muon d_{0} vs. Muon p_{T};muon p_{T} [GeV];muon d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", muonD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. pt
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPt"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon p_{T};muon p_{T} [GeV];muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.pt", muonD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. pt
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPt"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon p_{T};muon p_{T} [GeV];muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.pt", "10000*muon.innerTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. eta
        cms.PSet (
            name = cms.string("muonD0_vs_muonEta"),
            title = cms.string("Muon d_{0} vs. Muon #eta;muon #eta;muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.eta", muonD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. eta
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonEta"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #eta;muon #eta;muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.eta", muonD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. eta
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonEta"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #eta;muon #eta;muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.eta", "10000*muon.innerTrack.d0Error"),
        ),
        ###################################################################
        # 2D d0 vs. phi
        cms.PSet (
            name = cms.string("muonD0_vs_muonPhi"),
            title = cms.string("Muon d_{0} vs. Muon #phi;muon #phi;muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.phi", muonD0),
        ),
        ###################################################################
        # 2D sig(d0) vs. phi
        cms.PSet (
            name = cms.string("muonD0Sig_vs_muonPhi"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) vs. Muon #phi;muon #phi;muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("muon.phi", muonD0Sig),
        ),
        ###################################################################
        # 2D track d0 error vs. phi
        cms.PSet (
            name = cms.string("muonTrackD0Error_vs_muonPhi"),
            title = cms.string("Muon track #sigma(d_{0}) vs. Muon #phi;muon #phi;muon track #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("muon.phi", "10000*muon.innerTrack.d0Error"),
        ),
    )
)


ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (

        ###################################################################
        #

        cms.PSet (
            name = cms.string("beamspotD0Error"),
             title = cms.string("Beamspot #sigma(d_{0});beamspot #sigma(d_{0}) [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("10000*hypot(beamspot.x0Error, beamspot.y0Error)"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring(muonAbsD0, electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring(muonAbsD0, electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring(muonAbsD0, electronAbsD0),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_20cm"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200000),
            binsY = cms.untracked.vdouble(100,0,200000),
            inputVariables = cms.vstring(muonAbsD0, electronAbsD0),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_5"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,5),
            binsY = cms.untracked.vdouble(100,0,5),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_10"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,10),
            binsY = cms.untracked.vdouble(100,0,10),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_20"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,50),
            binsY = cms.untracked.vdouble(100,0,50),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
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

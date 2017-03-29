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
            inputVariables = cms.vstring(electronD0_um),
        ),
        cms.PSet (
            name = cms.string("electronD0_200um"),
             title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(electronD0_um),
        ),
        cms.PSet (
            name = cms.string("electronD0_500um"),
             title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(electronD0_um),
        ),
        cms.PSet (
            name = cms.string("electronD0_5mm"),
            title = cms.string("Electron d_{0};electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring(electronD0_um),
        ),
        cms.PSet (
            name = cms.string("electronD0_5cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(electronD0_cm),
        ),
        cms.PSet (
            name = cms.string("electronD0_10cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(electronD0_cm),
        ),
        cms.PSet (
            name = cms.string("electronD0_20cm"),
            title = cms.string("Electron d_{0};electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(electronD0_cm),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("electronAbsD0_100um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_200um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_500um"),
             title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring(electronAbsD0_cm),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_10cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring(electronAbsD0_cm),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_20cm"),
            title = cms.string("Electron |d_{0}|;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring(electronAbsD0_cm),
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
        cms.PSet (
            name = cms.string("electronD0Sig_100"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(electronD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_200"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(electronD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronD0Sig_500"),
            title = cms.string("Electron d_{0}/#sigma(d_{0});electron d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
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
        cms.PSet (
            name = cms.string("electronAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(electronAbsD0Sig),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronAbsD0Sig_50"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(electronAbsD0Sig, electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_5mm_vs_ElectronAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}| vs. Electron |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|;electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(electronAbsD0Sig, electronAbsD0_um),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("electronAbsD0_500um_vs_ElectronTrackD0Error_500"),
            title = cms.string("Electron |d_{0}| vs. Electron #sigma(d_{0});electron #sigma(d_{0}) [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*electron.gsfTrack.d0Error", electronAbsD0_um),
        ),

        ###################################################################
        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("electronD0_vs_electronPt"),
            title = cms.string("Electron d_{0} vs. Electron p_{T};electron p_{T} [GeV];electron d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("electron.pt", electronD0_um),
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
            inputVariables = cms.vstring("electron.eta", electronD0_um),
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
            inputVariables = cms.vstring("electron.phi", electronD0_um),
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
            inputVariables = cms.vstring(muonD0_um),
        ),
        cms.PSet (
            name = cms.string("muonD0_200um"),
             title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(muonD0_um),
        ),
        cms.PSet (
            name = cms.string("muonD0_500um"),
             title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring(muonD0_um),
        ),
        cms.PSet (
            name = cms.string("muonD0_5mm"),
            title = cms.string("Muon d_{0};muon d_{0} [#mum]"),
            binsX = cms.untracked.vdouble(100, -5000, 5000),
            inputVariables = cms.vstring(muonD0_um),
        ),
        cms.PSet (
            name = cms.string("muonD0_5cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring(muonD0_cm),
        ),
        cms.PSet (
            name = cms.string("muonD0_10cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(muonD0_cm),
        ),
        cms.PSet (
            name = cms.string("muonD0_20cm"),
            title = cms.string("Muon d_{0};muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring(muonD0_cm),
        ),

        ###################################################################
        # abs(d0) histograms
        cms.PSet (
            name = cms.string("muonAbsD0_100um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(muonAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_200um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(muonAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_500um"),
             title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(muonAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(muonAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring(muonAbsD0_cm),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_10cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring(muonAbsD0_cm),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_20cm"),
            title = cms.string("Muon |d_{0}|;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring(muonAbsD0_cm),
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
        cms.PSet (
            name = cms.string("muonD0Sig_100"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring(muonD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_200"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -200, 200),
            inputVariables = cms.vstring(muonD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonD0Sig_500"),
            title = cms.string("Muon d_{0}/#sigma(d_{0});muon d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -500, 500),
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
        cms.PSet (
            name = cms.string("muonAbsD0Sig_100"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_200"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(muonAbsD0Sig),
        ),

        ###################################################################
        # 2D abs(d0) vs. abs(sig(d0))
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonAbsD0Sig_50"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring(muonAbsD0Sig, muonAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0_5mm_vs_MuonAbsD0Sig_500"),
            title = cms.string("Muon |d_{0}| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 5000),
            inputVariables = cms.vstring(muonAbsD0Sig, muonAbsD0_um),
        ),

        ###################################################################
        # 2D abs(d0) vs. d0 error
        cms.PSet (
            name = cms.string("muonAbsD0_500um_vs_MuonTrackD0Error_500"),
            title = cms.string("Muon |d_{0}| vs. Muon #sigma(d_{0});muon #sigma(d_{0}) [#mum];muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("10000*muon.innerTrack.d0Error", muonAbsD0_um),
        ),

        ###################################################################
        # 2D d0 vs. pt
        cms.PSet (
            name = cms.string("muonD0_vs_muonPt"),
            title = cms.string("Muon d_{0} vs. Muon p_{T};muon p_{T} [GeV];muon d_{0} [#mum];"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            binsY = cms.untracked.vdouble(100, -500, 500),
            inputVariables = cms.vstring("muon.pt", muonD0_um),
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
            inputVariables = cms.vstring("muon.eta", muonD0_um),
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
            inputVariables = cms.vstring("muon.phi", muonD0_um),
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
            name = cms.string("electronAbsD0_vs_muonAbsD0_100um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring(muonAbsD0_um, electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_200um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring(muonAbsD0_um, electronAbsD0_um),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_500um"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [#mum];electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring(muonAbsD0_um, electronAbsD0_um),
        ),
        # This plot will be used for limit-setting, make it with 100um bins !!!
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_10cm"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [cm];electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(1000,0,10),
            binsY = cms.untracked.vdouble(1000,0,10),
            inputVariables = cms.vstring(muonAbsD0_cm, electronAbsD0_cm),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0_vs_muonAbsD0_20cm"),
            title = cms.string("Electron |d_{0}| vs. Muon |d_{0}|;muon |d_{0}| [cm];electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100,0,20),
            binsY = cms.untracked.vdouble(100,0,20),
            inputVariables = cms.vstring(muonAbsD0_cm, electronAbsD0_cm),
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
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_100"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,100),
            binsY = cms.untracked.vdouble(100,0,100),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_200"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,200),
            binsY = cms.untracked.vdouble(100,0,200),
            inputVariables = cms.vstring(muonAbsD0Sig, electronAbsD0Sig),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Sig_vs_muonAbsD0Sig_500"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| vs. Muon |d_{0}/#sigma(d_{0})|;muon |d_{0}/#sigma(d_{0})|;electron |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
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
            name = cms.string("electronScalingFactor"),
            title = cms.string("Electron Scaling Factor; Electron Scaling Factor"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("electronScalingFactor"),
        ),
        cms.PSet (
            name = cms.string("muonScalingFactor"),
            title = cms.string("Muon Scaling Factor; Muon Scaling Factor"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("muonScalingFactor"),
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

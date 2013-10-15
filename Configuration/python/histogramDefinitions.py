import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


MuonD0Histograms = cms.PSet(
    inputCollection = cms.string("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonD0BeamspotS"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotM"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotL"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotXL"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzS"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzM"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzL"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzXL"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
    )
)

SecondaryMuonD0Histograms = cms.PSet(
    inputCollection = cms.string("secondary muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("secondaryMuonD0BeamspotS"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryMuonD0BeamspotM"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryMuonD0BeamspotL"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryMuonD0BeamspotXL"),
            title = cms.string("Muon d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzS"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzM"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzL"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("muonAbsD0BeamspotVsAbsDzXL"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
    )
)

ElectronD0Histograms = cms.PSet(
    inputCollection = cms.string("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0BeamspotS"),
            title = cms.string("Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotM"),
            title = cms.string("Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotL"),
            title = cms.string("Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotXL"),
            title = cms.string("Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("correctedD0"),
        ),

        cms.PSet (
            name = cms.string("electronAbsD0BeamspotS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),

##         cms.PSet (
##             name = cms.string("electronAbsD0BeamspotVsAbsDzS"),
##             title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("electronAbsD0BeamspotVsAbsDzM"),
##             title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("electronAbsD0BeamspotVsAbsDzL"),
##             title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("electronAbsD0BeamspotVsAbsDzXL"),
##             title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
    )
)

SecondaryElectronD0Histograms = cms.PSet(
    inputCollection = cms.string("secondary electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("secondaryElectronD0BeamspotS"),
            title = cms.string("Secondary Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryElectronD0BeamspotM"),
            title = cms.string("Secondary Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryElectronD0BeamspotL"),
            title = cms.string("Secondary Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("correctedD0"),
        ),
        cms.PSet (
            name = cms.string("secondaryElectronD0BeamspotXL"),
            title = cms.string("Secondary Electron d_{0} wrt Beamspot; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("correctedD0"),
        ),

        cms.PSet (
            name = cms.string("secondaryElectronAbsD0BeamspotS"),
            title = cms.string("Secondary Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryElectronAbsD0BeamspotM"),
            title = cms.string("Secondary Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryElectronAbsD0BeamspotL"),
            title = cms.string("Secondary Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryElectronAbsD0BeamspotXL"),
            title = cms.string("Secondary Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),

##         cms.PSet (
##             name = cms.string("secondaryElectronAbsD0BeamspotVsAbsDzS"),
##             title = cms.string("Secondary Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryElectronAbsD0BeamspotVsAbsDzM"),
##             title = cms.string("Secondary Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryElectronAbsD0BeamspotVsAbsDzL"),
##             title = cms.string("Secondary Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryElectronAbsD0BeamspotVsAbsDzXL"),
##             title = cms.string("Secondary Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
    )
)

ElectronMuonCorrelationHistograms = cms.PSet(
    inputCollection = cms.string("electron-muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPtVsMuonPt"),
            title = cms.string("electronPtVsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("muonPt","electronPt"),
        ),
        cms.PSet (
            name = cms.string("electronEtaVsMuonEta"),
            title = cms.string("electronEtaVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, -3, 3),
            inputVariables = cms.vstring("muonEta","electronEta"),
        ),
        cms.PSet (
            name = cms.string("electronMetMtVsMuonMetMT"),
            title = cms.string("electronMetMtVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 200),
            inputVariables = cms.vstring("muonMetMT","electronMetMT"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotForLimits"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(400, 0, 2, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
    )
)

ElectronCorrelationHistograms = cms.PSet(
    inputCollection = cms.string("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0VsElectronEta"),
            title = cms.string("electronD0VsElectronEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, 0, 0.05),
            inputVariables = cms.vstring("eta","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0VsElectronPt"),
            title = cms.string("electronD0VsElectronPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 0.05),
            inputVariables = cms.vstring("pt","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronD0VsElectronMetMT"),
            title = cms.string("electronD0VsElectronMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 0.05),
            inputVariables = cms.vstring("metMT","abs(correctedD0)"),
        ),
        #
        cms.PSet (
            name = cms.string("electronPtVsElectronEta"),
            title = cms.string("electronPtVsElectronEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, 0, 500),
            inputVariables = cms.vstring("eta","pt"),
        ),
        cms.PSet (
            name = cms.string("electronPtVsElectronMetMT"),
            title = cms.string("electronPtVsElectronMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 500),
            inputVariables = cms.vstring("metMT","pt"),
        ),
        #
        cms.PSet (
            name = cms.string("electronEtaVsElectronMetMT"),
            title = cms.string("electronEtaVsElectronMetMT"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, -3, 3),
            inputVariables = cms.vstring("metMT","eta"),
        ),
    )
)

MuonCorrelationHistograms = cms.PSet(
    inputCollection = cms.string("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonD0VsMuonEta"),
            title = cms.string("muonD0VsMuonEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, 0, 0.05),
            inputVariables = cms.vstring("eta","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0VsMuonPt"),
            title = cms.string("muonD0VsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 0.05),
            inputVariables = cms.vstring("pt","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonD0VsMuonMetMT"),
            title = cms.string("muonD0VsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 0.05),
            inputVariables = cms.vstring("metMT","abs(correctedD0)"),
        ),
        #
        cms.PSet (
            name = cms.string("muonPtVsMuonEta"),
            title = cms.string("muonPtVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, 0, 500),
            inputVariables = cms.vstring("eta","pt"),
        ),
        cms.PSet (
            name = cms.string("muonPtVsMuonMetMT"),
            title = cms.string("muonPtVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 500),
            inputVariables = cms.vstring("metMT","pt"),
        ),
        #
        cms.PSet (
            name = cms.string("muonEtaVsMuonMetMT"),
            title = cms.string("muonEtaVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, -3, 3),
            inputVariables = cms.vstring("metMT","eta"),
        ),
    )
)



ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.string("electron-muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotForLimits"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(400, 0, 2, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 0.05),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5, 100, 0, 0.5),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5, 100, 0, 5),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50, 100, 0, 50),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
    )
)



StopHistograms = cms.PSet(
    inputCollection = cms.string("stops"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("stopCtau"),
            title = cms.string("Stop lifetime; c#tau [cm]"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("ctau"),
        ),

        cms.PSet (
            name = cms.string("stopClosestVertexRank"),
            title = cms.string("The p_{T} Rank of the Closest Vertex to the Stop; vertex p_{T} rank"),
            bins = cms.untracked.vdouble(49, 1, 50),
            inputVariables = cms.vstring("closestVertexRank"),
        ),
        cms.PSet (
            name = cms.string("stopVertexDistDifference"),
            title = cms.string("Difference between distance to chosen vertex and closest vertex; dist. to chosen PV - dist. to closest PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("distToVertexDifference"),
        ),
        cms.PSet (
            name = cms.string("stopDistToVertex"),
            title = cms.string("Stop Distance to Chosen Vertex; 3D distance to chosen PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("distToVertex"),
        ),
        cms.PSet (
            name = cms.string("stopMinDistToVertex"),
            title = cms.string("Stop Minimum Distance to Any Vertex; 3D distance to closest PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("minDistToVertex"),

        ),
        cms.PSet (
            name = cms.string("stopD0"),
            title = cms.string("Stop d_{0}; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("stopDZ"),
            title = cms.string("Stop d_{z}; d_{z} [cm]"),
            bins = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("dz"),
        ),
        cms.PSet (
            name = cms.string("stopAbsD0"),
            title = cms.string("Stop |d_{0}|; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("stopAbsDZ"),
            title = cms.string("Stop |d_{z}|; |d_{z}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(dz)"),
        ),
        cms.PSet (
            name = cms.string("stopAbsD0VsAbsDz"),
            title = cms.string("Stop |d_{z}| vs. |d_{z}|; |d_{z}| [cm];|d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 1),
            inputVariables = cms.vstring("abs(dz)","abs(d0)"),
        ),
        ###################################
        cms.PSet (
            name = cms.string("stopMinD0"),
            title = cms.string("Stop Minimum d_{0}; Minimum d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("minD0"),
        ),
        cms.PSet (
            name = cms.string("stopMinDZ"),
            title = cms.string("Stop Minimum d_{z}; Minimum d_{z} [cm]"),
            bins = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("minDz"),
        ),
        cms.PSet (
            name = cms.string("stopAbsMinD0"),
            title = cms.string("Stop Minimum |d_{0}|; Minimum |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("abs(minD0)"),
        ),
        cms.PSet (
            name = cms.string("stopAbsMinDZ"),
            title = cms.string("Stop Minimum |d_{z}|; Minimum |d_{z}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(minDz)"),
        ),
        ###################################
        cms.PSet (
            name = cms.string("stopAbsD0VsAbsMinD0"),
            title = cms.string("Stop |d_{0}| vs. Minimum |d_{0}|; Minimum |d_{0}| [cm]; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 1, 100, 0, 1),
            inputVariables = cms.vstring("abs(minD0)","abs(d0)"),
        ),
        cms.PSet (
            name = cms.string("stopAbsDzVsAbsMinDz"),
            title = cms.string("Stop |d_{z}| vs. Minimum |d_{z}|; Minimum |d_{z}| [cm]; |d_{z}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 20),
            inputVariables = cms.vstring("abs(minDz)","abs(dz)"),
        ),
        cms.PSet (
            name = cms.string("stopDistToVertexVsMinDistToVertexSmall"),
            title = cms.string("Stop Distance to Chosen Vertex vs. Stop Minimum Distance to Any Vertex; 3D distance to closest PV [cm]; 3D distance to chosen PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 0.05),
            inputVariables = cms.vstring("minDistToVertex","distToVertex"),
        ),
        cms.PSet (
            name = cms.string("stopDistToVertexVsMinDistToVertexMedium"),
            title = cms.string("Stop Distance to Chosen Vertex vs. Stop Minimum Distance to Any Vertex; 3D distance to closest PV [cm]; 3D distance to chosen PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5, 100, 0, 5),
            inputVariables = cms.vstring("minDistToVertex","distToVertex"),
        ),
        cms.PSet (
            name = cms.string("stopDistToVertexVsMinDistToVertexLarge"),
            title = cms.string("Stop Distance to Chosen Vertex vs. Stop Minimum Distance to Any Vertex; 3D distance to closest PV [cm]; 3D distance to chosen PV [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50, 100, 0, 50),
            inputVariables = cms.vstring("minDistToVertex","distToVertex"),
        ),
    )
)

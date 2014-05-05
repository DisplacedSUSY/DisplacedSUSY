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
            name = cms.string("muonAbsD0BeamspotSVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.000,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,0.020,0.022,0.024,0.026,0.028,0.030,0.034,0.038,0.042,0.050),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotMVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotMVariableBinsForOverflow"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.49,0.50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotLVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.8,1.0,1.50,2.0),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
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
            name = cms.string("secondaryMuonAbsD0BeamspotS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryMuonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryMuonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("secondaryMuonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
##         cms.PSet (
##             name = cms.string("secondaryMuonAbsD0BeamspotVsAbsDzS"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryMuonAbsD0BeamspotVsAbsDzM"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryMuonAbsD0BeamspotVsAbsDzL"),
##             title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
##             bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
##             inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
##         ),
##         cms.PSet (
##             name = cms.string("secondaryMuonAbsD0BeamspotVsAbsDzXL"),
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
            name = cms.string("electronAbsD0BeamspotSVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.000,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,0.020,0.022,0.024,0.026,0.028,0.030,0.034,0.038,0.042,0.050),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotMVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotMVariableBinsForOverflow"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.49,0.50),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotLVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            variableBinsX = cms.untracked.vdouble(0.00,0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.8,1.0,1.50,2.0),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),
        
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(correctedD0)")
        ),

        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.05),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 0.5),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 5),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; |d_{z}| [cm]; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, 0, 20, 100, 0, 50),
            inputVariables = cms.vstring("abs(correctedDZ)","abs(correctedD0)"),
        ),
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

ConversionHistograms = cms.PSet(
    inputCollection = cms.string("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronEscOverPin"),
            title = cms.string("Electron EscOverPin; "),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("EscOverPin"),
        ),
        cms.PSet (
            name = cms.string("electronEseedOverPout"),
            title = cms.string("Electron EseedOverPout; "),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("EseedOverPout"),
        ),
        cms.PSet (
            name = cms.string("electronhadOverEm"),
            title = cms.string("Electron hadOverEm; "),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("hadOverEm"),
        ),
        cms.PSet (
            name = cms.string("electronabsInvEMinusInvPin"),
            title = cms.string("Electron absInvEMinusInvPin ; "),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("absInvEMinusInvPin"),
        ),
        cms.PSet (
            name = cms.string("electrondist"),
            title = cms.string("Electron dist; "),
            bins = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("dist"),
        ),
        cms.PSet (
            name = cms.string("electrondcot"),
            title = cms.string("Electron dcot; "),
            bins = cms.untracked.vdouble(100, -10, 10 ),
            inputVariables = cms.vstring("dcot"),
        ),
        cms.PSet (
            name = cms.string("electronconvradius"),
            title = cms.string("Electron convradius; "),
            bins = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("convradius"),
        ),
        cms.PSet (
            name = cms.string("electronconvPointX"),
            title = cms.string("Electron convPointX; "),
            bins = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("convPointX"),
        ),
        cms.PSet (
            name = cms.string("electronconvPointY"),
            title = cms.string("Electron convPointY; "),
            bins = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("convPointY"),
        ),
        cms.PSet (
            name = cms.string("electronconvPointZ"),
            title = cms.string("Electron convPointZ; "),
            bins = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("convPointZ"),
        ),
        cms.PSet (
            name = cms.string("electronconvPointYvsconvPointY"),
            title = cms.string("Electron convPointY vs convPointX; x [cm]; y [cm]"),
            bins = cms.untracked.vdouble(500, -100, 100, 500, -100, 100),
            inputVariables = cms.vstring("convPointX","convPointY"),
        ),




    )
)

ElectronMuonCorrelationHistograms = cms.PSet(
    inputCollection = cms.string("electron-muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPtVsMuonD0"),
            title = cms.string("electronPtVsMuonD0"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 500),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","electronPt"),
        ),
        cms.PSet (
            name = cms.string("electronPtVsMuonPt"),
            title = cms.string("electronPtVsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("muonPt","electronPt"),
        ),
        cms.PSet (
            name = cms.string("electronPtVsMuonEta"),
            title = cms.string("electronPtVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3,3, 100, 0, 500),
            inputVariables = cms.vstring("muonEta","electronPt"),
        ),
        cms.PSet (
            name = cms.string("electronPtVsMuonMetMT"),
            title = cms.string("electronPtVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 500),
            inputVariables = cms.vstring("muonMetMT","electronPt"),
        ),
        ######
        cms.PSet (
            name = cms.string("electronEtaVsMuonD0"),
            title = cms.string("electronEtaVsMuonD0"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, -3, 3),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","electronEta"),
        ),
        cms.PSet (
            name = cms.string("electronEtaVsMuonPt"),
            title = cms.string("electronEtaVsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, -3, 3),
            inputVariables = cms.vstring("muonPt","electronEta"),
        ),
        cms.PSet (
            name = cms.string("electronEtaVsMuonEta"),
            title = cms.string("electronEtaVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, -3, 3),
            inputVariables = cms.vstring("muonEta","electronEta"),
        ),
        cms.PSet (
            name = cms.string("electronEtaVsMuonMetMT"),
            title = cms.string("electronEtaVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, -3, 3),
            inputVariables = cms.vstring("muonMetMT","electronEta"),
        ),
        ######
        cms.PSet (
            name = cms.string("electronMetMtVsMuonD0"),
            title = cms.string("electronMetMtVsMuonD0"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 200),
            inputVariables = cms.vstring("abs(muonCorrectedD0)","electronMetMT"),
        ),
        cms.PSet (
            name = cms.string("electronMetMtVsMuonPt"),
            title = cms.string("electronMetMtVsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 200),
            inputVariables = cms.vstring("muonPt","electronMetMT"),
        ),
        cms.PSet (
            name = cms.string("electronMetMtVsMuonEta"),
            title = cms.string("electronMetMtVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3,3, 100, 0, 200),
            inputVariables = cms.vstring("muonEta","electronMetMT"),
        ),
        cms.PSet (
            name = cms.string("electronMetMtVsMuonMetMT"),
            title = cms.string("electronMetMtVsMuonMetMT"),
            bins = cms.untracked.vdouble(100, 0, 200, 100, 0, 200),
            inputVariables = cms.vstring("muonMetMT","electronMetMT"),
        ),
        ####
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0"),
            title = cms.string("electronAbsD0BeamspotVsMuonAbsD0"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("abs(muonCorrectedD0)","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonPt"),
            title = cms.string("electronAbsD0BeamspotVsMuonPt"),
            bins = cms.untracked.vdouble(100, 0, 500, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("muonPt","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonEta"),
            title = cms.string("electronAbsD0BeamspotVsMuonEta"),
            bins = cms.untracked.vdouble(100, -3,3, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("muonEta","abs(electronCorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0"),
            title = cms.string("electronAbsD0BeamspotVsMuonAbsD0"),
            bins = cms.untracked.vdouble(100, 0, 200, 400, 0, 2), #50 um bins
            inputVariables = cms.vstring("muonMetMT","abs(electronCorrectedD0)"),
        ),
        #######
        
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
            bins = cms.untracked.vdouble(2000, 0, 2, 2000, 0, 2), #10 um bins
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

ElectronSecondaryElectronD0Histograms = cms.PSet(
    inputCollection = cms.string("electron-secondary electron pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsSecondaryElectronAbsD0BeamspotForLimits"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{0}| wrt Beamspot; secondary electron |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(2000, 0, 2, 2000, 0, 2), #10 um bins
            inputVariables = cms.vstring("abs(electron2CorrectedD0)","abs(electron1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsSecondaryElectronAbsD0BeamspotS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{0}| wrt Beamspot; secondary electron |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 0.05),
            inputVariables = cms.vstring("abs(electron2CorrectedD0)","abs(electron1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsSecondaryElectronAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{0}| wrt Beamspot; secondary electron |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5, 100, 0, 0.5),
            inputVariables = cms.vstring("abs(electron2CorrectedD0)","abs(electron1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsSecondaryElectronAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{0}| wrt Beamspot; secondary electron |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5, 100, 0, 5),
            inputVariables = cms.vstring("abs(electron2CorrectedD0)","abs(electron1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsSecondaryElectronAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Secondary Electron |d_{0}| wrt Beamspot; secondary electron |d_{0}| [cm]; electron |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50, 100, 0, 50),
            inputVariables = cms.vstring("abs(electron2CorrectedD0)","abs(electron1CorrectedD0)"),
        ),
    )
)


MuonSecondaryMuonD0Histograms = cms.PSet(
    inputCollection = cms.string("muon-secondary muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsSecondaryMuonAbsD0BeamspotForLimits"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Secondary Muon |d_{0}| wrt Beamspot; secondary muon |d_{0}| [cm]; muon |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(2000, 0, 2, 2000, 0, 2), #10 um bins
            inputVariables = cms.vstring("abs(muon2CorrectedD0)","abs(muon1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsSecondaryMuonAbsD0BeamspotS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Secondary Muon |d_{0}| wrt Beamspot; secondary muon |d_{0}| [cm]; muon |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.05, 100, 0, 0.05),
            inputVariables = cms.vstring("abs(muon2CorrectedD0)","abs(muon1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsSecondaryMuonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Secondary Muon |d_{0}| wrt Beamspot; secondary muon |d_{0}| [cm]; muon |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 0.5, 100, 0, 0.5),
            inputVariables = cms.vstring("abs(muon2CorrectedD0)","abs(muon1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsSecondaryMuonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Secondary Muon |d_{0}| wrt Beamspot; secondary muon |d_{0}| [cm]; muon |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 5, 100, 0, 5),
            inputVariables = cms.vstring("abs(muon2CorrectedD0)","abs(muon1CorrectedD0)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsSecondaryMuonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Secondary Muon |d_{0}| wrt Beamspot; secondary muon |d_{0}| [cm]; muon |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(100, 0, 50, 100, 0, 50),
            inputVariables = cms.vstring("abs(muon2CorrectedD0)","abs(muon1CorrectedD0)"),
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

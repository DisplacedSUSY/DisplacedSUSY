import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


ElectronD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (
        ###################################################################
        cms.PSet (
            name = cms.string("electronD0BeamspotS"),
             title = cms.string("Electron d_{0} wrt Beamspot; electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotM"),
            title = cms.string("Electron d_{0} wrt Beamspot; electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotL"),
            title = cms.string("Electron d_{0} wrt Beamspot; electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronD0BeamspotXL"),
            title = cms.string("Electron d_{0} wrt Beamspot; electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronD0SigBeamspotS"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("electronD0SigBeamspotM"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("electronD0SigBeamspotL"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("electronD0SigBeamspotXL"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspotS"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 10),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspotM"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspotL"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 50),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspotXL"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 100),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.05),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotSVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.000,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,0.020,0.022,0.024,0.026,0.028,0.030,0.034,0.038,0.042,0.050),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotMVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.50),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 5),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotLVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.00,0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.8,1.0,1.50,2.0),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)")
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsElectronAbsD0SigBeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; electron |d_{0}/#sigma(d_{0})| [cm]; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzS"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; electron |d_{z}| [cm]; |electron d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; electron |d_{z}| [cm]; |electron d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; electron |d_{z}| [cm]; |electron d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsAbsDzXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{z}|; electron |d_{z}| [cm]; |electron d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsEta"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |#eta|; electron |#eta|; |electron d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(25, 0, 2.5),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("abs(electron.eta)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        ###################################################################
    )
)
MuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (
        ###################################################################
        cms.PSet (
            name = cms.string("muonD0BeamspotS"),
             title = cms.string("Muon d_{0} wrt Beamspot; muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.05, 0.05),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotM"),
            title = cms.string("Muon d_{0} wrt Beamspot; muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotL"),
            title = cms.string("Muon d_{0} wrt Beamspot; muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonD0BeamspotXL"),
            title = cms.string("Muon d_{0} wrt Beamspot; muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonD0SigBeamspotS"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("muonD0SigBeamspotM"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("muonD0SigBeamspotL"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -50, 50),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("muonD0SigBeamspotXL"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot; d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -100, 100),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspotS"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 10),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspotM"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspotL"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 50),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspotXL"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; |d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 100),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.05),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotSVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.000,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,0.020,0.022,0.024,0.026,0.028,0.030,0.034,0.038,0.042,0.050),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotMVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.00,0.01,0.02,0.03,0.04,0.05,0.07,0.09,0.11,0.15,0.20,0.50),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 5),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotLVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(0.00,0.05,0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.8,1.0,1.50,2.0),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)")
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsMuonAbsD0SigBeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; muon |d_{0}/#sigma(d_{0})| [cm]; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            binsY = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))","abs((-(muon.vx - beamspot.x0)*mu\
on.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzS"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; muon |d_{z}| [cm]; |muon d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 0.05),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; muon |d_{z}| [cm]; |muon d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; muon |d_{z}| [cm]; |muon d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsAbsDzXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{z}|; muon |d_{z}| [cm]; |muon d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            binsY = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsEta"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |#eta|; muon |#eta|; |muon d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(25, 0, 2.5),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("abs(muon.eta)","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)"),
        ),
        ###################################################################
    )
)

ElectronMuonD0Histograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronIpMuonIpSmall"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(50,0,0.05),
            binsY = cms.untracked.vdouble(50,0,0.05),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpMedium"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(500,0,0.5),
            binsY = cms.untracked.vdouble(500,0,0.5),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpLarge"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [cm]"),
            binsX = cms.untracked.vdouble(50,0,5),
            binsY = cms.untracked.vdouble(50,0,5),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
    )
)


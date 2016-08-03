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
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(50, 0, 500),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotSVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,220,240,260,280,300,340,380,420,480,500),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotFineTunedBinningOne"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,10,20,30,40,50,60,70,80,90,100,120,140,160,180,200,250,300,350,400,450,500,600,700,800,900,1000,1010),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotFineTunedBinningTwo"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,20,40,60,80,100,150,200,250,300,400,500,600,800,1000,1010),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotM"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(500, 0, 5000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotMVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,100,200,300,400,500,700,900,1100,1500,2000,5000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(50, 0, 50000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotLVariableBins"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,500,1000,1500,2000,3000,4000,5000,6000,8000,10000,15000,20000,50000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotXL"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotInclusive"),
            title = cms.string("Electron |d_{0}| wrt Beamspot; electron |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000")
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsElectronAbsD0SigBeamspot"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Electron |d_{0}/#sigma(d_{0})| wrt Beamspot; electron |d_{0}/#sigma(d_{0})| [cm]; electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(500, 0, 0.05),
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
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(50, 0, 500),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotSVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,220,240,260,280,300,340,380,420,480,500),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotFineTunedBinningOne"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,10,20,30,40,50,60,70,80,90,100,120,140,160,180,200,250,300,350,400,450,500,600,700,800,900,1000,1010),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotFineTunedBinningTwo"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,20,40,60,80,100,150,200,250,300,400,500,600,800,1000,1010),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotM"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(500, 0, 5000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotMVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,100,200,300,400,500,700,900,1100,1500,2000,5000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(50, 0, 50000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotLVariableBins"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(0,500,1000,1500,2000,3000,4000,5000,6000,8000,10000,15000,20000,50000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotXL"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(100, 0, 200000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotInclusive"),
            title = cms.string("Muon |d_{0}| wrt Beamspot; muon |d_{0}| [#mum]"),
            binsX = cms.untracked.vdouble(1000, 0, 100000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000")
        ),
        ###################################################################
        cms.PSet (
            name = cms.string("muonAbsD0BeamspotVsMuonAbsD0SigBeamspot"),
            title = cms.string("Muon |d_{0}| wrt Beamspot vs. Muon |d_{0}/#sigma(d_{0})| wrt Beamspot; muon |d_{0}/#sigma(d_{0})| [cm]; muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            binsY = cms.untracked.vdouble(500, 0, 0.05),
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
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [#mum]"),
            binsX = cms.untracked.vdouble(50,0,500),
            binsY = cms.untracked.vdouble(50,0,500),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpMedium"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [#mum]"),
            binsX = cms.untracked.vdouble(500,0,5000),
            binsY = cms.untracked.vdouble(500,0,5000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000"),
        ),
        cms.PSet (
            name = cms.string("electronIpMuonIpLarge"),
            title = cms.string("Electron abs(Ip) vs Muon abs(Ip);|d_{xy}_{mu}| [#mum]"),
            binsX = cms.untracked.vdouble(1000,0,100000),
            binsY = cms.untracked.vdouble(1000,0,100000),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt) * 10000","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt) * 10000"),
        ),
    )
)


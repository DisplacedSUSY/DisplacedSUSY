bbbarMuFile = '/data/users/bing/condor/QCDMuon76X_IsoCorr_April11thPreApr/SingleMu_2015D.root'
bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_April11thPreApr/SingleEle_2015D.root'
#bbbarMuFile = '/data/users/bing/condor/AntiIsoDisplaced76X_IsoCorr_April11thPreApr/MuonEG_2015D.root'
#bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_SinglePhoton_April11thPreApr/SinglePhoton_2015D.root'
#bbbarEleFile = '/data/users/bing/condor/AntiIsoDisplaced76X_IsoCorr_April11thPreApr/MuonEG_2015D.root'
bbbarMuIPShape = 'QCDMuonControlRegionPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
bbbarEleIPShape = 'QCDElectronControlRegionPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'
#bbbarMuIPShape = 'AntiIsoElectronBlindedMuonDisplacedPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
#bbbarEleIPShape = 'AntiIsoMuonBlindedElectronDisplacedPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'

normSource = 'EMuPreselection'

dataNormFile = '/data/users/bing/condor/EMuPreselection76X_IsoCorr_April11thPreApr/MuonEG_2015D.root'
bgNormFile = '/data/users/bing/condor/EMuPreselection76X_IsoCorr_April11thPreApr/Background.root'
normIPDistribution = 'EMuPreselectionInclusiveTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

targetSource = 'Displaced control region'

dataTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_IsoCorr_April11thPreApr/MuonEG_2015D.root'
bgTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_IsoCorr_April11thPreApr/Background.root'
targetNormIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

normMuLow = 0.01
normMuHigh = 0.02
normEleLow = 0.01
normEleHigh = 0.02

targetMuLow = 0.02
targetMuHigh = 10
targetEleLow = 0.02
targetEleHigh = 10


dataDrivenQCDFile = './condor/DisplacedControlRegionWithSF_Feb8th/QCDFromData.root'
dataDrivenQCDIPDistribution = 'EMuPreselectionInclusiveTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

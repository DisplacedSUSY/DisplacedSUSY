bbbarMuFile = '/data/users/bing/condor/QCDMuon76X_IsoCorr_April5th/SingleMu_2015D.root'
bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_April5th/SingleEle_2015D.root'
bbbarMuIPShape = 'QCDMuonDisplacedControlRegionPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
bbbarEleIPShape = 'QCDElectronDisplacedControlRegionPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'

normSource = 'Displaced control region'

dataNormFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/MuonEG_2015D.root'
bgNormFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/Background.root'
normIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

targetSource = 'Displaced control region'

dataTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/MuonEG_2015D.root'
bgTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/Background.root'
targetNormIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

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

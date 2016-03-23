bbbarMuFile = '/data/users/bing/condor/QCDMuon76X/SingleMu_2015D.root'
bbbarEleFile = '/data/users/bing/condor/QCDElectron76X/SingleEle_2015D.root'
bbbarMuIPShape = 'QCDMuonControlRegionPlotter/Muon-beamspot Plots/muonAbsD0BeamspotS'
bbbarEleIPShape = 'QCDElectronControlRegionPlotter/Electron-beamspot Plots/electronAbsD0BeamspotS'

normSource = 'Displaced control region'

dataNormFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/MuonEG_2015D.root'
bgNormFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/Background.root'
normIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

#dataNormFile = '/data/users/bing/condor/PromptControlRegionWithSF_Feb8th/MuonEG_2015D.root'
#bgNormFile = '/data/users/bing/condor/PromptControlRegionWithSF_Feb8th/Background.root'
#normIPDistribution = 'MuEleNoIsoPromptControlRegionNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

targetSource = 'Displaced control region'

dataTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/MuonEG_2015D.root'
bgTargetFile = '/data/users/bing/condor/DisplacedControlRegion76X_March9/Background.root'
targetNormIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

normMuLow = 0.01
normMuHigh = 0.015
normEleLow = 0.01
normEleHigh = 0.012

targetMuLow = 0.015
targetMuHigh = 0.02
targetEleLow = 0.012
targetEleHigh = 0.02


#dataDrivenQCDFile = './condor/SignalSelectionsWithSF_Feb9th/QCDFromData.root'
#dataDrivenQCDIPDistribution = 'SignalRegionSelectionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'
dataDrivenQCDFile = './condor/DisplacedControlRegionWithSF_Feb8th/QCDFromData.root'
dataDrivenQCDIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpInclusive'

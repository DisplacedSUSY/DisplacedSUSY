#bbbarEleFile = '/data/users/bing/condor/QCDElectronControlRegion_Run2PreApproval/MCSubtracted.root'
#bbbarMuFile = '/data/users/bing/condor/QCDMuonControlRegion_Run2PreApproval/SingleMu_2015D.root'
#bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_July7th_NoJetArb/MCSubtracted.root'
bbbarEleFile = '/data/users/bing/condor/AntiIso_July11th/MuonEG_2015D.root'
#bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_July7th_NoJetArb/SingleEle_2015D.root'
#bbbarEleFile = '/data/users/bing/condor/QCDElectron76X_IsoCorr_July7th_NoJetArb/SingleEleStop200_1000mm.root'
#bbbarMuFile = '/data/users/bing/condor/QCDMuon76X_IsoCorr_July7th_NoJetArb/SingleMu_2015D.root'
bbbarMuFile = '/data/users/bing/condor/AntiIso_July11th/MuonEG_2015D.root'
#bbbarMuFile = '/data/users/bing/condor/QCDMuon76X_IsoCorr_July7th_NoJetArb/SingleMuStop200_1000mm.root'
#bbbarEleFile = '/data/users/bing/condor/QCDElectronSystematic_July10th/SingleEle_2015D.root'
#bbbarMuFile = '/data/users/bing/condor/QCDMuonSystematic_July10th/SingleMu_2015D.root'
#bbbarMuIPShape = 'QCDMuonDisplacedControlRegionPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
bbbarMuIPShape = 'AntiIsoElectronBlindedMuonDisplacedPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
#bbbarEleIPShape = 'QCDElectronDisplacedControlRegionPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'
bbbarEleIPShape = 'AntiIsoMuonBlindedElectronDisplacedPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'


normSource = 'Muon Displaced Region'
#dataNormFile = '/data/users/bing/condor/AntiIso_July11th/MuonEG_2015D.root'
#bgNormFile = '/data/users/bing/condor/AntiIso_July11th/Background.root'
#normIPDistribution = 'AntiIsoElectronBlindedMuonDisplacedPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'
dataNormFile = '/data/users/bing/condor/DisplacedControlRegion_July10th/stop200_0p5mm.root'
bgNormFile = '/data/users/bing/condor/DisplacedControlRegion_July10th/Background.root'
normIPDistribution = 'DisplacedControlRegionNoIsoInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

targetSource = 'Displaced control region'

#dataTargetFile = '/data/users/bing/condor/AntiIso_July11th/MuonEG_2015D.root'
#bgTargetFile = '/data/users/bing/condor/AntiIso_July11th/Background.root'
#targetNormIPDistribution = 'AntiIsoElectronBlindedMuonDisplacedPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'
dataTargetFile = '/data/users/bing/condor/DisplacedControlRegion_July10th/stop200_0p5mm.root'
bgTargetFile = '/data/users/bing/condor/DisplacedControlRegion_July10th/Background.root'
targetNormIPDistribution = 'DisplacedControlRegionNoIsoInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

regionMaps = {
"regionMap1" : {
"normMuLow" : 0.01,
"normMuHigh" : 0.02,
"normEleLow" : 0.01,
"normEleHigh" : 0.02,
"targetMuLow" : 0.02,
"targetMuHigh" : 10,
"targetEleLow" : 0.02,
"targetEleHigh": 10,},
"regionMap2" : {
"normMuLow" : 0.01,
"normMuHigh" : 0.02,
"normEleLow" : 0.01,
"normEleHigh" : 0.02,
"targetMuLow" : 0.05,
"targetMuHigh" : 10,
"targetEleLow" : 0.05,
"targetEleHigh": 10,},
"regionMap3" : {
"normMuLow" : 0.01,
"normMuHigh" : 0.02,
"normEleLow" : 0.01,
"normEleHigh" : 0.02,
"targetMuLow" : 0.1,
"targetMuHigh" : 10,
"targetEleLow" : 0.1,
"targetEleHigh": 10,},
}
#regionMaps = {
#"regionMap1" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.012,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.012,
#"targetEleHigh": 0.02,},
#"regionMap2" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.015,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.015,
#"targetEleHigh": 0.02,},
#"regionMap3" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.18,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.018,
#"targetEleHigh": 0.02,},
#"regionMap4" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.012,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.015,
#"targetEleHigh": 0.02,},
#"regionMap5" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.012,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.018,
#"targetEleHigh": 0.02,},
#"regionMap6" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.018,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.012,
#"targetEleHigh": 0.02,},
#"regionMap7" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.018,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.015,
#"targetEleHigh": 0.02,},
#"regionMap8" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.015,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.012,
#"targetEleHigh": 0.02,},
#"regionMap9" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.015,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.018,
#"targetEleHigh": 0.02,},
#}

performClosure = False

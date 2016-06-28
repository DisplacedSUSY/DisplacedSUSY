bbbarEleFile = '/data/users/bing/condor/QCDElectronControlRegion_Run2PreApproval/MCSubtracted.root'
bbbarMuFile = '/data/users/bing/condor/QCDMuonControlRegion_Run2PreApproval/SingleMu_2015D.root'
bbbarMuIPShape = 'QCDMuonIsoControlRegionPlotter/Muon-beamspot Plots/muonAbsD0BeamspotM'
bbbarEleIPShape = 'QCDElectronIsoControlRegionPlotter/Electron-beamspot Plots/electronAbsD0BeamspotM'

normSource = 'Displaced control region'
dataNormFile = '/data/users/bing/condor/DisplacedControlRegion_Run2PreApproval/MuonEG_2015D.root'
bgNormFile = '/data/users/bing/condor/DisplacedControlRegion_Run2PreApproval/Background.root'
normIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

targetSource = 'Displaced control region'

dataTargetFile = '/data/users/bing/condor/DisplacedControlRegion_Run2PreApproval/MuonEG_2015D.root'
bgTargetFile = '/data/users/bing/condor/DisplacedControlRegion_Run2PreApproval/Background.root'
targetNormIPDistribution = 'DisplacedControlRegionNoIsoNoOSInclusiveDisplacedTriggerPlotter/Electron-muon-beamspot Plots/electronIpMuonIpMedium'

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
#"targetMuLow" : 0.018,
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
#"targetMuLow" : 0.015,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.012,
#"targetEleHigh": 0.02,},
#"regionMap7" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.015,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.018,
#"targetEleHigh": 0.02,},
#"regionMap8" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.018,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.012,
#"targetEleHigh": 0.02,},
#"regionMap9" : {
#"normMuLow" : 0.01,
#"normMuHigh" : 0.02,
#"normEleLow" : 0.01,
#"normEleHigh" : 0.02,
#"targetMuLow" : 0.018,
#"targetMuHigh" : 0.02,
#"targetEleLow" : 0.015,
#"targetEleHigh": 0.02,},
#}

performClosure = False

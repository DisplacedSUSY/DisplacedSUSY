import FWCore.ParameterSet.Config as cms
import os
import copy

electronScaleFactors2016 = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("Reco"),
        version = cms.string("2016"),
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
    ),
)

electronScaleFactors2017 = cms.VPSet (
    #only "ID" SFs in 2017, no "Reco"
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2017"),
        wp = cms.string("Tight"),
    ),
)

muonScaleFactors2016 = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Iso"),
        version = cms.string("2016"),
        wp = cms.string("TightTightID"),
        eras = cms.vstring("GH"),
        lumis = cms.vdouble(16146),
        additionalSystematic = cms.double(0.005),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
        eras = cms.vstring("GH"),
        lumis = cms.vdouble(16146),
        additionalSystematic = cms.double(0.01),
    ),
)

muonScaleFactors2017 = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Iso"),
        version = cms.string("2017"),
        wp = cms.string("TightTightID"),
        additionalSystematic = cms.double(0.005), #to be updated when muon POG makes this update
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("ID"),
        version = cms.string("2017"),
        wp = cms.string("Tight"),
        additionalSystematic = cms.double(0.01),#additional systematic to be updated when muon POG makes this update
    ),
)

ElectronScaleFactorProducer = {
    'name'         : 'ObjectScalingFactorProducer',
    'electronFile' : cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root'),
    'muonFile'     : cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root'),
    'scaleFactors' : electronScaleFactors2016,
}

MuonScaleFactorProducer = copy.deepcopy(ElectronScaleFactorProducer)
MuonScaleFactorProducer['scaleFactors'] = muonScaleFactors2016

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Lepton SFs: 2016"
    ElectronScaleFactorProducer['scaleFactors'] = electronScaleFactors2016
    MuonScaleFactorProducer['scaleFactors'] = muonScaleFactors2016
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Lepton SFs: 2017"
    ElectronScaleFactorProducer['scaleFactors'] = electronScaleFactors2017
    MuonScaleFactorProducer['scaleFactors'] = muonScaleFactors2017

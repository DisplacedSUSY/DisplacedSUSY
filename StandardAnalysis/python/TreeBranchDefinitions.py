import FWCore.ParameterSet.Config as cms

from OSUT3Analysis.Configuration.cutUtilities import *
import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs

#######################################################
##### Set up the branches to be added to the tree #####
#######################################################

###########################
##### Event variables #####
###########################

EventVariableBranches_names = [
    "run",
    "ls",
    "event",
    "numPV",
    "deltaT_leadingTwoMuons",
]

EventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in EventVariableBranches_names]),
)

#to do: add lifetime weights like in https://github.com/OSU-CMS/DisappTrks/blob/master/StandardAnalysis/python/TreeBranchDefinitions.py#L92-L104

###########################
######### Leptons #########
###########################

LeptonBranches_names = [
    "pt",
    "eta",
    "phi",
    "charge",
]

###########################
######## Electrons ########
###########################

Electron0Branches = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x+"Electron0"), index = cms.untracked.int32(0), inputVariables = cms.vstring(x)) for x in LeptonBranches_names]),
)
Electron0Branches.branches.extend([cms.PSet(name = cms.string("rhoBasedIsolationElectron0"), index = cms.untracked.int32(0), inputVariables = cms.vstring(objectDefs.electron_newIso_string))])
Electron0Branches.branches.extend([cms.PSet(name = cms.string("genMatchMotherPdgIdElectron0"), index = cms.untracked.int32(0), inputVariables = cms.vstring("genMatchedParticle.noFlags.uniqueMotherPdgId"))])

Electron1Branches = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x+"Electron1"), index = cms.untracked.int32(1), inputVariables = cms.vstring(x)) for x in LeptonBranches_names]),
)
Electron1Branches.branches.extend([cms.PSet(name = cms.string("rhoBasedIsolationElectron1"), index = cms.untracked.int32(1), inputVariables = cms.vstring(objectDefs.electron_newIso_string))])
Electron0Branches.branches.extend([cms.PSet(name = cms.string("genMatchMotherPdgIdElectron1"), index = cms.untracked.int32(1), inputVariables = cms.vstring("genMatchedParticle.noFlags.uniqueMotherPdgId"))])


Electron0D0Branches = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("d0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absUnsmearedD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("d0SigElectron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet(
            name = cms.string("absD0SigElectron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0ErrorElectron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr),
        ),
    )
)

Electron1D0Branches = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("d0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+electronSmearedD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+electronSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absUnsmearedD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("d0SigElectron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring(electronD0WRTBeamspotSig),
        ),
        cms.PSet(
            name = cms.string("absD0SigElectron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("abs("+electronD0WRTBeamspotSig+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0ErrorElectron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+electronD0WRTBeamspotErr),
        ),
    )
)


###########################
########## Muons ##########
###########################

AdditionalMuonBranches_names = [
    "isGlobalMuon",
    "isPFMuon",
]

Muon0Branches = cms.PSet(
    inputCollection = cms.vstring("muons"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x+"Muon0"), index = cms.untracked.int32(0), inputVariables = cms.vstring(x)) for x in LeptonBranches_names]),
)
Muon0Branches.branches.extend([cms.PSet(name = cms.string(x+"0"), index = cms.untracked.int32(0), inputVariables = cms.vstring(x)) for x in AdditionalMuonBranches_names])
Muon0Branches.branches.extend([cms.PSet(name = cms.string("rhoBasedIsolationMuon0"), index = cms.untracked.int32(0), inputVariables = cms.vstring(objectDefs.muon_iso_string))])
Muon0Branches.branches.extend([cms.PSet(name = cms.string("genMatchMotherPdgIdMuon0"), index = cms.untracked.int32(0), inputVariables = cms.vstring("genMatchedParticle.noFlags.uniqueMotherPdgId"))])

Muon1Branches = cms.PSet(
    inputCollection = cms.vstring("muons"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x+"Muon1"), index = cms.untracked.int32(1), inputVariables = cms.vstring(x)) for x in LeptonBranches_names]),
)
Muon1Branches.branches.extend([cms.PSet(name = cms.string(x+"1"), index = cms.untracked.int32(1), inputVariables = cms.vstring(x)) for x in AdditionalMuonBranches_names])
Muon1Branches.branches.extend([cms.PSet(name = cms.string("rhoBasedIsolationMuon1"), index = cms.untracked.int32(1), inputVariables = cms.vstring(objectDefs.muon_iso_string))])
Muon0Branches.branches.extend([cms.PSet(name = cms.string("genMatchMotherPdgIdMuon1"), index = cms.untracked.int32(1), inputVariables = cms.vstring("genMatchedParticle.noFlags.uniqueMotherPdgId"))])

Muon0D0Branches = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("d0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absUnsmearedD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("d0SigMuon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet(
            name = cms.string("absD0SigMuon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0ErrorMuon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr),
        ),
    )
)

Muon1D0Branches = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("d0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+muonSmearedD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+muonSmearedD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspot),
        ),
        cms.PSet(
            name = cms.string("absUnsmearedD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+")"),
        ),
        cms.PSet(
            name = cms.string("d0SigMuon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring(muonD0WRTBeamspotSig),
        ),
        cms.PSet(
            name = cms.string("absD0SigMuon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("abs("+muonD0WRTBeamspotSig+")"),
        ),
        cms.PSet(
            name = cms.string("unsmearedD0ErrorMuon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*"+muonD0WRTBeamspotErr),
        ),
    )
)

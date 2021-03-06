import os
import FWCore.ParameterSet.Config as cms

from OSUT3Analysis.Configuration.cutUtilities import *
import DisplacedSUSY.StandardAnalysis.objectDefinitions as objectDefs
from DisplacedSUSY.StandardAnalysis.Options import *

#######################################################
# some stuff to set up first
#######################################################

# strings for lepton id/iso eventvariable branches
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    year = "2016"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    year = "2017"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    year = "2018"
else:
    year = "2018"
    print "What CMSSW release are you in? We expect you to be in 80X or 94X or 102X"

# for d0 smearing signal systematic uncertainty
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    electronD0SmearingWidth = 0.001475 #in cm; ave of values from e-e and e-mu pcr (elog 1281), also see elog 1760
    electronD0SmearingWidthUncert = 0.000036
    muonD0SmearingWidth = 0.000757 #in cm; ave of values from from e-mu and mu-mu pcr (elog 1281)
    muonD0SmearingWidthUncert = 0.000012
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    electronD0SmearingWidth = 0.000918 #in cm; ave of values from e-e and e-mu pcr (elog 1359), also see elog 1760
    electronD0SmearingWidthUncert = 0.000041
    muonD0SmearingWidth = 0.000811 #in cm; ave of values from from e-mu and mu-mu pcr (elog 1359)
    muonD0SmearingWidthUncert = 0.000008
else:
    electronD0SmearingWidth = 1.
    electronD0SmearingWidthUncert = 0
    muonD0SmearingWidth = 1
    muonD0SmearingWidthUncert = 0

electronD0SmearingWidthUp = electronD0SmearingWidth + electronD0SmearingWidthUncert
electronD0SmearingWidthDown = electronD0SmearingWidth - electronD0SmearingWidthUncert
muonD0SmearingWidthUp = muonD0SmearingWidth + muonD0SmearingWidthUncert
muonD0SmearingWidthDown = muonD0SmearingWidth - muonD0SmearingWidthUncert

electronD0SmearingWidthUpSF = str(1.0*electronD0SmearingWidthUp/electronD0SmearingWidth)
electronD0SmearingWidthDownSF = str(1.0*electronD0SmearingWidthDown/electronD0SmearingWidth)
muonD0SmearingWidthUpSF = str(1.0*muonD0SmearingWidthUp/muonD0SmearingWidth)
muonD0SmearingWidthDownSF = str(1.0*muonD0SmearingWidthDown/muonD0SmearingWidth)

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
    "cosAlpha_leadingTwoMuons",
    "nDispEEVtxsInMaterial",
    "vtxEEXInMaterial",
    "vtxEEYInMaterial",
    "vtxEEZInMaterial",
    "vtxEEXErrInMaterial",
    "vtxEEYErrInMaterial",
    "vtxEEZErrInMaterial",
    "vtxEEChisqInMaterial",
    "nDispMuMuVtxsInMaterial",
    "vtxMuMuXInMaterial",
    "vtxMuMuYInMaterial",
    "vtxMuMuZInMaterial",
    "vtxMuMuXErrInMaterial",
    "vtxMuMuYErrInMaterial",
    "vtxMuMuZErrInMaterial",
    "vtxMuMuChisqInMaterial",
    "nDispEMuVtxsInMaterial",
    "vtxEMuXInMaterial",
    "vtxEMuYInMaterial",
    "vtxEMuZInMaterial",
    "vtxEMuXErrInMaterial",
    "vtxEMuYErrInMaterial",
    "vtxEMuZErrInMaterial",
    "vtxEMuChisqInMaterial",
    "puScalingFactor",
    "puScalingFactorUp",
    "puScalingFactorDown",
    "cTau_1000006_0",
    "cTau_1000006_1",
    "cTau_1000006_2",
    "cTau_1000006_3",
    "cTau_1000006_4",
    "cTau_1000006_5",
    "cTau_1000006_6",
    "cTau_1000006_7",
    "cTau_1000006_8",
    "cTau_1000006_9",
    "cTau_9000006_0",
    "cTau_9000006_1",
    "cTau_9000006_2",
    "cTau_9000006_3",
    "cTau_9000006_4",
    "cTau_9000006_5",
    "cTau_9000006_6",
    "cTau_9000006_7",
    "cTau_9000006_8",
    "cTau_9000006_9",
    "lifetimeWeight",
]

EventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in EventVariableBranches_names]),
)

#everybody is in cm here
reweighting_pairs = []
if(HToSS):
    for sourceCTau in [0.1, 1, 10, 100, 1000, 10000, 100000]:
        srcCTau = str(int(sourceCTau)) if sourceCTau>=1 else str(sourceCTau).replace(".", "p")

        destinationCTaus = [float(0.1 * i * sourceCTau) for i in range(2, 11)]
        if sourceCTau == 0.1:
            destinationCTaus.extend([0.01])

        for dst in destinationCTaus:
            dstCTau = str(int(dst)) if dst>=1 else str(dst).replace(".", "p")
            thisName = "lifetimeWeight_9000006_" + srcCTau + "cmTo" + dstCTau + "cm"
            reweighting_pairs.append((srcCTau, dstCTau))
            #print thisName
            EventVariableBranches.branches.append(
                cms.PSet(
                    name = cms.string(thisName),
                    inputVariables = cms.vstring(thisName),
                )
            )

else:
    for sourceCTau in [0.01, 0.1, 1, 10, 100]:
        srcCTau = str(int(sourceCTau)) if sourceCTau>=1 else str(sourceCTau).replace(".", "p")

        destinationCTaus = [float(0.1 * i * sourceCTau) for i in range(2, 11)]
        if sourceCTau == 0.01:
            destinationCTaus.extend([0.001])
        if sourceCTau == 100:
            destinationCTaus.extend([float(1 * i * sourceCTau) for i in range(2, 11)])

        for dst in destinationCTaus:
            dstCTau = str(int(dst)) if dst>=1 else str(dst).replace(".", "p")
            thisName = "lifetimeWeight_1000006_" + srcCTau + "cmTo" + dstCTau + "cm"
            reweighting_pairs.append((srcCTau, dstCTau))
            #print thisName
            EventVariableBranches.branches.append(
                cms.PSet(
                    name = cms.string(thisName),
                    inputVariables = cms.vstring(thisName),
                )
            )

###########################
# electron event variables
ElectronEventVariableBranches_names = [
    "electronID"+year+"Tight",
    "electronID"+year+"TightUp",
    "electronID"+year+"TightDown",
]

EEEventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in ElectronEventVariableBranches_names]),
)

###########################
# muon event variables
MuonEventVariableBranches_names = [
    "muonIso"+year+"TightTightID",
    "muonIso"+year+"TightTightIDUp",
    "muonIso"+year+"TightTightIDDown",
]

MuMuEventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in MuonEventVariableBranches_names]),
)

###########################
# emu event variables
EMuEventVariableBranches_names = []
EMuEventVariableBranches_names.extend(ElectronEventVariableBranches_names)
EMuEventVariableBranches_names.extend(MuonEventVariableBranches_names)

EMuEventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in EMuEventVariableBranches_names]),
)



###########################
######### Leptons #########
###########################

LeptonBranches_names = [
    "p",
    "pt",
    "px",
    "py",
    "pz",
    "energy",
    "et",
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
            name = cms.string("smearedUpD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthUpSF+"*electron.d0SmearingVal)"), #unsmeared_d0 + UpSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedUpD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthUpSF+"*electron.d0SmearingVal)"),
        ),
        cms.PSet(
            name = cms.string("smearedDownD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthDownSF+"*electron.d0SmearingVal)"), #unsmeared_d0 + DownSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedDownD0Electron0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthDownSF+"*electron.d0SmearingVal)"),
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
            name = cms.string("smearedUpD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthUpSF+"*electron.d0SmearingVal)"), #unsmeared_d0 + UpSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedUpD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthUpSF+"*electron.d0SmearingVal)"),
        ),
        cms.PSet(
            name = cms.string("smearedDownD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthDownSF+"*electron.d0SmearingVal)"), #unsmeared_d0 + DownSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedDownD0Electron1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+electronD0WRTBeamspot+"+"+electronD0SmearingWidthDownSF+"*electron.d0SmearingVal)"),
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
            name = cms.string("smearedUpD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthUpSF+"*muon.d0SmearingVal)"), #unsmeared_d0 + UpSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedUpD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthUpSF+"*muon.d0SmearingVal)"),
        ),
        cms.PSet(
            name = cms.string("smearedDownD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthDownSF+"*muon.d0SmearingVal)"), #unsmeared_d0 + DownSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedDownD0Muon0"),
            index = cms.untracked.int32(0),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthDownSF+"*muon.d0SmearingVal)"),
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
            name = cms.string("smearedUpD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthUpSF+"*muon.d0SmearingVal)"), #unsmeared_d0 + UpSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedUpD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthUpSF+"*muon.d0SmearingVal)"),
        ),
        cms.PSet(
            name = cms.string("smearedDownD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthDownSF+"*muon.d0SmearingVal)"), #unsmeared_d0 + DownSF*d0_smearing_value
        ),
        cms.PSet(
            name = cms.string("absSmearedDownD0Muon1"),
            index = cms.untracked.int32(1),
            inputVariables = cms.vstring("10000*abs("+muonD0WRTBeamspot+"+"+muonD0SmearingWidthDownSF+"*muon.d0SmearingVal)"),
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

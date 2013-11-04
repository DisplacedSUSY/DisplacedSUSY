import FWCore.ParameterSet.Config as cms
import copy


#################################################################
############## STANDARD DISPLACED SUSY PRESELECTION #############
#################################################################

Preselection_MuMu = cms.PSet(
    name = cms.string("Preselection_MuMu"),
    triggers = cms.vstring("HLT_Mu17_Mu8_v"), # TRIGGER
    cuts = cms.VPSet (
      # EVENT CLEANING
      cms.PSet (
        inputCollection = cms.string("events"),
        cutString = cms.string("FilterOutScraping > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EVENT HAS GOOD PV
      cms.PSet (
        inputCollection = cms.string("primaryvertexs"),
        cutString = cms.string("isGood > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON ETA CUT
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON PT CUT
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON ID
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # MUON ISOLATION
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND NON-OVERLAPPING MUON
      cms.PSet (
        inputCollection = cms.string("muon-secondary muon pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND MUON ETA CUT
      cms.PSet (
        inputCollection = cms.string("secondary muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND MUON PT CUT
      cms.PSet (
        inputCollection = cms.string("secondary muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND MUON ID
      cms.PSet (
        inputCollection = cms.string("secondary muons"),
        cutString = cms.string("tightIDdisplaced > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND MUON ISOLATION
      cms.PSet (
        inputCollection = cms.string("secondary muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
      ),
      # OPPOSITE SIGN MU-MU PAIR
      cms.PSet (
        inputCollection = cms.string("muon-secondary muon pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EXTRA MUON VETO
      cms.PSet (
        inputCollection = cms.string("muon-secondary muon pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      # RESTRICT MUON TO RECONSTRUCTION ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      # RESTRICT SECOND MUON TO RECONSTRUCTION ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("secondary muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
   )
)

#################################################################
############ VARIATIONS ON THE STANDARD PRESELECTION ############
#################################################################

# PRESELECTION WITH SS LEPTONS

Preselection_MuMu_SS = cms.PSet(
        name = cms.string("Preselection_MuMu_SS"),
            triggers = copy.deepcopy(Preselection_MuMu.triggers),
            cuts = cms.VPSet ()
        )
Preselection_MuMu_SS.cuts.extend(copy.deepcopy(Preselection_MuMu.cuts))
for cut in Preselection_MuMu_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')

#################################################################

# PRESELECTION WITH PROMPT LEPTONS

Blinded_Preselection_MuMu = cms.PSet(
    name = cms.string("Blinded_Preselection_MuMu"),
    triggers = copy.deepcopy(Preselection_MuMu.triggers),
    cuts = cms.VPSet ()
)
Blinded_Preselection_MuMu.cuts.extend(copy.deepcopy(Preselection_MuMu.cuts))

muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection_MuMu.cuts.append(muon_d0_cut)

secondary_muon_d0_cut = cms.PSet (
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection_MuMu.cuts.append(secondary_muon_d0_cut)

#################################################################

# PRESELECTION WITH PROMPT SS LEPTONS

Blinded_Preselection_MuMu_SS = cms.PSet(
        name = cms.string("Blinded_Preselection_MuMu_SS"),
            triggers = copy.deepcopy(Preselection_MuMu.triggers),
            cuts = cms.VPSet ()
        )
Blinded_Preselection_MuMu_SS.cuts.extend(copy.deepcopy(Blinded_Preselection_MuMu.cuts))
for cut in Blinded_Preselection_MuMu_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')



import FWCore.ParameterSet.Config as cms
import copy


#################################################################
############## STANDARD DISPLACED SUSY PRESELECTION #############
#################################################################

Preselection_EE = cms.PSet(
    name = cms.string("Preselection_EE"),
    triggers = cms.vstring("HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"), # TRIGGER
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
      # ELECTRON ETA CUT
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      # ELECTRON CRACK VETO
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(eta) < 1.444 | abs(eta) > 1.566 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron ECAL crack veto")
      ),
      # ELECTRON PT CUT
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # ELECTRON ID
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("mvaNonTrig_HtoZZto4l > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # PHOTON CONVERSION VETO
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("passConvVeto > 0 & numberOfLostHits = 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("electron conversion rejection")
      ),
      # ELECTRON ISOLATION
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND NON-OVERLAPPING ELECTRON
      cms.PSet (
        inputCollection = cms.string("electron-secondary electron pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND ELECTRON ETA CUT
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND ELECTRON CRACK VETO
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("abs(eta) < 1.444 | abs(eta) > 1.566 "),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("secondary electron ECAL crack veto")
      ),
      # SECOND ELECTRON PT CUT
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
      ),
      # SECOND ELECTRON ID
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("mvaNonTrig_HtoZZto4l > 0"),
        numberRequired = cms.string(">= 1")
      ),
      # PHOTON CONVERSION VETO
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("passConvVeto > 0 & numberOfLostHits = 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("secondary electron conversion rejection")
      ),
      # SECOND ELECTRON ISOLATION
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string(">= 1")
      ),
      # OPPOSITE SIGN E-E PAIR
      cms.PSet (
        inputCollection = cms.string("electron-secondary electron pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string(">= 1")
      ),
      # EXTRA ELECTRON VETO
      cms.PSet (
        inputCollection = cms.string("electron-secondary electron pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      # RESTRICT ELECTRON TO RECONSTRUCTION ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      # RESTRICT SECOND ELECTRON TO RECONSTRUCTION ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("secondary electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
   )
)

#################################################################
############ VARIATIONS ON THE STANDARD PRESELECTION ############
#################################################################

# PRESELECTION WITH SS LEPTONS

Preselection_EE_SS = cms.PSet(
        name = cms.string("Preselection_EE_SS"),
            triggers = copy.deepcopy(Preselection_EE.triggers),
            cuts = cms.VPSet ()
        )
Preselection_EE_SS.cuts.extend(copy.deepcopy(Preselection_EE.cuts))
for cut in Preselection_EE_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')

#################################################################

# PRESELECTION WITH PROMPT LEPTONS

Blinded_Preselection_EE = cms.PSet(
    name = cms.string("Blinded_Preselection_EE"),
    triggers = copy.deepcopy(Preselection_EE.triggers),
    cuts = cms.VPSet ()
)
Blinded_Preselection_EE.cuts.extend(copy.deepcopy(Preselection_EE.cuts))

electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection_EE.cuts.append(electron_d0_cut)

secondary_electron_d0_cut = cms.PSet (
    inputCollection = cms.string("secondary_electrons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection_EE.cuts.append(secondary_electron_d0_cut)

#################################################################

# PRESELECTION WITH PROMPT SS LEPTONS

Blinded_Preselection_EE_SS = cms.PSet(
        name = cms.string("Blinded_Preselection_EE_SS"),
            triggers = copy.deepcopy(Preselection_EE.triggers),
            cuts = cms.VPSet ()
        )
Blinded_Preselection_EE_SS.cuts.extend(copy.deepcopy(Blinded_Preselection_EE.cuts))
for cut in Blinded_Preselection_EE_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')


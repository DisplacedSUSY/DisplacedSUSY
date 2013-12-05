import FWCore.ParameterSet.Config as cms
import copy

#################################################################
############ EMPTY SELECTION - TO LOOK AT ALL OBJECTS ###########
#################################################################


Empty_Selection = cms.PSet(
    name = cms.string("Empty_Selection"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
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
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 2")
      ),
   )
)



#################################################################
############## STANDARD DISPLACED SUSY PRESELECTION #############
#################################################################

Preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
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
        cutString = cms.string("isEBEEGap == 0"),
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
      # VETO EVENTS WITH EXTRA ELECTRON
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra electron veto")
      ),
      # VETO EVENTS WITH EXTRA MUON
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra muon veto")
      ),
      # OPPOSITE SIGN E-MU PAIR
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string("== 1")
      ),
      # ELECTRON AND MUON ARE NOT OVERLAPPING
      cms.PSet (
        inputCollection = cms.string("electron-muon pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string("== 1")
      ),

      #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET
      # ONLY CONSIDER 30 GEV JETS
      cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 30"),
        numberRequired = cms.string(">= 0")
      ),
      # ELECTRON NOT OVERLAPPING WITH JET
      cms.PSet (
        inputCollection = cms.string("electron-jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("electron near jet veto"),
      ),
      # MUON NOT OVERLAPPING WITH JET
      cms.PSet (
        inputCollection = cms.string("muon-jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto"),        
      ),
      ########### END OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET      

      # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
      # RESTRICT MUONS TO TRIGGER ACCEPTANCE
      cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(correctedD0) < 2"),
        numberRequired = cms.string("== 1")
      ),
##       cms.PSet (
##         inputCollection = cms.string("electrons"),
##         cutString = cms.string("abs(correctedDZ) < 2"),
##         numberRequired = cms.string("== 1")
##       ),
##       cms.PSet (
##         inputCollection = cms.string("muons"),
##         cutString = cms.string("abs(correctedDZ) < 2"),
##         numberRequired = cms.string("== 1")
##       ),

   )
)

#################################################################
############ VARIATIONS ON THE STANDARD PRESELECTION ############
#################################################################

# PRESELECTION WITH SS LEPTONS

Preselection_SS = cms.PSet(
        name = cms.string("Preselection_SS"),
            triggers = copy.deepcopy(Preselection.triggers),
            cuts = cms.VPSet ()
        )
Preselection_SS.cuts.extend(copy.deepcopy(Preselection.cuts))
for cut in Preselection_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')

#################################################################

# PRESELECTION WITH PROMPT LEPTONS

Blinded_Preselection = cms.PSet(
    name = cms.string("Blinded_Preselection"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Blinded_Preselection.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) < 0.01"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.01"),
    numberRequired = cms.string("== 1")
)
Blinded_Preselection.cuts.append(muon_d0_cut)

#################################################################

# PRESELECTION WITH PROMPT SS LEPTONS

Blinded_Preselection_SS = cms.PSet(
        name = cms.string("Blinded_Preselection_SS"),
            triggers = copy.deepcopy(Preselection.triggers),
            cuts = cms.VPSet ()
        )
Blinded_Preselection_SS.cuts.extend(copy.deepcopy(Blinded_Preselection.cuts))
for cut in Blinded_Preselection_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')

#################################################################
###### ADD GENERATOR-LEVEL MATCHING                       #######
###### USED TO SELECT SIGNAL EVENTS WITH E-MU FINAL STATE #######
#################################################################

from DisplacedSUSY.StandardAnalysis.SignalSelections import *

PreselectionWithGenMatching = cms.PSet(
    name = cms.string("PreselectionWithGenMatching"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
PreselectionWithGenMatching.cuts.extend(copy.deepcopy(SignalGenMatching.cuts))
PreselectionWithGenMatching.cuts.extend(copy.deepcopy(Preselection.cuts))

#################################################################

# PRESELECTION WITH 100 MICRON |D0| CUTS

Preselection_100um = cms.PSet(
    name = cms.string("Preselection_100um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_100um.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.01"),
    numberRequired = cms.string("== 1")
)
Preselection_100um.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.01"),
    numberRequired = cms.string("== 1")
)
Preselection_100um.cuts.append(muon_d0_cut)

#################################################################

# PRESELECTION WITH SS LEPTONS AND 100 MICRON |D0| CUTS

Preselection_SS_100um = cms.PSet(
        name = cms.string("Preselection_SS_100um"),
            triggers = copy.deepcopy(Preselection_100um.triggers),
            cuts = cms.VPSet ()
        )
Preselection_SS_100um.cuts.extend(copy.deepcopy(Preselection_100um.cuts))
for cut in Preselection_SS_100um.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')

#################################################################

# PRESELECTION WITH 50 MICRON |D0| CUTS

Preselection_50um = cms.PSet(
    name = cms.string("Preselection_50um"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Preselection_50um.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.005"),
    numberRequired = cms.string("== 1")
)
Preselection_50um.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.005"),
    numberRequired = cms.string("== 1")
)
Preselection_50um.cuts.append(muon_d0_cut)

#################################################################

# PRESELECTION WITH SS LEPTONS AND 50 MICRON |D0| CUTS

Preselection_SS_50um = cms.PSet(
        name = cms.string("Preselection_SS_50um"),
            triggers = copy.deepcopy(Preselection_50um.triggers),
            cuts = cms.VPSet ()
        )
Preselection_SS_50um.cuts.extend(copy.deepcopy(Preselection_50um.cuts))
for cut in Preselection_SS_50um.cuts:
    if "chargeProduct" in str(cut.cutString):
        cut.cutString = cms.string('chargeProduct > 0')


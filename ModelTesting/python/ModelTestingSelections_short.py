import FWCore.ParameterSet.Config as cms
import copy

#################################################################
############ EMPTY SELECTION - TO LOOK AT ALL OBJECTS ###########
#################################################################


### Get mc particles


##### Define few cuts that will be used multiple time


### d_0 cuts

### 200um
electron_d0_200um_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
    )

muon_d0_200um_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.02"),
    numberRequired = cms.string("== 1")
    )

### 500um
electron_d0_500um_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.05"),
    numberRequired = cms.string("== 1")
    )

muon_d0_500um_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.05"),
    numberRequired = cms.string("== 1")
    )


### 1000um
electron_d0_1000um_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.1"),
    numberRequired = cms.string("== 1")
    )

muon_d0_1000um_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.1"),
    numberRequired = cms.string("== 1")
    )

### Reconstruction cut
## One reco electron matched to signal

recoElectron_cut = cms.PSet (
    inputCollection = cms.string("electron-mcparticle pairs"),
    cutString = cms.string("deltaR < 0.05"),
    numberRequired = cms.string(">= 1")
    )

## One reco muon matched to signal

recoMuon_cut = cms.PSet (
    inputCollection = cms.string("muon-secondary mcparticle pairs"),
#    inputCollection = cms.string("muon-mcparticle pairs"),
    cutString = cms.string("deltaR < 0.05"),
    numberRequired = cms.string(">= 1")
    )

### Analysis cuts

## On Electron

# ELECTRON PT CUT
Electron_Pt_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )
# ELECTRON ID
Electron_Id_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("mvaNonTrig_HtoZZto4l > 0"),
    numberRequired = cms.string(">= 1")
    )
# ELECTRON ISOLATION
Electron_Isolation_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("relPFrhoIso < 0.1"),
    numberRequired = cms.string(">= 1")
    )
# ELECTRON CRACK VETO
Electron_crackVeto_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("isEBEEGap == 0"),
    numberRequired = cms.string(">= 1"),
    )
# PHOTON CONVERSION VETO
Electron_PhotonConversionVeto_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("passConvVeto > 0 & numberOfLostHits = 0"),
    numberRequired = cms.string(">= 1"),
    )

## On Muon

# MUON PT CUT
Muon_Pt_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1")
    )
# MUON ID
Muon_Id_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightIDdisplaced > 0"),
    numberRequired = cms.string(">= 1")
    )
# MUON ISOLATION
Muon_Isolation_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 1")
    )





### check reco efficiency

## electron initial
McPartInitial = cms.PSet(
    name = cms.string("McPartInitial"),
    cuts = cms.VPSet (
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 11"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE ETA CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE PT CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # VETO EVENTS WITH EXTRA MCPARTICLE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    ),
    ### MATCH SECONDARYMCPARTICLE TO MUON FOR CROSS CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 13"),
    numberRequired = cms.string(">= 0")
    ),
    # OPPOSITE SIGN MCPARTICLE-SECONDARYMCPARTICLE PAIR
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("chargeProduct < 0"),
    numberRequired = cms.string("== 1")
    ),
    # MCPARTCILE AND SECONDARYMCPARTICLE ARE NOT OVERLAPPING    
    cms.PSet (
    inputCollection = cms.string("secondary mcparticle-mcparticle pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string("== 1")
    ),
    #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET
    # ONLY CONSIDER 10 GEV GENJETS
    cms.PSet (
    inputCollection = cms.string("genjets"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 0")
    ),
    # MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),# hollow cone
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),    
    # RESTRICT MCPARTCILE TO RECONSTRUCTION ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("d0Beamspot < 2"),
    numberRequired = cms.string("== 1")
    ),
  )
)
## electron initial + reco
McPartInitial_OneRecoEl = cms.PSet(
    name = cms.string("McPartInitial_OneRecoEl"),
    cuts = cms.VPSet ()
    )
McPartInitial_OneRecoEl.cuts.extend(copy.deepcopy(McPartInitial.cuts))

McPartInitial_OneRecoEl.cuts.append(recoElectron_cut)


## electron initial + reco + selection

McPartInitial_OneRecoEl_Electron_cuts = cms.PSet(
    name = cms.string("McPartInitial_OneRecoEl_Electron_cuts"),
    cuts = cms.VPSet ()
    )
McPartInitial_OneRecoEl_Electron_cuts.cuts.extend(copy.deepcopy(McPartInitial_OneRecoEl.cuts))


McPartInitial_OneRecoEl_Electron_cuts.cuts.append(Electron_Pt_cut)
McPartInitial_OneRecoEl_Electron_cuts.cuts.append(Electron_Id_cut)
McPartInitial_OneRecoEl_Electron_cuts.cuts.append(Electron_Isolation_cut)
McPartInitial_OneRecoEl_Electron_cuts.cuts.append(Electron_crackVeto_cut)
McPartInitial_OneRecoEl_Electron_cuts.cuts.append(Electron_PhotonConversionVeto_cut)


## muon initial
SecondaryMcPartInitial = cms.PSet(
    name = cms.string("SecondaryMcPartInitial"),
    cuts = cms.VPSet (
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 13"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE ETA CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE PT CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # VETO EVENTS WITH EXTRA SECONDARYMCPARTICLE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    ),
    ### MATCH MCPARTICLE TO ELECTRON FOR CROSS CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 11"),
    numberRequired = cms.string(">= 0")
    ),
    # OPPOSITE SIGN MCPARTICLE-SECONDARYMCPARTICLE PAIR
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("chargeProduct < 0"),
    numberRequired = cms.string("== 1")
    ),
    # MCPARTCILE AND SECONDARYMCPARTICLE ARE NOT OVERLAPPING 
    cms.PSet (
    inputCollection = cms.string("secondary mcparticle-mcparticle pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string("== 1")
    ),
    #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET
    # ONLY CONSIDER 10 GEV GENJETS
    cms.PSet (
    inputCollection = cms.string("genjets"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 0")
    ),
    # SECONDARY MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("secondary mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),#0.5
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),
    # RESTRICT SECONDARY MCPARTICLES TO TRIGGER ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("d0Beamspot < 2"),
    numberRequired = cms.string("== 1")
    ),
  )
)
## muon initial + reco
SecondaryMcPartInitial_OneRecoMu = cms.PSet(
    name = cms.string("SecondaryMcPartInitial_OneRecoMu"),
    cuts = cms.VPSet ()
    )
SecondaryMcPartInitial_OneRecoMu.cuts.extend(copy.deepcopy(SecondaryMcPartInitial.cuts))

SecondaryMcPartInitial_OneRecoMu.cuts.append(recoMuon_cut)

## muon initial + reco + selected

SecondaryMcPartInitial_OneRecoMu_Muon_cuts = cms.PSet(
            name = cms.string("SecondaryMcPartInitial_OneRecoMu_Muon_cuts"),
                    cuts = cms.VPSet ()
                    )
SecondaryMcPartInitial_OneRecoMu_Muon_cuts.cuts.extend(copy.deepcopy(SecondaryMcPartInitial_OneRecoMu.cuts))

SecondaryMcPartInitial_OneRecoMu_Muon_cuts.cuts.append(Muon_Pt_cut)
SecondaryMcPartInitial_OneRecoMu_Muon_cuts.cuts.append(Muon_Id_cut)
SecondaryMcPartInitial_OneRecoMu_Muon_cuts.cuts.append(Muon_Isolation_cut)




### Channel with Cut applied on mcparticle and secondary mcparticle




### keep clean
Preselection_GenLevel = cms.PSet(
    name = cms.string("Preselection_GenLevel"),
    #    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
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
    # MCPARTICLE MATCHED TO SIGNAL
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 11"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE ETA CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE PT CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE MATCHED TO SIGNAL
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 13"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE ETA CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTCILE PT CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # VETO EVENTS WITH EXTRA MCPARTICLE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("extra mcparticle veto")
    ),
    # VETO EVENTS WITH EXTRA SECONDARY MCPARTICLE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("extra secondary mcparticle veto")
    ),
    # OPPOSITE SIGN SECONDARY MCPARTICLE MCPARTICLE PAIR
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("chargeProduct < 0"), # faco
    numberRequired = cms.string("== 1")
    ),
    # MCPARTICLE AND SECONDARY MCPARTICLE ARE NOT OVERLAPPING
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string("== 1")
    ),
    #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET
    # ONLY CONSIDER 30 GEV GENJETS
    cms.PSet (
    inputCollection = cms.string("genjets"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 0")
    ),
    # MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),
    # SECONDARY MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("secondary mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),
    ########### END OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET      
    
    # RESTRICT MCPARTICLES TO RECONSTRUCTION ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(d0Beamspot) < 2"),
    numberRequired = cms.string("== 1")
    ),
    # RESTRICT SECONDARY MCPARTICLES TO TRIGGER ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(d0Beamspot) < 2"),
    numberRequired = cms.string("== 1")
    ),
  )
)






### play with
Preselection_GenLevel_test = cms.PSet(
    name = cms.string("Preselection_GenLevel"),
    #    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
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
    # MCPARTICLE MATCHED TO SIGNAL
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 11"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE ETA CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTCILE PT CUT
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE MATCHED TO SIGNAL
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 & abs(id) = 13"),# 13!!!
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTICLE ETA CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 1")
    ),
    # SECONDARY MCPARTCILE PT CUT
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1")
    ),
    # VETO EVENTS WITH EXTRA MCPARTICLE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("extra mcparticle veto")
    ),
    # VETO EVENTS WITH EXTRA SECONDARY MCPARTICLE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("extra secondary mcparticle veto")
    ),    
    # OPPOSITE SIGN SECONDARY MCPARTICLE MCPARTICLE PAIR
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("chargeProduct < 0"), # faco
    numberRequired = cms.string(">= 1")
    ),
    # MCPARTICLE AND SECONDARY MCPARTICLE ARE NOT OVERLAPPING
    cms.PSet (
    inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string(">= 1")
    ),
    #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET
    # ONLY CONSIDER 30 GEV GENJETS
    cms.PSet (
    inputCollection = cms.string("genjets"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 0")
    ),
    # MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),
    # SECONDARY MCPARTICLE NOT OVERLAPPING WITH GENJET
    cms.PSet (
    inputCollection = cms.string("secondary mcparticle-genjet pairs"),
    cutString = cms.string("deltaR > 0.05 & deltaR < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    ),
    ########### END OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A GENJET      
    # RESTRICT MCPARTICLES TO RECONSTRUCTION ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(d0Beamspot) < 2"),
    numberRequired = cms.string(">= 1")
    ),
    # RESTRICT SECONDARY MCPARTICLES TO TRIGGER ACCEPTANCE
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(d0Beamspot) < 2"),
    numberRequired = cms.string(">= 1")
    ),
  )
)

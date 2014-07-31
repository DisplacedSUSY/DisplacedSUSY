import FWCore.ParameterSet.Config as cms
import copy

#################################################################
############ EMPTY SELECTION - TO LOOK AT ALL OBJECTS ###########
#################################################################



### Define the two channel to compare, one with GenToReco = True the other with GenToReco = False


### Channel to weight (use GenToReco = True)
### On gen quantity only and wihtout the analysis cut on lepton
SignalGenMatching_KynCuts_CrossCuts = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts"),
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
        #ELECTRON CUTS
        #Exactly  one electron
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
        numberRequired = cms.string("== 1")
        ),
        # ELECTRON ETA CUT
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
        # ELECTRON PT CUT
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("pt > 10"),
        numberRequired = cms.string(">= 1")
        ),
        # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),
        ### MUON CUTS
        #Exactly one muon
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
        numberRequired = cms.string("== 1")
        ),
        # MUON ETA CUT
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
        # MUON PT CUT
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("pt > 10"),
        numberRequired = cms.string(">= 1")
        ),
        # RESTRICT MUONS TO TRIGGER ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),
        ### CUT ON TWO OBJECTS
        # VETO EVENTS WITH EXTRA ELECTRON
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra mcparticle veto")
        ),
        # VETO EVENTS WITH EXTRA MUON
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("== 1"),
        alias = cms.string("extra secondary mcparticle veto")
        ),
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
        inputCollection = cms.string("mcparticle-secondary mcparticle pairs"), # what input collection?
        cutString = cms.string("chargeProduct < 0"),
        numberRequired = cms.string("== 1")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
        inputCollection = cms.string("mcparticle-secondary mcparticle pairs"),
        cutString = cms.string("deltaR > 0.5"),
        numberRequired = cms.string("== 1")
        ),
        #########START OF ADDITIONAL CUTS TO REQUIRE LEPTON IS NOT IN A JET
        # ONLY CONSIDER 30 GEV JETS
        cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 10"),
        numberRequired = cms.string(">= 0")
        ),
        # ELECTRON NOT OVERLAPPING WITH JET
        cms.PSet (
        inputCollection = cms.string("mcparticle-jet pairs"),## not sure here
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("mcparticle near jet veto"),
        ),
        # MUON NOT OVERLAPPING WITH JET
        cms.PSet (
        inputCollection = cms.string("secondary mcparticle-jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("secondary mcparticle near jet veto"),
        ),
    )
)






SignalGenMatching_KynCuts_CrossCuts_FullPreselection_NoTrigger = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts_FullPreselection_NoTrigger"),
        #        triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER  
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
        #ELECTRON CUTS
        #Exactly  one electron
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
        numberRequired = cms.string("== 1")
        ),
        # ELECTRON ETA CUT
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
        # ELECTRON PT CUT
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("pt > 10"),
        numberRequired = cms.string(">= 1")
        ),
        # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),
        ### MUON CUTS
        #Exactly one muon
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
        numberRequired = cms.string("== 1")
        ),
        # MUON ETA CUT
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
        # MUON PT CUT
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("pt > 10"),
        numberRequired = cms.string(">= 1")
        ),
        # RESTRICT MUONS TO TRIGGER ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),

        ### NOW all the cut in the Preselection as they are in the analysis
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
        cutString = cms.string("pt > 10"),
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
    )
)


SignalGenMatching_KynCuts_CrossCuts_FullPreselection = cms.PSet(
    name = cms.string("SignalGenMatching_KynCuts_CrossCuts_FullPreselection"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
    cuts = cms.VPSet ()
    )
SignalGenMatching_KynCuts_CrossCuts_FullPreselection.cuts.extend(copy.deepcopy(SignalGenMatching_KynCuts_CrossCuts_FullPreselection_NoTrigger.cuts))


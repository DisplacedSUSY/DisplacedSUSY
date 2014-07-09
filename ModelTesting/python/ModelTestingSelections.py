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
    alias = cms.string("electron ECAL crack veto")
    )
# PHOTON CONVERSION VETO
Electron_PhotonConversionVeto_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("passConvVeto > 0 & numberOfLostHits = 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("electron conversion rejection")
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




### Now we define the required channels



#### Signal Gen matching selection and variant


# channel 1
SignalGenMatching_KynCuts_CrossCuts = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts"),
        cuts = cms.VPSet (
    ### just added to allow acces of d0Beamspot in the reweighing
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
     ### eof just added

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
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
        inputCollection = cms.string("mcparticle-secondary mcparticle pairs"), # what input collection?
        cutString = cms.string("chargeProduct < 0"),
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
        alias = cms.string("electron near jet veto"),
        ),
        # MUON NOT OVERLAPPING WITH JET
        cms.PSet (
        inputCollection = cms.string("secondary mcparticle-jet pairs"),
        cutString = cms.string("deltaR < 0.5"),
        numberRequired = cms.string("== 0"),
        isVeto = cms.bool(True),
        alias = cms.string("muon near jet veto"),
        ),
        
    )
)






## channel 2a
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts_oneRecoEl"),
        cuts = cms.VPSet ()
        )
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl.cuts.extend(copy.deepcopy(SignalGenMatching_KynCuts_CrossCuts.cuts))
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl.cuts.append(recoElectron_cut)

## channel 2b 
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts_oneRecoMu"),
        cuts = cms.VPSet ()
        )
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu.cuts.extend(copy.deepcopy(SignalGenMatching_KynCuts_CrossCuts.cuts))
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu.cuts.append(recoMuon_cut)

## channel 3a 
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts"),
        cuts = cms.VPSet ()
        )
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.extend(copy.deepcopy(SignalGenMatching_KynCuts_CrossCuts_oneRecoEl.cuts))


SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.append(Electron_Pt_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.append(Electron_Id_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.append(Electron_Isolation_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.append(Electron_crackVeto_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoEl_Electron_cuts.cuts.append(Electron_PhotonConversionVeto_cut)

## channel 3b 
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts = cms.PSet(
        name = cms.string("SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts"),
        cuts = cms.VPSet ()
        )
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts.cuts.extend(copy.deepcopy(SignalGenMatching_KynCuts_CrossCuts_oneRecoMu.cuts))

SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts.cuts.append(Muon_Pt_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts.cuts.append(Muon_Id_cut)
SignalGenMatching_KynCuts_CrossCuts_oneRecoMu_Muon_cuts.cuts.append(Muon_Isolation_cut)



### channel 4 Preselection Signal matching no trigger

Preselection_SignalGenMatching_NoTrigger = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_NoTrigger"),
    cuts = cms.VPSet (
    #at least one electron
    cms.PSet (
    inputCollection = cms.string("mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
    numberRequired = cms.string("== 1")
    ),
    #at least one muon
    cms.PSet (
    inputCollection = cms.string("secondary mcparticles"),
    cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
    numberRequired = cms.string("== 1")
    ),
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
    )
)

### define the trigger efficiency


Preselection_SignalGenMatching = cms.PSet(
      name = cms.string("Preselection_SignalGenMatching"),
      triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER
      cuts = cms.VPSet ()
      )

Preselection_SignalGenMatching.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching_NoTrigger.cuts))




#### Define the 6 channels for the d_0 efficiency (2 leptons x 3 signal region)



#### 1st Signal region  
Preselection_SignalGenMatching_200umElectron = cms.PSet(
            name = cms.string("Preselection_SignalGenMatching_200umElectron"),
            cuts = cms.VPSet ()
            )

Preselection_SignalGenMatching_200umElectron.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_200umElectron.cuts.append(electron_d0_200um_cut)



Preselection_SignalGenMatching_200umMuon = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_200umMuon"),
    triggers = cms.vstring("HLT_Mu22_Photon22_CaloIdL_v"), # TRIGGER 
    cuts = cms.VPSet ()
    )

Preselection_SignalGenMatching_200umMuon.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_200umMuon.cuts.append(muon_d0_200um_cut)




#### 2 nd Signal region

Preselection_SignalGenMatching_500umElectron = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_500umElectron"),
    cuts = cms.VPSet ()
    )

Preselection_SignalGenMatching_500umElectron.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_500umElectron.cuts.append(electron_d0_500um_cut)



Preselection_SignalGenMatching_500umMuon = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_500umMuon"),
    cuts = cms.VPSet ()
    )

Preselection_SignalGenMatching_500umMuon.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_500umMuon.cuts.append(muon_d0_500um_cut)


#### 3 rd Signal region

Preselection_SignalGenMatching_1000umElectron = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_1000umElectron"),
    cuts = cms.VPSet ()
    )

Preselection_SignalGenMatching_1000umElectron.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_1000umElectron.cuts.append(electron_d0_1000um_cut)



Preselection_SignalGenMatching_1000umMuon = cms.PSet(
    name = cms.string("Preselection_SignalGenMatching_1000umMuon"),
    cuts = cms.VPSet ()
    )

Preselection_SignalGenMatching_1000umMuon.cuts.extend(copy.deepcopy(Preselection_SignalGenMatching.cuts))

Preselection_SignalGenMatching_1000umMuon.cuts.append(muon_d0_1000um_cut)







SignalGenMatching = cms.PSet(
        name = cms.string("SignalGenMatching"),
        cuts = cms.VPSet (
        #at least one electron
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 11"),
        numberRequired = cms.string("== 1")
        ),
        # RESTRICT ELECTRONS TO RECONSTRUCTION ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),
        #at least one muon
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("abs(genMatchedPdgGrandmotherId) = 1000006 | abs(genMatchedPdgGrandmotherId) = 24 & abs(id) = 13"),
        numberRequired = cms.string("== 1")
        ),
        # RESTRICT MUONS TO TRIGGER ACCEPTANCE
        cms.PSet (
        inputCollection = cms.string("secondary mcparticles"),
        cutString = cms.string("d0Beamspot < 2"),
        numberRequired = cms.string("== 1")
        ),
    )
)

import FWCore.ParameterSet.Config as cms
import copy





###########################################################
##### Set up the event selections (channels) #####
##########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters


# this trigger is disabled for a while (Juliette advice)
# ,"HLT_L2Mu20_eta2p1_NoVertex_v"



# define some interesting cut

OnZPeakCut  = cms.PSet(
    cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass < 106.2 && invMass > 76.2"),
    numberRequired = cms.string(">= 1")
    ),
    )



CosmicTightCut = cms.PSet (
    cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass > 106.2 | invMass < 76.2 && log(alpha) < -2.6 "),
    numberRequired = cms.string(">= 1")
    ),
    )


OffZPeakCut  = cms.PSet(
    cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass > 106.2 | invMass < 76.2"),
    numberRequired = cms.string(">= 1")
    ),
    )

# main channel

LooseCosmic_No_TightId = cms.PSet(
    name = cms.string("LooseCosmic_No_TightId"),
    triggers = cms.vstring("HLT_IsoMu24_v"),# check trigger!! not applied in the skim
    cuts = cms.VPSet (
    cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1")
    ),
    cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1")
    ),
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(eta) < 2.5"),
    numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 2")
    ),
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("extra muon veto")
    ),
    cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("chargeProduct < 0"),
    numberRequired = cms.string("== 1")
    ),
    cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("log(alpha) < -1 "),
    numberRequired = cms.string(">= 1")
    ),
    )
    )



# define sub channels

CosmicTight = cms.PSet(
    name = cms.string("CosmicTight"),
    triggers = copy.deepcopy(LooseCosmic_No_TightId.triggers),
    cuts = cms.VPSet ()
    )
CosmicTight.cuts.extend(copy.deepcopy(LooseCosmic_No_TightId.cuts))
CosmicTight.cuts.append(CosmicTightCut)


OffZPeak = cms.PSet(
    name = cms.string("OffZPeak"),
    triggers = copy.deepcopy(LooseCosmic_No_TightId.triggers),
    cuts = cms.VPSet ()
    )
OffZPeak.cuts.extend(copy.deepcopy(LooseCosmic_No_TightId.cuts))
OffZPeak.cuts.append(OffZPeakCut)


OnZPeak = cms.PSet(
    name = cms.string("OnZPeak"),
    triggers = copy.deepcopy(LooseCosmic_No_TightId.triggers),
    cuts = cms.VPSet ()
    )
OnZPeak.cuts.extend(copy.deepcopy(LooseCosmic_No_TightId.cuts))
OnZPeak.cuts.append(OnZPeakCut)





# for Id efficiency


One_TightIdCut = cms.VPSet(
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightIDdisplaced > 0"),
    numberRequired = cms.string("= 1")
    )
)



One_or_Plus_TightIdCut = cms.VPSet(
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightIDdisplaced > 0"),
    numberRequired = cms.string(">= 1")
    )
)



Two_TightIdCut = cms.VPSet(
    cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightIDdisplaced > 0"),
    numberRequired = cms.string("= 2")
    )
)






Cosmic_Two_TightId=copy.deepcopy(LooseCosmic_No_TightId)
Cosmic_Two_TightId.name="Cosmic_Two_TightId" # FAC full analysis cut
Cosmic_Two_TightId.cuts.extend(copy.deepcopy(Two_TightIdCut))



Cosmic_One_or_Plus_TightId=copy.deepcopy(LooseCosmic_No_TightId)
Cosmic_One_or_Plus_TightId.name="Cosmic_One_or_Plus_TightId" # FAC full analysis cut
Cosmic_One_or_Plus_TightId.cuts.extend(copy.deepcopy(One_or_Plus_TightIdCut))



Cosmic_One_TightId=copy.deepcopy(LooseCosmic_No_TightId)
Cosmic_One_TightId.name="Cosmic_OneTightId" # FAC full analysis cut
Cosmic_One_TightId.cuts.extend(copy.deepcopy(One_TightIdCut))

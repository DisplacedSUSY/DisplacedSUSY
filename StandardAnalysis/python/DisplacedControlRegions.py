import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters

from DisplacedSUSY.StandardAnalysis.Preselection import * 

#################################################################

# PRESELECTION WITH LEPTON 100um < d0 < 200um

# Region B of ABCD

Displaced_Control_Region = cms.PSet(
    name = cms.string("Displaced_Control_Region"),
    triggers = copy.deepcopy(Preselection.triggers),
    cuts = cms.VPSet ()
)
Displaced_Control_Region.cuts.extend(copy.deepcopy(Preselection.cuts))

electron_d0_cut = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("abs(correctedD0) > 0.01"),
    numberRequired = cms.string("== 1")
)
Displaced_Control_Region.cuts.append(electron_d0_cut)

muon_d0_cut = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) > 0.01"),    
    numberRequired = cms.string("== 1")
)
Displaced_Control_Region.cuts.append(muon_d0_cut)


# Region A of ABCD

Displaced_Control_Region_SS = cms.PSet(
    name = cms.string("Displaced_Control_Region_SS"),
    triggers = copy.deepcopy(Displaced_Control_Region.triggers),
    cuts = cms.VPSet ()
)
Displaced_Control_Region_SS.cuts.extend(copy.deepcopy(Displaced_Control_Region.cuts))
for cut in Displaced_Control_Region_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
                cut.cutString = cms.string('chargeProduct > 0')





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


# Region A of ABCD

Preselection_100um_SS = cms.PSet(
            name = cms.string("Preselection_100um_SS"),
                        triggers = copy.deepcopy(Preselection_100um.triggers),
                        cuts = cms.VPSet ()
                    )
Preselection_100um_SS.cuts.extend(copy.deepcopy(Preselection_100um.cuts))
for cut in Preselection_100um_SS.cuts:
    if "chargeProduct" in str(cut.cutString):
                cut.cutString = cms.string('chargeProduct > 0')


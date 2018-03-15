import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.MuMuChannel.CutDefinitions import *

#Selections without triggers

Denominator = cms.PSet(
    name = cms.string("Denominator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)

diMuon_deltaR_cut.cutString = cms.string("deltaR(muon,muon) > 0.1")

diMuon_invMass_Z_cut.cutString = cms.string("abs(invMass(muon,muon) - 91.2) < 20")
diMuon_invMass_Z_cut.alias = cms.string("abs(mass_mumu - mass_Z) < 20")

Denominator.cuts.append(muon_eta_cut)
Denominator.cuts.append(muon_pt_25_cut)
Denominator.cuts.append(muon_iso_cut)
Denominator.cuts.append(muon_2muon_cut)
Denominator.cuts.append(diMuon_deltaR_cut)
Denominator.cuts.append(diMuon_opposite_charge_cut)
Denominator.cuts.append(diMuon_invMass_Z_cut)

Numerator = cms.PSet(
    name = cms.string("Numerator"),
    triggers = cms.vstring(),
    cuts = cms.VPSet(copy.deepcopy(Denominator.cuts))
)

muon_global_cut.cutString = cms.string("isGlobalMuon")

Numerator.cuts.append(muon_global_cut)

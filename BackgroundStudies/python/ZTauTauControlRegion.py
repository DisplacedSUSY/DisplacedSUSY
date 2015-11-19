import FWCore.ParameterSet.Config as cms
import copy

from DisplacedSUSY.StandardAnalysis.CutDefinitions import *

ztautau_control_region_cuts = cms.VPSet(
        # ELECTRON MT CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons","mets"),
            cutString = cms.string("sqrt(2*electron.pt*met.pt*(1 - cos(deltaPhi(electron, met)))) < 50"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("electron m_{T} < 50 GeV")
        ),
        # MUON MT CUT
        cms.PSet (
            inputCollection = cms.vstring("muons","mets"),
            cutString = cms.string("sqrt(2*muon.pt*met.pt*(1 - cos(deltaPhi(muon, met)))) < 50"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("muon m_{T} < 50 GeV")
        ),
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("oppositely charged e-mu pair")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaPhi(electron, muon) > 2.5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
        ),
        # Electron MUON INVARIANT MASS
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("invMass(electron,muon) < 100"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("invariant mass < 100GeV")
        ),
        #Extra Lepton Veto
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra muon veto")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra electron veto")
        ),
)

ZTauTauControlRegion = cms.PSet(
    name = cms.string("ZTauTautoEMu"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"),
    cuts = cms.VPSet ()
)

ZTauTauControlRegion.cuts.extend(electron_basic_selection_cuts)
ZTauTauControlRegion.cuts.append(electron_iso_cut)
ZTauTauControlRegion.cuts.extend(muon_basic_selection_cuts)
ZTauTauControlRegion.cuts.append(muon_iso_cut)
ZTauTauControlRegion.cuts.extend(ztautau_control_region_cuts)


ztautau_preselection_cuts = cms.VPSet(
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("oppositely charged e-mu pair")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaPhi(electron, muon) > 2.5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
        ),
        #Extra Lepton Veto
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra muon veto")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra electron veto")
        ),
)

ZTauTauPreselection = cms.PSet(
    name = cms.string("ZTauTautoEMuPreselection"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"),
    cuts = cms.VPSet ()
)
                                                                       
ZTauTauPreselection.cuts.extend(electron_basic_selection_cuts)
ZTauTauPreselection.cuts.append(electron_iso_cut)
ZTauTauPreselection.cuts.extend(muon_basic_selection_cuts)
ZTauTauPreselection.cuts.append(muon_iso_cut)
ZTauTauPreselection.cuts.extend(ztautau_preselection_cuts)


ZTauTauControlRegion = cms.PSet(
    name = cms.string("ZTauTautoEMu"),
    triggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"),
    cuts = cms.VPSet ()
)

ZTauTauControlRegion.cuts.extend(electron_basic_selection_cuts)
ZTauTauControlRegion.cuts.append(electron_iso_cut)
ZTauTauControlRegion.cuts.extend(muon_basic_selection_cuts)
ZTauTauControlRegion.cuts.append(muon_iso_cut)
ZTauTauControlRegion.cuts.extend(ztautau_control_region_cuts)


ztautau_preselection_cuts = cms.VPSet(
        # OPPOSITE SIGN E-MU PAIR
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("electron.charge * muon.charge < 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("oppositely charged e-mu pair")
        ),
        # ELECTRON AND MUON ARE NOT OVERLAPPING
        cms.PSet (
            inputCollection = cms.vstring("electrons", "muons"),
            cutString = cms.string("deltaPhi(electron, muon) > 2.5"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("well separated(DeltaR > 0.5) e-mu pair")
        ),
        #Extra Lepton Veto
        cms.PSet (
            inputCollection = cms.vstring("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra muon veto")
        ),
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("== 1"),
            alias = cms.string("extra electron veto")
        ),
)

ZTauTauLowPtControlRegion = cms.PSet(
    name = cms.string("ZTauTauLowPtControlRegion"),
    triggers = cms.vstring("HLT_Mu23NoFiltersNoVtx_Photon23_CaloIdL_v"),
    cuts = cms.VPSet ()
)
                                                                       
ZTauTauLowPtControlRegion.cuts.extend(electron_basic_selection_cuts)
ZTauTauLowPtControlRegion.cuts.append(electron_iso_cut)
ZTauTauLowPtControlRegion.cuts.extend(muon_basic_selection_cuts)
ZTauTauLowPtControlRegion.cuts.append(muon_iso_cut)
ZTauTauLowPtControlRegion.cuts.extend(ztautau_control_region_cuts)

import FWCore.ParameterSet.Config as cms
import copy
import string

import DisplacedSUSY.Configuration.objectDefinitions as objectDefs

##########################################################################
### Set up various LLP (Z->ll)H -> aa -> bbbb control regions
##########################################################################

# analagous EE and MuMu selections

# minimal "Baseline" (standard triggers + good leptons + > 0 jets)
# off Z (minimal + !Z mass)
# on Z (minimal + Z mass)
# on Z low Pt (minimal + Z mass + !Z pt)
# on Z high Pt (minimal + Z mass + Z pt)


# cut definitions

##########################################################################

eetrigger = cms.vstring()
mumutrigger = cms.vstring()

##########################################################################


##########################################################################
# Jet selections

jet_eta_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 1")
    )

jet_pt_20_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1")
    )

jet_id_cut = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = objectDefs.jet_id_cutstring,
    numberRequired = cms.string(">= 1"),
    alias = objectDefs.jet_id_alias
    )

##########################################################################
# Electron cuts

electron_eta_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

electron_gap_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("isEBEEGap = 0"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("electron ECAL crack veto")
    )

# electrons are already cut at 40 in the skim...
electron_pt_40_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 2")
    )

electron_id_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_id_alias
    )

electron_iso_cut = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = objectDefs.electron_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.electron_iso_alias
    )

electron_extra_veto = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2")
    )



##########################################################################
# Di-electron (Z candidate) cuts

dielectron_os_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("electron.charge * electron.charge < 0"),
    numberRequired = cms.string(">= 1")
    )

dielectron_deltaR_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("deltaR(electron,electron) > 0.1"),
    numberRequired = cms.string(">= 1")
    )

dielectron_offZ_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("abs(90 - invMass(electron,electron)) > 20"),
    numberRequired = cms.string(">= 1")
    )

dielectron_onZ_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("abs(90 - invMass(electron,electron)) < 20"),
    numberRequired = cms.string(">= 1")
    )

dielectron_lowPt_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("pT(electron, electron) < 50"),
    numberRequired = cms.string(">= 1")
    )

dielectron_highPt_cut = cms.PSet(
    inputCollection = cms.vstring("electrons","electrons"),
    cutString = cms.string("pT(electron, electron) > 50"),
    numberRequired = cms.string(">= 1")
    )

##########################################################################
# Muon cuts

muon_eta_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("abs(eta) < 2.4"),
    numberRequired = cms.string(">= 2")
    )

# muons already cut at 28 in the skim...
muon_pt_28_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 28"),
    numberRequired = cms.string(">= 2")
    )

muon_global_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_global_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_global_alias
    )

muon_id_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_id_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_id_alias
    )

muon_iso_cut = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = objectDefs.muon_iso_cutstring,
    numberRequired = cms.string(">= 2"),
    alias = objectDefs.muon_iso_alias
    )

muon_extra_veto = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 2")
    )


##########################################################################
# Di-muon (Z candidate) cuts

dimuon_os_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("muon.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1")
    )

dimuon_deltaR_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("deltaR(muon,muon) > 0.1"),
    numberRequired = cms.string(">= 1")
    )

dimuon_offZ_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("abs(90 - invMass(muon,muon)) > 20"),
    numberRequired = cms.string(">= 1")
    )

dimuon_onZ_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("abs(90 - invMass(muon,muon)) < 20"),
    numberRequired = cms.string(">= 1")
    )

dimuon_lowPt_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("pT(muon, muon) < 50"),
    numberRequired = cms.string(">= 1")
    )

dimuon_highPt_cut = cms.PSet(
    inputCollection = cms.vstring("muons","muons"),
    cutString = cms.string("pT(muon, muon) > 50"),
    numberRequired = cms.string(">= 1")
    )

##########################################################################
# lepton-jet cuts

electronjet_deltaR_veto = cms.PSet(
    inputCollection = cms.vstring("electrons","jets"),
    cutString = cms.string("deltaR(electron, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )

muonjet_deltaR_veto = cms.PSet(
    inputCollection = cms.vstring("muons","jets"),
    cutString = cms.string("deltaR(muon, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True)
    )




##########################################################################
##########################################################################
##########################################################################
##########################################################################

#Begin Channel definitions

##########################################################################
# EE Channels

EEBaseline = cms.PSet(
    name = cms.string("EEBaseline"),
    triggers = eetrigger,
    cuts = cms.VPSet()
)
### >= 1 good 20 GeV jet
EEBaseline.cuts.append(jet_eta_cut)
EEBaseline.cuts.append(jet_pt_20_cut)
EEBaseline.cuts.append(jet_id_cut)
### == 2 good electrons
EEBaseline.cuts.append(electron_eta_cut)
EEBaseline.cuts.append(electron_gap_veto)
EEBaseline.cuts.append(electron_pt_40_cut)
EEBaseline.cuts.append(electron_id_cut)
EEBaseline.cuts.append(electron_iso_cut)
EEBaseline.cuts.append(electron_extra_veto)
### leptons not near jets
EEBaseline.cuts.append(electronjet_deltaR_veto)
### good Z candidate
EEBaseline.cuts.append(dielectron_os_cut)
EEBaseline.cuts.append(dielectron_deltaR_cut)


EEOffZ = cms.PSet(
    name = cms.string("EEOffZ"),
    triggers = eetrigger,
    cuts = copy.deepcopy(EEBaseline.cuts)
)
EEOffZ.cuts.append(dielectron_offZ_cut)

EEOnZ = cms.PSet(
    name = cms.string("EEOnZ"),
    triggers = eetrigger,
    cuts = copy.deepcopy(EEBaseline.cuts)
)
EEOnZ.cuts.append(dielectron_onZ_cut)

EEOnZLowPt = cms.PSet(
    name = cms.string("EEOnZLowPt"),
    triggers = eetrigger,
    cuts = copy.deepcopy(EEOnZ.cuts)
)
EEOnZLowPt.cuts.append(dielectron_lowPt_cut)

EEOnZHighPt = cms.PSet(
    name = cms.string("EEOnZHighPt"),
    triggers = eetrigger,
    cuts = copy.deepcopy(EEOnZ.cuts)
)
EEOnZHighPt.cuts.append(dielectron_highPt_cut)



##########################################################################
# MuMu Channels

MuMuBaseline = cms.PSet(
    name = cms.string("MuMuBaseline"),
    triggers = eetrigger,
    cuts = cms.VPSet()
)
### >= 1 good 20 GeV jet
MuMuBaseline.cuts.append(jet_eta_cut)
MuMuBaseline.cuts.append(jet_pt_20_cut)
MuMuBaseline.cuts.append(jet_id_cut)
### == 2 good muons
MuMuBaseline.cuts.append(muon_eta_cut)
MuMuBaseline.cuts.append(muon_pt_28_cut)
MuMuBaseline.cuts.append(muon_global_cut)
MuMuBaseline.cuts.append(muon_id_cut)
MuMuBaseline.cuts.append(muon_iso_cut)
MuMuBaseline.cuts.append(muon_extra_veto)
### leptons not near jets
MuMuBaseline.cuts.append(muonjet_deltaR_veto)
### good Z candidate
MuMuBaseline.cuts.append(dimuon_os_cut)
MuMuBaseline.cuts.append(dimuon_deltaR_cut)


MuMuOffZ = cms.PSet(
    name = cms.string("MuMuOffZ"),
    triggers = eetrigger,
    cuts = copy.deepcopy(MuMuBaseline.cuts)
)
MuMuOffZ.cuts.append(dimuon_offZ_cut)

MuMuOnZ = cms.PSet(
    name = cms.string("MuMuOnZ"),
    triggers = eetrigger,
    cuts = copy.deepcopy(MuMuBaseline.cuts)
)
MuMuOnZ.cuts.append(dimuon_onZ_cut)

MuMuOnZLowPt = cms.PSet(
    name = cms.string("MuMuOnZLowPt"),
    triggers = eetrigger,
    cuts = copy.deepcopy(MuMuOnZ.cuts)
)
MuMuOnZLowPt.cuts.append(dimuon_lowPt_cut)

MuMuOnZHighPt = cms.PSet(
    name = cms.string("MuMuOnZHighPt"),
    triggers = eetrigger,
    cuts = copy.deepcopy(MuMuOnZ.cuts)
)
MuMuOnZHighPt.cuts.append(dimuon_highPt_cut)


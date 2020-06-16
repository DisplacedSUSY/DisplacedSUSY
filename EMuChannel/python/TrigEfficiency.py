import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.StandardAnalysis.Triggers import *


##########################################################################
### Set up the TTbar regions for trigger efficiency plots
##########################################################################

# Opposite sign e-mu pair with >=2 jets and >= 1 b jet
# Designed to mimic the selection Bing used for trigger efficiency

##########################################################################

# Denominator: ttbar+(MET trigger)
TrigEffDen = cms.PSet(
    name = cms.string("TrigEffDen"),
    triggers = cms.vstring(),
    cuts = cms.VPSet()
)
### passes MET trigger (use eventvariable so that triggers can be ANDed)
TrigEffDen.cuts.append(pass_HLTMET_paths)
### at least one good, isolated electron
TrigEffDen.cuts.extend(atLeastOne_electron_basic_selection_cuts)
### at least one good, isolated muon
TrigEffDen.cuts.extend(atLeastOne_muon_basic_selection_cuts)
#TrigEffDen.cuts.append(muon_iso_cut)
### at least one good electron-muon pair
##TrigEffDen.cuts.append(emu_opposite_charge_cut)
##TrigEffDen.cuts.append(emu_deltaR_cut)
### at least two good jets, one medium b jet
#TrigEffDen.cuts.extend(atLeastTwo_jet_basic_selection_cuts)
#TrigEffDen.cuts.append(atLeastTwo_jet_lepton_cleaning_cut)
#TrigEffDen.cuts.append(jet_btag_mwp_cut)
### extra lepton vetoes
#TrigEffDen.cuts.append(electron_num_exactly_1_cut)
#TrigEffDen.cuts.append(muon_num_exactly_1_cut)

# Numerator: ttbar+(MET trigger)+(analysis trigger)
TrigEffNum = cms.PSet(
    name = cms.string("TrigEffNum"),
    triggers = triggersMuonPhoton,
    cuts = cms.VPSet(copy.deepcopy(TrigEffDen.cuts))
)


### Require high-pt electron
TrigEffNumHighPtE = cms.PSet(
    name = cms.string("TrigEffNumHighPtE"),
    triggers = copy.deepcopy(TrigEffNum.triggers),
    cuts = cms.VPSet(copy.deepcopy(TrigEffNum.cuts))
)
TrigEffNumHighPtE.cuts.append(electron_pt_50_cut)

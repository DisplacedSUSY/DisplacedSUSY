import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.EMuChannel.TTbarXsectionPaperLL import *

#############################################################################
### Set up the TTBar Paper JJ Selection for the displaced SUSY analysis #####
#############################################################################

TTbarXsectionPaperJJ = cms.PSet(
    name = cms.string("TTbarXsectionPaperJJ"),
    triggers = copy.deepcopy(TTbarXsectionPaperLL.triggers),
    cuts = cms.VPSet ()
)
TTbarXsectionPaperJJ.cuts = cms.VPSet (copy.deepcopy(TTbarXsectionPaperLL.cuts))

### Require jets
TTbarXsectionPaperJJ.cuts.append(jet_eta_real_cut)
TTbarXsectionPaperJJ.cuts.append(jet_pt_30_real_cut)
TTbarXsectionPaperJJ.cuts.append(jet_ttbar_paper_loose_id_cut)
TTbarXsectionPaperJJ.cuts.append(jet_lepton_cleaning_cut)

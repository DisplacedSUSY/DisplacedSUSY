import FWCore.ParameterSet.Config as cms
import copy
import string
from DisplacedSUSY.EMuChannel.CutDefinitions import *
from DisplacedSUSY.EMuChannel.TTbarXsectionPaperJJ import *

#############################################################################
### Set up the TTBar Paper BJet Selection for the displaced SUSY analysis #####
#############################################################################

TTbarXsectionPaperBJet = cms.PSet(
    name = cms.string("TTbarXsectionPaperBJet"),
    triggers = copy.deepcopy(TTbarXsectionPaperJJ.triggers),
    cuts = cms.VPSet ()
)
TTbarXsectionPaperBJet.cuts = cms.VPSet (copy.deepcopy(TTbarXsectionPaperJJ.cuts))

### one b jet
TTbarXsectionPaperBJet.cuts.append(jet_btag_lwp_cut)

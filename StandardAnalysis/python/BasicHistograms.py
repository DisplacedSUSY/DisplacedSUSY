import FWCore.ParameterSet.Config as cms

################################################################################
##### Basic histograms to be plotted for almost every selection ################
################################################################################ 

from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms, MetHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import BeamspotHistograms, eventHistograms

histograms = cms.VPSet()
histograms.append(JetHistograms)
histograms.append(MetHistograms)
histograms.append(BeamspotHistograms)
histograms.append(eventHistograms)

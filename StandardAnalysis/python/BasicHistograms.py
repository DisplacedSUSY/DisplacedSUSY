import FWCore.ParameterSet.Config as cms

################################################################################
##### Basic histograms to be plotted for almost every selection ################
################################################################################

from DisplacedSUSY.Configuration.histogramDefinitions import JetHistograms, MetHistograms, BjetHistograms, JetBjetHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import BeamspotHistograms, eventHistograms, GenParticleHistograms, GenParticleD0Histograms

histograms = cms.VPSet()
histograms.append(JetHistograms)
#histograms.append(BjetHistograms)
#histograms.append(JetBjetHistograms)
histograms.append(MetHistograms)
histograms.append(BeamspotHistograms)
histograms.append(eventHistograms)
#histograms.append(GenParticleHistograms)
#histograms.append(GenParticleD0Histograms)

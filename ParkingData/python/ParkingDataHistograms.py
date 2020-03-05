import FWCore.ParameterSet.Config as cms
from DisplacedSUSY.Configuration.histogramDefinitions import MuonHistograms, DiMuonHistograms, MuonJetHistograms, MuonMetHistograms
from DisplacedSUSY.Configuration.histogramDefinitions import MuonD0Histograms, DiMuonHistogramsExtra, eventHistograms
from DisplacedSUSY.StandardAnalysis.BasicHistograms import *

histograms.append(MuonHistograms)
histograms.append(DiMuonHistograms)
histograms.append(DiMuonHistogramsExtra)
histograms.append(MuonD0Histograms)
histograms.append(MuonJetHistograms)
histograms.append(MuonMetHistograms)

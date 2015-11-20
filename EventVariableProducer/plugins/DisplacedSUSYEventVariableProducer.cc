#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisplacedSUSY/EventVariableProducer/plugins/DisplacedSUSYEventVariableProducer.h"

DisplacedSUSYEventVariableProducer::DisplacedSUSYEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

DisplacedSUSYEventVariableProducer::~DisplacedSUSYEventVariableProducer() {}

void
DisplacedSUSYEventVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == MINI_AOD_CUSTOM || DATA_FORMAT == MINI_AOD
  objectsToGet_.insert ("jets");
  objectsToGet_.insert ("electrons");
  objectsToGet_.insert ("muons");
  objectsToGet_.insert ("primaryvertexs");
  getOriginalCollections (objectsToGet_, collections_, handles_, event);
  double sumJetPt = -1;
  double numPV = 0;
  for (const auto &jet1 : *handles_.jets) {
    if(jet1.pt() >= 25 && abs(jet1.eta()) <= 2.4 && jet1.neutralHadronEnergyFraction() < 0.99 && jet1.chargedEmEnergyFraction() < 0.99 && jet1.neutralEmEnergyFraction() < 0.99 && jet1.numberOfDaughters() > 1 && jet1.chargedHadronEnergyFraction() > 0.0 && jet1.chargedMultiplicity() > 0.0)
    {
      if(passCleaning(jet1.eta(),jet1.phi(), handles_) )  
        sumJetPt = sumJetPt + jet1.pt();
      }
    }
 for (const auto &pv1 : *handles_.primaryvertexs) {
    if(pv1.isValid())
      numPV = numPV + 1;
  }
  (*eventvariables)["sumJetPt"] = sumJetPt;
  (*eventvariables)["numPV"] = numPV;
 # endif
 }  

bool
DisplacedSUSYEventVariableProducer::passCleaning(double eta, double phi, OriginalCollections &handles)
{
  bool muonClean = true;
  bool eleClean = true;
  for (const auto &muon1 : *handles_.muons)
    {
      if(deltaR(eta,phi,muon1.eta(),muon1.phi()) < 0.5)
        {
          if(muon1.isPFMuon() && muon1.isGlobalMuon() && muon1.pt() > 25)
            {  
              muonClean = false; 
              break;
            }
        }
    }
 for (const auto &electron1 : *handles_.electrons)
   {
     if(deltaR(eta,phi,electron1.eta(),electron1.phi()) < 0.5)
       {
         if(electron1.pt() > 25 && ((electron1.isEB() && electron1.missingInnerHits() <= 2 && abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.0105 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.115 && electron1.full5x5_sigmaIetaIeta() < 0.0103 && electron1.hadronicOverEm() < 0.104 && abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.102 && !electron1.vtxFitConversion())|| (electron1.isEE() && electron1.missingInnerHits() <= 1 && abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00814 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.182 && electron1.full5x5_sigmaIetaIeta() < 0.0301 && electron1.hadronicOverEm() < 0.0897 && abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.126 && !electron1.vtxFitConversion())))
           {
             eleClean = false;       
             break;   
           }
       }      
   }
  return muonClean && eleClean;
}

void
DisplacedSUSYEventVariableProducer::getOriginalCollections (const unordered_set<string> &objectsToGet, const edm::ParameterSet &collections, OriginalCollections &handles, const edm::Event &event)
{

  //////////////////////////////////////////////////////////////////////////////
  // Retrieve each object collection which we need and print a warning if it is
  // missing.
  //////////////////////////////////////////////////////////////////////////////
  if  (VEC_CONTAINS  (objectsToGet,  "electrons")         &&  collections.exists  ("electrons"))         anatools::getCollection  (collections.getParameter<edm::InputTag>  ("electrons"),         handles.electrons,         event);
  if  (VEC_CONTAINS  (objectsToGet,  "jets")              &&  collections.exists  ("jets"))              anatools::getCollection  (collections.getParameter<edm::InputTag>  ("jets"),              handles.jets,              event);
  if  (VEC_CONTAINS  (objectsToGet,  "muons")             &&  collections.exists  ("muons"))             anatools::getCollection  (collections.getParameter<edm::InputTag>  ("muons"),             handles.muons,             event);
  if  (VEC_CONTAINS  (objectsToGet,  "primaryvertexs")    &&  collections.exists  ("primaryvertexs"))    anatools::getCollection  (collections.getParameter<edm::InputTag>  ("primaryvertexs"),    handles.primaryvertexs,    event);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisplacedSUSY/EventVariableProducer/plugins/DisplacedSUSYEventVariableProducer.h"

DisplacedSUSYEventVariableProducer::DisplacedSUSYEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  type_             (cfg.getParameter<string>("type"))
  //  triggerPath_      (cfg.getParameter<string>("triggerPath")),
  //  triggerScalingFactor_      (cfg.getParameter<double>("triggerScalingFactor"))
{
  pileUpInfosToken_ = consumes<vector<TYPE(pileupinfos)> > (collections_.getParameter<edm::InputTag> ("pileupinfos"));
  muonsToken_ = consumes<vector<TYPE(muons)> > (collections_.getParameter<edm::InputTag> ("muons"));
  electronsToken_ = consumes<vector<TYPE(electrons)> > (collections_.getParameter<edm::InputTag> ("electrons"));
  jetsToken_ = consumes<vector<TYPE(jets)> > (collections_.getParameter<edm::InputTag> ("jets"));
  primaryVertexsToken_ = consumes<vector<TYPE(primaryvertexs)> > (collections_.getParameter<edm::InputTag> ("primaryvertexs"));
  //  triggersToken_ = consumes<edm::TriggerResults> (collections_.getParameter<edm::InputTag> ("triggers"));
}
DisplacedSUSYEventVariableProducer::~DisplacedSUSYEventVariableProducer() {}

void
DisplacedSUSYEventVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == MINI_AOD_CUSTOM || DATA_FORMAT == MINI_AOD
  objectsToGet_.insert ("jets");
  objectsToGet_.insert ("electrons");
  objectsToGet_.insert ("muons");
  objectsToGet_.insert ("primaryvertexs");
  //  objectsToGet_.insert ("triggers");
  if(type_.find("MC") < type_.length())
      objectsToGet_.insert ("pileupinfos");
  getOriginalCollections (objectsToGet_, collections_, handles_, event);
  double sumJetPt = -1;
  double numPV = 0;
  double numTruePV = 0;
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
  if(type_.find("MC") < type_.length())
    {
      for (const auto &pv1 : *handles_.pileupinfos) {
      if(pv1.getBunchCrossing() == 0)
        numTruePV = pv1.getTrueNumInteractions();
      }
    }
  //  const edm::TriggerNames &names = event.triggerNames(*handles_.triggers);
  // double passTrigger = 0.0;
  // for (unsigned int i = 0; i < names.size() - 1 ; ++i){
  //   std::string name = names.triggerName(i);
  //   if(name.find(triggerPath_) < name.length() && handles_.triggers->accept(i))
  //    passTrigger = 1.0;
  // }
  // Identify tag muon to for trigger efficiency plotting
  bool tagMuonExists = false;
  double tagMuonPt = 0;
  double tagMuonEta = 0;
  double tagMuonPhi = -4; // -pi < phi < pi
  double tagMuonCharge = 0;
  for (const auto &muon1 : *handles_.muons) {
    // Use subset of muon selection criteria that can be implemented here without significant hassle
    // TagMuonPhi condition exists to pseudorandomly pick tag muon if multiple candidates exist
    if (muon1.pt() > 55 && muon1.phi() > tagMuonPhi && abs(muon1.eta()) < 2.4 && muon1.isGlobalMuon() && muon1.isPFMuon() && muon1.numberOfMatchedStations() > 1) {
      tagMuonExists = true;
      tagMuonPt = muon1.pt();
      tagMuonEta = muon1.eta();
      tagMuonPhi = muon1.phi();
      tagMuonCharge = muon1.charge();
    }
  }
  (*eventvariables)["tagMuonExists"] = tagMuonExists;
  (*eventvariables)["tagMuonPt"] = tagMuonPt;
  (*eventvariables)["tagMuonEta"] = tagMuonEta;
  (*eventvariables)["tagMuonPhi"] = tagMuonPhi;
  (*eventvariables)["tagMuonCharge"] = tagMuonCharge;
  (*eventvariables)["numTruePV"] = numTruePV;
  (*eventvariables)["sumJetPt"] = sumJetPt;
  (*eventvariables)["numPV"] = numPV;
  //  (*eventvariables)["passTrigger"] = passTrigger;
  //  (*eventvariables)["triggerScalingFactor"] = triggerScalingFactor_;
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
         if(electron1.pt() > 25 && ((electron1.isEB() && electron1.gsfTrack()->hitPattern ().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) <= 2 && abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.0105 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.115 && electron1.full5x5_sigmaIetaIeta() < 0.0103 && electron1.hadronicOverEm() < 0.104 && abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.102 )|| (electron1.isEE() && electron1.gsfTrack()->hitPattern ().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) <= 1 && abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00814 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.182 && electron1.full5x5_sigmaIetaIeta() < 0.0301 && electron1.hadronicOverEm() < 0.0897 && abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.126)))
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
  if  (VEC_CONTAINS  (objectsToGet,  "electrons"))       event.getByToken  (electronsToken_, handles.electrons);
  if  (VEC_CONTAINS  (objectsToGet,  "jets"))            event.getByToken  (jetsToken_, handles.jets);
  if  (VEC_CONTAINS  (objectsToGet,  "muons"))           event.getByToken  (muonsToken_, handles.muons);
  if  (VEC_CONTAINS  (objectsToGet,  "primaryvertexs"))  event.getByToken  (primaryVertexsToken_, handles.primaryvertexs);
  if  (VEC_CONTAINS  (objectsToGet,  "pileupinfos"))     event.getByToken  (pileUpInfosToken_, handles.pileupinfos);
  //  if  (VEC_CONTAINS  (objectsToGet,  "triggers"))        event.getByToken  (triggersToken_, handles.triggers);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

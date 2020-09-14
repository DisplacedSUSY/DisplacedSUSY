#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisplacedSUSY/EventVariableProducer/plugins/DisplacedSUSYEventVariableProducer.h"

DisplacedSUSYEventVariableProducer::DisplacedSUSYEventVariableProducer(const edm::ParameterSet &cfg) : EventVariableProducer(cfg) {

  pileUpInfosToken_ = consumes<vector<TYPE(pileupinfos)> > (collections_.getParameter<edm::InputTag> ("pileupinfos"));
  muonsToken_ = consumes<vector<TYPE(muons)> > (collections_.getParameter<edm::InputTag> ("muons"));
  electronsToken_ = consumes<vector<TYPE(electrons)> > (collections_.getParameter<edm::InputTag> ("electrons"));
  jetsToken_ = consumes<vector<TYPE(jets)> > (collections_.getParameter<edm::InputTag> ("jets"));
  beamspotsToken_ = consumes<TYPE(beamspots)> (collections_.getParameter<edm::InputTag> ("beamspots"));
  primaryVertexsToken_ = consumes<vector<TYPE(primaryvertexs)> > (collections_.getParameter<edm::InputTag> ("primaryvertexs"));
  triggersToken_ = consumes<edm::TriggerResults> (collections_.getParameter<edm::InputTag> ("triggers"));

  type_ = cfg.getParameter<string>("type");
  triggerPaths_ = cfg.getParameter<std::vector<std::string> >("triggerPaths");
  //fill a map of HLT paths
  for(unsigned int i = 0; i < triggerPaths_.size(); i++) HLTBitsMap[ triggerPaths_[i] ] = false;

  //L1 bits information, thanks to scouting dijet team
  //https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetScoutingTreeProducer.cc
  l1GtUtils_ = new l1t::L1TGlobalUtil(cfg,consumesCollector());
  algToken_ = consumes<BXVector<GlobalAlgBlk>>(cfg.getParameter<edm::InputTag>("AlgInputTag"));
  l1Seeds_ = cfg.getParameter<std::vector<std::string> >("l1Seeds");
  //fill a map of l1 seeds
  for(unsigned int i = 0; i < l1Seeds_.size(); i++) L1BitsMap[ l1Seeds_[i] ] = false;
}

DisplacedSUSYEventVariableProducer::~DisplacedSUSYEventVariableProducer() {}

void DisplacedSUSYEventVariableProducer::AddVariables (const edm::Event &event, const edm::EventSetup &setup) {
  objectsToGet_.insert ("jets");
  objectsToGet_.insert ("electrons");
  objectsToGet_.insert ("muons");
  objectsToGet_.insert ("beamspots");
  objectsToGet_.insert ("primaryvertexs");
  objectsToGet_.insert ("triggers");
  if(type_.find("MC") < type_.length()) {
    objectsToGet_.insert ("pileupinfos");
  }
  getOriginalCollections (objectsToGet_, collections_, handles_, event);

  double numPV = 0;
  for (const auto &pv1 : *handles_.primaryvertexs) {
    if(pv1.isValid()) {
      numPV = numPV + 1;
    }
  }

  double numTruePV = 0;
  if(type_.find("MC") < type_.length()) {
    for (const auto &pv1 : *handles_.pileupinfos) {
      if(pv1.getBunchCrossing() == 0) {
          numTruePV = pv1.getTrueNumInteractions();
      }
    }
  }

#if DATA_FORMAT_FROM_MINIAOD
  double sumJetPt = -1;
  for (const auto &jet1 : *handles_.jets) {
    if(jet1.pt() >= 25 && abs(jet1.eta()) <= 2.4 && jet1.neutralHadronEnergyFraction() < 0.99 && jet1.chargedEmEnergyFraction() < 0.99 && jet1.neutralEmEnergyFraction() < 0.99 && jet1.numberOfDaughters() > 1 && jet1.chargedHadronEnergyFraction() > 0.0 && jet1.chargedMultiplicity() > 0.0) {
      if(passCleaning(jet1.eta(),jet1.phi(), handles_) ) {
	sumJetPt = sumJetPt + jet1.pt();
      }
    }
  }

  double numSoftMuons = 0;
  for(const auto muon : *handles_.muons) {
    if(muon.isSoftMuon((*handles_.primaryvertexs)[0])) {
      numSoftMuons = numSoftMuons + 1;
    }
  }

  double numTightMuons = 0;
  for(const auto muon : *handles_.muons) {
    if(muon.isTightMuon((*handles_.primaryvertexs)[0])) {
      numTightMuons = numTightMuons + 1;
    }
  }
#endif

  // Pass trigger specified in config file
  const edm::TriggerNames &names = event.triggerNames(*handles_.triggers);
  for( unsigned int ipath = 0; ipath < triggerPaths_.size(); ipath++ ) {
    HLTBitsMap[triggerPaths_[ipath]] = false;
    bool passTrigger = 0;
    for (unsigned int i = 0; i < names.size() - 1 ; ++i) {
      std::string name = names.triggerName(i);
      if(name.find(triggerPaths_[ipath]) == 0 && handles_.triggers->accept(i)) {
	passTrigger = true;
      }
    }
    //std::cout<<"triggerPaths_[ipath] is: "<<triggerPaths_[ipath]<< " " << passTrigger << std::endl;
    if (passTrigger){
      HLTBitsMap[triggerPaths_[ipath]] = true;
    }
  }


  // Identify tag muon to for trigger efficiency plotting
  bool tagMuonExists = false;
  double tagMuonPt = 0;
  double tagMuonEta = 0;
  double tagMuonPhi = -4; // -pi < phi < pi
  double tagMuonCharge = 0;
  double tagMuonUnsmearedD0 = 0;
  auto beamspot = *handles_.beamspots;
  for (const auto &muon1 : *handles_.muons) {
    // Use subset of muon selection criteria that can be implemented here without significant hassle
  // This is a hideous approach. These magic numbers should be replaced by a better approach
  // TagMuonPhi condition exists to pseudorandomly pick tag muon if multiple candidates exist
    if (muon1.pt() > 55 && muon1.phi() > tagMuonPhi && abs(muon1.eta()) < 2.4 && muon1.isGlobalMuon() && muon1.isPFMuon() && muon1.numberOfMatchedStations() > 1) {
      tagMuonExists = true;
      tagMuonPt = muon1.pt();
      tagMuonEta = muon1.eta();
      tagMuonPhi = muon1.phi();
      tagMuonCharge = muon1.charge();
      tagMuonUnsmearedD0 = (-(muon1.vx() - beamspot.x0())*muon1.py() + (muon1.vy() - beamspot.y0())*muon1.px())/muon1.pt();
    }
  }

  // Store leading and subleading muon properties
  double leadingMuonPt = 0;
  double leadingMuonEta = 0;
  double leadingMuonPhi = -4; // -pi < phi < pi
  double leadingMuonUnsmearedD0 = 0;
  double leadingMuonTime = -100;
  int    leadingMuonTimeNDof = 0;
  double subleadingMuonPt = 0;
  double subleadingMuonEta = 0;
  double subleadingMuonPhi = -4; // -pi < phi < pi
  double subleadingMuonUnsmearedD0 = 0;
  double subleadingMuonTime = 100;
  int    subleadingMuonTimeNDof = 0;
  for (const auto &muon1 : *handles_.muons) {
    if (muon1.isGlobalMuon() && muon1.isPFMuon() && muon1.numberOfMatchedStations() > 1) {
       if (muon1.pt() > subleadingMuonPt) {
	if (muon1.pt() > leadingMuonPt) {
	  subleadingMuonPt = leadingMuonPt;
	  subleadingMuonEta = leadingMuonEta;
	  subleadingMuonPhi = leadingMuonPhi;
          subleadingMuonUnsmearedD0 = leadingMuonUnsmearedD0;
	  subleadingMuonTime = leadingMuonTime;
	  subleadingMuonTimeNDof = leadingMuonTimeNDof;
          leadingMuonPt = muon1.pt();
          leadingMuonEta = muon1.eta();
          leadingMuonPhi = muon1.phi();
          leadingMuonUnsmearedD0 = (-(muon1.vx() - beamspot.x0())*muon1.py() + (muon1.vy() - beamspot.y0())*muon1.px())/muon1.pt();
	  leadingMuonTime = muon1.time().timeAtIpInOut;
	  leadingMuonTimeNDof = muon1.time().nDof;
        }
        else {
          subleadingMuonPt = muon1.pt();
          subleadingMuonEta = muon1.eta();
          subleadingMuonPhi = muon1.phi();
          subleadingMuonUnsmearedD0 = (-(muon1.vx() - beamspot.x0())*muon1.py() + (muon1.vy() - beamspot.y0())*muon1.px())/muon1.pt();
	  subleadingMuonTime = muon1.time().timeAtIpInOut;
	  subleadingMuonTimeNDof = muon1.time().nDof;
        }
      }
    }
  }

  double upperMuonTime = leadingMuonTime;
  double lowerMuonTime = subleadingMuonTime;
  double upperMuonTimeNDof = leadingMuonTimeNDof;
  double lowerMuonTimeNDof = subleadingMuonTimeNDof;
  if(leadingMuonPhi < subleadingMuonPhi){
    upperMuonTime = subleadingMuonTime;
    lowerMuonTime = leadingMuonTime;
    upperMuonTimeNDof = subleadingMuonTimeNDof;
    lowerMuonTimeNDof = leadingMuonTimeNDof;
  }
  double deltaT = upperMuonTime - lowerMuonTime;

  bool vetoTiming = false;
  if (deltaT < -20.0 && leadingMuonTimeNDof > 7 && subleadingMuonTimeNDof > 7) vetoTiming = true;

  // Identify tag electron for trigger efficiency plotting
#if DATA_FORMAT_FROM_MINIAOD
  bool tagElectronExists = false;
  double tagElectronPt = -999;
  double tagElectronEta = 0;
  double tagElectronPhi = -4;
  double tagElectronCharge = -999;
  double tagElectronUnsmearedD0 = 0;
  for (const auto &electron1 : *handles_.electrons) {
    // electron ID: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
    // These magic numbers should be replaced by a better approach
    if (electron1.pt() > 55 && electron1.phi() > tagElectronPhi && abs(electron1.eta()) <= 1.479 &&
        electron1.full5x5_sigmaIetaIeta() < 0.00998 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.0816 &&
        abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00308 && electron1.hadronicOverEm() < 0.0414 &&
        abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.0129 &&
	electron1.passConversionVeto()) {
      tagElectronExists = true;
      tagElectronPt = electron1.pt();
      tagElectronEta = electron1.eta();
      tagElectronPhi = electron1.phi();
      tagElectronCharge = electron1.charge();
      tagElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
    }
    if (electron1.pt() > 55 && electron1.phi() > tagElectronPhi && abs(electron1.eta()) > 1.479 &&
        electron1.full5x5_sigmaIetaIeta() < 0.0292 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.0394 &&
        abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00605 && electron1.hadronicOverEm() < 0.0641 &&
        abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.0129 &&
        electron1.passConversionVeto()) {
      tagElectronExists = true;
      tagElectronPt = electron1.pt();
      tagElectronEta = electron1.eta();
      tagElectronPhi = electron1.phi();
      tagElectronCharge = electron1.charge();
      tagElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
    }
  }


  // Store leading and subleading electron properties
  double leadingElectronPt = 0;
  double leadingElectronEta = 0;
  double leadingElectronPhi = -4; // -pi < phi < pi
  double leadingElectronUnsmearedD0 = 0;
  double subleadingElectronPt = 0;
  double subleadingElectronEta = 0;
  double subleadingElectronPhi = -4; // -pi < phi < pi
  double subleadingElectronUnsmearedD0 = 0;
  for (const auto &electron1 : *handles_.electrons) {
    if (abs(electron1.eta()) < 1.479 && electron1.full5x5_sigmaIetaIeta() < 0.00998 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.0816 &&
        abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00308 && electron1.hadronicOverEm() < 0.0414 &&
        abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.0129 &&
        electron1.passConversionVeto()) {
      if (electron1.pt() > subleadingElectronPt) {
        if (electron1.pt() > leadingElectronPt) {
          subleadingElectronPt = leadingElectronPt;
          subleadingElectronEta = leadingElectronEta;
          subleadingElectronPhi = leadingElectronPhi;
          subleadingElectronUnsmearedD0 = leadingElectronUnsmearedD0;
          leadingElectronPt = electron1.pt();
          leadingElectronEta = electron1.eta();
          leadingElectronPhi = electron1.phi();
          leadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
        }
        else {
          subleadingElectronPt = electron1.pt();
          subleadingElectronEta = electron1.eta();
          subleadingElectronPhi = electron1.phi();
          subleadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
        }
      }
    }
    if (abs(electron1.eta()) < 1.479 && electron1.full5x5_sigmaIetaIeta() < 0.0292 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.0394 &&
        abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00605 && electron1.hadronicOverEm() < 0.0641 &&
        abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.0129 &&
        electron1.passConversionVeto()) {
      if (electron1.pt() > subleadingElectronPt) {
        if (electron1.pt() > leadingElectronPt) {
          subleadingElectronPt = leadingElectronPt;
          subleadingElectronEta = leadingElectronEta;
          subleadingElectronPhi = leadingElectronPhi;
          subleadingElectronUnsmearedD0 = leadingElectronUnsmearedD0;
          leadingElectronPt = electron1.pt();
          leadingElectronEta = electron1.eta();
          leadingElectronPhi = electron1.phi();
          leadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
        }
        else {
          subleadingElectronPt = electron1.pt();
          subleadingElectronEta = electron1.eta();
          subleadingElectronPhi = electron1.phi();
          subleadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
        }
      }
    }
  }
#endif




  //L1 bits
  l1GtUtils_->retrieveL1(event,setup,algToken_);
  //std::cout<<"starting to loop over L1 seeds"<<std::endl;
  for( unsigned int iseed = 0; iseed < l1Seeds_.size(); iseed++ ) {
    L1BitsMap[l1Seeds_[iseed]] = false;
    bool l1htbit = 0;
    l1GtUtils_->getFinalDecisionByName(l1Seeds_[iseed], l1htbit);
    //std::cout<<l1Seeds_[iseed]<< " " << l1htbit << std::endl;
    if (l1htbit){
      L1BitsMap[l1Seeds_[iseed]] = true;
    }
  }

  (*eventvariables)["tagMuonExists"] = tagMuonExists;
  (*eventvariables)["tagMuonPt"] = tagMuonPt;
  (*eventvariables)["tagMuonEta"] = tagMuonEta;
  (*eventvariables)["tagMuonPhi"] = tagMuonPhi;
  (*eventvariables)["tagMuonCharge"] = tagMuonCharge;
  (*eventvariables)["tagMuonUnsmearedD0"] = tagMuonUnsmearedD0;
  (*eventvariables)["leadingMuonPt"] = leadingMuonPt;
  (*eventvariables)["leadingMuonEta"] = leadingMuonEta;
  (*eventvariables)["leadingMuonPhi"] = leadingMuonPhi;
  (*eventvariables)["leadingMuonUnsmearedD0"] = leadingMuonUnsmearedD0;
  (*eventvariables)["subleadingMuonPt"] = subleadingMuonPt;
  (*eventvariables)["subleadingMuonEta"] = subleadingMuonEta;
  (*eventvariables)["subleadingMuonPhi"] = subleadingMuonPhi;
  (*eventvariables)["subleadingMuonUnsmearedD0"] = subleadingMuonUnsmearedD0;
#if DATA_FORMAT_FROM_MINIAOD
  (*eventvariables)["tagElectronExists"] = tagElectronExists;
  (*eventvariables)["tagElectronPt"] = tagElectronPt;
  (*eventvariables)["tagElectronEta"] = tagElectronEta;
  (*eventvariables)["tagElectronPhi"] = tagElectronPhi;
  (*eventvariables)["tagElectronCharge"] = tagElectronCharge;
  (*eventvariables)["tagElectronUnsmearedD0"] = tagElectronUnsmearedD0;
  (*eventvariables)["leadingElectronPt"] = leadingElectronPt;
  (*eventvariables)["leadingElectronEta"] = leadingElectronEta;
  (*eventvariables)["leadingElectronPhi"] = leadingElectronPhi;
  (*eventvariables)["leadingElectronUnsmearedD0"] = leadingElectronUnsmearedD0;
  (*eventvariables)["subleadingElectronPt"] = subleadingElectronPt;
  (*eventvariables)["subleadingElectronEta"] = subleadingElectronEta;
  (*eventvariables)["subleadingElectronPhi"] = subleadingElectronPhi;
  (*eventvariables)["subleadingElectronUnsmearedD0"] = subleadingElectronUnsmearedD0;
  (*eventvariables)["sumJetPt"] = sumJetPt;
  (*eventvariables)["numSoftMuons"] = numSoftMuons;
  (*eventvariables)["numTightMuons"] = numTightMuons;
#endif
  if (leadingMuonTimeNDof > 7 && subleadingMuonTimeNDof > 7){
    (*eventvariables)["deltaT_leadingTwoMuons"] = deltaT;
    (*eventvariables)["upperMuonTime"] = upperMuonTime;
    (*eventvariables)["lowerMuonTime"] = lowerMuonTime;
  }
  (*eventvariables)["upperMuonTimeNDof"] = upperMuonTimeNDof;
  (*eventvariables)["lowerMuonTimeNDof"] = lowerMuonTimeNDof;
  (*eventvariables)["vetoTiming"] = vetoTiming;
  (*eventvariables)["numTruePV"] = numTruePV;
  (*eventvariables)["numPV"] = numPV;
  for( unsigned int ipath = 0; ipath < triggerPaths_.size(); ipath++ ) {
    (*eventvariables)[triggerPaths_[ipath].c_str()] = HLTBitsMap[triggerPaths_[ipath]];
  }
  for( unsigned int iseed = 0; iseed < l1Seeds_.size(); iseed++ ) {
    (*eventvariables)[l1Seeds_[iseed].c_str()] = L1BitsMap[l1Seeds_[iseed]];
  }

}

bool DisplacedSUSYEventVariableProducer::passCleaning(double eta, double phi, OriginalCollections &handles) {
  bool muonClean = true;
  bool eleClean = true;
  for (const auto &muon1 : *handles_.muons) {
    if(deltaR(eta,phi,muon1.eta(),muon1.phi()) < 0.5) {
      if(muon1.isPFMuon() && muon1.isGlobalMuon() && muon1.pt() > 25) {
        muonClean = false;
        break;
      }
    }
  }
  // These magic numbers should be replaced by a better approach
  for (const auto &electron1 : *handles_.electrons) {
    if(deltaR(eta,phi,electron1.eta(),electron1.phi()) < 0.5) {
      if(electron1.pt() > 25 &&
      ((electron1.isEB() &&
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
	  electron1.gsfTrack()->hitPattern ().numberOfAllHits(reco::HitPattern::MISSING_INNER_HITS) <= 2 &&
#else
	  electron1.gsfTrack()->hitPattern ().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) <= 2 &&
#endif
	  abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.0105 &&
	  abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.115 &&
	  electron1.full5x5_sigmaIetaIeta() < 0.0103 &&
	  electron1.hadronicOverEm() < 0.104 &&
	  abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.102 )||
	  (electron1.isEE() &&
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
	  electron1.gsfTrack()->hitPattern ().numberOfAllHits(reco::HitPattern::MISSING_INNER_HITS) <= 1 &&
#else
	  electron1.gsfTrack()->hitPattern ().numberOfHits(reco::HitPattern::MISSING_INNER_HITS) <= 1 &&
#endif
	  abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00814 &&
	  abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.182 &&
	  electron1.full5x5_sigmaIetaIeta() < 0.0301 &&
	  electron1.hadronicOverEm() < 0.0897 &&
	  abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.126))) {
        eleClean = false;
        break;
      }
    }
  }
  return muonClean && eleClean;
}

void DisplacedSUSYEventVariableProducer::getOriginalCollections (const unordered_set<string> &objectsToGet,
                                                                 const edm::ParameterSet &collections,
                                                                 OriginalCollections &handles,
                                                                 const edm::Event &event) {

  //////////////////////////////////////////////////////////////////////////////
  // Retrieve each object collection which we need and print a warning if it is
  // missing.
  //////////////////////////////////////////////////////////////////////////////
  if  (VEC_CONTAINS  (objectsToGet,  "electrons"))       event.getByToken  (electronsToken_, handles.electrons);
  if  (VEC_CONTAINS  (objectsToGet,  "jets"))            event.getByToken  (jetsToken_, handles.jets);
  if  (VEC_CONTAINS  (objectsToGet,  "muons"))           event.getByToken  (muonsToken_, handles.muons);
  if  (VEC_CONTAINS  (objectsToGet,  "beamspots"))       event.getByToken  (beamspotsToken_, handles.beamspots);
  if  (VEC_CONTAINS  (objectsToGet,  "primaryvertexs"))  event.getByToken  (primaryVertexsToken_, handles.primaryvertexs);
  if  (VEC_CONTAINS  (objectsToGet,  "pileupinfos"))     event.getByToken  (pileUpInfosToken_, handles.pileupinfos);
  if  (VEC_CONTAINS  (objectsToGet,  "triggers"))        event.getByToken  (triggersToken_, handles.triggers);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

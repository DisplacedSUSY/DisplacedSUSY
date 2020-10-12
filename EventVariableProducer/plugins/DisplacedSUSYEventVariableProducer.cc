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

  beamPipe_x_center_ = cfg.getParameter<double>("beamPipe_x_center");
  beamPipe_y_center_ = cfg.getParameter<double>("beamPipe_y_center");
  beamPipe_outerR_ = cfg.getParameter<double>("beamPipe_outerR");
  beamPipe_innerR_ = cfg.getParameter<double>("beamPipe_innerR");

  nearInnerShield_x_center_ = cfg.getParameter<double>("nearInnerShield_x_center");
  nearInnerShield_y_center_ = cfg.getParameter<double>("nearInnerShield_y_center");
  farInnerShield_x_center_ = cfg.getParameter<double>("farInnerShield_x_center");
  farInnerShield_y_center_ = cfg.getParameter<double>("farInnerShield_y_center");
  innerShield_outerR_ = cfg.getParameter<double>("innerShield_outerR");
  innerShield_innerR_ = cfg.getParameter<double>("innerShield_innerR");

  bpix_x_center_ = cfg.getParameter<double>("bpix_x_center");
  bpix_y_center_ = cfg.getParameter<double>("bpix_y_center");
  bpix_z_center_ = cfg.getParameter<double>("bpix_z_center");
  bpix_z_halfLength_ = cfg.getParameter<double>("bpix_z_halfLength");
  bpixL1_outerR_ = cfg.getParameter<double>("bpixL1_outerR");
  bpixL1_innerR_ = cfg.getParameter<double>("bpixL1_innerR");
  bpixL2_outerR_ = cfg.getParameter<double>("bpixL2_outerR");
  bpixL2_innerR_ = cfg.getParameter<double>("bpixL2_innerR");
  bpixL3_outerR_ = cfg.getParameter<double>("bpixL3_outerR");
  bpixL3_innerR_ = cfg.getParameter<double>("bpixL3_innerR");
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
  bpixL4_outerR_ = cfg.getParameter<double>("bpixL4_outerR");
  bpixL4_innerR_ = cfg.getParameter<double>("bpixL4_innerR");
#endif

  fpix_x_center_ = cfg.getParameter<double>("fpix_x_center");
  fpix_y_center_ = cfg.getParameter<double>("fpix_y_center");
  fpixD1_z_center_ = cfg.getParameter<double>("fpixD1_z_center");
  fpixD2_z_center_ = cfg.getParameter<double>("fpixD2_z_center");
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
  fpixD3_z_center_ = cfg.getParameter<double>("fpixD3_z_center");
#endif
  fpix_outerR_ = cfg.getParameter<double>("fpix_outerR");
  fpix_innerR_ = cfg.getParameter<double>("fpix_innerR");
  fpix_z_halfThickness_ = cfg.getParameter<double>("fpix_z_halfThickness");

  supportTube_x_center_ = cfg.getParameter<double>("supportTube_x_center");
  supportTube_y_center_ = cfg.getParameter<double>("supportTube_y_center");
  supportTube_outerRX_ = cfg.getParameter<double>("supportTube_outerRX");
  supportTube_outerRY_ = cfg.getParameter<double>("supportTube_outerRY");
  supportTube_innerRX_ = cfg.getParameter<double>("supportTube_innerRX");
  supportTube_innerRY_ = cfg.getParameter<double>("supportTube_innerRY");

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

  //get the transient track builder:
  edm::ESHandle<TransientTrackBuilder> theB;
  setup.get<TransientTrackRecord>().get("TransientTrackBuilder", theB);

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
  reco::TransientTrack leadingMuonTrack;
  double subleadingMuonPt = 0;
  double subleadingMuonEta = 0;
  double subleadingMuonPhi = -4; // -pi < phi < pi
  double subleadingMuonUnsmearedD0 = 0;
  double subleadingMuonTime = 100;
  int    subleadingMuonTimeNDof = 0;
  reco::TransientTrack subleadingMuonTrack;

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
	  subleadingMuonTrack = leadingMuonTrack;
          leadingMuonPt = muon1.pt();
          leadingMuonEta = muon1.eta();
          leadingMuonPhi = muon1.phi();
          leadingMuonUnsmearedD0 = (-(muon1.vx() - beamspot.x0())*muon1.py() + (muon1.vy() - beamspot.y0())*muon1.px())/muon1.pt();
	  leadingMuonTime = muon1.time().timeAtIpInOut;
	  leadingMuonTimeNDof = muon1.time().nDof;
	  if (!muon1.innerTrack().isNull()) leadingMuonTrack = (*theB).build(muon1.innerTrack());
	  else std::cout<<"leadingMuonTrack is null"<<std::endl;
        }
        else {
          subleadingMuonPt = muon1.pt();
          subleadingMuonEta = muon1.eta();
          subleadingMuonPhi = muon1.phi();
          subleadingMuonUnsmearedD0 = (-(muon1.vx() - beamspot.x0())*muon1.py() + (muon1.vy() - beamspot.y0())*muon1.px())/muon1.pt();
	  subleadingMuonTime = muon1.time().timeAtIpInOut;
	  subleadingMuonTimeNDof = muon1.time().nDof;
	  if (!muon1.innerTrack().isNull()) subleadingMuonTrack = (*theB).build(muon1.innerTrack());
	  else std::cout<<"subleadingMuonTrack is null"<<std::endl;
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
  reco::TransientTrack leadingElectronTrack;
  double subleadingElectronPt = 0;
  double subleadingElectronEta = 0;
  double subleadingElectronPhi = -4; // -pi < phi < pi
  double subleadingElectronUnsmearedD0 = 0;
  reco::TransientTrack subleadingElectronTrack;

  for (const auto &electron1 : *handles_.electrons) {
    //if (abs(electron1.eta()) < 1.479 && electron1.full5x5_sigmaIetaIeta() < 0.00998 && abs(electron1.deltaPhiSuperClusterTrackAtVtx()) < 0.0816 &&
    //abs(electron1.deltaEtaSuperClusterTrackAtVtx()) < 0.00308 && electron1.hadronicOverEm() < 0.0414 &&
    //abs(1/electron1.ecalEnergy() - electron1.eSuperClusterOverP()/electron1.ecalEnergy()) < 0.0129 &&
    //electron1.passConversionVeto()) {
      if (electron1.pt() > subleadingElectronPt) {
        if (electron1.pt() > leadingElectronPt) {
          subleadingElectronPt = leadingElectronPt;
          subleadingElectronEta = leadingElectronEta;
          subleadingElectronPhi = leadingElectronPhi;
          subleadingElectronUnsmearedD0 = leadingElectronUnsmearedD0;
	  subleadingElectronTrack = leadingElectronTrack;
          leadingElectronPt = electron1.pt();
          leadingElectronEta = electron1.eta();
          leadingElectronPhi = electron1.phi();
          leadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
	  if (!electron1.gsfTrack().isNull()) leadingElectronTrack = (*theB).build(electron1.gsfTrack());
	  else std::cout<<"leadingElectronTrack is null"<<std::endl;
        }
        else {
          subleadingElectronPt = electron1.pt();
          subleadingElectronEta = electron1.eta();
          subleadingElectronPhi = electron1.phi();
          subleadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
	  if (!electron1.gsfTrack().isNull()) subleadingElectronTrack = (*theB).build(electron1.gsfTrack());
	  else std::cout<<"subleadingElectronTrack is null"<<std::endl;
        }
      }
      //}
      /*
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
	  subleadingElectronTrack = leadingElectronTrack;
          leadingElectronPt = electron1.pt();
          leadingElectronEta = electron1.eta();
          leadingElectronPhi = electron1.phi();
          leadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
	  if (!electron1.gsfTrack().isNull()) leadingElectronTrack = (*theB).build(electron1.gsfTrack());
	  else std::cout<<"leadingElectronTrack is null"<<std::endl;
        }
        else {
          subleadingElectronPt = electron1.pt();
          subleadingElectronEta = electron1.eta();
          subleadingElectronPhi = electron1.phi();
          subleadingElectronUnsmearedD0 = (-(electron1.vx() - beamspot.x0())*electron1.py() + (electron1.vy() - beamspot.y0())*electron1.px())/electron1.pt();
	  if (!electron1.gsfTrack().isNull()) subleadingElectronTrack = (*theB).build(electron1.gsfTrack());
	  else std::cout<<"subleadingElectronTrack is null"<<std::endl;
        }
      }
    }
      */
  }

  // try a vertex fit for the two leptons, to see if it overlaps with the tracker material

  vector<reco::TransientTrack> t_tks_ee;
  if(leadingElectronTrack.isValid() && subleadingElectronTrack.isValid()){
    //make sure the leading ele is not also the subleading ele (need two different tracks)
    if(leadingElectronPt!=subleadingElectronPt && leadingElectronEta!=subleadingElectronEta && leadingElectronPhi!=subleadingElectronPhi){
      t_tks_ee.push_back(leadingElectronTrack);
      t_tks_ee.push_back(subleadingElectronTrack);
    }
  }

  vector<reco::TransientTrack> t_tks_mumu;
  if(leadingMuonTrack.isValid() && subleadingMuonTrack.isValid()){
    //make sure the leading mu is not also the subleading mu (need two different tracks)
    if(leadingMuonPt!=subleadingMuonPt && leadingMuonEta!=subleadingMuonEta && leadingMuonPhi!=subleadingMuonPhi){
      t_tks_mumu.push_back(leadingMuonTrack);
      t_tks_mumu.push_back(subleadingMuonTrack);
    }
  }

  vector<reco::TransientTrack> t_tks_emu;
  if(leadingMuonTrack.isValid() && leadingElectronTrack.isValid()){
      t_tks_emu.push_back(leadingMuonTrack);
      t_tks_emu.push_back(leadingElectronTrack);
  }

  DispVtx dvEE = getDispVtx(t_tks_ee);
  DispVtx dvMuMu = getDispVtx(t_tks_mumu);
  DispVtx dvEMu = getDispVtx(t_tks_emu);

  //if(dvEE.vtxChisq!=-5000.) std::cout<<"ee vertex x/y/z/chisq is: "<<dvEE.vtxX<<"/"<<dvEE.vtxY<<"/"<<dvEE.vtxZ<<"/"<<dvEE.vtxChisq<<std::endl;
  //if(dvMuMu.vtxChisq!=-5000.) std::cout<<"mumu vertex x/y/z/chisq is: "<<dvMuMu.vtxX<<"/"<<dvMuMu.vtxY<<"/"<<dvMuMu.vtxZ<<"/"<<dvMuMu.vtxChisq<<std::endl;
  //if(dvEMu.vtxChisq!=-5000.) std::cout<<"emu vertex x/y/z/chisq is: "<<dvEMu.vtxX<<"/"<<dvEMu.vtxY<<"/"<<dvEMu.vtxZ<<"/"<<dvEMu.vtxChisq<<std::endl;

  //vertices in tracker material?
  bool dvEE_inMaterial = inMaterial(dvEE.vtxX, dvEE.vtxY, dvEE.vtxZ);
  bool dvMuMu_inMaterial = inMaterial(dvMuMu.vtxX, dvMuMu.vtxY, dvMuMu.vtxZ);
  bool dvEMu_inMaterial = inMaterial(dvEMu.vtxX, dvEMu.vtxY, dvEMu.vtxZ);


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

  (*eventvariables)["run"] = event.id().run();
  (*eventvariables)["ls"] = event.luminosityBlock();
  (*eventvariables)["event"] = event.id().event();
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
  (*eventvariables)["nDispEEVtxs"] = dvEE.nDispVtxs;
  (*eventvariables)["vtxEEX"] = dvEE.vtxX;
  (*eventvariables)["vtxEEY"] = dvEE.vtxY;
  (*eventvariables)["vtxEEZ"] = dvEE.vtxZ;
  (*eventvariables)["vtxEEXErr"] = dvEE.vtxXErr;
  (*eventvariables)["vtxEEYErr"] = dvEE.vtxYErr;
  (*eventvariables)["vtxEEZErr"] = dvEE.vtxZErr;
  (*eventvariables)["vtxEEChisq"] = dvEE.vtxChisq;
  (*eventvariables)["nDispMuMuVtxs"] = dvMuMu.nDispVtxs;
  (*eventvariables)["vtxMuMuX"] = dvMuMu.vtxX;
  (*eventvariables)["vtxMuMuY"] = dvMuMu.vtxY;
  (*eventvariables)["vtxMuMuZ"] = dvMuMu.vtxZ;
  (*eventvariables)["vtxMuMuXErr"] = dvMuMu.vtxXErr;
  (*eventvariables)["vtxMuMuYErr"] = dvMuMu.vtxYErr;
  (*eventvariables)["vtxMuMuZErr"] = dvMuMu.vtxZErr;
  (*eventvariables)["vtxMuMuChisq"] = dvMuMu.vtxChisq;
  (*eventvariables)["nDispEMuVtxs"] = dvEMu.nDispVtxs;
  (*eventvariables)["vtxEMuX"] = dvEMu.vtxX;
  (*eventvariables)["vtxEMuY"] = dvEMu.vtxY;
  (*eventvariables)["vtxEMuZ"] = dvEMu.vtxZ;
  (*eventvariables)["vtxEMuXErr"] = dvEMu.vtxXErr;
  (*eventvariables)["vtxEMuYErr"] = dvEMu.vtxYErr;
  (*eventvariables)["vtxEMuZErr"] = dvEMu.vtxZErr;
  (*eventvariables)["vtxEMuChisq"] = dvEMu.vtxChisq;
  if(dvEE_inMaterial){
    (*eventvariables)["nDispEEVtxsInMaterial"] = dvEE.nDispVtxs;
    (*eventvariables)["vtxEEXInMaterial"] = dvEE.vtxX;
    (*eventvariables)["vtxEEYInMaterial"] = dvEE.vtxY;
    (*eventvariables)["vtxEEZInMaterial"] = dvEE.vtxZ;
    (*eventvariables)["vtxEEXErrInMaterial"] = dvEE.vtxXErr;
    (*eventvariables)["vtxEEYErrInMaterial"] = dvEE.vtxYErr;
    (*eventvariables)["vtxEEZErrInMaterial"] = dvEE.vtxZErr;
    (*eventvariables)["vtxEEChisqInMaterial"] = dvEE.vtxChisq;
  }
  else (*eventvariables)["nDispEEVtxsInMaterial"] = 0;
  if(dvMuMu_inMaterial){
    (*eventvariables)["nDispMuMuVtxsInMaterial"] = dvMuMu.nDispVtxs;
    (*eventvariables)["vtxMuMuXInMaterial"] = dvMuMu.vtxX;
    (*eventvariables)["vtxMuMuYInMaterial"] = dvMuMu.vtxY;
    (*eventvariables)["vtxMuMuZInMaterial"] = dvMuMu.vtxZ;
    (*eventvariables)["vtxMuMuXErrInMaterial"] = dvMuMu.vtxXErr;
    (*eventvariables)["vtxMuMuYErrInMaterial"] = dvMuMu.vtxYErr;
    (*eventvariables)["vtxMuMuZErrInMaterial"] = dvMuMu.vtxZErr;
    (*eventvariables)["vtxMuMuChisqInMaterial"] = dvMuMu.vtxChisq;
  }
  else (*eventvariables)["nDispMuMuVtxsInMaterial"] = 0;
  if(dvEMu_inMaterial){
    (*eventvariables)["nDispEMuVtxsInMaterial"] = dvEMu.nDispVtxs;
    (*eventvariables)["vtxEMuXInMaterial"] = dvEMu.vtxX;
    (*eventvariables)["vtxEMuYInMaterial"] = dvEMu.vtxY;
    (*eventvariables)["vtxEMuZInMaterial"] = dvEMu.vtxZ;
    (*eventvariables)["vtxEMuXErrInMaterial"] = dvEMu.vtxXErr;
    (*eventvariables)["vtxEMuYErrInMaterial"] = dvEMu.vtxYErr;
    (*eventvariables)["vtxEMuZErrInMaterial"] = dvEMu.vtxZErr;
    (*eventvariables)["vtxEMuChisqInMaterial"] = dvEMu.vtxChisq;
  }
  else (*eventvariables)["nDispEMuVtxsInMaterial"] = 0;

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

DispVtx DisplacedSUSYEventVariableProducer::getDispVtx(vector<reco::TransientTrack> t_tks){

  DispVtx DV;

  if (t_tks.size() == 2){
    //std::cout<<"2 good tracks, trying to make a vertex"<<std::endl;
    KalmanVertexFitter kvf;
    TransientVertex tv = kvf.vertex(t_tks);

    if (tv.isValid()){
      DV.nDispVtxs++;
      reco::Vertex vtx = tv;
      //GlobalPoint vtxPos = vtx.position();
      DV.vtxX     = vtx.x();
      DV.vtxY     = vtx.y();
      DV.vtxZ     = vtx.z();
      DV.vtxXErr  = vtx.xError();
      DV.vtxYErr  = vtx.yError();
      DV.vtxZErr  = vtx.zError();
      DV.vtxChisq = vtx.normalizedChi2();
    }
  }
  //if(DV.vtxChisq!=-5000.) std::cout<<"vertex x/y/z/chisq is: "<<DV.vtxX<<"/"<<DV.vtxY<<"/"<<DV.vtxZ<<"/"<<DV.vtxChisq<<std::endl;

  return DV;
}

bool DisplacedSUSYEventVariableProducer::inRectangle(double x_center, double y_center, double r, double x, double y) {
  return x > x_center - r && x < x_center + r &&
    y > y_center - r && y < y_center + r;
}

bool DisplacedSUSYEventVariableProducer::inRectangle(double x_min, double x_max, double y_min, double y_max, double x, double y) {
  return x > x_min && x < x_max &&
    y > y_min && y < y_max;
}

bool DisplacedSUSYEventVariableProducer::inCircle(double x_center, double y_center, double r, double x, double y) {
  double dx = x_center - x;
  double dy = y_center - y;
  double square_dist = dx*dx + dy*dy;
  return (square_dist < r*r);
}

bool DisplacedSUSYEventVariableProducer::inEllipse(double x_center, double y_center, double rX, double rY, double x, double y) {
  double dx = x_center - x;
  double dy = y_center - y;
  double dist = 1.0*dx*dx/(rX*rX) + 1.0*dy*dy/(rY*rY);
  return (dist < 1.0);
}

bool DisplacedSUSYEventVariableProducer::inMaterial(double vX, double vY, double vZ) {

  //Bpix layer 4 and Fpix disk 3 only exist in Phase 1 detector (2017 and 2018)
  bool inBpixL4, inFpixD3;
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
  inBpixL4 = inCircle(bpix_x_center_, bpix_y_center_, bpixL4_outerR_, vX, vY)
    && !inCircle(bpix_x_center_, bpix_y_center_, bpixL4_innerR_, vX, vY);
  inFpixD3 = ((vZ > fpix_z_center_ + fpixD3_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ + fpixD3_z_center_ + fpix_z_halfThickness_)) ||
    ((vZ > fpix_z_center_ - fpixD3_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ - fpixD3_z_center_ + fpix_z_halfThickness_));
#else
  inBpixL4 = false;
  inFpixD3 = false;
#endif

  //see if vertices are within each piece of tracker material:
  //in beam pipe: is vertex btw inner and outer circles (thickness) of beam pipe radius (x and y)? vertex can have any z
  if(inCircle(beamPipe_x_center_, beamPipe_y_center_, beamPipe_outerR_, vX, vY)
     && !inCircle(beamPipe_x_center_, beamPipe_y_center_, beamPipe_innerR_, vX, vY))
    return true;

  //in BPIX inner shield: is vertex in BPIX z range? is vertex btw inner and outer circles (thickness) of inner shield (x and y)?
  //near half-circle: positive x
  //far half-circle: negative x
  //assume no gap between two half-circles
  else if(((vZ > bpix_z_center_ - bpix_z_halfLength_) && (vZ < bpix_z_center_ + bpix_z_halfLength_)) &&
	  ((vX > 0. && inCircle(nearInnerShield_x_center_, nearInnerShield_y_center_, innerShield_outerR_, vX, vY) &&
	    !inCircle(nearInnerShield_x_center_, nearInnerShield_y_center_, innerShield_innerR_, vX, vY)) ||
	   (vX < 0. && inCircle(farInnerShield_x_center_, farInnerShield_y_center_, innerShield_outerR_, vX, vY) &&
	    !inCircle(farInnerShield_x_center_, farInnerShield_y_center_, innerShield_innerR_, vX, vY))))
    return true;

  //in BPIX layers: is vertex in BPIX z range? is vertex btw inner and outer circles (thickness) of BPIX layers?
  else if(((vZ > bpix_z_center_ - bpix_z_halfLength_) && (vZ < bpix_z_center_ + bpix_z_halfLength_)) &&
	  ((inCircle(bpix_x_center_, bpix_y_center_, bpixL1_outerR_, vX, vY)
	    && !inCircle(bpix_x_center_, bpix_y_center_, bpixL1_innerR_, vX, vY)) ||
	   (inCircle(bpix_x_center_, bpix_y_center_, bpixL2_outerR_, vX, vY)
	    && !inCircle(bpix_x_center_, bpix_y_center_, bpixL2_innerR_, vX, vY)) ||
	   (inCircle(bpix_x_center_, bpix_y_center_, bpixL3_outerR_, vX, vY)
	    && !inCircle(bpix_x_center_, bpix_y_center_, bpixL3_innerR_, vX, vY)) ||
	   inBpixL4))
    return true;

  //in FPIX disks: is vertex btw inner and outer circles of FPIX radii (x and y)? is vertex within FPIX disk thicknesses in z? (pos and neg side disks)
  else if((inCircle(fpix_x_center_, fpix_y_center_, fpix_outerR_, vX, vY)
	   && !inCircle(fpix_x_center_, fpix_y_center_, fpix_innerR_, vX, vY)) &&
	  (((vZ > fpix_z_center_ + fpixD1_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ + fpixD1_z_center_ + fpix_z_halfThickness_)) ||
	   ((vZ > fpix_z_center_ - fpixD1_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ - fpixD1_z_center_ + fpix_z_halfThickness_)) ||
	   ((vZ > fpix_z_center_ + fpixD2_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ + fpixD2_z_center_ + fpix_z_halfThickness_)) ||
	   ((vZ > fpix_z_center_ - fpixD2_z_center_ - fpix_z_halfThickness_) && (vZ < fpix_z_center_ - fpixD2_z_center_ + fpix_z_halfThickness_)) ||
	   inFpixD3))
    return true;

  //BPIX outer shield?

  //in pixel support tube: is vertex btw inner and outer ellipses (thickness) of pixel support tube radius (x and y)? vertex can have any z
  else if(inEllipse(supportTube_x_center_, supportTube_y_center_, supportTube_outerRX_, supportTube_outerRY_, vX, vY)
	  && !inEllipse(supportTube_x_center_, supportTube_y_center_, supportTube_innerRX_, supportTube_innerRY_, vX, vY))
    return true;

  //BPIX support rails?

  else return false;
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

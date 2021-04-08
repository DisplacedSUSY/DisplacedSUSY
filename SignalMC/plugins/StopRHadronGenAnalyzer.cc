//makes plots at gen level for stops WITHOUT cloud model turned on and decay done in pythia

#include "DisplacedSUSY/SignalMC/plugins/StopRHadronGenAnalyzer.h"

StopRHadronGenAnalyzer::StopRHadronGenAnalyzer(const edm::ParameterSet &cfg) :
  //tracks_                    (cfg.getParameter<edm::InputTag>("tracks")),
  genParticles_              (cfg.getParameter<edm::InputTag>("genParticles"))
//cutPythia8Flag_            (cfg.getUntrackedParameter<bool>("cutPythia8Flag", false))
{
  TH1::SetDefaultSumw2();
  oneDHists_["nStops"] = fs_->make<TH1D>("nStops", ";number of stops", 5, -0.5, 4.5);
  oneDHists_["genCharge"] = fs_->make<TH1D>("genCharge", ";generator stop charge", 3, -1.5, 1.5);
  oneDHists_["genMass"] = fs_->make<TH1D>("genMass", ";generator stop mass [GeV]", 1000, -0.5, 999.5);
  oneDHists_["genPt"] = fs_->make<TH1D>("genPt", ";generator stop p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genPhi"] = fs_->make<TH1D>("genPhi", ";generator stop #phi", 100, -3.2, 3.2);
  oneDHists_["genEta"] = fs_->make<TH1D>("genEta", ";generator stop #eta", 100, -5.0, 5.0);
  oneDHists_["genP"] = fs_->make<TH1D>("genP", ";generator stop p [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genBeta"] = fs_->make<TH1D>("genBeta", ";generator stop #beta", 500, 0.0, 1.0);
  oneDHists_["genGamma"] = fs_->make<TH1D>("genGamma", ";generator stop #gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGamma"] = fs_->make<TH1D>("genBetaGamma", ";generator stop #beta#gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGammaM"] = fs_->make<TH1D>("genBetaGammaM", ";generator stop #beta#gammam [GeV]", 500, 0.0, 1000.0);

  oneDHists_["genDecayLength_10"] = fs_->make<TH1D>("genDecayLength_10", ";generator stop decay length [cm]", 1000, 0.0, 10.0);
  oneDHists_["genDecayLength_100"] = fs_->make<TH1D>("genDecayLength_100", ";generator stop decay length [cm]", 1000, 0.0, 100.0);
  oneDHists_["genDecayLength_1000"] = fs_->make<TH1D>("genDecayLength_1000", ";generator stop decay length [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genDecayLength_10000"] = fs_->make<TH1D>("genDecayLength_10000", ";generator stop decay length [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genDecayLength_100000"] = fs_->make<TH1D>("genDecayLength_100000", ";generator stop decay length [cm]", 1000, 0.0, 100000.0);

  oneDHists_["genCTau_10"] = fs_->make<TH1D>("genCTau_10", ";generator stop c#tau [cm]", 1000, 0.0, 10.0);
  oneDHists_["genCTau_100"] = fs_->make<TH1D>("genCTau_100", ";generator stop c#tau [cm]", 1000, 0.0, 100.0);
  oneDHists_["genCTau_1000"] = fs_->make<TH1D>("genCTau_1000", ";generator stop c#tau [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genCTau_10000"] = fs_->make<TH1D>("genCTau_10000", ";generator stop c#tau [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genCTau_100000"] = fs_->make<TH1D>("genCTau_100000", ";generator stop c#tau [cm]", 1000, 0.0, 100000.0);

  oneDHists_["genRhadronId_10006XX"] = fs_->make<TH1D>("genRhadronId_10006XX", ";generator r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["genRhadronId_1006XXX"] = fs_->make<TH1D>("genRhadronId_1006XXX", ";generator r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["nStopDaughters"] = fs_->make<TH1D>("nStopDaughters", ";number of initial stop r-hadron daughters", 5, -0.5, 4.5);
  oneDHists_["stopDaughterId"] = fs_->make<TH1D>("stopDaughterId", ";stop r-hadron daughter |pdgid|",20,0,20);

  oneDHists_["genElectronPt"] = fs_->make<TH1D>("genElectronPt", ";gen electron p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["genElectronP"] = fs_->make<TH1D>("genElectronP", ";gen electron p [GeV]", 200, 0, 2000);
  oneDHists_["genElectronEta"] = fs_->make<TH1D>("genElectronEta", ";gen electron #eta", 100, -5.0, 5.0);
  oneDHists_["genElectronPhi"] = fs_->make<TH1D>("genElectronPhi", ";gen electron #phi", 100, -3.2, 3.2);
  oneDHists_["genElectronStatus"] = fs_->make<TH1D>("genElectronStatus", ";gen electron status",10, -0.5, 9.5);
  oneDHists_["genElectronAbsD0_100um"] = fs_->make<TH1D>("genElectronAbsD0_100um", ";gen electron |d0|", 100, 0, 100);
  oneDHists_["genElectronAbsD0_1000um"] = fs_->make<TH1D>("genElectronAbsD0_1000um", ";gen electron |d0|", 100, 0, 1000);
  oneDHists_["genElectronAbsD0_10000um"] = fs_->make<TH1D>("genElectronAbsD0_10000um", ";gen electron |d0|", 100, 0, 10000);
  oneDHists_["genElectronAbsD0_100000um"] = fs_->make<TH1D>("genElectronAbsD0_100000um", ";gen electron |d0|", 1000, 0, 100000);
  oneDHists_["genRHadron_genElectron_deltaEta"] = fs_->make<TH1D>("genRHadron_genElectron_deltaEta", ";|#Delta#eta(r-hadron, daughter electron)|",60,0,6);
  oneDHists_["genRHadron_genElectron_deltaPhi"] = fs_->make<TH1D>("genRHadron_genElectron_deltaPhi", ";|#Delta#phi(r-hadron, daughter electron)|",32, 0, 3.2);
  oneDHists_["genRHadron_genElectron_deltaR"] = fs_->make<TH1D>("genRHadron_genElectron_deltaR", ";#DeltaR(r-hadron, daughter electron)",60,0,6);

  oneDHists_["genMuonPt"] = fs_->make<TH1D>("genMuonPt", ";gen muon p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["genMuonP"] = fs_->make<TH1D>("genMuonP", ";gen muon p [GeV]", 200, 0, 2000);
  oneDHists_["genMuonEta"] = fs_->make<TH1D>("genMuonEta", ";gen muon #eta", 100, -5.0, 5.0);
  oneDHists_["genMuonPhi"] = fs_->make<TH1D>("genMuonPhi", ";gen muon #phi", 100, -3.2, 3.2);
  oneDHists_["genMuonStatus"] = fs_->make<TH1D>("genMuonStatus", ";gen muon status",10, -0.5, 9.5);
  oneDHists_["genMuonAbsD0_100um"] = fs_->make<TH1D>("genMuonAbsD0_100um", ";gen muon |d0|", 100, 0, 100);
  oneDHists_["genMuonAbsD0_1000um"] = fs_->make<TH1D>("genMuonAbsD0_1000um", ";gen muon |d0|", 100, 0, 1000);
  oneDHists_["genMuonAbsD0_10000um"] = fs_->make<TH1D>("genMuonAbsD0_10000um", ";gen muon |d0|", 100, 0, 10000);
  oneDHists_["genMuonAbsD0_100000um"] = fs_->make<TH1D>("genMuonAbsD0_100000um", ";gen muon |d0|", 1000, 0, 100000);
  oneDHists_["genRHadron_genMuon_deltaEta"] = fs_->make<TH1D>("genRHadron_genMuon_deltaEta", ";|#Delta#eta(r-hadron, daughter muon)|",60,0,6);
  oneDHists_["genRHadron_genMuon_deltaPhi"] = fs_->make<TH1D>("genRHadron_genMuon_deltaPhi", ";|#Delta#phi(r-hadron, daughter muon)|",32, 0, 3.2);
  oneDHists_["genRHadron_genMuon_deltaR"] = fs_->make<TH1D>("genRHadron_genMuon_deltaR", ";#DeltaR(r-hadron, daughter muon)",60,0,6);

  /*
  oneDHists_["matchedTrack"] = fs_->make<TH1D>("matchedTrack", ";matched track found", 2, -0.5, 1.5);
  oneDHists_["charge"] = fs_->make<TH1D>("charge", ";track charge", 3, -1.5, 1.5);
  oneDHists_["pt"] = fs_->make<TH1D>("pt", ";track p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["phi"] = fs_->make<TH1D>("phi", ";track #phi", 100, -3.2, 3.2);
  oneDHists_["eta"] = fs_->make<TH1D>("eta", ";track #eta", 100, -5.0, 5.0);

  oneDHists_["numberOfValidHits"] = fs_->make<TH1D>("numberOfValidHits", ";track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["numberOfMissingInnerHits"] = fs_->make<TH1D>("numberOfMissingInnerHits", ";track number of missing inner hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingMiddleHits"] = fs_->make<TH1D>("numberOfMissingMiddleHits", ";track number of missing middle hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingOuterHits"] = fs_->make<TH1D>("numberOfMissingOuterHits", ";track number of missing outer hits", 20, -0.5, 19.5);

  tracksToken_         = consumes<vector<reco::Track> >          (tracks_);
  */
  genParticlesToken_   = consumes<vector<reco::GenParticle> >    (genParticles_);

}

StopRHadronGenAnalyzer::~StopRHadronGenAnalyzer()
{
}

void
StopRHadronGenAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
  //edm::Handle<vector<reco::Track> > tracks;
  //event.getByToken(tracksToken_, tracks);

  //////////////////////////////////////////////////////////

  //gen particles
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken(genParticlesToken_, genParticles);

  //loop over gen particles
  //to find generated stop r-hadrons from pythia
  unsigned nStops = 0;
  int genRhadronId_0 = 0;
  int genRhadronId_1 = 0;

  for(const auto &genParticle : *genParticles) {
    //if decay is done in pythia:
    //find stops (the magic ones that are both first and last copy, which are the ones that appear AFTER the r-hadrons in the decay chain)
    if(abs(genParticle.pdgId()) != 1000006) continue;
    if(!genParticle.isLastCopy()) continue;
    if(!genParticle.statusFlags().isFirstCopy()) continue;

    nStops++;

    TVector3 x(genParticle.vx(), genParticle.vy(), genParticle.vz()),
      y(0.0, 0.0, 0.0);
    double boost = 1.0 /(genParticle.p4().Beta() * genParticle.p4().Gamma());
    getEndVertex(genParticle, y);

    oneDHists_.at("genCharge")->Fill(genParticle.charge());
    oneDHists_.at("genMass")->Fill(genParticle.mass());
    oneDHists_.at("genPt")->Fill(genParticle.pt());
    oneDHists_.at("genPhi")->Fill(genParticle.phi());
    oneDHists_.at("genEta")->Fill(genParticle.eta());
    oneDHists_.at("genP")->Fill(genParticle.p());
    oneDHists_.at("genBeta")->Fill(genParticle.p4().Beta());
    oneDHists_.at("genGamma")->Fill(genParticle.p4().Gamma());
    oneDHists_.at("genBetaGamma")->Fill(genParticle.p4().Beta() * genParticle.p4().Gamma());
    oneDHists_.at("genBetaGammaM")->Fill(genParticle.p4().Beta() * genParticle.p4().Gamma() * genParticle.mass());

    oneDHists_.at("genDecayLength_10")->Fill((x - y).Mag());
    oneDHists_.at("genDecayLength_100")->Fill((x - y).Mag());
    oneDHists_.at("genDecayLength_1000")->Fill((x - y).Mag());
    oneDHists_.at("genDecayLength_10000")->Fill((x - y).Mag());
    oneDHists_.at("genDecayLength_100000")->Fill((x - y).Mag());

    oneDHists_.at("genCTau_10")->Fill((x - y).Mag() * boost);
    oneDHists_.at("genCTau_100")->Fill((x - y).Mag() * boost);
    oneDHists_.at("genCTau_1000")->Fill((x - y).Mag() * boost);
    oneDHists_.at("genCTau_10000")->Fill((x - y).Mag() * boost);
    oneDHists_.at("genCTau_100000")->Fill((x - y).Mag() * boost);

    LogDebug("StopRHadronGenAnalyzer")<<" stop has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status();
    //std::cout<<" stop has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status()<<std::endl;
    /*
      if(genParticle.pt() < 10.0)
      {
      oneDHists_.at("matchedTrack")->Fill(-1.0);
      continue;
      }

      const reco::Track *track = getMatchedTrack(genParticle, tracks);

      if(track)
        {
          oneDHists_.at("matchedTrack")->Fill(1.0);
          oneDHists_.at("charge")->Fill(track->charge());
          oneDHists_.at("pt")->Fill(track->pt());
          oneDHists_.at("phi")->Fill(track->phi());
          oneDHists_.at("eta")->Fill(track->eta());

          oneDHists_.at("numberOfValidHits")->Fill(track->numberOfValidHits());
          oneDHists_.at("numberOfMissingInnerHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
          oneDHists_.at("numberOfMissingMiddleHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
          oneDHists_.at("numberOfMissingOuterHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
        }
      else {
        oneDHists_.at("matchedTrack")->Fill(0.0);
      }
    */

    //if decay done in pythia, find r-hadron mother particle
    const reco::Candidate* mother = genParticle.mother();
    int partId = mother->pdgId();

    if( (abs(partId)>1000600 && abs(partId)<1000700) || (abs(partId)>1006000 && abs(partId)<1007000)){ //if mother of stop is stop r-hadron
      LogDebug("StopRHadronGenAnalyzer")<<"gen stop mother is a gen r-hadron with id "<<partId<<", eta is: "<<mother->eta()<<", phi is: "<<mother->phi()<<", status is: "<<genParticle.status();
      //std::cout<<" stop mother is a gen r-hadron with id "<<partId<<", pt is: "<<mother->pt()<<", eta is: "<<mother->eta()<<", phi is: "<<mother->phi()<<", status is: "<<genParticle.status()<<std::endl;
      if(genRhadronId_0==0 && genRhadronId_1==0){
	genRhadronId_0 = partId;
      }
      else if(genRhadronId_0!=0 && genRhadronId_1==0){
	genRhadronId_1 = partId;
      }
      else edm::LogInfo("StopRHadronGenAnalyzer")<<"you have a third gen r-hadron??";

    }
    else edm::LogInfo("StopRHadronGenAnalyzer")<<"stop has no gen r-hadron mother!!!";


    oneDHists_.at("nStopDaughters")->Fill(genParticle.numberOfDaughters());

    //find stop daughter particles (from pythia)
    for(size_t j=0; j<genParticle.numberOfDaughters(); j++){
      const reco::Candidate* daughter = genParticle.daughter(j);
      int daughterId = daughter->pdgId();
      double daughterPt = daughter->pt();
      double daughterP = daughter->p();
      double daughterEta = daughter->eta();
      double daughterPhi = daughter->phi();
      int daughterStatus = daughter->status();
      double daughterAbsD0 = 10000*abs((-(daughter->vx())*daughter->py() + daughter->vy()*daughter->px())/daughterPt);

      oneDHists_.at("stopDaughterId")->Fill(abs(daughterId));

      LogDebug("StopRHadronGenAnalyzer")<<"stop daughter "<<daughterId<<" has pt/eta/phi/status of "<<daughterPt<<"/"<<daughterEta<<"/"<<daughterPhi<<"/"<<daughterStatus;
      //std::cout<<"stop daughter "<<daughterId<<" has pt/eta/phi/status of "<<daughterPt<<"/"<<daughterEta<<"/"<<daughterPhi<<"/"<<daughterStatus<<std::endl;

      if(abs(daughterId)==5){ //if b-quark, does it decay?
	for(size_t k=0; k<daughter->numberOfDaughters(); k++){
	  const reco::Candidate* bQuarkDaughter = daughter->daughter(k);
	  LogDebug("StopRHadronGenAnalyzer")<<"b-quark daughter is: "<<bQuarkDaughter->pdgId()<<" with status "<<bQuarkDaughter->status();
	  //std::cout<<"b-quark daughter is: "<<bQuarkDaughter->pdgId()<<" with status "<<bQuarkDaughter->status()<<std::endl;
	}
      }
      else if(abs(daughterId)==15){ //if tau, does it decay?
	for(size_t k=0; k<daughter->numberOfDaughters(); k++){
	  const reco::Candidate* tauDaughter = daughter->daughter(k);
	  LogDebug("StopRHadronGenAnalyzer")<<"tau daughter "<<tauDaughter->pdgId()<<" has pt/eta/phi/status of "<<tauDaughter->pt()<<"/"<<tauDaughter->eta()<<"/"<<tauDaughter->phi()<<"/"<<tauDaughter->status();
	  //std::cout<<"tau daughter "<<tauDaughter->pdgId()<<" has pt/eta/phi/status of "<<tauDaughter->pt()<<"/"<<tauDaughter->eta()<<"/"<<tauDaughter->phi()<<"/"<<tauDaughter->status()<<std::endl;
	}
      }

      //fill hists when daughter of r-hadron is electron
      else if(abs(daughterId)==11){
	oneDHists_.at("genElectronPt")->Fill(daughterPt);
	oneDHists_.at("genElectronP")->Fill(daughterP);
	oneDHists_.at("genElectronEta")->Fill(daughterEta);
	oneDHists_.at("genElectronPhi")->Fill(daughterPhi);
	oneDHists_.at("genElectronStatus")->Fill(daughterStatus);
	oneDHists_.at("genElectronAbsD0_100um")->Fill(daughterAbsD0);
	oneDHists_.at("genElectronAbsD0_1000um")->Fill(daughterAbsD0);
	oneDHists_.at("genElectronAbsD0_10000um")->Fill(daughterAbsD0);
	oneDHists_.at("genElectronAbsD0_100000um")->Fill(daughterAbsD0);

	oneDHists_.at("genRHadron_genElectron_deltaEta")->Fill(abs(mother->eta()-daughterEta));
	oneDHists_.at("genRHadron_genElectron_deltaPhi")->Fill(abs(mother->phi()-daughterPhi));
	oneDHists_.at("genRHadron_genElectron_deltaR")->Fill(deltaR(mother->eta(),mother->phi(),daughterEta,daughterPhi));
      }

      //fill hists when daughter of r-hadron is muon
      else if(abs(daughterId)==13){
	oneDHists_.at("genMuonPt")->Fill(daughterPt);
	oneDHists_.at("genMuonP")->Fill(daughterP);
	oneDHists_.at("genMuonEta")->Fill(daughterEta);
	oneDHists_.at("genMuonPhi")->Fill(daughterPhi);
	oneDHists_.at("genMuonStatus")->Fill(daughterStatus);
	oneDHists_.at("genMuonAbsD0_100um")->Fill(daughterAbsD0);
	oneDHists_.at("genMuonAbsD0_1000um")->Fill(daughterAbsD0);
	oneDHists_.at("genMuonAbsD0_10000um")->Fill(daughterAbsD0);
	oneDHists_.at("genMuonAbsD0_100000um")->Fill(daughterAbsD0);

	oneDHists_.at("genRHadron_genMuon_deltaEta")->Fill(abs(mother->eta()-daughterEta));
	oneDHists_.at("genRHadron_genMuon_deltaPhi")->Fill(abs(mother->phi()-daughterPhi));
	oneDHists_.at("genRHadron_genMuon_deltaR")->Fill(deltaR(mother->eta(),mother->phi(),daughterEta,daughterPhi));
      }

    } //end loop over daughters
  }//end loop over gen particles

  oneDHists_.at("nStops")->Fill(nStops);
  if(!nStops) edm::LogInfo("StopRHadronGenAnalyzer") << "[" << event.id() << "] No stops found!";

  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_1));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_1));

}//end analyze


void StopRHadronGenAnalyzer::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
{
  if(!genParticle.numberOfDaughters())
    y.SetXYZ(99999.0, 99999.0, 99999.0);
  else
    for(const auto &daughter : genParticle)
      {
        if(abs(daughter.pdgId()) != 1000022)
          continue;

        y.SetXYZ(daughter.vx(), daughter.vy(), daughter.vz());
        break;
      }
}

/*
const reco::Track * StopRHadronGenAnalyzer::getMatchedTrack(const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Track> > &tracks) const
{
  const reco::Track *matchedTrack = NULL;
  double minDR = -1.0;
  int i = -1;
  for(const auto &track : *tracks) {
    i++;
    if(track.pt() < 10.0) continue;
    const double dR = deltaR(genParticle, track);
    if(dR > 0.1) continue;
    if(!matchedTrack || dR < minDR) {
      matchedTrack = &(tracks->at(i));
      minDR = dR;
    }
  }

  return matchedTrack;
}
*/

DEFINE_FWK_MODULE(StopRHadronGenAnalyzer);

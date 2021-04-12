//makes plots at gen level for stops WITHOUT cloud model turned on and decay done in pythia
//matches the gen electrons and muons from the decay to pat electrons and muons, and makes plots of those

#include "DisplacedSUSY/SignalMC/plugins/StopRHadronGenAnalyzer.h"

StopRHadronGenAnalyzer::StopRHadronGenAnalyzer(const edm::ParameterSet &cfg) :
  electrons_                 (cfg.getParameter<edm::InputTag>("electrons")),
  muons_                     (cfg.getParameter<edm::InputTag>("muons")),
  beamspots_                 (cfg.getParameter<edm::InputTag>("beamspots")),
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
  oneDHists_["genElectronAbsD0_100um"] = fs_->make<TH1D>("genElectronAbsD0_100um", ";gen electron |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["genElectronAbsD0_1000um"] = fs_->make<TH1D>("genElectronAbsD0_1000um", ";gen electron |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["genElectronAbsD0_10000um"] = fs_->make<TH1D>("genElectronAbsD0_10000um", ";gen electron |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["genElectronAbsD0_100000um"] = fs_->make<TH1D>("genElectronAbsD0_100000um", ";gen electron |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_genElectron_deltaEta"] = fs_->make<TH1D>("genRHadron_genElectron_deltaEta", ";|#Delta#eta(r-hadron, daughter electron)|",60,0,6);
  oneDHists_["genRHadron_genElectron_deltaPhi"] = fs_->make<TH1D>("genRHadron_genElectron_deltaPhi", ";|#Delta#phi(r-hadron, daughter electron)|",32, 0, 3.2);
  oneDHists_["genRHadron_genElectron_deltaR"] = fs_->make<TH1D>("genRHadron_genElectron_deltaR", ";#DeltaR(r-hadron, daughter electron)",60,0,6);

  oneDHists_["genMuonPt"] = fs_->make<TH1D>("genMuonPt", ";gen muon p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["genMuonP"] = fs_->make<TH1D>("genMuonP", ";gen muon p [GeV]", 200, 0, 2000);
  oneDHists_["genMuonEta"] = fs_->make<TH1D>("genMuonEta", ";gen muon #eta", 100, -5.0, 5.0);
  oneDHists_["genMuonPhi"] = fs_->make<TH1D>("genMuonPhi", ";gen muon #phi", 100, -3.2, 3.2);
  oneDHists_["genMuonStatus"] = fs_->make<TH1D>("genMuonStatus", ";gen muon status",10, -0.5, 9.5);
  oneDHists_["genMuonAbsD0_100um"] = fs_->make<TH1D>("genMuonAbsD0_100um", ";gen muon |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["genMuonAbsD0_1000um"] = fs_->make<TH1D>("genMuonAbsD0_1000um", ";gen muon |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["genMuonAbsD0_10000um"] = fs_->make<TH1D>("genMuonAbsD0_10000um", ";gen muon |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["genMuonAbsD0_100000um"] = fs_->make<TH1D>("genMuonAbsD0_100000um", ";gen muon |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_genMuon_deltaEta"] = fs_->make<TH1D>("genRHadron_genMuon_deltaEta", ";|#Delta#eta(r-hadron, daughter muon)|",60,0,6);
  oneDHists_["genRHadron_genMuon_deltaPhi"] = fs_->make<TH1D>("genRHadron_genMuon_deltaPhi", ";|#Delta#phi(r-hadron, daughter muon)|",32, 0, 3.2);
  oneDHists_["genRHadron_genMuon_deltaR"] = fs_->make<TH1D>("genRHadron_genMuon_deltaR", ";#DeltaR(r-hadron, daughter muon)",60,0,6);

  oneDHists_["matchedElectron"] = fs_->make<TH1D>("matchedElectron", ";matched electron found", 2, -0.5, 1.5);
  oneDHists_["electronPt"] = fs_->make<TH1D>("electronPt", ";electron p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["electronP"] = fs_->make<TH1D>("electronP", ";electron p [GeV]", 200, 0, 2000);
  oneDHists_["electronEta"] = fs_->make<TH1D>("electronEta", ";electron #eta", 100, -5.0, 5.0);
  oneDHists_["electronPhi"] = fs_->make<TH1D>("electronPhi", ";electron #phi", 100, -3.2, 3.2);
  oneDHists_["electronCharge"] = fs_->make<TH1D>("electronCharge", ";electron charge", 3, -1.5, 1.5);
  oneDHists_["electronNumberOfValidHits"] = fs_->make<TH1D>("electronNumberOfValidHits", ";electron number of valid hits", 100, -0.5, 99.5);
  oneDHists_["electronNumberOfValidPixelHits"] = fs_->make<TH1D>("electronNumberOfValidPixelHits", ";electron number of valid pixel hits", 10, -0.5, 9.5);
  oneDHists_["electronAbsD0_100um"] = fs_->make<TH1D>("electronAbsD0_100um", ";electron |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["electronAbsD0_1000um"] = fs_->make<TH1D>("electronAbsD0_1000um", ";electron |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["electronAbsD0_10000um"] = fs_->make<TH1D>("electronAbsD0_10000um", ";electron |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["electronAbsD0_100000um"] = fs_->make<TH1D>("electronAbsD0_100000um", ";electron |d_{0}| [#mum]", 1000, 0, 100000);

  oneDHists_["matchedMuon"] = fs_->make<TH1D>("matchedMuon", ";matched muon found", 2, -0.5, 1.5);
  oneDHists_["muonPt"] = fs_->make<TH1D>("muonPt", ";muon p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["muonP"] = fs_->make<TH1D>("muonP", ";muon p [GeV]", 200, 0, 2000);
  oneDHists_["muonEta"] = fs_->make<TH1D>("muonEta", ";muon #eta", 100, -5.0, 5.0);
  oneDHists_["muonPhi"] = fs_->make<TH1D>("muonPhi", ";muon #phi", 100, -3.2, 3.2);
  oneDHists_["muonCharge"] = fs_->make<TH1D>("muonCharge", ";muon charge", 3, -1.5, 1.5);
  oneDHists_["muonNumberOfValidHits"] = fs_->make<TH1D>("muonNumberOfValidHits", ";muon number of valid hits", 100, -0.5, 99.5);
  oneDHists_["muonNumberOfValidPixelHits"] = fs_->make<TH1D>("muonNumberOfValidPixelHits", ";muon number of valid pixel hits", 10, -0.5, 9.5);
  oneDHists_["muonIsGlobal"] = fs_->make<TH1D>("muonIsGlobal", ";muon is global", 2, -0.5, 1.5);
  oneDHists_["muonIsPF"] = fs_->make<TH1D>("muonIsPF", ";muon is PF", 2, -0.5, 1.5);
  oneDHists_["muonAbsD0_100um"] = fs_->make<TH1D>("muonAbsD0_100um", ";muon |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["muonAbsD0_1000um"] = fs_->make<TH1D>("muonAbsD0_1000um", ";muon |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["muonAbsD0_10000um"] = fs_->make<TH1D>("muonAbsD0_10000um", ";muon |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["muonAbsD0_100000um"] = fs_->make<TH1D>("muonAbsD0_100000um", ";muon |d_{0}| [#mum]", 1000, 0, 100000);

  electronsToken_      = consumes<vector<pat::Electron> >        (electrons_);
  muonsToken_          = consumes<vector<pat::Muon> >            (muons_);
  beamspotsToken_      = consumes<reco::BeamSpot>                (beamspots_);
  genParticlesToken_   = consumes<vector<reco::GenParticle> >    (genParticles_);

}

StopRHadronGenAnalyzer::~StopRHadronGenAnalyzer()
{
}

void
StopRHadronGenAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::Electron> > electrons;
  event.getByToken(electronsToken_, electrons);

  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken(muonsToken_, muons);

  edm::Handle<reco::BeamSpot> beamspots;
  event.getByToken(beamspotsToken_, beamspots);
  auto beamspot = *beamspots;

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

	//match gen electron to reco electron
	if(daughterPt < 10.0){
	  oneDHists_.at("matchedElectron")->Fill(-1.0);
	  continue;
	}

	const pat::Electron *electron = getMatchedElectron(*daughter, electrons);

	if(electron){
	  double electronAbsD0 = 10000*abs((-(electron->vx() - beamspot.x0())*electron->py() + (electron->vy() - beamspot.y0())*electron->px())/electron->pt());

          oneDHists_.at("matchedElectron")->Fill(1.0);
          oneDHists_.at("electronPt")->Fill(electron->pt());
          oneDHists_.at("electronP")->Fill(electron->p());
          oneDHists_.at("electronEta")->Fill(electron->eta());
          oneDHists_.at("electronPhi")->Fill(electron->phi());
          oneDHists_.at("electronCharge")->Fill(electron->charge());
          oneDHists_.at("electronNumberOfValidHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidHits());
          oneDHists_.at("electronNumberOfValidPixelHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidPixelHits());
	  oneDHists_.at("electronAbsD0_100um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_1000um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_10000um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_100000um")->Fill(electronAbsD0);
        }
	else {
	  oneDHists_.at("matchedElectron")->Fill(0.0);
	}

      } //end if daughter of r-hadron is an electron


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

	//match gen muon to reco muon
	if(daughterPt < 10.0){
	  oneDHists_.at("matchedMuon")->Fill(-1.0);
	  continue;
	}

	const pat::Muon *muon = getMatchedMuon(*daughter, muons);

	if(muon){
	  double muonAbsD0 = 10000*abs((-(muon->vx() - beamspot.x0())*muon->py() + (muon->vy() - beamspot.y0())*muon->px())/muon->pt());

          oneDHists_.at("matchedMuon")->Fill(1.0);
          oneDHists_.at("muonPt")->Fill(muon->pt());
          oneDHists_.at("muonP")->Fill(muon->p());
          oneDHists_.at("muonEta")->Fill(muon->eta());
          oneDHists_.at("muonPhi")->Fill(muon->phi());
          oneDHists_.at("muonCharge")->Fill(muon->charge());
          oneDHists_.at("muonNumberOfValidHits")->Fill(muon->numberOfValidHits());
          oneDHists_.at("muonNumberOfValidPixelHits")->Fill(muon->innerTrack()->hitPattern().numberOfValidPixelHits());
          oneDHists_.at("muonIsGlobal")->Fill(muon->isGlobalMuon());
          oneDHists_.at("muonIsPF")->Fill(muon->isPFMuon());
	  oneDHists_.at("muonAbsD0_100um")->Fill(muonAbsD0);
	  oneDHists_.at("muonAbsD0_1000um")->Fill(muonAbsD0);
	  oneDHists_.at("muonAbsD0_10000um")->Fill(muonAbsD0);
	  oneDHists_.at("muonAbsD0_100000um")->Fill(muonAbsD0);
        }
	else {
	  oneDHists_.at("matchedMuon")->Fill(0.0);
	}

      }//end if daughter of r-hadron is a muon

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


const pat::Electron * StopRHadronGenAnalyzer::getMatchedElectron(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Electron> > &electrons) const
{
  const pat::Electron *matchedElectron = NULL;
  double minDR = -1.0;
  int i = -1;
  for(const auto &electron : *electrons) {
    i++;
    if(electron.pt() < 10.0) continue;
    const double dR = deltaR(genParticle, electron);
    if(dR > 0.1) continue;
    if(!matchedElectron || dR < minDR) {
      matchedElectron = &(electrons->at(i));
      minDR = dR;
    }
  }

  return matchedElectron;
}

const pat::Muon * StopRHadronGenAnalyzer::getMatchedMuon(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Muon> > &muons) const
{
  const pat::Muon *matchedMuon = NULL;
  double minDR = -1.0;
  int i = -1;
  for(const auto &muon : *muons) {
    i++;
    if(muon.pt() < 10.0) continue;
    const double dR = deltaR(genParticle, muon);
    if(dR > 0.1) continue;
    if(!matchedMuon || dR < minDR) {
      matchedMuon = &(muons->at(i));
      minDR = dR;
    }
  }

  return matchedMuon;
}


DEFINE_FWK_MODULE(StopRHadronGenAnalyzer);

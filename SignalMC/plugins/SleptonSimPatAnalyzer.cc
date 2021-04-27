//makes plots at gen (and sim level: geantPlusGenParticles) for GMSB sleptons generated in madgraph (and things hadronized in pythia) and decay done in geant
//matches the gen electrons and muons from the decay to pat electrons and muons, and makes plots of those

#include "DisplacedSUSY/SignalMC/plugins/SleptonSimPatAnalyzer.h"

SleptonSimPatAnalyzer::SleptonSimPatAnalyzer(const edm::ParameterSet &cfg) :
  electrons_                 (cfg.getParameter<edm::InputTag>("electrons")),
  muons_                     (cfg.getParameter<edm::InputTag>("muons")),
  beamspots_                 (cfg.getParameter<edm::InputTag>("beamspots")),
  genParticles_              (cfg.getParameter<edm::InputTag>("genParticles"))
//cutPythia8Flag_            (cfg.getUntrackedParameter<bool>("cutPythia8Flag", false))
{
  TH1::SetDefaultSumw2();
  oneDHists_["nSleptons"] = fs_->make<TH1D>("nSleptons", ";number of sleptons", 5, -0.5, 4.5);
  oneDHists_["genCharge"] = fs_->make<TH1D>("genCharge", ";generator slepton charge", 3, -1.5, 1.5);
  oneDHists_["genMass"] = fs_->make<TH1D>("genMass", ";generator slepton mass [GeV]", 1000, -0.5, 999.5);
  oneDHists_["genPt"] = fs_->make<TH1D>("genPt", ";generator slepton p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genPhi"] = fs_->make<TH1D>("genPhi", ";generator slepton #phi", 100, -3.2, 3.2);
  oneDHists_["genEta"] = fs_->make<TH1D>("genEta", ";generator slepton #eta", 100, -5.0, 5.0);
  oneDHists_["genP"] = fs_->make<TH1D>("genP", ";generator slepton p [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genBeta"] = fs_->make<TH1D>("genBeta", ";generator slepton #beta", 500, 0.0, 1.0);
  oneDHists_["genGamma"] = fs_->make<TH1D>("genGamma", ";generator slepton #gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGamma"] = fs_->make<TH1D>("genBetaGamma", ";generator slepton #beta#gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGammaM"] = fs_->make<TH1D>("genBetaGammaM", ";generator slepton #beta#gammam [GeV]", 500, 0.0, 1000.0);

  oneDHists_["genDecayLength_10"] = fs_->make<TH1D>("genDecayLength_10", ";generator slepton decay length [cm]", 1000, 0.0, 10.0);
  oneDHists_["genDecayLength_100"] = fs_->make<TH1D>("genDecayLength_100", ";generator slepton decay length [cm]", 1000, 0.0, 100.0);
  oneDHists_["genDecayLength_1000"] = fs_->make<TH1D>("genDecayLength_1000", ";generator slepton decay length [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genDecayLength_10000"] = fs_->make<TH1D>("genDecayLength_10000", ";generator slepton decay length [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genDecayLength_100000"] = fs_->make<TH1D>("genDecayLength_100000", ";generator slepton decay length [cm]", 1000, 0.0, 100000.0);

  oneDHists_["genCTau_10"] = fs_->make<TH1D>("genCTau_10", ";generator slepton c#tau [cm]", 1000, 0.0, 10.0);
  oneDHists_["genCTau_100"] = fs_->make<TH1D>("genCTau_100", ";generator slepton c#tau [cm]", 1000, 0.0, 100.0);
  oneDHists_["genCTau_1000"] = fs_->make<TH1D>("genCTau_1000", ";generator slepton c#tau [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genCTau_10000"] = fs_->make<TH1D>("genCTau_10000", ";generator slepton c#tau [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genCTau_100000"] = fs_->make<TH1D>("genCTau_100000", ";generator slepton c#tau [cm]", 1000, 0.0, 100000.0);

  oneDHists_["nSleptonDaughters"] = fs_->make<TH1D>("nSleptonDaughters", ";number of slepton daughters", 5, -0.5, 4.5);

  oneDHists_["SMDaughterId"] = fs_->make<TH1D>("SMDaughterId", ";daughter |pdgid| (SM range)",20,0,20);
  oneDHists_["gravitinoDaughterId"] = fs_->make<TH1D>("gravitinoDaughterId", ";is slepton daughter a gravitino",2,0,2);

  oneDHists_["simElectronPt"] = fs_->make<TH1D>("simElectronPt", ";sim electron p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["simElectronP"] = fs_->make<TH1D>("simElectronP", ";sim electron p [GeV]", 200, 0, 2000);
  oneDHists_["simElectronEta"] = fs_->make<TH1D>("simElectronEta", ";sim electron #eta", 100, -5.0, 5.0);
  oneDHists_["simElectronPhi"] = fs_->make<TH1D>("simElectronPhi", ";sim electron #phi", 100, -3.2, 3.2);
  oneDHists_["simElectronAbsD0_100um"] = fs_->make<TH1D>("simElectronAbsD0_100um", ";sim electron |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["simElectronAbsD0_1000um"] = fs_->make<TH1D>("simElectronAbsD0_1000um", ";sim electron |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["simElectronAbsD0_10000um"] = fs_->make<TH1D>("simElectronAbsD0_10000um", ";sim electron |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["simElectronAbsD0_100000um"] = fs_->make<TH1D>("simElectronAbsD0_100000um", ";sim electron |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genSlepton_simElectron_deltaEta"] = fs_->make<TH1D>("genSlepton_simElectron_deltaEta", ";|#Delta#eta(slepton, daughter electron)|",60,0,6);
  oneDHists_["genSlepton_simElectron_deltaPhi"] = fs_->make<TH1D>("genSlepton_simElectron_deltaPhi", ";|#Delta#phi(slepton, daughter electron)|",32, 0, 3.2);
  oneDHists_["genSlepton_simElectron_deltaR"] = fs_->make<TH1D>("genSlepton_simElectron_deltaR", ";#DeltaR(slepton, daughter electron)",60,0,6);

  oneDHists_["simMuonPt"] = fs_->make<TH1D>("simMuonPt", ";sim muon p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["simMuonP"] = fs_->make<TH1D>("simMuonP", ";sim muon p [GeV]", 200, 0, 2000);
  oneDHists_["simMuonEta"] = fs_->make<TH1D>("simMuonEta", ";sim muon #eta", 100, -5.0, 5.0);
  oneDHists_["simMuonPhi"] = fs_->make<TH1D>("simMuonPhi", ";sim muon #phi", 100, -3.2, 3.2);
  oneDHists_["simMuonAbsD0_100um"] = fs_->make<TH1D>("simMuonAbsD0_100um", ";sim muon |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["simMuonAbsD0_1000um"] = fs_->make<TH1D>("simMuonAbsD0_1000um", ";sim muon |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["simMuonAbsD0_10000um"] = fs_->make<TH1D>("simMuonAbsD0_10000um", ";sim muon |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["simMuonAbsD0_100000um"] = fs_->make<TH1D>("simMuonAbsD0_100000um", ";sim muon |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genSlepton_simMuon_deltaEta"] = fs_->make<TH1D>("genSlepton_simMuon_deltaEta", ";|#Delta#eta(slepton, daughter muon)|",60,0,6);
  oneDHists_["genSlepton_simMuon_deltaPhi"] = fs_->make<TH1D>("genSlepton_simMuon_deltaPhi", ";|#Delta#phi(slepton, daughter muon)|",32, 0, 3.2);
  oneDHists_["genSlepton_simMuon_deltaR"] = fs_->make<TH1D>("genSlepton_simMuon_deltaR", ";#DeltaR(slepton, daughter muon)",60,0,6);

  oneDHists_["simTauPt"] = fs_->make<TH1D>("simTauPt", ";sim tau p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["simTauP"] = fs_->make<TH1D>("simTauP", ";sim tau p [GeV]", 200, 0, 2000);
  oneDHists_["simTauEta"] = fs_->make<TH1D>("simTauEta", ";sim tau #eta", 100, -5.0, 5.0);
  oneDHists_["simTauPhi"] = fs_->make<TH1D>("simTauPhi", ";sim tau #phi", 100, -3.2, 3.2);
  oneDHists_["simTauAbsD0_100um"] = fs_->make<TH1D>("simTauAbsD0_100um", ";sim tau |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["simTauAbsD0_1000um"] = fs_->make<TH1D>("simTauAbsD0_1000um", ";sim tau |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["simTauAbsD0_10000um"] = fs_->make<TH1D>("simTauAbsD0_10000um", ";sim tau |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["simTauAbsD0_100000um"] = fs_->make<TH1D>("simTauAbsD0_100000um", ";sim tau |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genSlepton_simTau_deltaEta"] = fs_->make<TH1D>("genSlepton_simTau_deltaEta", ";|#Delta#eta(slepton, daughter tau)|",60,0,6);
  oneDHists_["genSlepton_simTau_deltaPhi"] = fs_->make<TH1D>("genSlepton_simTau_deltaPhi", ";|#Delta#phi(slepton, daughter tau)|",32, 0, 3.2);
  oneDHists_["genSlepton_simTau_deltaR"] = fs_->make<TH1D>("genSlepton_simTau_deltaR", ";#DeltaR(slepton, daughter tau)",60,0,6);

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

SleptonSimPatAnalyzer::~SleptonSimPatAnalyzer()
{
}

void
SleptonSimPatAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
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
  //to find generated sleptons
  unsigned nSleptons = 0;
  for(const auto &genParticle : *genParticles) {
    //if decay is done in geant:
    //find sleptons that have status 1 (madgraph and pythia see sleptons as stable)
    if(! (abs(genParticle.pdgId()) == 1000011 || abs(genParticle.pdgId()) == 1000013 || abs(genParticle.pdgId()) == 1000015 || //~e_L, ~mu_L, ~tau_1
	  abs(genParticle.pdgId()) == 2000011 || abs(genParticle.pdgId()) == 2000013 || abs(genParticle.pdgId()) == 2000015))  //~e_R, ~mu_R, ~tau_2
      continue;
    if(genParticle.status() != 1) continue;

    nSleptons++;

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

    LogDebug("SleptonSimPatAnalyzer")<<" slepton has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status();
    //std::cout<<" slepton has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status()<<std::endl;

    oneDHists_.at("nSleptonDaughters")->Fill(genParticle.numberOfDaughters());

    //if decay done in geant, find daughters of sleptons
    for(size_t j=0; j<genParticle.numberOfDaughters(); j++){
      const reco::Candidate* daughter = genParticle.daughter(j);

      int partId = daughter->pdgId();
      double pt = daughter->pt();
      double p = daughter->p();
      double eta = daughter->eta();
      double phi = daughter->phi();
      double absd0 = 10000*abs((-(daughter->vx())*daughter->py() + daughter->vy()*daughter->px())/pt);

      LogDebug("SleptonSimPatAnalyzer")<<"gen slepton daughter has id "<<partId<<", eta is: "<<eta<<", phi is: "<<phi<<", status is: "<<daughter->status();
      //std::cout<<" slepton daughter has id "<<partId<<", pt is: "<<pt<<", eta is: "<<eta<<", phi is: "<<phi<<", status is: "<<daughter->status()<<std::endl;

      //fill hists for when daughter of slepton is anythng
      oneDHists_.at("SMDaughterId")->Fill(abs(partId));
      if(abs(partId)==1000039) oneDHists_.at("gravitinoDaughterId")->Fill(1);
      else oneDHists_.at("gravitinoDaughterId")->Fill(0);

      //fill hists when daughter of slepton is electron
      if(abs(partId)==11){
	oneDHists_.at("simElectronPt")->Fill(pt);
	oneDHists_.at("simElectronP")->Fill(p);
	oneDHists_.at("simElectronEta")->Fill(eta);
	oneDHists_.at("simElectronPhi")->Fill(phi);
	oneDHists_.at("simElectronAbsD0_100um")->Fill(absd0);
	oneDHists_.at("simElectronAbsD0_1000um")->Fill(absd0);
	oneDHists_.at("simElectronAbsD0_10000um")->Fill(absd0);
	oneDHists_.at("simElectronAbsD0_100000um")->Fill(absd0);

	oneDHists_.at("genSlepton_simElectron_deltaEta")->Fill(abs(genParticle.eta()-eta));
	oneDHists_.at("genSlepton_simElectron_deltaPhi")->Fill(abs(genParticle.phi()-phi));
	oneDHists_.at("genSlepton_simElectron_deltaR")->Fill(deltaR(genParticle.eta(),genParticle.phi(),eta,phi));

	//match gen electron to reco electron
	if(pt < 10.0){
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
	  if (!electron->gsfTrack().isNull()){
	    oneDHists_.at("electronNumberOfValidHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidHits());
	    oneDHists_.at("electronNumberOfValidPixelHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidPixelHits());
	  }
	  oneDHists_.at("electronAbsD0_100um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_1000um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_10000um")->Fill(electronAbsD0);
	  oneDHists_.at("electronAbsD0_100000um")->Fill(electronAbsD0);
	}
	else {
	  oneDHists_.at("matchedElectron")->Fill(0.0);
	}
      } //end of if daughter of slepton is electron

      //fill hists when daughter of slepton is muon
      else if(abs(partId)==13){
	oneDHists_.at("simMuonPt")->Fill(pt);
	oneDHists_.at("simMuonP")->Fill(p);
	oneDHists_.at("simMuonEta")->Fill(eta);
	oneDHists_.at("simMuonPhi")->Fill(phi);
	oneDHists_.at("simMuonAbsD0_100um")->Fill(absd0);
	oneDHists_.at("simMuonAbsD0_1000um")->Fill(absd0);
	oneDHists_.at("simMuonAbsD0_10000um")->Fill(absd0);
	oneDHists_.at("simMuonAbsD0_100000um")->Fill(absd0);

	oneDHists_.at("genSlepton_simMuon_deltaEta")->Fill(abs(genParticle.eta()-eta));
	oneDHists_.at("genSlepton_simMuon_deltaPhi")->Fill(abs(genParticle.phi()-phi));
	oneDHists_.at("genSlepton_simMuon_deltaR")->Fill(deltaR(genParticle.eta(),genParticle.phi(),eta,phi));

	//match gen muon to reco muon
	if(pt < 10.0){
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
	  if (!muon->innerTrack().isNull()){
	    oneDHists_.at("muonNumberOfValidPixelHits")->Fill(muon->innerTrack()->hitPattern().numberOfValidPixelHits());
	  }
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
      }//end of if slepton daughter is muon

      //fill hists when daughter of slepton is tau
      else if(abs(partId)==15){
	oneDHists_.at("simTauPt")->Fill(pt);
	oneDHists_.at("simTauP")->Fill(p);
	oneDHists_.at("simTauEta")->Fill(eta);
	oneDHists_.at("simTauPhi")->Fill(phi);
	oneDHists_.at("simTauAbsD0_100um")->Fill(absd0);
	oneDHists_.at("simTauAbsD0_1000um")->Fill(absd0);
	oneDHists_.at("simTauAbsD0_10000um")->Fill(absd0);
	oneDHists_.at("simTauAbsD0_100000um")->Fill(absd0);

	oneDHists_.at("genSlepton_simTau_deltaEta")->Fill(abs(genParticle.eta()-eta));
	oneDHists_.at("genSlepton_simTau_deltaPhi")->Fill(abs(genParticle.phi()-phi));
	oneDHists_.at("genSlepton_simTau_deltaR")->Fill(deltaR(genParticle.eta(),genParticle.phi(),eta,phi));

	for(size_t k=0; j<daughter->numberOfDaughters(); k++){
	  if(!daughter->daughter(k)) continue;
	  const reco::Candidate* daughterOfTau = daughter->daughter(k);

	  int partIdOfDaughterOfTau = daughterOfTau->pdgId();
	  double ptOfDaughterOfTau = daughterOfTau->pt();
	  double pOfDaughterOfTau = daughterOfTau->p();
	  double etaOfDaughterOfTau = daughterOfTau->eta();
	  double phiOfDaughterOfTau = daughterOfTau->phi();
	  double absd0OfDaughterOfTau = 10000*abs((-(daughterOfTau->vx())*daughterOfTau->py() + daughterOfTau->vy()*daughterOfTau->px())/ptOfDaughterOfTau);

	  //fill hists when daughter of tau is electron
	  if(abs(partIdOfDaughterOfTau)==11 && ptOfDaughterOfTau>10.){
	    oneDHists_.at("simElectronPt")->Fill(ptOfDaughterOfTau);
	    oneDHists_.at("simElectronP")->Fill(pOfDaughterOfTau);
	    oneDHists_.at("simElectronEta")->Fill(etaOfDaughterOfTau);
	    oneDHists_.at("simElectronPhi")->Fill(phiOfDaughterOfTau);
	    oneDHists_.at("simElectronAbsD0_100um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simElectronAbsD0_1000um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simElectronAbsD0_10000um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simElectronAbsD0_100000um")->Fill(absd0OfDaughterOfTau);

	    oneDHists_.at("genSlepton_simElectron_deltaEta")->Fill(abs(genParticle.eta()-etaOfDaughterOfTau));
	    oneDHists_.at("genSlepton_simElectron_deltaPhi")->Fill(abs(genParticle.phi()-phiOfDaughterOfTau));
	    oneDHists_.at("genSlepton_simElectron_deltaR")->Fill(deltaR(genParticle.eta(),genParticle.phi(),etaOfDaughterOfTau,phiOfDaughterOfTau));

	    //match gen electron to reco electron
	    if(pt < 10.0){
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
	      if (!electron->gsfTrack().isNull()){
		oneDHists_.at("electronNumberOfValidHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidHits());
		oneDHists_.at("electronNumberOfValidPixelHits")->Fill(electron->gsfTrack()->hitPattern().numberOfValidPixelHits());
	      }
	      oneDHists_.at("electronAbsD0_100um")->Fill(electronAbsD0);
	      oneDHists_.at("electronAbsD0_1000um")->Fill(electronAbsD0);
	      oneDHists_.at("electronAbsD0_10000um")->Fill(electronAbsD0);
	      oneDHists_.at("electronAbsD0_100000um")->Fill(electronAbsD0);
	    }
	    else {
	      oneDHists_.at("matchedElectron")->Fill(0.0);
	    }
	  } //end of if daughter of tau is electron

	  //fill hists when daughter of tau is muon
	  else if(abs(partIdOfDaughterOfTau)==13 && ptOfDaughterOfTau>10.){
	    oneDHists_.at("simMuonPt")->Fill(ptOfDaughterOfTau);
	    oneDHists_.at("simMuonP")->Fill(pOfDaughterOfTau);
	    oneDHists_.at("simMuonEta")->Fill(etaOfDaughterOfTau);
	    oneDHists_.at("simMuonPhi")->Fill(phiOfDaughterOfTau);
	    oneDHists_.at("simMuonAbsD0_100um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simMuonAbsD0_1000um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simMuonAbsD0_10000um")->Fill(absd0OfDaughterOfTau);
	    oneDHists_.at("simMuonAbsD0_100000um")->Fill(absd0OfDaughterOfTau);

	    oneDHists_.at("genSlepton_simMuon_deltaEta")->Fill(abs(genParticle.eta()-etaOfDaughterOfTau));
	    oneDHists_.at("genSlepton_simMuon_deltaPhi")->Fill(abs(genParticle.phi()-phiOfDaughterOfTau));
	    oneDHists_.at("genSlepton_simMuon_deltaR")->Fill(deltaR(genParticle.eta(),genParticle.phi(),etaOfDaughterOfTau,phiOfDaughterOfTau));

	    //match gen muon to reco muon
	    if(pt < 10.0){
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
	      if (!muon->innerTrack().isNull()){
		oneDHists_.at("muonNumberOfValidPixelHits")->Fill(muon->innerTrack()->hitPattern().numberOfValidPixelHits());
	      }
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
	  }//end of if daughter of tau is muon
	}//end of loop over daughters of tau
      }//end of if slepton daughter is tau

    }//end loop over daughters
  }//end loop over gen particles
  oneDHists_.at("nSleptons")->Fill(nSleptons);
  if(!nSleptons) edm::LogInfo("SleptonSimPatAnalyzer") << "[" << event.id() << "] No sleptons found!";

}//end analyze

void SleptonSimPatAnalyzer::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
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

const pat::Electron * SleptonSimPatAnalyzer::getMatchedElectron(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Electron> > &electrons) const
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

const pat::Muon * SleptonSimPatAnalyzer::getMatchedMuon(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Muon> > &muons) const
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

DEFINE_FWK_MODULE(SleptonSimPatAnalyzer);

//makes plots at gen (and sim level: geantPlusGenParticles) for stops with cloud model turned on and decay done in geant
//matches the gen electrons and muons from the decay to pat electrons and muons, and makes plots of those

#include "DisplacedSUSY/SignalMC/plugins/StopRHadronSimPatAnalyzer.h"

StopRHadronSimPatAnalyzer::StopRHadronSimPatAnalyzer(const edm::ParameterSet &cfg) :
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

  oneDHists_["nGeantDaughters"] = fs_->make<TH1D>("nGeantDaughters", ";number of initial r-hadron daughters", 5, -0.5, 4.5);

  oneDHists_["geantDaughterPt"] = fs_->make<TH1D>("geantDaughterPt", ";r-hadron daughter p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["geantDaughterP"] = fs_->make<TH1D>("geantDaughterP", ";r-hadron daughter p [GeV]", 200, 0, 2000);
  oneDHists_["geantDaughterEta"] = fs_->make<TH1D>("geantDaughterEta", ";r-hadron daughter #eta", 100, -5.0, 5.0);
  oneDHists_["geantDaughterPhi"] = fs_->make<TH1D>("geantDaughterPhi", ";r-hadron daughter #phi", 100, -3.2, 3.2);
  oneDHists_["geantDaughterStatus"] = fs_->make<TH1D>("geantDaughterStatus", ";r-hadron daughter status",10, -0.5, 9.5);
  oneDHists_["geantDaughterAbsD0_100um"] = fs_->make<TH1D>("geantDaughterAbsD0_100um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["geantDaughterAbsD0_1000um"] = fs_->make<TH1D>("geantDaughterAbsD0_1000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["geantDaughterAbsD0_10000um"] = fs_->make<TH1D>("geantDaughterAbsD0_10000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["geantDaughterAbsD0_100000um"] = fs_->make<TH1D>("geantDaughterAbsD0_100000um", ";r-hadron daughter |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_GeantDaughter_deltaEta"] = fs_->make<TH1D>("genRHadron_GeantDaughter_deltaEta", ";|#Delta#eta(r-hadron, daughter)|",60,0,6);
  oneDHists_["genRHadron_GeantDaughter_deltaPhi"] = fs_->make<TH1D>("genRHadron_GeantDaughter_deltaPhi", ";|#Delta#phi(r-hadron, daughter)|",32, 0, 3.2);
  oneDHists_["genRHadron_GeantDaughter_deltaR"] = fs_->make<TH1D>("genRHadron_GeantDaughter_deltaR", ";#DeltaR(r-hadron, daughter)",60,0,6);

  oneDHists_["SMGeantDaughterId"] = fs_->make<TH1D>("SMGeantDaughterId", ";SM r-hadron daughter |pdgid| (1st range)",20,0,20);
  oneDHists_["SMGeantDaughterPt"] = fs_->make<TH1D>("SMGeantDaughterPt", ";SM r-hadron daughter p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["SMGeantDaughterP"] = fs_->make<TH1D>("SMGeantDaughterP", ";SM r-hadron daughter p [GeV]", 200, 0, 2000);
  oneDHists_["SMGeantDaughterEta"] = fs_->make<TH1D>("SMGeantDaughterEta", ";SM r-hadron daughter #eta", 100, -5.0, 5.0);
  oneDHists_["SMGeantDaughterPhi"] = fs_->make<TH1D>("SMGeantDaughterPhi", ";SM r-hadron daughter #phi", 100, -3.2, 3.2);
  oneDHists_["SMGeantDaughterStatus"] = fs_->make<TH1D>("SMGeantDaughterStatus", ";SM r-hadron daughter status",10, -0.5, 9.5);
  oneDHists_["SMGeantDaughterAbsD0_100um"] = fs_->make<TH1D>("SMGeantDaughterAbsD0_100um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["SMGeantDaughterAbsD0_1000um"] = fs_->make<TH1D>("SMGeantDaughterAbsD0_1000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["SMGeantDaughterAbsD0_10000um"] = fs_->make<TH1D>("SMGeantDaughterAbsD0_10000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["SMGeantDaughterAbsD0_100000um"] = fs_->make<TH1D>("SMGeantDaughterAbsD0_100000um", ";r-hadron daughter |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_SMGeantDaughter_deltaEta"] = fs_->make<TH1D>("genRHadron_SMGeantDaughter_deltaEta", ";|#Delta#eta(r-hadron, SM daughter)|",60,0,6);
  oneDHists_["genRHadron_SMGeantDaughter_deltaPhi"] = fs_->make<TH1D>("genRHadron_SMGeantDaughter_deltaPhi", ";|#Delta#phi(r-hadron, SM daughter)|",32, 0, 3.2);
  oneDHists_["genRHadron_SMGeantDaughter_deltaR"] = fs_->make<TH1D>("genRHadron_SMGeantDaughter_deltaR", ";#DeltaR(r-hadron, SM daughter)",60,0,6);

  oneDHists_["electronGeantDaughterPt"] = fs_->make<TH1D>("electronGeantDaughterPt", ";sim electron p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["electronGeantDaughterP"] = fs_->make<TH1D>("electronGeantDaughterP", ";sim electron p [GeV]", 200, 0, 2000);
  oneDHists_["electronGeantDaughterEta"] = fs_->make<TH1D>("electronGeantDaughterEta", ";sim electron #eta", 100, -5.0, 5.0);
  oneDHists_["electronGeantDaughterPhi"] = fs_->make<TH1D>("electronGeantDaughterPhi", ";sim electron #phi", 100, -3.2, 3.2);
  oneDHists_["electronGeantDaughterAbsD0_100um"] = fs_->make<TH1D>("electronGeantDaughterAbsD0_100um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["electronGeantDaughterAbsD0_1000um"] = fs_->make<TH1D>("electronGeantDaughterAbsD0_1000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["electronGeantDaughterAbsD0_10000um"] = fs_->make<TH1D>("electronGeantDaughterAbsD0_10000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["electronGeantDaughterAbsD0_100000um"] = fs_->make<TH1D>("electronGeantDaughterAbsD0_100000um", ";r-hadron daughter |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_electronGeantDaughter_deltaEta"] = fs_->make<TH1D>("genRHadron_electronGeantDaughter_deltaEta", ";|#Delta#eta(r-hadron, daughter electron)|",60,0,6);
  oneDHists_["genRHadron_electronGeantDaughter_deltaPhi"] = fs_->make<TH1D>("genRHadron_electronGeantDaughter_deltaPhi", ";|#Delta#phi(r-hadron, daughter electron)|",32, 0, 3.2);
  oneDHists_["genRHadron_electronGeantDaughter_deltaR"] = fs_->make<TH1D>("genRHadron_electronGeantDaughter_deltaR", ";#DeltaR(r-hadron, daughter electron)",60,0,6);

  oneDHists_["muonGeantDaughterPt"] = fs_->make<TH1D>("muonGeantDaughterPt", ";sim muon p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["muonGeantDaughterP"] = fs_->make<TH1D>("muonGeantDaughterP", ";sim muon p [GeV]", 200, 0, 2000);
  oneDHists_["muonGeantDaughterEta"] = fs_->make<TH1D>("muonGeantDaughterEta", ";sim muon #eta", 100, -5.0, 5.0);
  oneDHists_["muonGeantDaughterPhi"] = fs_->make<TH1D>("muonGeantDaughterPhi", ";sim muon #phi", 100, -3.2, 3.2);
  oneDHists_["muonGeantDaughterAbsD0_100um"] = fs_->make<TH1D>("muonGeantDaughterAbsD0_100um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 100);
  oneDHists_["muonGeantDaughterAbsD0_1000um"] = fs_->make<TH1D>("muonGeantDaughterAbsD0_1000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 1000);
  oneDHists_["muonGeantDaughterAbsD0_10000um"] = fs_->make<TH1D>("muonGeantDaughterAbsD0_10000um", ";r-hadron daughter |d_{0}| [#mum]", 100, 0, 10000);
  oneDHists_["muonGeantDaughterAbsD0_100000um"] = fs_->make<TH1D>("muonGeantDaughterAbsD0_100000um", ";r-hadron daughter |d_{0}| [#mum]", 1000, 0, 100000);
  oneDHists_["genRHadron_muonGeantDaughter_deltaEta"] = fs_->make<TH1D>("genRHadron_muonGeantDaughter_deltaEta", ";|#Delta#eta(r-hadron, daughter muon)|",60,0,6);
  oneDHists_["genRHadron_muonGeantDaughter_deltaPhi"] = fs_->make<TH1D>("genRHadron_muonGeantDaughter_deltaPhi", ";|#Delta#phi(r-hadron, daughter muon)|",32, 0, 3.2);
  oneDHists_["genRHadron_muonGeantDaughter_deltaR"] = fs_->make<TH1D>("genRHadron_muonGeantDaughter_deltaR", ";#DeltaR(r-hadron, daughter muon)",60,0,6);

  oneDHists_["rhadronGeantDaughterId_10006XX"] = fs_->make<TH1D>("rhadronGeantDaughterId_10006XX", ";r-hadron r-hadron daughter |pdgid| (2nd range)", 100, 1000600,1000700);
  oneDHists_["rhadronGeantDaughterId_1006XXX"] = fs_->make<TH1D>("rhadronGeantDaughterId_1006XXX", ";r-hadron r-hadron daughter |pdgid| (3rd range)", 1000, 1006000,1007000);
  oneDHists_["rhadronGeantDaughterPt"] = fs_->make<TH1D>("rhadronGeantDaughterPt", ";r-hadron r-hadron daughter p_{T} [GeV]", 200, 0, 2000);
  oneDHists_["rhadronGeantDaughterP"] = fs_->make<TH1D>("rhadronGeantDaughterP", ";r-hadron r-hadron daughter p [GeV]", 200, 0, 2000);
  oneDHists_["rhadronGeantDaughterEta"] = fs_->make<TH1D>("rhadronGeantDaughterEta", ";r-hadron r-hadron daughter #eta", 100, -5.0, 5.0);
  oneDHists_["rhadronGeantDaughterPhi"] = fs_->make<TH1D>("rhadronGeantDaughterPhi", ";r-hadron r-hadron daughter #phi", 100, -3.2, 3.2);
  oneDHists_["rhadronGeantDaughterStatus"] = fs_->make<TH1D>("rhadronGeantDaughterStatus", ";r-hadron r-hadron daughter status",10, -0.5, 9.5);
  oneDHists_["genRHadron_rhadronGeantDaughter_deltaEta"] = fs_->make<TH1D>("genRHadron_rhadronGeantDaughter_deltaEta", ";|#Delta#eta(r-hadron, r-hadron daughter)|",60,0,6);
  oneDHists_["genRHadron_rhadronGeantDaughter_deltaPhi"] = fs_->make<TH1D>("genRHadron_rhadronGeantDaughter_deltaPhi", ";|#Delta#phi(r-hadron, r-hadron daughter)|",32, 0, 3.2);
  oneDHists_["genRHadron_rhadronGeantDaughter_deltaR"] = fs_->make<TH1D>("genRHadron_rhadronGeantDaughter_deltaR", ";#DeltaR(r-hadron, r-hadron daughter)",60,0,6);

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

StopRHadronSimPatAnalyzer::~StopRHadronSimPatAnalyzer()
{
}

void
StopRHadronSimPatAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
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
    //if decay is done in geant:
    //find stops that have status 101
    if(abs(genParticle.pdgId()) != 1000006) continue;
    if(genParticle.status() != 102) continue;

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

    LogDebug("StopRHadronSimPatAnalyzer")<<" stop has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status();
    //std::cout<<" stop has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status()<<std::endl;

    //if decay done in geant, find r-hadron daughter particles
    for(size_t j=0; j<genParticle.numberOfDaughters(); j++){
      const reco::Candidate* daughter = genParticle.daughter(j);
      int partId = daughter->pdgId();

      if( (abs(partId)>1000600 && abs(partId)<1000700) || (abs(partId)>1006000 && abs(partId)<1007000)){ //if daughter of stop is stop r-hadron
	LogDebug("StopRHadronSimPatAnalyzer")<<"gen stop daughter is a gen r-hadron with id "<<partId<<", eta is: "<<daughter->eta()<<", phi is: "<<daughter->phi()<<", status is: "<<daughter->status();
	//std::cout<<" stop daughter is a gen r-hadron with id "<<partId<<", pt is: "<<daughter->pt()<<", eta is: "<<daughter->eta()<<", phi is: "<<daughter->phi()<<", status is: "<<daughter->status()<<std::endl;
	if(genRhadronId_0==0 && genRhadronId_1==0){
	  genRhadronId_0 = partId;
	}
	else if(genRhadronId_0!=0 && genRhadronId_1==0){
	  genRhadronId_1 = partId;
	}
	else edm::LogInfo("StopRHadronSimPatAnalyzer")<<"you have a third gen r-hadron??";

	//find daughters of r-hadron
	oneDHists_.at("nGeantDaughters")->Fill(daughter->numberOfDaughters());

	for(size_t k=0; k<daughter->numberOfDaughters(); k++){
	  const reco::Candidate* daughterOfRHadron = daughter->daughter(k);
	  int partIdDaughterOfRHadron = daughterOfRHadron->pdgId();
	  double ptDaughterOfRHadron = daughterOfRHadron->pt();
	  double etaDaughterOfRHadron = daughterOfRHadron->eta();
	  double phiDaughterOfRHadron = daughterOfRHadron->phi();
	  double absd0DaughterOfRHadron = 10000*abs((-(daughterOfRHadron->vx())*daughterOfRHadron->py() + daughterOfRHadron->vy()*daughterOfRHadron->px())/ptDaughterOfRHadron);

	  LogDebug("StopRHadronSimPatAnalyzer")<<"   R-hadron daughter has id "<<partIdDaughterOfRHadron<<", pt is: "<<ptDaughterOfRHadron<<", eta is: "<<etaDaughterOfRHadron<<", phi is: "<<phiDaughterOfRHadron<<", status is: "<<daughterOfRHadron->status();
	  //std::cout<<"   R-hadron daughter has id "<<partIdDaughterOfRHadron<<", pt is: "<<ptDaughterOfRHadron<<", eta is: "<<etaDaughterOfRHadron<<", phi is: "<<phiDaughterOfRHadron<<", status is: "<<daughterOfRHadron->status()<<std::endl;

	  //fill hists for when daughter of r-hadron is anythng
	  oneDHists_.at("SMGeantDaughterId")->Fill(abs(partIdDaughterOfRHadron));
	  oneDHists_.at("rhadronGeantDaughterId_10006XX")->Fill(abs(partIdDaughterOfRHadron));
	  oneDHists_.at("rhadronGeantDaughterId_1006XXX")->Fill(abs(partIdDaughterOfRHadron));

	  oneDHists_.at("geantDaughterPt")->Fill(ptDaughterOfRHadron);
	  oneDHists_.at("geantDaughterP")->Fill(daughterOfRHadron->p());
	  oneDHists_.at("geantDaughterEta")->Fill(etaDaughterOfRHadron);
	  oneDHists_.at("geantDaughterPhi")->Fill(phiDaughterOfRHadron);
	  oneDHists_.at("geantDaughterStatus")->Fill(daughterOfRHadron->status());
	  oneDHists_.at("geantDaughterAbsD0_100um")->Fill(absd0DaughterOfRHadron);
	  oneDHists_.at("geantDaughterAbsD0_1000um")->Fill(absd0DaughterOfRHadron);
	  oneDHists_.at("geantDaughterAbsD0_10000um")->Fill(absd0DaughterOfRHadron);
	  oneDHists_.at("geantDaughterAbsD0_100000um")->Fill(absd0DaughterOfRHadron);

	  oneDHists_.at("genRHadron_GeantDaughter_deltaEta")->Fill(abs(daughter->eta()-etaDaughterOfRHadron));
	  oneDHists_.at("genRHadron_GeantDaughter_deltaPhi")->Fill(abs(daughter->phi()-phiDaughterOfRHadron));
	  oneDHists_.at("genRHadron_GeantDaughter_deltaR")->Fill(deltaR(daughter->eta(),daughter->phi(),etaDaughterOfRHadron,phiDaughterOfRHadron));


	  //fill hists for when daughter of r-hadron is SM particle (b/q quark or lepton)
	  if(abs(partIdDaughterOfRHadron)<20){
	    oneDHists_.at("SMGeantDaughterPt")->Fill(ptDaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterP")->Fill(daughterOfRHadron->p());
	    oneDHists_.at("SMGeantDaughterEta")->Fill(etaDaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterPhi")->Fill(phiDaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterStatus")->Fill(daughterOfRHadron->status());
	    oneDHists_.at("SMGeantDaughterAbsD0_100um")->Fill(absd0DaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterAbsD0_1000um")->Fill(absd0DaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterAbsD0_10000um")->Fill(absd0DaughterOfRHadron);
	    oneDHists_.at("SMGeantDaughterAbsD0_100000um")->Fill(absd0DaughterOfRHadron);

	    oneDHists_.at("genRHadron_SMGeantDaughter_deltaEta")->Fill(abs(daughter->eta()-etaDaughterOfRHadron));
	    oneDHists_.at("genRHadron_SMGeantDaughter_deltaPhi")->Fill(abs(daughter->phi()-phiDaughterOfRHadron));
	    oneDHists_.at("genRHadron_SMGeantDaughter_deltaR")->Fill(deltaR(daughter->eta(),daughter->phi(),etaDaughterOfRHadron,phiDaughterOfRHadron));

	    //fill hists when daughter of r-hadron is electron
	    if(abs(partIdDaughterOfRHadron)==11){
	      oneDHists_.at("electronGeantDaughterPt")->Fill(ptDaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterP")->Fill(daughterOfRHadron->p());
	      oneDHists_.at("electronGeantDaughterEta")->Fill(etaDaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterPhi")->Fill(phiDaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterAbsD0_100um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterAbsD0_1000um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterAbsD0_10000um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("electronGeantDaughterAbsD0_100000um")->Fill(absd0DaughterOfRHadron);

	      oneDHists_.at("genRHadron_electronGeantDaughter_deltaEta")->Fill(abs(daughter->eta()-etaDaughterOfRHadron));
	      oneDHists_.at("genRHadron_electronGeantDaughter_deltaPhi")->Fill(abs(daughter->phi()-phiDaughterOfRHadron));
	      oneDHists_.at("genRHadron_electronGeantDaughter_deltaR")->Fill(deltaR(daughter->eta(),daughter->phi(),etaDaughterOfRHadron,phiDaughterOfRHadron));

	      //match gen electron to reco electron
	      if(ptDaughterOfRHadron < 10.0){
		oneDHists_.at("matchedElectron")->Fill(-1.0);
		continue;
	      }

	      const pat::Electron *electron = getMatchedElectron(*daughterOfRHadron, electrons);

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
	    } //end of if daughter of r-hadron is electron

	    //fill hists when daughter of r-hadron is muon
	    else if(abs(partIdDaughterOfRHadron)==13){
	      oneDHists_.at("muonGeantDaughterPt")->Fill(ptDaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterP")->Fill(daughterOfRHadron->p());
	      oneDHists_.at("muonGeantDaughterEta")->Fill(etaDaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterPhi")->Fill(phiDaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterAbsD0_100um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterAbsD0_1000um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterAbsD0_10000um")->Fill(absd0DaughterOfRHadron);
	      oneDHists_.at("muonGeantDaughterAbsD0_100000um")->Fill(absd0DaughterOfRHadron);

	      oneDHists_.at("genRHadron_muonGeantDaughter_deltaEta")->Fill(abs(daughter->eta()-etaDaughterOfRHadron));
	      oneDHists_.at("genRHadron_muonGeantDaughter_deltaPhi")->Fill(abs(daughter->phi()-phiDaughterOfRHadron));
	      oneDHists_.at("genRHadron_muonGeantDaughter_deltaR")->Fill(deltaR(daughter->eta(),daughter->phi(),etaDaughterOfRHadron,phiDaughterOfRHadron));

	      //match gen muon to reco muon
	      if(ptDaughterOfRHadron < 10.0){
		oneDHists_.at("matchedMuon")->Fill(-1.0);
		continue;
	      }

	      const pat::Muon *muon = getMatchedMuon(*daughterOfRHadron, muons);

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
	    }//end of if r-hadron daughter is muon

	  }//end of if r-hadron daughter is SM particle


	  //fill hists for when daughter of r-hadron is another r-hadron
	  bool geantDaughterId_10006XX = false;
	  bool geantDaughterId_1006XXX = false;
	  if(abs(partIdDaughterOfRHadron)>1000600 && abs(partIdDaughterOfRHadron)<1000700) geantDaughterId_10006XX = true;
	  else if(abs(partIdDaughterOfRHadron)>1006000 && abs(partIdDaughterOfRHadron)<1007000) geantDaughterId_1006XXX = true;

	  if(geantDaughterId_10006XX || geantDaughterId_1006XXX){
	    oneDHists_.at("rhadronGeantDaughterPt")->Fill(ptDaughterOfRHadron);
	    oneDHists_.at("rhadronGeantDaughterP")->Fill(daughterOfRHadron->p());
	    oneDHists_.at("rhadronGeantDaughterEta")->Fill(etaDaughterOfRHadron);
	    oneDHists_.at("rhadronGeantDaughterPhi")->Fill(phiDaughterOfRHadron);
	    oneDHists_.at("rhadronGeantDaughterStatus")->Fill(daughterOfRHadron->status());

	    oneDHists_.at("genRHadron_rhadronGeantDaughter_deltaEta")->Fill(abs(daughter->eta()-etaDaughterOfRHadron));
	    oneDHists_.at("genRHadron_rhadronGeantDaughter_deltaPhi")->Fill(abs(daughter->phi()-phiDaughterOfRHadron));
	    oneDHists_.at("genRHadron_rhadronGeantDaughter_deltaR")->Fill(deltaR(daughter->eta(),daughter->phi(),etaDaughterOfRHadron,phiDaughterOfRHadron));
	  }

	}

      }
    }


  }//end loop over gen particles
  oneDHists_.at("nStops")->Fill(nStops);
  if(!nStops) edm::LogInfo("StopRHadronSimPatAnalyzer") << "[" << event.id() << "] No stops found!";

  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_1));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_1));



}//end analyze

void StopRHadronSimPatAnalyzer::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
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

const pat::Electron * StopRHadronSimPatAnalyzer::getMatchedElectron(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Electron> > &electrons) const
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

const pat::Muon * StopRHadronSimPatAnalyzer::getMatchedMuon(const reco::Candidate &genParticle, const edm::Handle<vector<pat::Muon> > &muons) const
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

DEFINE_FWK_MODULE(StopRHadronSimPatAnalyzer);

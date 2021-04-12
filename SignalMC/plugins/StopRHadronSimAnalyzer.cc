//makes plots at gen and sim level for stops with cloud model turned on and decay done in geant

#include "DisplacedSUSY/SignalMC/plugins/StopRHadronSimAnalyzer.h"

StopRHadronSimAnalyzer::StopRHadronSimAnalyzer(const edm::ParameterSet &cfg) :
  //tracks_                    (cfg.getParameter<edm::InputTag>("tracks")),
  genParticles_              (cfg.getParameter<edm::InputTag>("genParticles")),
  simTracks_                 (cfg.getParameter<edm::InputTag>("simTracks")),
  simVertexs_                (cfg.getParameter<edm::InputTag>("simVertexs")),
  hepMC_                     (cfg.getParameter<edm::InputTag>("hepMC")),
  PixelBarrelHighTofSimHits_ (cfg.getParameter<edm::InputTag>("PixelBarrelHighTofSimHits")),
  PixelBarrelLowTofSimHits_  (cfg.getParameter<edm::InputTag>("PixelBarrelLowTofSimHits")),
  PixelEndcapHighTofSimHits_ (cfg.getParameter<edm::InputTag>("PixelEndcapHighTofSimHits")),
  PixelEndcapLowTofSimHits_  (cfg.getParameter<edm::InputTag>("PixelEndcapLowTofSimHits")),
  TECHighTofSimHits_         (cfg.getParameter<edm::InputTag>("TECHighTofSimHits")),
  TECLowTofSimHits_          (cfg.getParameter<edm::InputTag>("TECLowTofSimHits")),
  TIBHighTofSimHits_         (cfg.getParameter<edm::InputTag>("TIBHighTofSimHits")),
  TIBLowTofSimHits_          (cfg.getParameter<edm::InputTag>("TIBLowTofSimHits")),
  TIDHighTofSimHits_         (cfg.getParameter<edm::InputTag>("TIDHighTofSimHits")),
  TIDLowTofSimHits_          (cfg.getParameter<edm::InputTag>("TIDLowTofSimHits")),
  TOBHighTofSimHits_         (cfg.getParameter<edm::InputTag>("TOBHighTofSimHits")),
  TOBLowTofSimHits_          (cfg.getParameter<edm::InputTag>("TOBLowTofSimHits")),
  CSCSimHits_                (cfg.getParameter<edm::InputTag>("CSCSimHits")),
  DTSimHits_                 (cfg.getParameter<edm::InputTag>("DTSimHits")),
  RPCSimHits_                (cfg.getParameter<edm::InputTag>("RPCSimHits"))
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

  oneDHists_["nSimTracks"] = fs_->make<TH1D>("nSimTracks", ";number of sim tracks per gen stop r-hadron", 10, -0.5, 9.5);

  oneDHists_["simTrackRhadronId_10006XX"] = fs_->make<TH1D>("simTrackRhadronId_10006XX", ";sim track r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["simTrackRhadronId_1006XXX"] = fs_->make<TH1D>("simTrackRhadronId_1006XXX", ";sim track r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  twoDHists_["genRhadronId_10006XX_vs_simTrackRhadronId_10006XX_matched"] = fs_->make<TH2D>("genRhadronId_10006XX_vs_simTrackRhadronId_10006XX_matched", ";generator r-hadron |pdgid| (1st range);sim track r-hadron |pdgid| (1st range)", 100, 1000600,1000700, 100, 1000600,1000700);
  twoDHists_["genRhadronId_1006XXX_vs_simTrackRhadronId_1006XXX_matched"] = fs_->make<TH2D>("genRhadronId_1006XXX_vs_simTrackRhadronId_1006XXX_matched", ";generator r-hadron |pdgid| (2nd range);sim track r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000, 1000, 1006000,1007000);
  twoDHists_["genRhadronId_10006XX_vs_simTrackRhadronId_1006XXX_matched"] = fs_->make<TH2D>("genRhadronId_10006XX_vs_simTrackRhadronId_1006XXX_matched", ";generator r-hadron |pdgid| (1st range);sim track r-hadron |pdgid| (2nd range)", 100, 1000600,1000700, 1000, 1006000,1007000);
  twoDHists_["genRhadronId_1006XXX_vs_simTrackRhadronId_10006XX_matched"] = fs_->make<TH2D>("genRhadronId_1006XXX_vs_simTrackRhadronId_10006XX_matched", ";generator r-hadron |pdgid| (2nd range);sim track r-hadron |pdgid| (1st range)", 1000, 1006000,1007000, 100, 1000600,1000700);

  oneDHists_["gen1000612_simTrackFlipping"] = fs_->make<TH1D>("gen1000612_simTrackFlipping", ";number of times gen id 1000612 flips",10,0,10);
  oneDHists_["gen1000622_simTrackFlipping"] = fs_->make<TH1D>("gen1000622_simTrackFlipping", ";number of times gen id 1000622 flips",10,0,10);
  oneDHists_["gen1000632_simTrackFlipping"] = fs_->make<TH1D>("gen1000632_simTrackFlipping", ";number of times gen id 1000632 flips",10,0,10);
  oneDHists_["gen1000642_simTrackFlipping"] = fs_->make<TH1D>("gen1000642_simTrackFlipping", ";number of times gen id 1000642 flips",10,0,10);
  oneDHists_["gen1000652_simTrackFlipping"] = fs_->make<TH1D>("gen1000652_simTrackFlipping", ";number of times gen id 1000652 flips",10,0,10);
  oneDHists_["gen1006113_simTrackFlipping"] = fs_->make<TH1D>("gen1006113_simTrackFlipping", ";number of times gen id 1006113 flips",10,0,10);
  oneDHists_["gen1006211_simTrackFlipping"] = fs_->make<TH1D>("gen1006211_simTrackFlipping", ";number of times gen id 1006211 flips",10,0,10);
  oneDHists_["gen1006213_simTrackFlipping"] = fs_->make<TH1D>("gen1006213_simTrackFlipping", ";number of times gen id 1006213 flips",10,0,10);
  oneDHists_["gen1006223_simTrackFlipping"] = fs_->make<TH1D>("gen1006223_simTrackFlipping", ";number of times gen id 1006223 flips",10,0,10);
  oneDHists_["gen1006311_simTrackFlipping"] = fs_->make<TH1D>("gen1006311_simTrackFlipping", ";number of times gen id 1006311 flips",10,0,10);
  oneDHists_["gen1006313_simTrackFlipping"] = fs_->make<TH1D>("gen1006313_simTrackFlipping", ";number of times gen id 1006313 flips",10,0,10);
  oneDHists_["gen1006321_simTrackFlipping"] = fs_->make<TH1D>("gen1006321_simTrackFlipping", ";number of times gen id 1006321 flips",10,0,10);
  oneDHists_["gen1006323_simTrackFlipping"] = fs_->make<TH1D>("gen1006323_simTrackFlipping", ";number of times gen id 1006323 flips",10,0,10);
  oneDHists_["gen1006333_simTrackFlipping"] = fs_->make<TH1D>("gen1006333_simTrackFlipping", ";number of times gen id 1006333 flips",10,0,10);


  oneDHists_["PixelBarrelHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("PixelBarrelHighTofSimHitRhadronId_10006XX", ";pixel barrel high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["PixelBarrelHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("PixelBarrelHighTofSimHitRhadronId_1006XXX", ";pixel barrel high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["PixelBarrelLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("PixelBarrelLowTofSimHitRhadronId_10006XX", ";pixel barrel low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["PixelBarrelLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("PixelBarrelLowTofSimHitRhadronId_1006XXX", ";pixel barrel low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["PixelEndcapHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("PixelEndcapHighTofSimHitRhadronId_10006XX", ";pixel endcap high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["PixelEndcapHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("PixelEndcapHighTofSimHitRhadronId_1006XXX", ";pixel endcap high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["PixelEndcapLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("PixelEndcapLowTofSimHitRhadronId_10006XX", ";pixel endcap low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["PixelEndcapLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("PixelEndcapLowTofSimHitRhadronId_1006XXX", ";pixel endcap low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TECHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TECHighTofSimHitRhadronId_10006XX", ";TEC high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TECHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TECHighTofSimHitRhadronId_1006XXX", ";TEC high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TECLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TECLowTofSimHitRhadronId_10006XX", ";TEC low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TECLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TECLowTofSimHitRhadronId_1006XXX", ";TEC low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TIBHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TIBHighTofSimHitRhadronId_10006XX", ";TIB high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TIBHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TIBHighTofSimHitRhadronId_1006XXX", ";TIB high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TIBLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TIBLowTofSimHitRhadronId_10006XX", ";TIB low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TIBLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TIBLowTofSimHitRhadronId_1006XXX", ";TIB low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TIDHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TIDHighTofSimHitRhadronId_10006XX", ";TID high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TIDHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TIDHighTofSimHitRhadronId_1006XXX", ";TID high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TIDLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TIDLowTofSimHitRhadronId_10006XX", ";TID low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TIDLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TIDLowTofSimHitRhadronId_1006XXX", ";TID low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TOBHighTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TOBHighTofSimHitRhadronId_10006XX", ";TOB high tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TOBHighTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TOBHighTofSimHitRhadronId_1006XXX", ";TOB high tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["TOBLowTofSimHitRhadronId_10006XX"] = fs_->make<TH1D>("TOBLowTofSimHitRhadronId_10006XX", ";TOB low tof sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["TOBLowTofSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("TOBLowTofSimHitRhadronId_1006XXX", ";TOB low tof sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["CSCSimHitRhadronId_10006XX"] = fs_->make<TH1D>("CSCSimHitRhadronId_10006XX", ";CSC sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["CSCSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("CSCSimHitRhadronId_1006XXX", ";CSC sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["DTSimHitRhadronId_10006XX"] = fs_->make<TH1D>("DTSimHitRhadronId_10006XX", ";DT sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["DTSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("DTSimHitRhadronId_1006XXX", ";DT sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  oneDHists_["RPCSimHitRhadronId_10006XX"] = fs_->make<TH1D>("RPCSimHitRhadronId_10006XX", ";RPC sim hit r-hadron |pdgid| (1st range)", 100, 1000600,1000700);
  oneDHists_["RPCSimHitRhadronId_1006XXX"] = fs_->make<TH1D>("RPCSimHitRhadronId_1006XXX", ";RPC sim hit r-hadron |pdgid| (2nd range)", 1000, 1006000,1007000);

  twoDHists_["SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  twoDHists_["gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (1st range); sim hit collection", 100, 1000600,1000700, 15, 0, 15);
  twoDHists_["gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection"] = fs_->make<TH2D>("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection", ";sim hit r-hadron |pdgid| (2nd range); sim hit collection", 1000, 1006000,1007000, 15, 0, 15);

  oneDHists_["gen1000612_SimHitCollection"] = fs_->make<TH1D>("gen1000612_SimHitCollection", ";sim hit collection for gen id 1000612", 15, 0, 15);
  oneDHists_["gen1000622_SimHitCollection"] = fs_->make<TH1D>("gen1000622_SimHitCollection", ";sim hit collection for gen id 1000622", 15, 0, 15);
  oneDHists_["gen1000632_SimHitCollection"] = fs_->make<TH1D>("gen1000632_SimHitCollection", ";sim hit collection for gen id 1000632", 15, 0, 15);
  oneDHists_["gen1000642_SimHitCollection"] = fs_->make<TH1D>("gen1000642_SimHitCollection", ";sim hit collection for gen id 1000642", 15, 0, 15);
  oneDHists_["gen1000652_SimHitCollection"] = fs_->make<TH1D>("gen1000652_SimHitCollection", ";sim hit collection for gen id 1000652", 15, 0, 15);
  oneDHists_["gen1006113_SimHitCollection"] = fs_->make<TH1D>("gen1006113_SimHitCollection", ";sim hit collection for gen id 1006113", 15, 0, 15);
  oneDHists_["gen1006211_SimHitCollection"] = fs_->make<TH1D>("gen1006211_SimHitCollection", ";sim hit collection for gen id 1006211", 15, 0, 15);
  oneDHists_["gen1006213_SimHitCollection"] = fs_->make<TH1D>("gen1006213_SimHitCollection", ";sim hit collection for gen id 1006213", 15, 0, 15);
  oneDHists_["gen1006223_SimHitCollection"] = fs_->make<TH1D>("gen1006223_SimHitCollection", ";sim hit collection for gen id 1006223", 15, 0, 15);
  oneDHists_["gen1006311_SimHitCollection"] = fs_->make<TH1D>("gen1006311_SimHitCollection", ";sim hit collection for gen id 1006311", 15, 0, 15);
  oneDHists_["gen1006313_SimHitCollection"] = fs_->make<TH1D>("gen1006313_SimHitCollection", ";sim hit collection for gen id 1006313", 15, 0, 15);
  oneDHists_["gen1006321_SimHitCollection"] = fs_->make<TH1D>("gen1006321_SimHitCollection", ";sim hit collection for gen id 1006321", 15, 0, 15);
  oneDHists_["gen1006323_SimHitCollection"] = fs_->make<TH1D>("gen1006323_SimHitCollection", ";sim hit collection for gen id 1006323", 15, 0, 15);
  oneDHists_["gen1006333_SimHitCollection"] = fs_->make<TH1D>("gen1006333_SimHitCollection", ";sim hit collection for gen id 1006333", 15, 0, 15);


  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000612_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000612_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000622_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000622_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000632_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000632_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000642_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000642_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000652_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1000652_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006113_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006113_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006211_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006211_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006213_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006213_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006223_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006223_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006311_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006311_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006313_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006313_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006321_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006321_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006323_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006323_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006333_SimHitRhadronId_10006XX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(5,"TECHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(6,"TECLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(7,"TIBHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(8,"TIBLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(9,"TIDHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(10,"TIDLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(11,"TOBHighTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(12,"TOBLowTof");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(13,"CSC");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(14,"DT");
  twoDHists_.at("gen1006333_SimHitRhadronId_1006XXX_vs_SimHitCollection")->GetYaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1000612_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1000622_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1000632_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1000642_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1000652_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006113_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006211_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006213_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006223_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006311_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006313_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006321_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006323_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");

  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(1,"PixelBarrelHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(2,"PixelBarrelLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(3,"PixelEndcapHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(4,"PixelEndcapLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(5,"TECHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(6,"TECLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(7,"TIBHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(8,"TIBLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(9,"TIDHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(10,"TIDLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(11,"TOBHighTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(12,"TOBLowTof");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(13,"CSC");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(14,"DT");
  oneDHists_.at("gen1006333_SimHitCollection")->GetXaxis()->SetBinLabel(15,"RPC");


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

  simTracksToken_ = consumes<edm::SimTrackContainer> (simTracks_);
  simVertexsToken_ = consumes<edm::SimVertexContainer> (simVertexs_);

  hepMCToken_ = consumes<edm::HepMCProduct> (hepMC_);

  PixelBarrelHighTofSimHitsToken_ = consumes<edm::PSimHitContainer> (PixelBarrelHighTofSimHits_);
  PixelBarrelLowTofSimHitsToken_  = consumes<edm::PSimHitContainer> (PixelBarrelLowTofSimHits_);
  PixelEndcapHighTofSimHitsToken_ = consumes<edm::PSimHitContainer> (PixelEndcapHighTofSimHits_);
  PixelEndcapLowTofSimHitsToken_  = consumes<edm::PSimHitContainer> (PixelEndcapLowTofSimHits_);
  TECHighTofSimHitsToken_         = consumes<edm::PSimHitContainer> (TECHighTofSimHits_);
  TECLowTofSimHitsToken_          = consumes<edm::PSimHitContainer> (TECLowTofSimHits_);
  TIBHighTofSimHitsToken_         = consumes<edm::PSimHitContainer> (TIBHighTofSimHits_);
  TIBLowTofSimHitsToken_          = consumes<edm::PSimHitContainer> (TIBLowTofSimHits_);
  TIDHighTofSimHitsToken_         = consumes<edm::PSimHitContainer> (TIDHighTofSimHits_);
  TIDLowTofSimHitsToken_          = consumes<edm::PSimHitContainer> (TIDLowTofSimHits_);
  TOBHighTofSimHitsToken_         = consumes<edm::PSimHitContainer> (TOBHighTofSimHits_);
  TOBLowTofSimHitsToken_          = consumes<edm::PSimHitContainer> (TOBLowTofSimHits_);
  CSCSimHitsToken_                = consumes<edm::PSimHitContainer> (CSCSimHits_);
  DTSimHitsToken_                 = consumes<edm::PSimHitContainer> (DTSimHits_),
  RPCSimHitsToken_                = consumes<edm::PSimHitContainer> (RPCSimHits_);

}

StopRHadronSimAnalyzer::~StopRHadronSimAnalyzer()
{
}

void
StopRHadronSimAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
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
  double genRhadronEta_0 = -10.;
  double genRhadronEta_1 = -10.;
  double genRhadronPhi_0 = -10.;
  double genRhadronPhi_1 = -10.;
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

    LogDebug("StopRHadronSimAnalyzer")<<" stop has id "<<genParticle.pdgId()<<", pt is: "<<genParticle.pt()<<", eta is: "<<genParticle.eta()<<", phi is: "<<genParticle.phi()<<", status is: "<<genParticle.status();
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

    //if decay done in geant, find r-hadron daughter particles
    for(size_t j=0; j<genParticle.numberOfDaughters(); j++){
      const reco::Candidate* daughter = genParticle.daughter(j);
      int partId = daughter->pdgId();

      if( (abs(partId)>1000600 && abs(partId)<1000700) || (abs(partId)>1006000 && abs(partId)<1007000)){ //if daughter of stop is stop r-hadron
	LogDebug("StopRHadronSimAnalyzer")<<"gen stop daughter is a gen r-hadron with id "<<partId<<", eta is: "<<daughter->eta()<<", phi is: "<<daughter->phi()<<", status is: "<<daughter->status();
	//std::cout<<" stop daughter is a gen r-hadron with id "<<partId<<", pt is: "<<daughter->pt()<<", eta is: "<<daughter->eta()<<", phi is: "<<daughter->phi()<<", status is: "<<daughter->status()<<std::endl;
	if(genRhadronId_0==0 && genRhadronId_1==0){
	  genRhadronId_0 = partId;
	  genRhadronEta_0 = daughter->eta();
	  genRhadronPhi_0 = daughter->phi();
	}
	else if(genRhadronId_0!=0 && genRhadronId_1==0){
	  genRhadronId_1 = partId;
	  genRhadronEta_1 = daughter->eta();
	  genRhadronPhi_1 = daughter->phi();
	}
	else edm::LogInfo("StopRHadronSimAnalyzer")<<"you have a third gen r-hadron??";

	//find daughters of r-hadron
	oneDHists_.at("nGeantDaughters")->Fill(daughter->numberOfDaughters());

	for(size_t k=0; k<daughter->numberOfDaughters(); k++){
	  const reco::Candidate* daughterOfRHadron = daughter->daughter(k);
	  int partIdDaughterOfRHadron = daughterOfRHadron->pdgId();
	  double ptDaughterOfRHadron = daughterOfRHadron->pt();
	  double etaDaughterOfRHadron = daughterOfRHadron->eta();
	  double phiDaughterOfRHadron = daughterOfRHadron->phi();
	  double absd0DaughterOfRHadron = 10000*abs((-(daughterOfRHadron->vx())*daughterOfRHadron->py() + daughterOfRHadron->vy()*daughterOfRHadron->px())/ptDaughterOfRHadron);

	  LogDebug("StopRHadronSimAnalyzer")<<"   R-hadron daughter has id "<<partIdDaughterOfRHadron<<", pt is: "<<ptDaughterOfRHadron<<", eta is: "<<etaDaughterOfRHadron<<", phi is: "<<phiDaughterOfRHadron<<", status is: "<<daughterOfRHadron->status();
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
	    }

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
	    }

	  }


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
  if(!nStops) edm::LogInfo("StopRHadronSimAnalyzer") << "[" << event.id() << "] No stops found!";

  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_10006XX")->Fill(abs(genRhadronId_1));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_0));
  oneDHists_.at("genRhadronId_1006XXX")->Fill(abs(genRhadronId_1));

  //////////////////////////////////////////////////////////

  //sim tracks
  edm::Handle<edm::SimTrackContainer> simTracks;
  event.getByToken(simTracksToken_, simTracks);

  edm::Handle<edm::SimVertexContainer> simVertexs;
  event.getByToken(simVertexsToken_, simVertexs);

  edm::Handle<edm::HepMCProduct> MCEvt;
  event.getByToken(hepMCToken_, MCEvt);
  const HepMC::GenEvent* evt = MCEvt->GetEvent();

  int gen0_1000612flip = -1;
  int gen0_1000622flip = -1;
  int gen0_1000632flip = -1;
  int gen0_1000642flip = -1;
  int gen0_1000652flip = -1;
  int gen0_1006113flip = -1;
  int gen0_1006211flip = -1;
  int gen0_1006213flip = -1;
  int gen0_1006223flip = -1;
  int gen0_1006311flip = -1;
  int gen0_1006313flip = -1;
  int gen0_1006321flip = -1;
  int gen0_1006323flip = -1;
  int gen0_1006333flip = -1;

  int gen1_1000612flip = -1;
  int gen1_1000622flip = -1;
  int gen1_1000632flip = -1;
  int gen1_1000642flip = -1;
  int gen1_1000652flip = -1;
  int gen1_1006113flip = -1;
  int gen1_1006211flip = -1;
  int gen1_1006213flip = -1;
  int gen1_1006223flip = -1;
  int gen1_1006311flip = -1;
  int gen1_1006313flip = -1;
  int gen1_1006321flip = -1;
  int gen1_1006323flip = -1;
  int gen1_1006333flip = -1;


  if(abs(genRhadronId_0)==1000612) gen0_1000612flip = 0;
  else if(abs(genRhadronId_0)==1000622) gen0_1000622flip = 0;
  else if(abs(genRhadronId_0)==1000632) gen0_1000632flip = 0;
  else if(abs(genRhadronId_0)==1000642) gen0_1000642flip = 0;
  else if(abs(genRhadronId_0)==1000652) gen0_1000652flip = 0;
  else if(abs(genRhadronId_0)==1006113) gen0_1006113flip = 0;
  else if(abs(genRhadronId_0)==1006211) gen0_1006211flip = 0;
  else if(abs(genRhadronId_0)==1006213) gen0_1006213flip = 0;
  else if(abs(genRhadronId_0)==1006223) gen0_1006223flip = 0;
  else if(abs(genRhadronId_0)==1006311) gen0_1006311flip = 0;
  else if(abs(genRhadronId_0)==1006313) gen0_1006313flip = 0;
  else if(abs(genRhadronId_0)==1006321) gen0_1006321flip = 0;
  else if(abs(genRhadronId_0)==1006323) gen0_1006323flip = 0;
  else if(abs(genRhadronId_0)==1006333) gen0_1006333flip = 0;

  if(abs(genRhadronId_1)==1000612) gen1_1000612flip = 0;
  else if(abs(genRhadronId_1)==1000622) gen1_1000622flip = 0;
  else if(abs(genRhadronId_1)==1000632) gen1_1000632flip = 0;
  else if(abs(genRhadronId_1)==1000642) gen1_1000642flip = 0;
  else if(abs(genRhadronId_1)==1000652) gen1_1000652flip = 0;
  else if(abs(genRhadronId_1)==1006113) gen1_1006113flip = 0;
  else if(abs(genRhadronId_1)==1006211) gen1_1006211flip = 0;
  else if(abs(genRhadronId_1)==1006213) gen1_1006213flip = 0;
  else if(abs(genRhadronId_1)==1006223) gen1_1006223flip = 0;
  else if(abs(genRhadronId_1)==1006311) gen1_1006311flip = 0;
  else if(abs(genRhadronId_1)==1006313) gen1_1006313flip = 0;
  else if(abs(genRhadronId_1)==1006321) gen1_1006321flip = 0;
  else if(abs(genRhadronId_1)==1006323) gen1_1006323flip = 0;
  else if(abs(genRhadronId_1)==1006333) gen1_1006333flip = 0;

  int gen0_partId = -1;
  int gen1_partId = -1;

  bool atLeastOneSimTrackMatchedToGen0 = false;
  bool atLeastOneSimTrackMatchedToGen1 = false;

  int gen0_nSimTracks = 0;
  int gen1_nSimTracks = 0;

  for(const auto &simTrack : *simTracks) {
    int partId = simTrack.type();

    if( (abs(partId)>1000600 && abs(partId)<1000700) || (abs(partId)>1006000 && abs(partId)<1007000)){ //sim track is stop r-hadron
      int vertexIndex = simTrack.vertIndex();
      int trackId = simTrack.trackId();
      double simTrackEta = simTrack.momentum().eta();
      double simTrackPhi = simTrack.momentum().phi();
      LogDebug("StopRHadronSimAnalyzer")<<"sim track id "<<simTrack.trackId()<<", type is: "<<simTrack.type()<<", gen particle index is: "<<simTrack.genpartIndex()<<", vertex index is: "<<simTrack.vertIndex()<<", eta is: "<<simTrack.momentum().eta()<<", phi is: "<<simTrack.momentum().phi();
      //std::cout<<"sim track id "<<simTrack.trackId()<<", type is: "<<simTrack.type()<<", gen particle index is: "<<simTrack.genpartIndex()<<", vertex index is: "<<simTrack.vertIndex()<<", eta is: "<<simTrack.momentum().eta()<<", phi is: "<<simTrack.momentum().phi()<<std::endl;

      if(deltaR(simTrackEta, simTrackPhi, genRhadronEta_0, genRhadronPhi_0)<0.1){ //match sim track r-hadron to gen r-hadron 0 in deltaR
	atLeastOneSimTrackMatchedToGen0 = true;

	if(partId!=gen0_partId){ //only take sim tracks with a new partId (count sequential sim tracks with same partId as one sim track)
	  gen0_partId = partId;
	  gen0_nSimTracks++;

	  oneDHists_.at("simTrackRhadronId_10006XX")->Fill(abs(gen0_partId));
	  oneDHists_.at("simTrackRhadronId_1006XXX")->Fill(abs(gen0_partId));

	  twoDHists_.at("genRhadronId_10006XX_vs_simTrackRhadronId_10006XX_matched")->Fill(abs(genRhadronId_0), abs(gen0_partId));
	  twoDHists_.at("genRhadronId_1006XXX_vs_simTrackRhadronId_1006XXX_matched")->Fill(abs(genRhadronId_0), abs(gen0_partId));
	  twoDHists_.at("genRhadronId_10006XX_vs_simTrackRhadronId_1006XXX_matched")->Fill(abs(genRhadronId_0), abs(gen0_partId));
	  twoDHists_.at("genRhadronId_1006XXX_vs_simTrackRhadronId_10006XX_matched")->Fill(abs(genRhadronId_0), abs(gen0_partId));

	  //find out how often the track flips charge
	  if(gen0_nSimTracks>1){//the first matched sim track has the same partId as the gen r-hadron, so don't count that as a flip
	    if(abs(genRhadronId_0)==1000612) gen0_1000612flip++;
	    else if(abs(genRhadronId_0)==1000622) gen0_1000622flip++;
	    else if(abs(genRhadronId_0)==1000632) gen0_1000632flip++;
	    else if(abs(genRhadronId_0)==1000642) gen0_1000642flip++;
	    else if(abs(genRhadronId_0)==1000652) gen0_1000652flip++;
	    else if(abs(genRhadronId_0)==1006113) gen0_1006113flip++;
	    else if(abs(genRhadronId_0)==1006211) gen0_1006211flip++;
	    else if(abs(genRhadronId_0)==1006213) gen0_1006213flip++;
	    else if(abs(genRhadronId_0)==1006223) gen0_1006223flip++;
	    else if(abs(genRhadronId_0)==1006311) gen0_1006311flip++;
	    else if(abs(genRhadronId_0)==1006313) gen0_1006313flip++;
	    else if(abs(genRhadronId_0)==1006321) gen0_1006321flip++;
	    else if(abs(genRhadronId_0)==1006323) gen0_1006323flip++;
	    else if(abs(genRhadronId_0)==1006333) gen0_1006333flip++;
	  }
	}
      }

      else if(deltaR(simTrackEta, simTrackPhi, genRhadronEta_1, genRhadronPhi_1)<0.1){ //match sim track r-hadron to gen r-hadron 1 in deltaR
	atLeastOneSimTrackMatchedToGen1 = true;

	if(partId!=gen1_partId){ //only take sim tracks with a new partId (count sequential sim tracks with same partId as one sim track)
	  gen1_partId = partId;
	  gen1_nSimTracks++;

	  oneDHists_.at("simTrackRhadronId_10006XX")->Fill(abs(gen1_partId));
	  oneDHists_.at("simTrackRhadronId_1006XXX")->Fill(abs(gen1_partId));

	  twoDHists_.at("genRhadronId_10006XX_vs_simTrackRhadronId_10006XX_matched")->Fill(abs(genRhadronId_1), abs(gen1_partId));
	  twoDHists_.at("genRhadronId_1006XXX_vs_simTrackRhadronId_1006XXX_matched")->Fill(abs(genRhadronId_1), abs(gen1_partId));
	  twoDHists_.at("genRhadronId_10006XX_vs_simTrackRhadronId_1006XXX_matched")->Fill(abs(genRhadronId_1), abs(gen1_partId));
	  twoDHists_.at("genRhadronId_1006XXX_vs_simTrackRhadronId_10006XX_matched")->Fill(abs(genRhadronId_1), abs(gen1_partId));

	  //find out how often the track flips charge
	  if(gen1_nSimTracks>1){//the first matched sim track has the same partId as the gen r-hadron, so don't count that as a flip
	    if(abs(genRhadronId_1)==1000612) gen1_1000612flip++;
	    else if(abs(genRhadronId_1)==1000622) gen1_1000622flip++;
	    else if(abs(genRhadronId_1)==1000632) gen1_1000632flip++;
	    else if(abs(genRhadronId_1)==1000642) gen1_1000642flip++;
	    else if(abs(genRhadronId_1)==1000652) gen1_1000652flip++;
	    else if(abs(genRhadronId_1)==1006113) gen1_1006113flip++;
	    else if(abs(genRhadronId_1)==1006211) gen1_1006211flip++;
	    else if(abs(genRhadronId_1)==1006213) gen1_1006213flip++;
	    else if(abs(genRhadronId_1)==1006223) gen1_1006223flip++;
	    else if(abs(genRhadronId_1)==1006311) gen1_1006311flip++;
	    else if(abs(genRhadronId_1)==1006313) gen1_1006313flip++;
	    else if(abs(genRhadronId_1)==1006321) gen1_1006321flip++;
	    else if(abs(genRhadronId_1)==1006323) gen1_1006323flip++;
	    else if(abs(genRhadronId_1)==1006333) gen1_1006333flip++;
	  }
	}
      }

      else edm::LogInfo("StopRHadronSimAnalyzer")<<"sim track not dR matched to either gen r-hadron!!";

      if (simTrack.genpartIndex() != -1) {
	HepMC::GenParticle* part = evt->barcode_to_particle(simTrack.genpartIndex());
	if (part) {
	  LogDebug("StopRHadronSimAnalyzer") << "  ---> Corresponding to HepMC particle " << *part << std::endl;
	}
	else {
	  LogDebug("StopRHadronSimAnalyzer") << " ---> Corresponding HepMC particle to barcode " << simTrack.genpartIndex()
		    << " not in selected event " << std::endl;
	}
      }
      int vertexCounter = 0;
      for(const auto &simVertex : *simVertexs) {
	if(vertexCounter == vertexIndex) {
	  LogDebug("StopRHadronSimAnalyzer")<<"vertex number "<<vertexCounter<<" has trackId of "<<simVertex.parentIndex();
	  //std::cout<<"vertex number "<<vertexCounter<<" has trackId of "<<simVertex.parentIndex()<<std::endl;
	}//end if vertexCounter == vertexIndex
	if(simVertex.parentIndex() == trackId){
	  LogDebug("StopRHadronSimAnalyzer")<<"vertex number "<<vertexCounter<<" has trackId of "<<simVertex.parentIndex();
	  //std::cout<<"vertex number of decay is "<<vertexCounter<<", and has trackId of "<<simVertex.parentIndex()<<std::endl;
	}
	vertexCounter++;
      }//end loop over sim vertexs
    }//end if sim track is r-hadron
  }//end loop over sim tracks

  oneDHists_.at("nSimTracks")->Fill(gen0_nSimTracks);
  oneDHists_.at("nSimTracks")->Fill(gen1_nSimTracks);

  if(atLeastOneSimTrackMatchedToGen0){
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1000612flip is: "<<gen0_1000612flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1000622flip is: "<<gen0_1000622flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1000632flip is: "<<gen0_1000632flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1000642flip is: "<<gen0_1000642flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1000652flip is: "<<gen0_1000652flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006113flip is: "<<gen0_1006113flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006211flip is: "<<gen0_1006211flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006213flip is: "<<gen0_1006213flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006223flip is: "<<gen0_1006223flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006311flip is: "<<gen0_1006311flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006313flip is: "<<gen0_1006313flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006321flip is: "<<gen0_1006321flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006323flip is: "<<gen0_1006323flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen0_1006333flip is: "<<gen0_1006333flip;

    if(gen0_1000612flip > -1) oneDHists_.at("gen1000612_simTrackFlipping")->Fill(gen0_1000612flip);
    else if (gen0_1000622flip > -1) oneDHists_.at("gen1000622_simTrackFlipping")->Fill(gen0_1000622flip);
    else if (gen0_1000632flip > -1) oneDHists_.at("gen1000632_simTrackFlipping")->Fill(gen0_1000632flip);
    else if (gen0_1000642flip > -1) oneDHists_.at("gen1000642_simTrackFlipping")->Fill(gen0_1000642flip);
    else if (gen0_1000652flip > -1) oneDHists_.at("gen1000652_simTrackFlipping")->Fill(gen0_1000652flip);
    else if (gen0_1006113flip > -1) oneDHists_.at("gen1006113_simTrackFlipping")->Fill(gen0_1006113flip);
    else if (gen0_1006211flip > -1) oneDHists_.at("gen1006211_simTrackFlipping")->Fill(gen0_1006211flip);
    else if (gen0_1006213flip > -1) oneDHists_.at("gen1006213_simTrackFlipping")->Fill(gen0_1006213flip);
    else if (gen0_1006223flip > -1) oneDHists_.at("gen1006223_simTrackFlipping")->Fill(gen0_1006223flip);
    else if (gen0_1006311flip > -1) oneDHists_.at("gen1006311_simTrackFlipping")->Fill(gen0_1006311flip);
    else if (gen0_1006313flip > -1) oneDHists_.at("gen1006313_simTrackFlipping")->Fill(gen0_1006313flip);
    else if (gen0_1006321flip > -1) oneDHists_.at("gen1006321_simTrackFlipping")->Fill(gen0_1006321flip);
    else if (gen0_1006323flip > -1) oneDHists_.at("gen1006323_simTrackFlipping")->Fill(gen0_1006323flip);
    else if (gen0_1006333flip > -1) oneDHists_.at("gen1006333_simTrackFlipping")->Fill(gen0_1006333flip);
  }

  if(atLeastOneSimTrackMatchedToGen1){
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1000612flip is: "<<gen1_1000612flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1000622flip is: "<<gen1_1000622flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1000632flip is: "<<gen1_1000632flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1000642flip is: "<<gen1_1000642flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1000652flip is: "<<gen1_1000652flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006113flip is: "<<gen1_1006113flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006211flip is: "<<gen1_1006211flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006213flip is: "<<gen1_1006213flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006223flip is: "<<gen1_1006223flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006311flip is: "<<gen1_1006311flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006313flip is: "<<gen1_1006313flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006321flip is: "<<gen1_1006321flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006323flip is: "<<gen1_1006323flip;
    LogDebug("StopRHadronSimAnalyzer")<<"gen1_1006333flip is: "<<gen1_1006333flip;

    if(gen1_1000612flip > -1) oneDHists_.at("gen1000612_simTrackFlipping")->Fill(gen1_1000612flip);
    else if (gen1_1000622flip > -1) oneDHists_.at("gen1000622_simTrackFlipping")->Fill(gen1_1000622flip);
    else if (gen1_1000632flip > -1) oneDHists_.at("gen1000632_simTrackFlipping")->Fill(gen1_1000632flip);
    else if (gen1_1000642flip > -1) oneDHists_.at("gen1000642_simTrackFlipping")->Fill(gen1_1000642flip);
    else if (gen1_1000652flip > -1) oneDHists_.at("gen1000652_simTrackFlipping")->Fill(gen1_1000652flip);
    else if (gen1_1006113flip > -1) oneDHists_.at("gen1006113_simTrackFlipping")->Fill(gen1_1006113flip);
    else if (gen1_1006211flip > -1) oneDHists_.at("gen1006211_simTrackFlipping")->Fill(gen1_1006211flip);
    else if (gen1_1006213flip > -1) oneDHists_.at("gen1006213_simTrackFlipping")->Fill(gen1_1006213flip);
    else if (gen1_1006223flip > -1) oneDHists_.at("gen1006223_simTrackFlipping")->Fill(gen1_1006223flip);
    else if (gen1_1006311flip > -1) oneDHists_.at("gen1006311_simTrackFlipping")->Fill(gen1_1006311flip);
    else if (gen1_1006313flip > -1) oneDHists_.at("gen1006313_simTrackFlipping")->Fill(gen1_1006313flip);
    else if (gen1_1006321flip > -1) oneDHists_.at("gen1006321_simTrackFlipping")->Fill(gen1_1006321flip);
    else if (gen1_1006323flip > -1) oneDHists_.at("gen1006323_simTrackFlipping")->Fill(gen1_1006323flip);
    else if (gen1_1006333flip > -1) oneDHists_.at("gen1006333_simTrackFlipping")->Fill(gen1_1006333flip);
  }

  //////////////////////////////////////////////////////////

  //sim hits
  edm::Handle<edm::PSimHitContainer> PixelBarrelHighTofSimHits;
  event.getByToken(PixelBarrelHighTofSimHitsToken_, PixelBarrelHighTofSimHits);
  string simHitCollection = "PixelBarrelHighTof";
  doSimHits(PixelBarrelHighTofSimHits, simTracks, simHitCollection, 0, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> PixelBarrelLowTofSimHits;
  event.getByToken(PixelBarrelLowTofSimHitsToken_, PixelBarrelLowTofSimHits);
  simHitCollection = "PixelBarrelLowTof";
  doSimHits(PixelBarrelLowTofSimHits, simTracks, simHitCollection, 1, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> PixelEndcapHighTofSimHits;
  event.getByToken(PixelEndcapHighTofSimHitsToken_, PixelEndcapHighTofSimHits);
  simHitCollection = "PixelEndcapHighTof";
  doSimHits(PixelEndcapHighTofSimHits, simTracks, simHitCollection, 2, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> PixelEndcapLowTofSimHits;
  event.getByToken(PixelEndcapLowTofSimHitsToken_, PixelEndcapLowTofSimHits);
  simHitCollection = "PixelEndcapLowTof";
  doSimHits(PixelEndcapLowTofSimHits, simTracks, simHitCollection, 3, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TECHighTofSimHits;
  event.getByToken(TECHighTofSimHitsToken_, TECHighTofSimHits);
  simHitCollection = "TECHighTof";
  doSimHits(TECHighTofSimHits, simTracks, simHitCollection, 4, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TECLowTofSimHits;
  event.getByToken(TECLowTofSimHitsToken_, TECLowTofSimHits);
  simHitCollection = "TECLowTof";
  doSimHits(TECLowTofSimHits, simTracks, simHitCollection, 5, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TIBHighTofSimHits;
  event.getByToken(TIBHighTofSimHitsToken_, TIBHighTofSimHits);
  simHitCollection = "TIBHighTof";
  doSimHits(TIBHighTofSimHits, simTracks, simHitCollection, 6, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TIBLowTofSimHits;
  event.getByToken(TIBLowTofSimHitsToken_, TIBLowTofSimHits);
  simHitCollection = "TIBLowTof";
  doSimHits(TIBLowTofSimHits, simTracks, simHitCollection, 7, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TIDHighTofSimHits;
  event.getByToken(TIDHighTofSimHitsToken_, TIDHighTofSimHits);
  simHitCollection = "TIDHighTof";
  doSimHits(TIDHighTofSimHits, simTracks, simHitCollection, 8, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TIDLowTofSimHits;
  event.getByToken(TIDLowTofSimHitsToken_, TIDLowTofSimHits);
  simHitCollection = "TIDLowTof";
  doSimHits(TIDLowTofSimHits, simTracks, simHitCollection, 9, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TOBHighTofSimHits;
  event.getByToken(TOBHighTofSimHitsToken_, TOBHighTofSimHits);
  simHitCollection = "TOBHighTof";
  doSimHits(TOBHighTofSimHits, simTracks, simHitCollection, 10, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> TOBLowTofSimHits;
  event.getByToken(TOBLowTofSimHitsToken_, TOBLowTofSimHits);
  simHitCollection = "TOBLowTof";
  doSimHits(TOBLowTofSimHits, simTracks, simHitCollection, 11, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> CSCSimHits;
  event.getByToken(CSCSimHitsToken_, CSCSimHits);
  simHitCollection = "CSC";
  doSimHits(CSCSimHits, simTracks, simHitCollection, 12, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> DTSimHits;
  event.getByToken(DTSimHitsToken_, DTSimHits);
  simHitCollection = "DT";
  doSimHits(DTSimHits, simTracks, simHitCollection, 13, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);

  edm::Handle<edm::PSimHitContainer> RPCSimHits;
  event.getByToken(RPCSimHitsToken_, RPCSimHits);
  simHitCollection = "RPC";
  doSimHits(RPCSimHits, simTracks, simHitCollection, 14, genRhadronId_0, genRhadronEta_0, genRhadronPhi_0, genRhadronId_1, genRhadronEta_1, genRhadronPhi_1);


}//end analyze

void StopRHadronSimAnalyzer::doSimHits(const edm::Handle<edm::PSimHitContainer> &container, const edm::Handle<edm::SimTrackContainer> &simTracks, string & simHitCollection, int simHitCol, int genRhadronId_0, double genRhadronEta_0, double genRhadronPhi_0, int genRhadronId_1, double genRhadronEta_1, double genRhadronPhi_1)
{
  int nSimHits = 0;

  //loop over sim hits
  if(container.isValid()){
    for(const auto &hit : *container) {
      int partId = abs(hit.particleType());
      if( (partId>1000600 && partId<1000700) || (partId>1006000 && partId<1007000)){ //stop r-hadron produced this sim hit
	nSimHits++;

	LogDebug("StopRHadronSimAnalyzer")<<"sim hit r-hadron with id "<<partId<<" in collection "<<simHitCollection<<", trackId is: "<<hit.trackId();
	//std::cout<<"sim hit r-hadron with id "<<partId<<" in collection "<<simHitCollection<<", trackId is: "<<hit.trackId()<<std::endl;

	oneDHists_.at(simHitCollection+"SimHitRhadronId_10006XX")->Fill(partId);
	oneDHists_.at(simHitCollection+"SimHitRhadronId_1006XXX")->Fill(partId);
	twoDHists_.at("SimHitRhadronId_10006XX_vs_SimHitCollection")->Fill(partId,simHitCol);
	twoDHists_.at("SimHitRhadronId_1006XXX_vs_SimHitCollection")->Fill(partId,simHitCol);

	for(const auto &simTrack : *simTracks) {
	  if(hit.trackId()==simTrack.trackId()){

	    double simTrackEta = simTrack.momentum().eta();
	    double simTrackPhi = simTrack.momentum().phi();
	    string genId = "";
	    if(deltaR(simTrackEta, simTrackPhi, genRhadronEta_0, genRhadronPhi_0)<0.1){
	      if(abs(genRhadronId_0)==1000612) {
		genId = "1000612";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1000622) {
		genId = "1000622";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1000632) {
		genId = "1000632";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1000642) {
		genId = "1000642";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1000652) {
		genId = "1000652";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006113) {
		genId = "1006113";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006211) {
		genId = "1006211";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006213) {
		genId = "1006213";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006223) {
		genId = "1006223";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006311) {
		genId = "1006311";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006313) {
		genId = "1006313";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006321) {
		genId = "1006321";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006323) {
		genId = "1006323";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_0)==1006333) {
		genId = "1006333";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	    }
	    else if(deltaR(simTrackEta, simTrackPhi, genRhadronEta_1, genRhadronPhi_1)<0.1){
	      if(abs(genRhadronId_1)==1000612) {
		genId = "1000612";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1000622) {
		genId = "1000622";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1000632) {
		genId = "1000632";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1000642) {
		genId = "1000642";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1000652) {
		genId = "1000652";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006113) {
		genId = "1006113";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006211) {
		genId = "1006211";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006213) {
		genId = "1006213";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006223) {
		genId = "1006223";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006311) {
		genId = "1006311";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006313) {
		genId = "1006313";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006321) {
		genId = "1006321";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006323) {
		genId = "1006323";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	      else if(abs(genRhadronId_1)==1006333) {
		genId = "1006333";
		fillVsSimHitColHists(genId,partId,simHitCol,nSimHits);
	      }
	    }//end if rhadronid_1 matched to sim track
	  }//end if sim hit track id is the same as sim track id
	}//end loop over sim tracks
      }//end if sim hit particle is a stop r-hadron
    }//end loop over sim hit container
  }//end container is valid
}//end void doSimHits

void StopRHadronSimAnalyzer::fillVsSimHitColHists(string & genId, double partId, int & simHitCol, int nSimHits)
{
  twoDHists_.at("gen"+genId+"_SimHitRhadronId_10006XX_vs_SimHitCollection")->Fill(partId,simHitCol);
  twoDHists_.at("gen"+genId+"_SimHitRhadronId_1006XXX_vs_SimHitCollection")->Fill(partId,simHitCol);

  if(nSimHits==1) oneDHists_.at("gen"+genId+"_SimHitCollection")->Fill(simHitCol); //fill just for first sim hit of each collection
}

void StopRHadronSimAnalyzer::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
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
const reco::Track * StopRHadronSimAnalyzer::getMatchedTrack(const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Track> > &tracks) const
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

DEFINE_FWK_MODULE(StopRHadronSimAnalyzer);

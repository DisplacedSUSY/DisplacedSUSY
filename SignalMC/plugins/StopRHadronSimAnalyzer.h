#ifndef STOPRHADRONSIMANALYZER

#define STOPRHADRONSIMANALYZER

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
#include "SimDataFormats/TrackingHit/interface/PSimHit.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "HepMC/GenEvent.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace std;

class StopRHadronSimAnalyzer : public edm::EDAnalyzer {
 public:
  explicit StopRHadronSimAnalyzer (const edm::ParameterSet &);
  ~StopRHadronSimAnalyzer ();

 private:
  void analyze (const edm::Event &, const edm::EventSetup &);

  //edm::InputTag tracks_;
  edm::InputTag genParticles_;
  edm::InputTag simTracks_;
  edm::InputTag simVertexs_;
  edm::InputTag hepMC_;
  edm::InputTag PixelBarrelHighTofSimHits_;
  edm::InputTag PixelBarrelLowTofSimHits_;
  edm::InputTag PixelEndcapHighTofSimHits_;
  edm::InputTag PixelEndcapLowTofSimHits_;
  edm::InputTag TECHighTofSimHits_;
  edm::InputTag TECLowTofSimHits_;
  edm::InputTag TIBHighTofSimHits_;
  edm::InputTag TIBLowTofSimHits_;
  edm::InputTag TIDHighTofSimHits_;
  edm::InputTag TIDLowTofSimHits_;
  edm::InputTag TOBHighTofSimHits_;
  edm::InputTag TOBLowTofSimHits_;
  edm::InputTag CSCSimHits_;
  edm::InputTag DTSimHits_;
  edm::InputTag RPCSimHits_;

  //edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
  edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
  edm::EDGetTokenT<edm::SimTrackContainer> simTracksToken_;
  edm::EDGetTokenT<edm::SimVertexContainer> simVertexsToken_;
  edm::EDGetTokenT<edm::HepMCProduct> hepMCToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> PixelBarrelHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> PixelBarrelLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> PixelEndcapHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> PixelEndcapLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TECHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TECLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TIBHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TIBLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TIDHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TIDLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TOBHighTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> TOBLowTofSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> CSCSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> DTSimHitsToken_;
  edm::EDGetTokenT<edm::PSimHitContainer> RPCSimHitsToken_;


  //bool cutPythia8Flag_;

  edm::Service<TFileService> fs_;
  map<string, TH1D *> oneDHists_;
  map<string, TH2D *> twoDHists_;

  void getEndVertex (const reco::GenParticle &, TVector3 &) const;
  void doSimHits(const edm::Handle<edm::PSimHitContainer> &, const edm::Handle<edm::SimTrackContainer> &, string &, int, int, double, double, int, double, double);
  void fillVsSimHitColHists(string &, double, int &, int);

  //const reco::Track * getMatchedTrack (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
};

#endif

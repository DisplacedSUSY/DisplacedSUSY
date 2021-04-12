#ifndef STOPRHADRONSIMPATANALYZER

#define STOPRHADRONSIMPATANALYZER

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace std;

class StopRHadronSimPatAnalyzer : public edm::EDAnalyzer {
 public:
  explicit StopRHadronSimPatAnalyzer (const edm::ParameterSet &);
  ~StopRHadronSimPatAnalyzer ();

 private:
  void analyze (const edm::Event &, const edm::EventSetup &);

  edm::InputTag electrons_;
  edm::InputTag muons_;
  edm::InputTag beamspots_;
  edm::InputTag genParticles_;

  edm::EDGetTokenT<vector<pat::Electron> > electronsToken_;
  edm::EDGetTokenT<vector<pat::Muon> > muonsToken_;
  edm::EDGetTokenT<reco::BeamSpot> beamspotsToken_;
  edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

  //bool cutPythia8Flag_;

  edm::Service<TFileService> fs_;
  map<string, TH1D *> oneDHists_;
  map<string, TH2D *> twoDHists_;

  void getEndVertex (const reco::GenParticle &, TVector3 &) const;
  const pat::Electron * getMatchedElectron (const reco::Candidate &, const edm::Handle<vector<pat::Electron> > &) const;
  const pat::Muon * getMatchedMuon (const reco::Candidate &, const edm::Handle<vector<pat::Muon> > &) const;

};

#endif

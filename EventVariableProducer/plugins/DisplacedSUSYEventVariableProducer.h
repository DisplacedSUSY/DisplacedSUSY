#ifndef DisplacedSUSYEVENT_VARIABLE_PRODUCER
#define DisplacedSUSYEVENT_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/L1TGlobal/interface/GlobalAlgBlk.h" //Pre-firing
#include "L1Trigger/L1TGlobal/interface/L1TGlobalUtil.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"

struct OriginalCollections
{

  edm::Handle<reco::BeamSpot>               beamspots;
  edm::Handle<vector<reco::Vertex> >        primaryvertexs;
  edm::Handle<vector<PileupSummaryInfo>>    pileupinfos;
  edm::Handle<edm::TriggerResults>          triggers;

#if DATA_FORMAT_FROM_AOD
  edm::Handle<vector<reco::GsfElectron> >    electrons;
  edm::Handle<vector<reco::PFJet> >          jets;
  edm::Handle<vector<reco::Muon> >           muons;
#elif DATA_FORMAT_FROM_MINIAOD
  edm::Handle<vector<pat::Electron> >       electrons;
  edm::Handle<vector<pat::Jet> >            jets;
  edm::Handle<vector<pat::Muon> >           muons;
#endif

};

struct DispVtx {
  int nDispVtxs;
  double vtxX, vtxY, vtxZ, vtxXErr, vtxYErr, vtxZErr, vtxChisq;

  DispVtx () :
  nDispVtxs(0),
    vtxX(-5000.), vtxY(-5000.), vtxZ(-5000.),
    vtxXErr(-5000.), vtxYErr(-5000.), vtxZErr(-5000.),
    vtxChisq(-5000.)
  {
  }
};


class DisplacedSUSYEventVariableProducer : public EventVariableProducer
  {
    public:
        DisplacedSUSYEventVariableProducer (const edm::ParameterSet &);
        void getOriginalCollections (const unordered_set<string> &objectsToGet, const edm::ParameterSet &collections, OriginalCollections &handles, const edm::Event &event);
        bool passCleaning (double eta, double phi, OriginalCollections &handles);
	~DisplacedSUSYEventVariableProducer ();
        OriginalCollections handles_;

    private:
        void AddVariables(const edm::Event &, const edm::EventSetup &);
        string type_;
	std::vector<std::string> triggerPaths_;
	std::map<std::string, bool> HLTBitsMap;
        edm::EDGetTokenT<vector<TYPE(pileupinfos)> > pileUpInfosToken_;
        edm::EDGetTokenT<TYPE(beamspots)> beamspotsToken_;
        edm::EDGetTokenT<vector<TYPE(primaryvertexs)> > primaryVertexsToken_;
        edm::EDGetTokenT<vector<TYPE(muons)> > muonsToken_;
        edm::EDGetTokenT<vector<TYPE(electrons)> > electronsToken_;
        edm::EDGetTokenT<vector<TYPE(jets)> > jetsToken_;
	edm::EDGetTokenT<edm::TriggerResults> triggersToken_;

	//L1 bits information; thanks to dijet scouting team
	//https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetCaloScoutingTreeProducer.h
	edm::EDGetToken algToken_;
	l1t::L1TGlobalUtil *l1GtUtils_;
	std::vector<std::string> l1Seeds_;
	std::map<std::string, bool> L1BitsMap;
	std::vector<bool> *l1Result_;

	DispVtx getDispVtx(vector<reco::TransientTrack> t_tks);

  };
#endif

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
  edm::Handle<vector<reco::GenParticle>>    hardInteractionMcparticles;

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
        edm::EDGetTokenT<vector<TYPE(hardInteractionMcparticles)> > hardInteractionMcparticlesToken_;

	//L1 bits information; thanks to dijet scouting team
	//https://github.com/CMSDIJET/DijetScoutingRootTreeMaker/blob/master/plugins/DijetCaloScoutingTreeProducer.h
	edm::EDGetToken algToken_;
	l1t::L1TGlobalUtil *l1GtUtils_;
	std::vector<std::string> l1Seeds_;
	std::map<std::string, bool> L1BitsMap;
	std::vector<bool> *l1Result_;

	double beamPipe_x_center_;
	double beamPipe_y_center_;
	double beamPipe_outerR_;
	double beamPipe_innerR_;

	double nearInnerShield_x_center_;
	double nearInnerShield_y_center_;
	double farInnerShield_x_center_;
	double farInnerShield_y_center_;
	double innerShield_outerR_;
	double innerShield_innerR_;

	double bpix_x_center_;
	double bpix_y_center_;
	double bpix_z_center_;
	double bpix_z_halfLength_;
	double bpixL1_outerR_;
	double bpixL1_innerR_;
	double bpixL2_outerR_;
	double bpixL2_innerR_;
	double bpixL3_outerR_;
	double bpixL3_innerR_;
	double bpixL4_outerR_;
	double bpixL4_innerR_;

	double fpix_x_center_;
	double fpix_y_center_;
	double fpix_z_center_;
	double fpixD1_z_center_;
	double fpixD2_z_center_;
	double fpixD3_z_center_;
	double fpix_outerR_;
	double fpix_innerR_;
	double fpix_z_halfThickness_;

	double supportTube_x_center_;
	double supportTube_y_center_;
	double supportTube_outerRX_;
	double supportTube_outerRY_;
	double supportTube_innerRX_;
	double supportTube_innerRY_;

	DispVtx getDispVtx(vector<reco::TransientTrack>);
	bool inRectangle(double, double, double, double, double);
	bool inRectangle(double, double, double, double, double, double);
	bool inCircle(double, double, double, double, double);
	bool inEllipse(double, double, double, double, double, double);
	bool inMaterial(double, double, double);
  };
#endif

#ifndef DisplacedSUSYEVENT_VARIABLE_PRODUCER
#define DisplacedSUSYEVENT_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
struct OriginalCollections
{
  edm::Handle<vector<pat::Electron> >       electrons;
  edm::Handle<vector<pat::Jet> >            jets;
  edm::Handle<vector<pat::Muon> >           muons;
  edm::Handle<reco::BeamSpot>               beamspots;
  edm::Handle<vector<reco::Vertex> >        primaryvertexs;
  edm::Handle<vector<PileupSummaryInfo>>    pileupinfos;
  edm::Handle<edm::TriggerResults>          triggers;
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
        void AddVariables(const edm::Event &);
        string type_;
	    string triggerPath_;
	    double triggerScaleFactor_;
        edm::EDGetTokenT<vector<TYPE(pileupinfos)> > pileUpInfosToken_;
        edm::EDGetTokenT<TYPE(beamspots)> beamspotsToken_;
        edm::EDGetTokenT<vector<TYPE(primaryvertexs)> > primaryVertexsToken_;
        edm::EDGetTokenT<vector<TYPE(muons)> > muonsToken_;
        edm::EDGetTokenT<vector<TYPE(electrons)> > electronsToken_;
        edm::EDGetTokenT<vector<TYPE(jets)> > jetsToken_;
	    edm::EDGetTokenT<edm::TriggerResults> triggersToken_;
  };
#endif

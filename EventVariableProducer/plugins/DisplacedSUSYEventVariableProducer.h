#ifndef DisplacedSUSYEVENT_VARIABLE_PRODUCER
#define DisplacedSUSYEVENT_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
struct OriginalCollections
{
  edm::Handle<osu::Beamspot>                beamspots;
  edm::Handle<vector<osu::Bxlumi> >         bxlumis;
  edm::Handle<vector<osu::Electron> >       electrons;
  edm::Handle<vector<osu::Event> >          events;
  edm::Handle<vector<osu::Genjet> >         genjets;
  edm::Handle<vector<pat::Jet> >            jets;
  edm::Handle<vector<osu::Basicjet> >       basicjets;
  edm::Handle<vector<CandidateJet> >        candjets;
  edm::Handle<vector<osu::Candele> >        candeles;
  edm::Handle<vector<osu::Mcparticle> >     mcparticles;
  edm::Handle<vector<osu::Met> >            mets;
  edm::Handle<vector<osu::Muon> >           muons;
  edm::Handle<vector<osu::Photon> >         photons;
  edm::Handle<vector<reco::Vertex> >  primaryvertexs;
  edm::Handle<vector<osu::Supercluster> >   superclusters;
  edm::Handle<vector<osu::Tau> >            taus;
  edm::Handle<vector<osu::Track> >          tracks;
  edm::Handle<vector<osu::Trigobj> >        trigobjs;
  vector<edm::Handle<osu::Uservariable> >   uservariables;
  vector<edm::Handle<osu::Eventvariable> >  eventvariables;

  edm::Handle<TYPE(triggers)>                 triggers;
  edm::Handle<TYPE(prescales)>                prescales;
  edm::Handle<TYPE(generatorweights)>         generatorweights;
};

class DisplacedSUSYEventVariableProducer : public EventVariableProducer
  {
    public:
        DisplacedSUSYEventVariableProducer (const edm::ParameterSet &);
        void getOriginalCollections (const unordered_set<string> &objectsToGet, const edm::ParameterSet &collections, OriginalCollections &handles, const edm::Event &event);
	~DisplacedSUSYEventVariableProducer ();
        OriginalCollections handles_;

    private:
        void AddVariables(const edm::Event &);
  };
#endif

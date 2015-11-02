#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisplacedSUSY/EventVariableProducer/plugins/DisplacedSUSYEventVariableProducer.h"

DisplacedSUSYEventVariableProducer::DisplacedSUSYEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

DisplacedSUSYEventVariableProducer::~DisplacedSUSYEventVariableProducer() {}

void
DisplacedSUSYEventVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == MINI_AOD_CUSTOM
  objectsToGet_.insert ("candjets");
  objectsToGet_.insert ("primaryvertexs");
  getOriginalCollections (objectsToGet_, collections_, handles_, event);
  double sumJetPt = 0;
  double numLooseBjets = 0; 
  double numMediumBjets = 0; 
  double numTightBjets = 0; 
  double numPV = 0;
  for (const auto &candjet1 : *handles_.candjets) {
    //if(getMember(candjet1, "pt") >= 25 && abs(getMember(candjet1, "eta")) <= 2.4 && getMember(candjet1,"neutralHadronEnergyFraction") < 0.99 && getMember(candjet1,"chargedEmEnergyFraction") < 0.99 && getMember(candjet1, "neutralEmEnergyFraction") < 0.99 && getMember(candjet1, "numberOfDaughters") > 1 && getMember(candjet1, "chargedHadronEnergyFraction") > 0.0 && getMember(candjet1, "chargedMultiplicity") > 0.0 )  
     // sumJetPt = sumJetPt + getMember(candjet1, "pt");
    //if(getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.605)
    //  numLooseBjets = numLooseBjets + 1;
    //if(getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.89)
    //  numMediumBjets = numMediumBjets + 1;
    //if(getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.97)
    //  numTightBjets = numTightBjets + 1;
    if(candjet1.pt() >= 25)
      sumJetPt = sumJetPt + candjet1.pt();
  }
 for (const auto &pv1 : *handles_.primaryvertexs) {
    if(pv1.isValid())
      numPV = numPV + 1;
  }
  (*eventvariables)["sumJetPt"] = sumJetPt;
  (*eventvariables)["numLooseBjets"] = numLooseBjets;
  (*eventvariables)["numMediumBjets"] = numMediumBjets;
  (*eventvariables)["numTightBjets"] = numTightBjets;
  (*eventvariables)["numPV"] = numPV;
 # endif
 }  
void
DisplacedSUSYEventVariableProducer::getOriginalCollections (const unordered_set<string> &objectsToGet, const edm::ParameterSet &collections, OriginalCollections &handles, const edm::Event &event)
{

  //////////////////////////////////////////////////////////////////////////////
  // Retrieve each object collection which we need and print a warning if it is
  // missing.
  //////////////////////////////////////////////////////////////////////////////
  if  (VEC_CONTAINS  (objectsToGet,  "beamspots")         &&  collections.exists  ("beamspots"))         anatools::getCollection  (collections.getParameter<edm::InputTag>  ("beamspots"),         handles.beamspots,         event);
  if  (VEC_CONTAINS  (objectsToGet,  "bxlumis")           &&  collections.exists  ("bxlumis"))           anatools::getCollection  (collections.getParameter<edm::InputTag>  ("bxlumis"),           handles.bxlumis,           event);
  if  (VEC_CONTAINS  (objectsToGet,  "electrons")         &&  collections.exists  ("electrons"))         anatools::getCollection  (collections.getParameter<edm::InputTag>  ("electrons"),         handles.electrons,         event);
  if  (VEC_CONTAINS  (objectsToGet,  "events")            &&  collections.exists  ("events"))            anatools::getCollection  (collections.getParameter<edm::InputTag>  ("events"),            handles.events,            event);
  if  (VEC_CONTAINS  (objectsToGet,  "genjets")           &&  collections.exists  ("genjets"))           anatools::getCollection  (collections.getParameter<edm::InputTag>  ("genjets"),           handles.genjets,           event);
  if  (VEC_CONTAINS  (objectsToGet,  "jets")              &&  collections.exists  ("jets"))              anatools::getCollection  (collections.getParameter<edm::InputTag>  ("jets"),              handles.jets,              event);
  if  (VEC_CONTAINS  (objectsToGet,  "basicjets")         &&  collections.exists  ("basicjets"))         anatools::getCollection  (collections.getParameter<edm::InputTag>  ("basicjets"),         handles.basicjets,         event);
  if  (VEC_CONTAINS  (objectsToGet,  "candjets")          &&  collections.exists  ("candjets"))          anatools::getCollection  (collections.getParameter<edm::InputTag>  ("candjets"),          handles.candjets,          event);
  if  (VEC_CONTAINS  (objectsToGet,  "candeles")          &&  collections.exists  ("candeles"))          anatools::getCollection  (collections.getParameter<edm::InputTag>  ("candeles"),          handles.candeles,          event);
  if  (VEC_CONTAINS  (objectsToGet,  "generatorweights")  &&  collections.exists  ("generatorweights"))  anatools::getCollection  (collections.getParameter<edm::InputTag>  ("generatorweights"),  handles.generatorweights,  event);
  if  (VEC_CONTAINS  (objectsToGet,  "mcparticles")       &&  collections.exists  ("mcparticles"))       anatools::getCollection  (collections.getParameter<edm::InputTag>  ("mcparticles"),       handles.mcparticles,       event);
  if  (VEC_CONTAINS  (objectsToGet,  "mets")              &&  collections.exists  ("mets"))              anatools::getCollection  (collections.getParameter<edm::InputTag>  ("mets"),              handles.mets,              event);
  if  (VEC_CONTAINS  (objectsToGet,  "muons")             &&  collections.exists  ("muons"))             anatools::getCollection  (collections.getParameter<edm::InputTag>  ("muons"),             handles.muons,             event);
  if  (VEC_CONTAINS  (objectsToGet,  "photons")           &&  collections.exists  ("photons"))           anatools::getCollection  (collections.getParameter<edm::InputTag>  ("photons"),           handles.photons,           event);
  if  (VEC_CONTAINS  (objectsToGet,  "prescales")         &&  collections.exists  ("prescales"))         anatools::getCollection  (collections.getParameter<edm::InputTag>  ("prescales"),         handles.prescales,         event);
  if  (VEC_CONTAINS  (objectsToGet,  "primaryvertexs")    &&  collections.exists  ("primaryvertexs"))    anatools::getCollection  (collections.getParameter<edm::InputTag>  ("primaryvertexs"),    handles.primaryvertexs,    event);
  if  (VEC_CONTAINS  (objectsToGet,  "superclusters")     &&  collections.exists  ("superclusters"))     anatools::getCollection  (collections.getParameter<edm::InputTag>  ("superclusters"),     handles.superclusters,     event);
  if  (VEC_CONTAINS  (objectsToGet,  "taus")              &&  collections.exists  ("taus"))              anatools::getCollection  (collections.getParameter<edm::InputTag>  ("taus"),              handles.taus,              event);
  if  (VEC_CONTAINS  (objectsToGet,  "tracks")            &&  collections.exists  ("tracks"))            anatools::getCollection  (collections.getParameter<edm::InputTag>  ("tracks"),            handles.tracks,            event);
  if  (VEC_CONTAINS  (objectsToGet,  "triggers")          &&  collections.exists  ("triggers"))          anatools::getCollection  (collections.getParameter<edm::InputTag>  ("triggers"),          handles.triggers,          event);
  if  (VEC_CONTAINS  (objectsToGet,  "trigobjs")          &&  collections.exists  ("trigobjs"))          anatools::getCollection  (collections.getParameter<edm::InputTag>  ("trigobjs"),          handles.trigobjs,          event);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

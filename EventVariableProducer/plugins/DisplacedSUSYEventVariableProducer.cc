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
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);
  double sumJetPt = 0;
  double numLooseBjets = 0; 
  double numMediumBjets = 0; 
  double numTightBjets = 0; 
  double numPV = 0;
  for (const auto &candjet1 : *handles_.candjets) {
    if(anatools::getMember(candjet1, "pt") >= 25 && abs(anatools::getMember(candjet1, "eta")) <= 2.4 && anatools::getMember(candjet1,"neutralHadronEnergyFraction") < 0.99 && anatools::getMember(candjet1,"chargedEmEnergyFraction") < 0.99 && anatools::getMember(candjet1, "neutralEmEnergyFraction") < 0.99 && anatools::getMember(candjet1, "numberOfDaughters") > 1 && anatools::getMember(candjet1, "chargedHadronEnergyFraction") > 0.0 && anatools::getMember(candjet1, "chargedMultiplicity") > 0.0 )  
      sumJetPt = sumJetPt + anatools::getMember(candjet1, "pt");
    if(anatools::getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.605)
      numLooseBjets = numLooseBjets + 1;
    if(anatools::getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.89)
      numMediumBjets = numMediumBjets + 1;
    if(anatools::getMember(candjet1, "pfCombinedInclusiveSecondaryVertexV2BJetTags") >= 0.97)
      numTightBjets = numTightBjets + 1;
  }
 for (const auto &pv1 : *handles_.primaryvertexs) {
    if(anatools::getMember(pv1,"isValid"))
      numPV = numPV + 1;
  }
  (*eventvariables)["sumJetPt"] = sumJetPt;
  (*eventvariables)["numLooseBjets"] = numLooseBjets;
  (*eventvariables)["numMediumBjets"] = numMediumBjets;
  (*eventvariables)["numTightBjets"] = numTightBjets;
  (*eventvariables)["numPV"] = numPV;
#  endif
  }  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

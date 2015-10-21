#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisplacedSUSY/EventVariableProducer/plugins/DisplacedSUSYEventVariableProducer.h"

DisplacedSUSYEventVariableProducer::DisplacedSUSYEventVariableProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg) {}

DisplacedSUSYEventVariableProducer::~DisplacedSUSYEventVariableProducer() {}

void
DisplacedSUSYEventVariableProducer::AddVariables (const edm::Event &event) {
#if DATA_FORMAT == MINI_AOD_CUSTOM

  objectsToGet_.insert ("candjets");
  anatools::getRequiredCollections (objectsToGet_, collections_, handles_, event);
  double value = 0;
  for (const auto &candjet1 : *handles_.candjets) {
    value = value + anatools::getMember(candjet1, "pt");
  }
  (*eventvariables)["sumJetPt"] = value;
#  endif
  }  
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYEventVariableProducer);

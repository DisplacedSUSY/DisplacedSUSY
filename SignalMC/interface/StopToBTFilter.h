#ifndef STOP_TO_BT_FILTER

#define STOP_TO_BT_FILTER

#include <string>
#include <vector>
#include <map>

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

using namespace std;

class StopToBTFilter : public edm::EDFilter
{
  public:
    StopToBTFilter (const edm::ParameterSet &);
    virtual ~StopToBTFilter ();
    bool filter (edm::Event &, edm::EventSetup const &);

  private:
    edm::InputTag genParticles_;
};

#endif

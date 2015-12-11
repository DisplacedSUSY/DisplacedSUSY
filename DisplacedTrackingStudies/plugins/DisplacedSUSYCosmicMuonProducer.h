#ifndef MUON_PRODUCER
#define MUON_PRODUCER

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "OSUT3Analysis/Collections/interface/Muon.h"

class DisplacedSUSYCosmicMuonProducer : public edm::EDProducer
{
  public:
    DisplacedSUSYCosmicMuonProducer (const edm::ParameterSet &);
    ~DisplacedSUSYCosmicMuonProducer ();

    void produce (edm::Event &, const edm::EventSetup &);
    bool PassCosmicSelection (osu::Muon muon1, osu::Muon muon2); 
  private:
    ////////////////////////////////////////////////////////////////////////////
    // Private variables initialized by the constructor.
    ////////////////////////////////////////////////////////////////////////////
    edm::InputTag      muons_;
    edm::ParameterSet  cfg_;
    ////////////////////////////////////////////////////////////////////////////

    // Payload for this EDFilter.
    auto_ptr<vector<osu::Muon> > pl_;
};

#endif

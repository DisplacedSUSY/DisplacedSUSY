#include "DisplacedSUSY/DisplacedTrackingStudies/plugins/DisplacedSUSYCosmicMuonProducer.h"

#if IS_VALID(muons)
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

DisplacedSUSYCosmicMuonProducer::DisplacedSUSYCosmicMuonProducer (const edm::ParameterSet &cfg) :
  muons_ (cfg.getParameter<edm::InputTag> ("muons")),
  cfg_ (cfg)
{
  produces<vector<osu::Muon> > ();
}

DisplacedSUSYCosmicMuonProducer::~DisplacedSUSYCosmicMuonProducer ()
{
}

void
DisplacedSUSYCosmicMuonProducer::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<osu::Muon>> collection;
  if (!anatools::getCollection (muons_, collection, event, false))
    return;
  edm::Handle<vector<osu::Mcparticle> > particles;
  anatools::getCollection (edm::InputTag ("", ""), particles, event);

  pl_ = auto_ptr<vector<osu::Muon> > (new vector<osu::Muon> ());
  for (const auto &object : *collection)
    {
        osu::Muon muon1 (object, particles, cfg_);
        for (const auto &object : *collection)
         { 
           osu::Muon muon2 (object, particles, cfg_);
           if(muon1.isGlobalMuon() && muon2.isGlobalMuon() && PassCosmicSelection(muon1,muon2) && muon1.phi() != muon2.phi() && muon1.pt() > 30)
             {
               pl_->push_back (muon1);
               break;
             }
         }
    }

  event.put (pl_);
  pl_.reset ();
}

bool 
DisplacedSUSYCosmicMuonProducer::PassCosmicSelection(osu::Muon muon1, osu::Muon muon2)
{
  bool matched = false;
  static const double pi = 3.1415926535897932384626433832795028841971693993751058;
  TVector3 threeVector1(muon1.px(), muon1.py(), muon1.pz());
  TVector3 threeVector2(muon2.px(), muon2.py(), muon2.pz());
  double value = (pi-threeVector1.Angle(threeVector2));
  if(log(value) < -2.8){matched = true;} 
  return matched;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DisplacedSUSYCosmicMuonProducer);

#endif

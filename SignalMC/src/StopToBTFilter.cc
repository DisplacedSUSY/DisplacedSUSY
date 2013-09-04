#include "DisplacedSUSY/SignalMC/interface/StopToBTFilter.h"

StopToBTFilter::StopToBTFilter (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
}

StopToBTFilter::~StopToBTFilter ()
{
}

bool
StopToBTFilter::filter (edm::Event &event, edm::EventSetup const &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  int quarkID0 = -1, quarkID1 = -1,
      leptonID0 = -1, leptonID1 = -1;
  bool useQuarks = true, useLeptons = true;
  for (vector<reco::GenParticle>::const_iterator genParticle = genParticles->begin (); genParticle != genParticles->end (); genParticle++)
    {
      if (abs (genParticle->pdgId ()) != 1000006)
        continue;
      int quarkID = -1, leptonID = -1;
      for (unsigned i = 0; i < genParticle->numberOfDaughters (); i++)
        {
          int id = abs (genParticle->daughter (i)->pdgId ());
          if (id >= 5 && id <= 6)
            {
              if (quarkID < 0)
                quarkID = id;
              else
                useQuarks = false;
            }
          if (id >= 11 && id <= 16)
            {
              if (leptonID < 0)
                leptonID = id;
              else
                useLeptons = false;
            }
        }

      if (quarkID0 < 0)
        quarkID0 = quarkID;
      else
        quarkID1 = quarkID;
      if (leptonID0 < 0)
        leptonID0 = leptonID;
      else
        leptonID1 = leptonID;
    }

  bool pass = false;
  if (useQuarks)
    pass = quarkID0 != quarkID1;
  else if (useLeptons)
    pass = ((leptonID0 == 11 || leptonID0 == 13 || leptonID0 == 15) && (leptonID1 == 12 || leptonID1 == 14 || leptonID1 == 16))
        || ((leptonID1 == 11 || leptonID1 == 13 || leptonID1 == 15) && (leptonID0 == 12 || leptonID0 == 14 || leptonID0 == 16));

  return pass;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(StopToBTFilter);

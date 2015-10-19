// -*- C++ -*-
//
// Package:    DisplacedSUSY/CandidateJetProducer
// Class:      CandidateJetProducer
// 
/**\class CandidateJetProducer CandidateJetProducer.cc DisplacedSUSY/CandidateJetProducer/plugins/CandidateJetProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Bingxuan Liu
//         Created:  Tue, 06 Oct 2015 17:19:53 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DisplacedSUSY/CandidateJetProducer/interface/CandidateJet.h"
using namespace std; 
//
// class declaration
//

class CandidateJetProducer : public edm::EDProducer {
   public:
      explicit CandidateJetProducer(const edm::ParameterSet&);
      ~CandidateJetProducer();
      void setVariables(CandidateJet& candJet, const pat::Jet& jet);
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      edm::InputTag patJet_; 
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
};

CandidateJetProducer::CandidateJetProducer(const edm::ParameterSet& iConfig):
   patJet_               (iConfig.getParameter <edm::InputTag>("patJet"))
{
   produces<vector<CandidateJet> > (); 

}


CandidateJetProducer::~CandidateJetProducer()
{
}
void
CandidateJetProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace pat;
   edm::Handle<vector<pat::Jet>> jets;
   iEvent.getByLabel (patJet_, jets);
   
   auto_ptr<vector<CandidateJet> > candJets (new vector<CandidateJet> ()); 
   for (const auto &jet : *jets) {
    CandidateJet candJet(jet);  
    setVariables(candJet,jet);
    candJets->push_back (candJet);  
   }
   iEvent.put (candJets);
}

void
CandidateJetProducer::setVariables(CandidateJet& candJet, const pat::Jet& jet)
{
  candJet.set_pfCombinedInclusiveSecondaryVertexV2BJetTags(jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"));
  candJet.set_pfCombinedSecondaryVertexV2BJetTags(jet.bDiscriminator("pfCombinedSecondaryVertexV2BJetTags"));
}

// ------------ method called once each job just before starting event loop  ------------
void 
CandidateJetProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CandidateJetProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
CandidateJetProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
CandidateJetProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
CandidateJetProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
CandidateJetProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CandidateJetProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateJetProducer);

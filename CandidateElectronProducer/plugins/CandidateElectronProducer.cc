// -*- C++ -*-
//
// Package:    DisplacedSUSY/CandidateElectronProducer
// Class:      CandidateElectronProducer
// 
/**\class CandidateElectronProducer CandidateElectronProducer.cc DisplacedSUSY/CandidateElectronProducer/plugins/CandidateElectronProducer.cc

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
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"
#include "DisplacedSUSY/CandidateElectronProducer/interface/CandidateElectron.h"
#include "EgammaAnalysis/ElectronTools/interface/EGammaCutBasedEleId.h"
#include "EgammaAnalysis/ElectronTools/interface/ElectronEffectiveArea.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
using namespace std;
//
// class declaration
//

class CandidateElectronProducer : public edm::EDProducer {
   public:
      explicit CandidateElectronProducer(const edm::ParameterSet&);
      ~CandidateElectronProducer();
      void setVariables(CandidateElectron& candEle, const reco::GsfElectron& electron, const double &rho, const reco::BeamSpot &beamSpot, const edm::Handle<reco::ConversionCollection> &conversions);
      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      edm::InputTag beamSpot_;
      edm::InputTag conversions_;
      edm::EDGetToken electronsMiniAODToken_;
      edm::InputTag rho_;
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
};

CandidateElectronProducer::CandidateElectronProducer(const edm::ParameterSet& iConfig):
   beamSpot_               (iConfig.getParameter <edm::InputTag>("beamSpot")),
   conversions_            (iConfig.getParameter<edm::InputTag>("conversions")),
   rho_                    (iConfig.getParameter<edm::InputTag>("rho"))
{
   produces<vector<CandidateElectron> > ();
   electronsMiniAODToken_ = mayConsume<edm::View<reco::GsfElectron> >(iConfig.getParameter<edm::InputTag>("electronsMiniAOD"));

}


CandidateElectronProducer::~CandidateElectronProducer()
{
}
void
CandidateElectronProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace reco;
   edm::Handle<edm::View<reco::GsfElectron> > electrons;
   iEvent.getByToken(electronsMiniAODToken_,electrons);
   edm::Handle<reco::ConversionCollection> conversions;
   iEvent.getByLabel (conversions_, conversions);
   edm::Handle<reco::BeamSpot> beamSpot;
   iEvent.getByLabel (beamSpot_, beamSpot);
   edm::Handle<double> rho;
   iEvent.getByLabel (rho_, rho);

   auto_ptr<vector<CandidateElectron> > candElectrons (new vector<CandidateElectron> ());
   for (const auto &electron : *electrons) {
    CandidateElectron candElectron(electron);
    setVariables(candElectron, electron, *rho, *beamSpot, conversions);
    candElectrons->push_back (candElectron);
   }
   iEvent.put (candElectrons);
}

void
CandidateElectronProducer::setVariables(CandidateElectron& candElectron, const reco::GsfElectron& electron, const double &rho, const reco::BeamSpot &beamSpot, const edm::Handle<reco::ConversionCollection> &conversions)
{
  candElectron.set_rho((float)(rho));
  candElectron.set_vtxFitConversion(ConversionTools::hasMatchedConversion(electron, conversions, beamSpot.position()));
  candElectron.set_missingInnerHits(electron.gsfTrack()->hitPattern ().numberOfHits(reco::HitPattern::MISSING_INNER_HITS));
  float effectiveArea = 0;
  if(abs(electron.superCluster()->eta()) >= 0.0000 && abs(electron.superCluster()->eta()) < 1.0000)
    effectiveArea = 0.1752;
  if(abs(electron.superCluster()->eta()) >= 1.0000 && abs(electron.superCluster()->eta()) < 1.4790)
    effectiveArea = 0.1862;
  if(abs(electron.superCluster()->eta()) >= 1.4790 && abs(electron.superCluster()->eta()) < 2.0000)
    effectiveArea = 0.1411;
  if(abs(electron.superCluster()->eta()) >= 2.0000 && abs(electron.superCluster()->eta()) < 2.2000)
    effectiveArea = 0.1534;
  if(abs(electron.superCluster()->eta()) >= 2.2000 && abs(electron.superCluster()->eta()) < 2.3000)
    effectiveArea = 0.1903;
  if(abs(electron.superCluster()->eta()) >= 2.3000 && abs(electron.superCluster()->eta()) < 2.4000)
    effectiveArea = 0.2243;
  if(abs(electron.superCluster()->eta()) >= 2.4000 && abs(electron.superCluster()->eta()) < 5.0000)
    effectiveArea = 0.2687;
  candElectron.set_AEff(effectiveArea);
}

// ------------ method called once each job just before starting event loop  ------------
void
CandidateElectronProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
CandidateElectronProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
CandidateElectronProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
CandidateElectronProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
CandidateElectronProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
CandidateElectronProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CandidateElectronProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateElectronProducer);

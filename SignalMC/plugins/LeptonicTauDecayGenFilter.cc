#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"

#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class LeptonicTauDecayGenFilter : public edm::stream::EDFilter<> {
public:
  explicit LeptonicTauDecayGenFilter(const edm::ParameterSet&);
  ~LeptonicTauDecayGenFilter() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginStream(edm::StreamID) override;
  bool filter(edm::Event&, const edm::EventSetup&) override;
  void endStream() override;

  edm::InputTag inputTag_;
  edm::EDGetTokenT<reco::GenParticleCollection> genParticleCollection_;

  edm::Handle<reco::GenParticleCollection> gen_handle;

  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  // ----------member data ---------------------------
};

LeptonicTauDecayGenFilter::LeptonicTauDecayGenFilter(const edm::ParameterSet& iConfig) {
  inputTag_ = iConfig.getParameter<edm::InputTag>("inputTag");
  genParticleCollection_ = consumes<reco::GenParticleCollection>(inputTag_);
}

LeptonicTauDecayGenFilter::~LeptonicTauDecayGenFilter() {}

bool LeptonicTauDecayGenFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  iEvent.getByToken(genParticleCollection_, gen_handle);

  int nLeptonicDecays = 0;
  int nTaus = 0;

  for (unsigned int i = 0; i < gen_handle->size(); i++) {
    const reco::GenParticle gen_particle = (*gen_handle)[i];

    if (abs(gen_particle.pdgId()) == 15 && gen_particle.status()==8){
      //std::cout << "for event number "<<iEvent.id().event()<<std::endl;
      //std::cout << "pdgId " << gen_particle.pdgId() << std::endl;
      //std::cout << "nDaughters " << gen_particle.numberOfDaughters() << std::endl;

      nTaus++;
      // Check if tau decays leptonically
      for(size_t j=0; j<gen_particle.numberOfDaughters(); j++){
	const reco::Candidate* daughterOfTau = gen_particle.daughter(j);
	int daughterOfTauPdgId = abs(daughterOfTau->pdgId());

	if((daughterOfTauPdgId==11 || daughterOfTauPdgId==13) && daughterOfTau->pt()>10. && abs(daughterOfTau->eta())<3.){
	  //std::cout << "daughter pdgid " << daughterOfTauPdgId <<std::endl;
	  //std::cout << "daughter pt " << daughterOfTau->pt() <<std::endl;
	  //std::cout << "daughter eta " << daughterOfTau->eta() <<std::endl;
	  nLeptonicDecays++;
	}
      } //end loop over tau daughters
    }//end if gen particle is a tau
  }//end loop over gen particles

  std::cout<<" nTaus is: "<<nTaus<<std::endl;
  std::cout<<" nLeptonicDecays is: "<<nLeptonicDecays<<std::endl;
  //need each tau to decay leptonically
  if(nLeptonicDecays>1) return true;
  else return false;

}
// ------------ method called once each stream before processing any runs, lumis or events  ------------
void LeptonicTauDecayGenFilter::beginStream(edm::StreamID) {}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void LeptonicTauDecayGenFilter::endStream() {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void LeptonicTauDecayGenFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(LeptonicTauDecayGenFilter);

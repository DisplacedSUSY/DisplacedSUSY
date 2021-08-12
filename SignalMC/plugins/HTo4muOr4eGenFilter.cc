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

class HTo4muOr4eGenFilter : public edm::stream::EDFilter<> {
public:
  explicit HTo4muOr4eGenFilter(const edm::ParameterSet&);
  ~HTo4muOr4eGenFilter() override;

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

HTo4muOr4eGenFilter::HTo4muOr4eGenFilter(const edm::ParameterSet& iConfig) {
  inputTag_ = iConfig.getParameter<edm::InputTag>("inputTag");
  genParticleCollection_ = consumes<reco::GenParticleCollection>(inputTag_);
}

HTo4muOr4eGenFilter::~HTo4muOr4eGenFilter() {}

bool HTo4muOr4eGenFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup) {
  iEvent.getByToken(genParticleCollection_, gen_handle);

  int nScalars = 0;
  int nElectrons = 0;
  int nMuons = 0;

  for (unsigned int i = 0; i < gen_handle->size(); i++) {
    const reco::GenParticle gen_particle = (*gen_handle)[i];

    if (abs(gen_particle.pdgId()) == 9000006){
      //std::cout << "for event number "<<iEvent.id().event()<<std::endl;
      //std::cout << "pdgId " << gen_particle.pdgId() << std::endl;
      //std::cout << "nDaughters " << gen_particle.numberOfDaughters() << std::endl;

      nScalars++;
      // Check if scalar decays to electrons or muons
      for(size_t j=0; j<gen_particle.numberOfDaughters(); j++){
	const reco::Candidate* daughterOfScalar = gen_particle.daughter(j);
	int daughterOfScalarPdgId = abs(daughterOfScalar->pdgId());

	if(daughterOfScalarPdgId==11){
	  //std::cout << "daughter pdgid " << daughterOfScalarPdgId <<std::endl;
	  //std::cout << "daughter pt " << daughterOfScalar->pt() <<std::endl;
	  //std::cout << "daughter eta " << daughterOfScalar->eta() <<std::endl;
	  nElectrons++;
	}
	else if(daughterOfScalarPdgId==13) {
	  nMuons++;
	}

      } //end loop over tau daughters
    }//end if gen particle is a tau
  }//end loop over gen particles

  std::cout<<" nScalars is: "<<nScalars<<std::endl;
  std::cout<<" nElectrons is: "<<nElectrons<<std::endl;
  std::cout<<" nMuons is: "<<nMuons<<std::endl;

  //need both scalars to decay to 2 electrons each, or both scalars to decay to 2 muons each
  if(nElectrons>3 || nMuons>3){
    std::cout<<" pass filter!"<<std::endl;
    return true;
  }
  else return false;

}
// ------------ method called once each stream before processing any runs, lumis or events  ------------
void HTo4muOr4eGenFilter::beginStream(edm::StreamID) {}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void HTo4muOr4eGenFilter::endStream() {}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void HTo4muOr4eGenFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(HTo4muOr4eGenFilter);

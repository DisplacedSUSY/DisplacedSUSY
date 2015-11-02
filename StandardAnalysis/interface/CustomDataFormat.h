#ifndef CUSTOM_DATA_FORMAT
  
  #define  beamspots_TYPE         reco::BeamSpot
  #define  bxlumis_TYPE           INVALID_TYPE
  #define  electrons_TYPE         pat::Electron
  #define  events_TYPE            INVALID_TYPE
  #define  genjets_TYPE           reco::GenJet
  #define  basicjets_TYPE         pat::Jet
  #define  jets_TYPE              pat::Jet
  #define  bjets_TYPE             INVALID_TYPE
  #define  candeles_TYPE          CandidateElectron
  #define  candjets_TYPE          CandidateJet
  #define  mcparticles_TYPE       pat::PackedGenParticle
  #define  mets_TYPE              pat::MET
  #define  muons_TYPE             pat::Muon
  #define  photons_TYPE           pat::Photon
  #define  primaryvertexs_TYPE    reco::Vertex
  #define  superclusters_TYPE     reco::SuperCluster
  #define  taus_TYPE              pat::Tau
  #define  tracks_TYPE            INVALID_TYPE
  #define  trigobjs_TYPE          pat::TriggerObjectStandAlone
  #define  uservariables_TYPE     VariableProducerPayload
  #define  eventvariables_TYPE    EventVariableProducerPayload

  #define  triggers_TYPE          edm::TriggerResults
  #define  prescales_TYPE         pat::PackedTriggerPrescales
  #define  generatorweights_TYPE  GenEventInfoProduct

  #define  bxlumis_INVALID
  #define  events_INVALID
  #define  tracks_INVALID
  #define  bjets_INVALID

  #include "DataFormats/BeamSpot/interface/BeamSpot.h"
  #include "DataFormats/Common/interface/TriggerResults.h"
  #include "DataFormats/EgammaReco/interface/SuperCluster.h"
  #include "DataFormats/JetReco/interface/BasicJet.h"
  #include "DataFormats/JetReco/interface/GenJet.h"
  #include "DataFormats/PatCandidates/interface/Electron.h"
  #include "DataFormats/PatCandidates/interface/Jet.h"
  #include "DataFormats/PatCandidates/interface/MET.h"
  #include "DataFormats/PatCandidates/interface/Muon.h"
  #include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
  #include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
  #include "DataFormats/PatCandidates/interface/Photon.h"
  #include "DataFormats/PatCandidates/interface/Tau.h"
  #include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
  #include "DataFormats/VertexReco/interface/Vertex.h"
  #include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
  #include "DisplacedSUSY/CandidateElectronProducer/interface/CandidateElectron.h"
  #include "DisplacedSUSY/CandidateJetProducer/interface/CandidateJet.h"


#endif

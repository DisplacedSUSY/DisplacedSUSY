#ifndef CUSTOM_DATA_FORMAT

  #include "OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h"

  #undef   candeles_TYPE
  #undef   candjets_TYPE

  #undef   candeles_INVALID
  #undef   candjets_INVALID

  #define  candeles_TYPE          CandidateElectron
  #define  candjets_TYPE          CandidateJet

  #include "DisplacedSUSY/CandidateElectronProducer/interface/CandidateElectron.h"
  #include "DisplacedSUSY/CandidateJetProducer/interface/CandidateJet.h"

#endif

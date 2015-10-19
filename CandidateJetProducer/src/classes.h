#include "DataFormats/Common/interface/Wrapper.h"
#include "DisplacedSUSY/CandidateJetProducer/interface/CandidateJet.h"

namespace {
  struct DisplacedSUSY_CandidateJetProducer {
    CandidateJet                         candidateJet0;
    vector<CandidateJet>                 candidateJet1;
    edm::Wrapper<CandidateJet>           candidateJet2;
    edm::Wrapper<vector<CandidateJet> >  candidateJet3;
  };
}

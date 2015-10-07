#include "DataFormats/Common/interface/Wrapper.h"
#include "DisplacedSUSY/CandidateElectronProducer/interface/CandidateElectron.h"

namespace {
  struct DisplacedSUSY_CandidateElectronProducer {
    CandidateElectron                         candidateElectron0;
    vector<CandidateElectron>                 candidateElectron1;
    edm::Wrapper<CandidateElectron>           candidateElectron2;
    edm::Wrapper<vector<CandidateElectron> >  candidateElectron3;
  };
}

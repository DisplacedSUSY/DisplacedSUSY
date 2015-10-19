#ifndef CANDIDATEJET_H
#define CANDIDATEJET_H

#include "DataFormats/PatCandidates/interface/Jet.h"

using namespace std;

class CandidateJet : public pat::Jet
{
  public:
    CandidateJet ();
    CandidateJet (const pat::Jet &);
    ~CandidateJet ();

    const float pfCombinedSecondaryVertexV2BJetTags () const;
    const float pfCombinedInclusiveSecondaryVertexV2BJetTags () const;
    void set_pfCombinedSecondaryVertexV2BJetTags (float value) { pfCombinedSecondaryVertexV2BJetTags_  = value; }  
    void set_pfCombinedInclusiveSecondaryVertexV2BJetTags (float value) { pfCombinedInclusiveSecondaryVertexV2BJetTags_  = value; }  
  private:
    float pfCombinedSecondaryVertexV2BJetTags_;
    float pfCombinedInclusiveSecondaryVertexV2BJetTags_;
};

#endif

#include "DisplacedSUSY/CandidateJetProducer/interface/CandidateJet.h"

CandidateJet::CandidateJet () : 
  pfCombinedSecondaryVertexV2BJetTags_           (numeric_limits<float>::min ()),    
  pfCombinedInclusiveSecondaryVertexV2BJetTags_  (numeric_limits<float>::min ())  
{
}

CandidateJet::CandidateJet (const pat::Jet &jet) : 
  pat::Jet(jet),
  pfCombinedSecondaryVertexV2BJetTags_           (numeric_limits<float>::min ()),    
  pfCombinedInclusiveSecondaryVertexV2BJetTags_  (numeric_limits<float>::min ())  
{
}

CandidateJet::~CandidateJet ()
{
}

const float
CandidateJet::pfCombinedSecondaryVertexV2BJetTags () const
{
  return pfCombinedSecondaryVertexV2BJetTags_; 
}

const float
CandidateJet::pfCombinedInclusiveSecondaryVertexV2BJetTags () const
{
  return pfCombinedInclusiveSecondaryVertexV2BJetTags_;
}

#include "DisplacedSUSY/CandidateElectronProducer/interface/CandidateElectron.h"

CandidateElectron::CandidateElectron () :
  vtxFitConversion_     (false),
  rho_                  (numeric_limits<float>::min ())
{
}

CandidateElectron::CandidateElectron (const reco::GsfElectron &ele) :
  pat::Electron(ele),
  vtxFitConversion_     (false),
  rho_                  (numeric_limits<float>::min ())
{
}

CandidateElectron::~CandidateElectron ()
{
}

const int
CandidateElectron::missingInnerHits () const
{
  return missingInnerHits_;
}

const float
CandidateElectron::AEff () const
{
  return AEff_;
}

const float
CandidateElectron::rho () const
{
  return this->rho_;
}

const bool
CandidateElectron::vtxFitConversion () const
{
  return this->vtxFitConversion_;
}

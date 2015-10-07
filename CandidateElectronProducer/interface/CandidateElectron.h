#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"

using namespace std;

class CandidateElectron : public pat::Electron
{
  public:
    CandidateElectron ();
    CandidateElectron (const reco::GsfElectron &);
    ~CandidateElectron ();

    const int missingInnerHits () const;
    const float AEff () const;
    const float rho() const;
    const bool vtxFitConversion() const;
    void set_rho (float value) { rho_  = value; }
    void set_AEff (float value) { AEff_  = value; }
    void set_missingInnerHits(int value) { missingInnerHits_ = value; }
    void set_vtxFitConversion(bool value) { vtxFitConversion_ = value; }
  private:
    bool vtxFitConversion_;
    float rho_;
    int missingInnerHits_;
    float AEff_;
};

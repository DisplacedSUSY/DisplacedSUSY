#ifndef DisplacedSUSYEVENT_VARIABLE_PRODUCER
#define DisplacedSUSYEVENT_VARIABLE_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "DisplacedSUSY/StandardAnalysis/interface/CustomDataFormat.h"
class DisplacedSUSYEventVariableProducer : public EventVariableProducer
  {
    public:
        DisplacedSUSYEventVariableProducer (const edm::ParameterSet &);
	~DisplacedSUSYEventVariableProducer ();

    private:
        void AddVariables(const edm::Event &);
  };
#endif

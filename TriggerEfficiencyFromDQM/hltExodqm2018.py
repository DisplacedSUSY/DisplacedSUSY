# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: hltEXOdqm -s DQM:exoticaMonitorHLT --conditions=92X_dataRun2_Prompt_v9 --geometry DB:Extended --eventcontent DQM --datatier DQMIO --data --era Run2_2017 --filetype=EDM -n 100 --filein /store/data/Run2017B/SingleMuon/AOD/23Jun2017-v1/120003/FA9120E3-AA59-E711-B0F9-0242AC1C0503.root --fileout DQM_onlyEXOHLT.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('DQM',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2018A/DoubleMuon/AOD/PromptReco-v2/000/316/239/00000/00175E6D-1B59-E811-B38A-FA163EECA815.root'
        ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('hltEXOdqm nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
                                     dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
        ),
                                     fileName = cms.untracked.string('DQM_onlyEXOHLT.root'),
    outputCommands = process.DQMEventContent.outputCommands,
                                     splitLevel = cms.untracked.int32(0),
                                     )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '101X_dataRun2_Prompt_v9', '')

# Path and EndPath definitions
process.dqmoffline_step = cms.EndPath(process.exoticaMonitorHLT*process.exoHLTDQMSourceExtra)
process.dqmofflineOnPAT_step = cms.EndPath(process.exoticaMonitorHLT*process.exoHLTDQMSourceExtra)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.dqmoffline_step,process.DQMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

#######################################################
##### Set up the options relevant to our analysis #####
#######################################################

######################################################################
##### Overwrite specific variables defined in osuAnalysis_cfi.py #####
######################################################################

process.OSUAnalysis.dataset = cms.string ('DYToTauTau_20')#dummy variable
process.OSUAnalysis.datasetType = cms.string ('bgMC')#dummy variable
process.OSUAnalysis.stopCTau = cms.vdouble(100.0, 50.0)  # Original and target stop <c*tau> values; only used if
                                      # datasetType_ == "signalMC" and dataset_ matches "stop.*to.*_.*mm.*"


# print-out options
process.OSUAnalysis.printAllTriggers = cms.bool(False)  # prints all available triggers (for first event only)  
process.OSUAnalysis.printEventInfo   = cms.bool(False)  # produces a lot of output, recommend using only with few channels and histograms
process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(False)
process.OSUAnalysis.plotAllObjectsInPassingEvents = cms.bool(False)
process.OSUAnalysis.verbose = cms.int32(0)

# Parameters for event weighting, including systematics  


#process.OSUAnalysis.dataPU          = cms.string ('PU_data_190456_208686_69300xSec') # central value
#process.OSUAnalysis.dataPU          = cms.string ('PU_data_190456_208686_66805xSec') # -1 sigma
#process.OSUAnalysis.dataPU          = cms.string ('PU_data_190456_208686_71795xSec') # +1 sigma


process.OSUAnalysis.applyLeptonSF = cms.bool(True)  #  multiplies scale factors in the case of multiple leptons


process.OSUAnalysis.electronSFFile = cms.string (os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/MVANonTrig_HtoZZto4l_IdIsoSip.root')
process.OSUAnalysis.electronSFID = cms.string ('')
process.OSUAnalysis.electronSF = cms.string ('h_electronScaleFactor_IdIsoSip')
process.OSUAnalysis.electronSFShift = cms.string('central') # change to 'up' to shift factors up 1 sigma, to 'down' to shift factors down 1

process.OSUAnalysis.muonSFFile = cms.string (os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/Configuration/data/MuonSF_ID_ISO_2D.root')
process.OSUAnalysis.muonSF = cms.string ('Combined_TOT')
process.OSUAnalysis.muonSFShift = cms.string('central') # change to 'up' to shift factors up 1 sigma, to 'down' to shift factors down 1 sigma



process.OSUAnalysis.applyTriggerSF = cms.bool(True)
process.OSUAnalysis.triggerScaleFactor = cms.double(0.981)#0.981+0.015 #ONLY RELEVANT FOR DISPLACED SUSY ANALYSIS



process.OSUAnalysis.applyTrackingSF = cms.bool(True) 
process.OSUAnalysis.trackSFShift = cms.string('central') # change to 'up' to shift factors up 1 sigma, to 'down' to shift factors down 1 sigma                                       



process.OSUAnalysis.doTopPtReweighting = cms.bool(True)



process.OSUAnalysis.applyBtagSF = cms.bool(False)
process.OSUAnalysis.minBtag = cms.int32(1)
process.OSUAnalysis.maxBtag = cms.int32(5)

process.OSUAnalysis.calcPdfWeights = cms.bool(False)      # If setting this to true, recompile with: src> touch OSUT3Analysis/AnaTools/BuildFile.xml; scram setup lhapdffull; scram b -j 9 
process.OSUAnalysis.pdfSet = cms.string('cteq66.LHgrid')  # only used if calcPdfWeights is True
process.OSUAnalysis.pdfSetFlag = cms.int32(1)             # only used if calcPdfWeights is True

################################################################################
# Redo batch mode configuration since we modified dataset and datasetType
################################################################################
if osusub.batchMode:
  dataset = osusub.dataset
  sourceLabel = get_short_name (dataset, dataset_names)
  if sourceLabel=="Unknown":
    print "Error[osuAnalysis_cfi.py]:  Could not find short name for dataset: %s; this will cause job to crash." % dataset  
  label = osusub.datasetLabel
  process.OSUAnalysis.dataset = cms.string (sourceLabel)
  process.OSUAnalysis.datasetType = cms.string (types[sourceLabel])

  if process.OSUAnalysis.datasetType == cms.string ("signalMC") and re.match (r"stop[^_]*to[^_]*_[^_]*mm.*", label):
    stopCTau = stop_ctau (label)
    sourceStopCTau = source_stop_ctau (stopCTau)
    process.OSUAnalysis.stopCTau = cms.vdouble (sourceStopCTau / 10.0, stopCTau / 10.0)

  if process.OSUAnalysis.datasetType == cms.string ("signalMC") and re.match (r"AMSB*", label):
    charginoCTau =  chargino_ctau (label)
    sourceCharginoCTau = source_chargino_ctau (charginoCTau)
    process.OSUAnalysis.stopCTau = cms.vdouble (sourceCharginoCTau, charginoCTau)
    print "Setting stopCTau = (" + str(sourceCharginoCTau) + ", " + str(charginoCTau) + ") "  

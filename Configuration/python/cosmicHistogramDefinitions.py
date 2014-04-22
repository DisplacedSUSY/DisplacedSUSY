import FWCore.ParameterSet.Config as cms





###############################################
##### Set up the histograms to be plotted #####
###############################################




CosmicMuonHistogramsLargeIP = cms.PSet(
    inputCollection = cms.string("muons"),
    histograms = cms.VPSet (
    
    cms.PSet (
    name = cms.string("muonAbsD0VertexLargeIP"),
    title = cms.string("Muon |d_{0}| wrt Vertex; |d_{0}| [cm]"),
    bins = cms.untracked.vdouble(2500, 0, 5),
    inputVariables = cms.vstring("abs(correctedD0Vertex)"),
    ),

    cms.PSet (
    name = cms.string("muonAbsDzLargeIP"),
    title = cms.string("Muon |d_{z}|; |d_{z}| [cm]"),
    bins = cms.untracked.vdouble(5000, 1, 20),
    inputVariables = cms.vstring("abs(correctedDZ)"),
    ),
)
)



CosmicMuonHistograms = cms.PSet(
    inputCollection = cms.string("muons"),
    histograms = cms.VPSet (

        cms.PSet (
            name = cms.string("MuontimeAtIpInOut"),
            title = cms.string("Muon timeAtIpInOut; timeAtIpInOut"),
            bins = cms.untracked.vdouble(1000, -30, 30),
            inputVariables = cms.vstring("timeAtIpInOut"),
        ),


        
    )
)



CosmicDiMuonHistograms = cms.PSet(
        inputCollection = cms.string("muon-muon pairs"),
            histograms = cms.VPSet (

            cms.PSet (
                name = cms.string("diMuonPiMinusThreeDAngle"),
                title = cms.string("Pi - angle between the two muons;log(#alpha [rad])"),
                bins = cms.untracked.vdouble(100, -9, 1),
                inputVariables = cms.vstring("log10(alpha)"),
                ),
            
          

           # 2D plots for hybrid Dimuons
            cms.PSet (
                name = cms.string("diMuonThreeDAnglevsmuon2timeAtIpInOut"),
                title = cms.string("angle between the two muons vs muon2timeAtIpInOut; #theta [rad]; time in [ps]"),
                bins = cms.untracked.vdouble(100, 0, 3.15,100,-30,30),
                inputVariables = cms.vstring("threeDAngle", "muon2timeAtIpInOut"),
                ),

            cms.PSet (
                name = cms.string("diMuonThreeDAnglevsmuon1timeAtIpInOut"),
                title = cms.string("angle between the two muons vs muon1timeAtIpInOut; #theta [rad]; time in [ps]"),
                bins = cms.untracked.vdouble(100, 0, 3.15,100,-30,30),
                inputVariables = cms.vstring("threeDAngle", "muon1timeAtIpInOut"),
                ),

             cms.PSet (
                name = cms.string("diMuonThreeDAnglevsInvMass"),
                title = cms.string("angle between the two muons vs Inv.mass; #theta [rad]; Inv.mass [GeV]"),
                bins = cms.untracked.vdouble(100, 0, 3.15,100,0,400),
                inputVariables = cms.vstring("threeDAngle", "invMass"),
                ),
             cms.PSet (
                name = cms.string("diMuonD0SignVSdiMuonDeltaAbsD0"),
                title = cms.string(" diMuonD0Sign vs diMuonDeltaAbsD0 ;|#Delta(d_{0})| [cm] ;  sign(d_{0}_{1}*{0}_{2})"),
                bins = cms.untracked.vdouble(100, 0, 0.5,2,-1,1),
                inputVariables = cms.vstring("abs(deltaAbsCorrectedD0Vertex)", "d0Sign"),
                ),
            #### abs d0 (vertex/bs) vs Inv mass
             cms.PSet (
                name = cms.string("diMuoninvMassVSdiMuonDeltaAbsD0"),
                title = cms.string(" diMuoninvMass vs diMuonDeltaAbsD0 ;|#Delta(d_{0})| [cm] ;  InvMass [GeV]"),
                bins = cms.untracked.vdouble(100, 0, 1,100,0,400),
                inputVariables = cms.vstring("abs(muon1CorrectedD0Vertex)", "invMass"),
                ),

#            cms.PSet (
#                name = cms.string("diMuoninvMassVSdiMuonAbsd0Beamspot"),
#                title = cms.string(" diMuoninvMass vs diMuonDeltaAbsD0 ;|#Delta(d_{0})| [cm] ;  InvMass [GeV]"),
#                bins = cms.untracked.vdouble(100, 0, 1,100,0,400),
#                inputVariables = cms.vstring("abs(muon1correctedD0)", "invMass"),
#                ),
            cms.PSet (
                name = cms.string("UpDownDeltaPtvsUpDownDeltaPhi"),
                title = cms.string(" UpDownDeltaPt vs UpDownDeltaPhi ; #Delta(#phi) [rad] ;  #Delta(p_{T}) [GeV]"),
                bins = cms.untracked.vdouble(100, -200, 200,100,0,6.3),
                inputVariables = cms.vstring("UpDownDeltaPt", "UpDownDeltaPhi"),
                ),
            cms.PSet (
                name = cms.string("diMuonDeltaPt"),
                title = cms.string("Di-muon #DeltaPt; #Delta(p_{T})"),
                bins = cms.untracked.vdouble(100, -200, 200),
                inputVariables = cms.vstring("deltaPt"),
                ),
            cms.PSet (
                name = cms.string("diMuonUpDownDeltaPt"),
                title = cms.string("Di-muon #UpDownDeltaPt; #Delta(p_{T})"),
                bins = cms.untracked.vdouble(100, -200, 200),
                inputVariables = cms.vstring("UpDownDeltaPt"),
                ),
            cms.PSet (
                name = cms.string("diMuonUpDownDeltaPhi"),
                title = cms.string("Di-muon #UpDownDeltaPhi; #Delta(#phi)"),
                bins = cms.untracked.vdouble(100, 0, 6.3),
                inputVariables = cms.vstring("UpDownDeltaPhi"),
                ),
            
            )
        )

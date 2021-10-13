from __future__ import print_function
from hepdata_lib import Submission, Table, Variable, Uncertainty, RootFileReader


def makeD0D0table(version):

    if version=="emu_bkg": #emu ABCD 2018 bkg sim (paper figure 2)
        table = Table("Leading muon $|d_0|$ vs leading electron $|d_0|$, bkg simulation")
        table.description = "Two-dimensional distribution of $|d_{0}^{a}|$ vs $|d_{0}^{b}|$, for simulated background events passing the e$\\mu$ preselection with 2018 conditions. In each $|d_{0}^{a}|$-$|d_{0}^{b}|$ bin, the number of events divided by the bin area is plotted. The inclusive signal region covers the region between 100 $\\mu$m and 10 cm in each $|d_{0}|$ variable shown."
        table.location = "Data from Figure 2"
        table.add_image("data/abcdMethod.pdf")
        d0xName = "Leading muon $|d_{0}|$"
        d0yName = "Leading electron $|d_{0}|$"

    elif version=="emu": #emu ABCD data (supplemental material figure 2)
        table = Table("Leading muon $|d_{0}|$ vs leading electron $|d_{0}|$")
        table.description = "Two-dimensional distributions of the leading electron vs the leading muon $|d_{0}|$, for the events that pass the e$\\mu$ preselection. Data events and $\\tilde{t} \\to b\\ell$ signal events with a $\\tilde{t}$ mass of 700 GeV and a proper decay length of 10 mm that correspond to 2018 data-taking conditions are shown. In each $|d_{0}|$-$|d_{0}|$ bin, the number of events divided by the bin area is plotted. The inclusive signal region covers the region between 100 $\\mu$m and 10 cm in each $|d_{0}|$ variable shown."
        table.location = "Supplemental material"
        table.add_image("data/d0vsd0_emu.pdf")
        table.add_image("data/d0vsd0_emu_stopToLB700_10mm.pdf")
        d0xName = "Leading muon $|d_{0}|$"
        d0yName = "Leading electron $|d_{0}|$"

    elif version=="ee": #ee ABCD data (supplemental material figure 3)
        table = Table("Subleading electron $|d_0|$ vs leading electron $|d_0|$")
        table.description = "Two-dimensional distributions of the leading vs the subleading electron $|d_0|$, for the events that pass the ee preselection. Data events and $\\tilde{t} \\to b\\ell$ signal events with a $\\tilde{t}$ mass of 700 GeV and a proper decay length of 10 mm that correspond to 2018 data-taking conditions are shown. In each $|d_{0}|$-$|d_{0}|$ bin, the number of events divided by the bin area is plotted. The inclusive signal region covers the region between 100 $\\mu$m and 10 cm in each $|d_{0}|$ variable shown."
        table.location = "Supplemental material"
        table.add_image("data/d0vsd0_ee.pdf")
        table.add_image("data/d0vsd0_ee_stopToLB700_10mm.pdf")
        d0xName = "Subleading electron $|d_{0}|$"
        d0yName = "Leading electron $|d_{0}|$"

    elif version=="mumu": #mumu ABCD data (supplemental material figure 4)
        table = Table("Subleading muon $|d_{0}|$ vs leading muon $|d_{0}|$")
        table.description = "Two-dimensional distributions of the leading vs the subleading muon $|d_{0}|$, for the events that pass the $\\mu\\mu$ preselection. Data events and $\\tilde{t} \\to b\\ell$ signal events with a $\\tilde{t}$ mass of 700 GeV and a proper decay length of 10 mm that correspond to 2018 data-taking conditions are shown. In each $|d_{0}|$-$|d_{0}|$ bin, the number of events divided by the bin area is plotted. The inclusive signal region covers the region between 100 $\\mu$m and 10 cm in each $|d_{0}|$ variable shown."
        table.location = "Supplemental material"
        table.add_image("data/d0vsd0_mumu.pdf")
        table.add_image("data/d0vsd0_mumu_stopToLB700_10mm.pdf")
        d0xName = "Subleading muon $|d_{0}|$"
        d0yName = "Leading muon $|d_{0}|$"

    table.keywords["observables"] = ["D0"]

    reader = RootFileReader("data/d0vsd0_"+version+".root")
    data = reader.read_hist_2d("h")

    if version=="emu" or version=="ee" or version=="mumu":
        readerSignal = RootFileReader("data/d0vsd0_"+version+"_stopToLB700_10mm.root")
        dataSignal = readerSignal.read_hist_2d("h")

    #for key in data.keys():
    #    print(key, type(data[key]), type(data[key][0]))

    ### define variables
    d0x = Variable(d0xName, is_independent=True, is_binned=True, units="$\\mu$m")
    d0x.values = data["x_edges"]

    d0y = Variable(d0yName, is_independent=True, is_binned=True, units="$\\mu$m")
    d0y.values = data["y_edges"]

    events = Variable("Event yield", is_independent=False, is_binned=False, units="1/$\\mu$m$^2$")
    events.values = data["z"]
    events.add_qualifier("SQRT(S)", 13, "TeV")

    #add values for signal plot:
    if version=="emu" or version=="ee" or version=="mumu":
        events.add_qualifier("Sample","Data")
        eventsSignal = Variable("Event yield", is_independent=False, is_binned=False, units="1/$\\mu$m$^2$")
        eventsSignal.values = dataSignal["z"]
        eventsSignal.add_qualifier("SQRT(S)", 13, "TeV")
        eventsSignal.add_qualifier("Sample","Signal")

    #overwrite values for bkg MC plot:
    elif version=="emu_bkg":
        events.add_qualifier("Sample","Bkg simulation")

    ### add variables and add table to submission
    table.add_variable(d0x)
    table.add_variable(d0y)
    table.add_variable(events)
    if version=="emu" or version=="ee" or version=="mumu":
        table.add_variable(eventsSignal)

    return table

###################################################################################################### 

def makeSRyieldsTable(year):

    if year=="Run2":
        table = Table("SR yields")
        table.description = "The number of observed and estimated background events in each channel and SR, with a representative signal overlaid. For each background estimate and signal yield, the total uncertainty (statistical plus systematic) is given. The distributions shown correspond to the events before the final maximum likelihood fit to the data."
        table.location = "Data from Figure 3"
        table.add_image("data/SRRun2yields_withRatioPlots.pdf")

    elif year=="2016":
        table = Table("SR yields, 2016")
        table.description = "The number of observed and estimated background events in each channel and SR in 2016, with a representative signal overlaid. For each background estimate and signal yield, the total uncertainty is given. The distributions shown correspond to the events before the final maximum likelihood fit to the data."
        table.location = "Supplemental material"
        table.add_image("data/SR2016yields_withRatioPlots.pdf")

    elif year=="201718":
        table = Table("SR yields, 2017-2018")
        table.description = "The number of observed and estimated background events in each channel and SR in 2017 and 2018, with a representative signal overlaid. For each background estimate and signal yield, the total uncertainty is given. The distributions shown correspond to the events before the final maximum likelihood fit to the data."
        table.location = "Supplemental material"
        table.add_image("data/SR201718yields_withRatioPlots.pdf")

    table.keywords["observables"] = ["yields"]
    table.keywords["reactions"] = ['P P --> STOP STOP', 'STOP --> LEPTON BQ']

    reader = RootFileReader("data/SRyields.root")
    signal = reader.read_hist_1d("hSig"+year)
    obs = reader.read_hist_1d("hObs"+year)
    expUncert = reader.read_graph("hExpUncert"+year)

    ### define variables
    SRbin = Variable("SR", is_independent=True, is_binned=False, units="")
    SRbin.values = ["e$\\mu$, I, low $\mathrm{p_{T}}$", "e$\\mu$, I, high $\mathrm{p_{T}}$", "e$\\mu$, II", "e$\\mu$, III", "e$\\mu$, IV",
                    "ee, I, low $\mathrm{p_{T}}$", "ee, I, high $\mathrm{p_{T}}$", "ee, II", "ee, III", "ee, IV",
                    "$\\mu\\mu$, I, low $\mathrm{p_{T}}$", "$\\mu\\mu$, I, high $\mathrm{p_{T}}$", "$\\mu\\mu$, II", "$\\mu\\mu$, III", "$\\mu\\mu$, IV" ]

    signalEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    signalEvents.values = signal["y"]
    signalUncert = Uncertainty("68% CL", is_symmetric=True)
    signalUncert.values = signal["dy"]
    signalEvents.add_uncertainty(signalUncert)
    signalEvents.add_qualifier("SQRT(S)", 13, "TeV")
    signalEvents.add_qualifier("Sample","Signal")

    dataEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    dataEvents.values = obs["y"]
    dataEvents.add_qualifier("SQRT(S)", 13, "TeV")
    dataEvents.add_qualifier("Sample","Data")

    backgroundEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    backgroundEvents.values = expUncert["y"]
    bkgUncert = Uncertainty("68% CL", is_symmetric=False)
    bkgUncert.values = expUncert["dy"]
    backgroundEvents.add_uncertainty(bkgUncert)
    backgroundEvents.add_qualifier("SQRT(S)", 13, "TeV")
    backgroundEvents.add_qualifier("Sample","Background")

    ### add variables and add table to submission
    table.add_variable(SRbin)
    table.add_variable(dataEvents)
    table.add_variable(backgroundEvents)
    table.add_variable(signalEvents)

    return table


###################################################################################################### 

def makeStopPaper2DLimitsTable(decay):

    if decay=="lb":
        table = Table("$\\tilde{t} \\to b\\ell$ cross section limits")
        table.description = "The observed 95% CL upper limits on the long-lived top squark production cross section, in the $c\\tau_0$ -- mass plane, for the three channels combined. The $\\tilde{t} \\to b\\ell $ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to b\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
        table.location = "Data from Figure 4 left"
        table.add_image("data/2DlimitsCombinedStopToLB.pdf")

    elif decay=="ld":
        table = Table("$\\tilde{t} \\to d\\ell$ cross section limits")
        table.description = "The observed 95% CL upper limits on the long-lived top squark production cross section, in the $c\\tau_0$ -- mass plane, for the three channels combined. The $\\tilde{t} \\to d\\ell$ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to d\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
        table.location = "Data from Figure 4 right"
        table.add_image("data/2DlimitsCombinedStopToLD.pdf")

    reader = RootFileReader("data/StopLimits/"+decay+"/limit_plot.root")
    twoD = reader.read_hist_2d("h_combined_standard_"+decay+"_with_observed_limits;1")

    ### define variables
    mass = Variable("$m_{\\tilde{t}}$", is_independent=True, is_binned=True, units="GeV")
    mass.values = twoD["x_edges"]

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=True, units="cm")
    ctau.values = twoD["y_edges"]

    obsLimits = Variable("Observed $\sigma_{\mathrm{95%CL}}$", is_independent=False, is_binned=False, units="pb")
    obsLimits.values = twoD["z"]
    obsLimits.add_qualifier("SQRT(S)", 13, "TeV")

    ### add variables and add table to submission
    table.add_variable(mass)
    table.add_variable(ctau)
    table.add_variable(obsLimits)

    return table

def makeStopPaperGraphLimitsTable(decay):

    if decay=="lb":
        table = Table("$\\tilde{t} \\to b\\ell$ mass limits vs $c\\tau_0$")
        table.description = "The observed 95% CL upper limits on the long-lived top squark production cross section, in the $c\\tau_0$ -- mass plane, for the three channels combined. The $\\tilde{t} \\to b\\ell $ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to b\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
        table.location = "Data from Figure 4 left"
        table.add_image("data/2DlimitsCombinedStopToLB.pdf")

    elif decay=="ld":
        table = Table("$\\tilde{t} \\to d\\ell$ mass limits vs $c\\tau_0$")
        table.description = "The observed 95% CL upper limits on the long-lived top squark production cross section, in the $c\\tau_0$ -- mass plane, for the three channels combined. The $\\tilde{t} \\to d\\ell$ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to d\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
        table.location = "Data from Figure 4 right"
        table.add_image("data/2DlimitsCombinedStopToLD.pdf")

    reader = RootFileReader("data/StopLimits/"+decay+"/limit_plot.root")
    obs = reader.read_graph("g_obs;1")
    exp = reader.read_graph("g_exp;1")
    #exp1sigma = reader.read_graph("g_1sigmaExp;1")

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs["y"]

    obsLimits = Variable("95% CL upper limits on $m_{\\tilde{t}}$", is_independent=False, is_binned=False, units="GeV")
    obsLimits.values = obs["x"]
    obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
    obsLimits.add_qualifier("Limits","Observed")

    expLimits = Variable("95% CL upper limits on $m_{\\tilde{t}}$", is_independent=False, is_binned=False, units="GeV")
    expLimits.values = exp["x"]
    #exp1sigmaLimits = Uncertainty("68% CL", is_symmetric=False)
    #exp1sigmaLimits.values = exp1sigma["dx"]
    #expLimits.add_uncertainty(exp1sigmaLimits)
    expLimits.add_qualifier("SQRT(S)", 13, "TeV")
    expLimits.add_qualifier("Limits","Expected")
    ### add variables and add table to submission
    table.add_variable(ctau)
    table.add_variable(obsLimits)
    table.add_variable(expLimits)

    return table



##################################

def makeStop3ChannelLimitsTable(decay):

    if decay=="lb":
        table = Table("$\\tilde{t} \\to b\\ell$ mass limits vs $c\\tau_0$ for each channel")
        table.description = "The 95% CL upper limits on the long-lived top squark proper decay length ($c\\tau_0$) as a function of its mass, for the e$\\mu$, ee, and $\\mu\\mu$ channels, and their combination. The $\\tilde{t} \\to b\\ell $ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to b\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton."
        table.location = "Supplemental material"
        table.add_image("data/2DlimitsStopToLB.pdf")

    elif decay=="ld":
        table = Table("$\\tilde{t} \\to d\\ell$ mass limits vs $c\\tau_0$ for each channel")
        table.description = "The 95% CL upper limits on the long-lived top squark proper decay length ($c\\tau_0$) as a function of its mass, for the e$\\mu$, ee, and $\\mu\\mu$ channels, and their combination. The $\\tilde{t} \\to d\\ell$ process is shown. These limits assume $\\mathcal{B}(\\tilde{t} \\to d\\ell)$ is 100%, and each lepton has an equal probability of being an electron, a muon, or a tau lepton."
        table.location = "Supplemental material"
        table.add_image("data/2DlimitsStopToLD.pdf")

    reader = RootFileReader("data/StopLimits/"+decay+"/limit_plot.root")

    obs = []
    exp = []
    channelExpNums = ["7","9","11","13"]
    channelObsNums = ["8","10","12","14"]
    for channelNum in channelExpNums:
        exp.append(reader.read_graph("L;"+channelNum))
    for channelNum in channelObsNums:
        obs.append(reader.read_graph("L;"+channelNum))

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs[0]["y"]
    table.add_variable(ctau)

    for i,channel in enumerate(channelExpNums):
        if channel=="7":
            channelName = "Combination"
        elif channel=="9":
            channelName = "e$\\mu$"
        elif channel=="11":
            channelName = "ee"
        elif channel=="13":
            channelName = "$\\mu\\mu$"

        expLimits = Variable("95% CL upper limits on $m_{\\tilde{t}}$", is_independent=False, is_binned=False, units="GeV")
        expLimits.values = exp[i]["x"]
        expLimits.add_qualifier("SQRT(S)", 13, "TeV")
        expLimits.add_qualifier("Limits","Expected")
        expLimits.add_qualifier("Channel",channelName)
        table.add_variable(expLimits)

    for i,channel in enumerate(channelObsNums):
        if channel=="8":
            channelName = "Combination"
        elif channel=="10":
            channelName = "e$\\mu$"
        elif channel=="12":
            channelName = "ee"
        elif channel=="14":
            channelName = "$\\mu\\mu$"

        obsLimits = Variable("95% CL upper limits on $m_{\\tilde{t}}$", is_independent=False, is_binned=False, units="GeV")
        obsLimits.values = obs[i]["x"]
        obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
        obsLimits.add_qualifier("Limits","Observed")
        obsLimits.add_qualifier("Channel",channelName)
        table.add_variable(obsLimits)

    return table

###################################################################################################### 

def makeGMSBPaperLimitsTable():

    table = Table("$\\tilde{\\ell} \\to \\ell\\tilde{G}$ mass limits vs $c\\tau_0$")
    table.description = "The 95% CL constraints on the long-lived slepton $c\\tau_{0}$ and mass. The $\\tilde{\\tau}$ and co-NLSP limits are shown for the three channels combined, while the $\\tilde{e}$ and $\\tilde{\\mu}$ NLSP limits are shown for the ee and $\\mu\\mu$ channels, respectively. These limits assume that the superpartners of the left- and right-handed leptons are degenerate in mass and $\\mathcal{B}(\\tilde{\\ell} \\to \\ell\\tilde{G})$ is 100%. The area to the left of the solid curves represents the observed exclusion region, and the dashed lines indicate the expected limits."
    table.location = "Data from Figure 5"
    table.add_image("data/2D_limits_gmsb_all_ns.pdf")

    reader = RootFileReader("data/GmsbLimits/limit_plot.root")

    obs = []
    exp = []
    channelNums = ["3","4","5","6"]
    for channelNum in channelNums:
        obs.append(reader.read_graph("g_obs;"+channelNum))
        exp.append(reader.read_graph("g_exp;"+channelNum))

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs[0]["y"]
    table.add_variable(ctau)

    for i,channelNum in enumerate(channelNums):
        if channelNum=="3":
            channelName = "co-"
        elif channelNum=="4":
            channelName = "$\\tilde{\\mu}$ "
        elif channelNum=="5":
            channelName = "$\\tilde{e}$ "
        elif channelNum=="6":
            channelName = "$\\tilde{\\tau}$ "

        obsLimits = Variable("95% CL upper limits on $m_{\\tilde{\\ell}}$", is_independent=False, is_binned=False, units="GeV")
        obsLimits.values = obs[i]["x"]
        obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
        obsLimits.add_qualifier("Limits","Observed")
        obsLimits.add_qualifier("Channel",channelName+"NLSP")

        expLimits = Variable("95% CL upper limits on $m_{\\tilde{\\ell}}$", is_independent=False, is_binned=False, units="GeV")
        expLimits.values = exp[i]["x"]
        expLimits.add_qualifier("SQRT(S)", 13, "TeV")
        expLimits.add_qualifier("Limits","Expected")
        expLimits.add_qualifier("Channel",channelName+"NLSP")

        #fix the stau case, where there's less values (set the mass to 0 for these):
        if len(obs[i]["x"]) < len(ctau.values):
            for j in range(len(ctau.values) - len(obs[i]["x"])):
                obsLimits.values.append(0)
        if len(exp[i]["x"]) < len(ctau.values):
            for j in range(len(ctau.values) - len(exp[i]["x"])):
                expLimits.values.append(0)

        ### add variables and add table to submission
        table.add_variable(obsLimits)
        table.add_variable(expLimits)

    return table

def makeGMSBcoNLSP2DLimitsTable():

    table = Table("$\\tilde{\\ell} \\to \\ell\\tilde{G}$ co-NLSP cross section limits")
    table.description = "The observed 95% CL upper limits on the long-lived slepton production cross section, in the $c\\tau_0$ -- mass plane. The co-NLSP limits are shown for the three channels combined. These limits assume that the superpartners of the left- and right-handed leptons are degenerate in mass and $\\mathcal{B}(\\tilde{\\ell} \\to \\ell\\tilde{G})$ is 100%. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
    table.location = "Supplemental material"
    table.add_image("data/limits_gmsb_coNLSP_2DwGrid.pdf")

    reader = RootFileReader("data/GmsbLimits/limit_plot.root")
    twoD = reader.read_hist_2d("h_combined_standard_gmsb_runII_with_observed_limits")

    ### define variables
    mass = Variable("$m_{\\tilde{\\ell}}$", is_independent=True, is_binned=True, units="GeV")
    mass.values = twoD["x_edges"]

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=True, units="cm")
    ctau.values = twoD["y_edges"]

    obsLimits = Variable("Observed $\sigma_{\mathrm{95%CL}}$", is_independent=False, is_binned=False, units="pb")
    obsLimits.values = twoD["z"]
    obsLimits.add_qualifier("SQRT(S)", 13, "TeV")

    ### add variables and add table to submission
    table.add_variable(mass)
    table.add_variable(ctau)
    table.add_variable(obsLimits)

    return table

def makeGMSBcoNLSPGraphLimitsTable():

    table = Table("$\\tilde{\\ell}\\to\\ell\\tilde{G}$ co-NLSP mass limits vs $c\\tau_0$")
    table.description = "The observed 95% CL upper limits on the long-lived slepton production cross section, in the $c\\tau_0$ -- mass plane. The co-NLSP limits are shown for the three channels combined. These limits assume that the superpartners of the left- and right-handed leptons are degenerate in mass and $\\mathcal{B}(\\tilde{\\ell} \\to \\ell\\tilde{G})$ is 100%. The area to the left of the black curve represents the observed exclusion region, and the dashed red lines indicate the expected limits and their 68% confidence intervals."
    table.location = "Supplemental material"
    table.add_image("data/limits_gmsb_coNLSP_2DwGrid.pdf")

    reader = RootFileReader("data/GmsbLimits/limit_plot.root")
    obs = reader.read_graph("g_obs;1")
    exp = reader.read_graph("g_exp;1")
    exp1sigma = reader.read_graph("g_1sigmaExp;1")

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs["y"]

    obsLimits = Variable("95% CL upper limits on $m_{\\tilde{\\ell}}$", is_independent=False, is_binned=False, units="GeV")
    obsLimits.values = obs["x"]
    obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
    obsLimits.add_qualifier("Limits","Observed")
    

    expLimits = Variable("95% CL upper limits on $m_{\\tilde{\\ell}}$", is_independent=False, is_binned=False, units="GeV")
    expLimits.values = exp["x"]
    expLimits.add_qualifier("SQRT(S)", 13, "TeV")
    expLimits.add_qualifier("Limits","Expected")

    ### add variables and add table to submission
    table.add_variable(ctau)
    table.add_variable(obsLimits)
    table.add_variable(expLimits)

    return table

###################################################################################################### 

def makeHToSSLimitsTable(mH):

    if mH=="125":
        table = Table("H(125) $\\to$ SS, S $\\to \\ell^{+}\\ell^{-}$, bf limits")
        table.description = "The 95% CL upper limits on the $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ branching fraction as a function of $c\\tau_0$, for a Higgs boson with a mass of 125 GeV and a long-lived scalar with a mass of 30 GeV or 50 GeV, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curve represents the observed (expected) exclusion region."
        table.location = "Data from Figure 6"
        mSes = ["30", "50"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BR.root")

    elif mH=="300":
        table = Table("H(300) $\\to$ SS, S $\\to\\ell^{+}\\ell^{-}, \\sigma\\times$ bf limits")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ as a function of $c\\tau_0$, for a 300 GeV Higgs boson and several long-lived scalar masses, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["20", "50", "150"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BRXS.root")

    elif mH=="400":
        table = Table("H(400) $\\to$ SS, S $\\to\\ell^{+}\\ell^{-}, \\sigma\\times$ bf limits")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ as a function of $c\\tau_0$, for a 400 GeV Higgs boson and several long-lived scalar masses, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["50", "150"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BRXS.root")

    elif mH=="600":
        table = Table("H(600) $\\to$ SS, S $\\to\\ell^{+}\\ell^{-}, \\sigma\\times$ bf limits")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ as a function of $c\\tau_0$, for a 600 GeV Higgs boson and several long-lived scalar masses, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["50", "150"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BRXS.root")

    elif mH=="800":
        table = Table("H(800) $\\to$ SS, S $\\to\\ell^{+}\\ell^{-}, \\sigma\\times$ bf limits")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ as a function of $c\\tau_0$, for a 800 GeV Higgs boson and several long-lived scalar masses, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["50", "150", "250"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BRXS.root")

    elif mH=="1000":
        table = Table("H(1000) $\\to$ SS, S$\\to\\ell^{+}\\ell^{-}, \\sigma\\times$ bf limits")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S}, \\mathrm{S} \\to \\ell^{+}\\ell^{-}$ as a function of $c\\tau_0$, for a 1000 GeV Higgs boson and several long-lived scalar masses, for the three channels combined. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons or two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["150", "350"]
        reader = RootFileReader("data/HToSSLimits/limit_plot_BRXS.root")

    table.add_image("data/HToSSLimits/limits_vs_lifetime_H"+mH+".pdf")
    table.keywords["observables"] = ["95% CL upper limits, ctau"]

    obs = []
    exp = []

    for mS in mSes:
        obs.append(reader.read_graph("h_m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))
        exp.append(reader.read_graph("h_Median expected: m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs[1]["x"]
    table.add_variable(ctau)

    for i,mS in enumerate(mSes):

        if mH=="125":        
            obsLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
            expLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
        else:
            obsLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")
            expLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")


        obsLimits.values = obs[i]["y"]
        obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
        obsLimits.add_qualifier("Limits","Observed")
        obsLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        expLimits.values = exp[i]["y"]
        expLimits.add_qualifier("SQRT(S)", 13, "TeV")
        expLimits.add_qualifier("Limits","Expected")
        expLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        #fix the H(125), S(30) case, where there's less values (set the BR to 1 for these):
        if len(obs[i]["y"]) != len(ctau.values):
            for j in range(abs(len(ctau.values) - len(obs[i]["y"]))):
                obsLimits.values.append(1)
        if len(exp[i]["y"]) != len(ctau.values):
            for j in range(abs(len(ctau.values) - len(exp[i]["y"]))):
                expLimits.values.append(1)

        #print("length of obs " +str(i) + "y is: "+str(len(obsLimits.values)))
        #print("length of exp " +str(i) + "y is: "+str(len(expLimits.values)))
        #print("")

        table.add_variable(obsLimits)
        table.add_variable(expLimits)

    return table


def makeHToSSTo4eLimitsTable(mH):

    if mH=="125":
        table = Table("H(125) $\\to 4\\ell$, bf limits, ee channel")
        table.description = "The 95% CL upper limits on the $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ branching fraction as a function of $c\\tau_0$, for a Higgs boson with a mass of 125 GeV and a long-lived scalar with a mass of 30 GeV or 50 GeV, for the ee channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons. The area above the solid (dashed) curve represents the observed (expected) exclusion region. The curves are not smooth because very few ee channel events pass the preselection for the Higgs boson and scalar masses shown in this figure."
        table.location = "Supplemental material"
        mSes = ["30", "50"]
        reader = RootFileReader("data/HToSSTo4e/limit_plot_eeBR.root")

    elif mH=="600":
        table = Table("H(600) $\\to 4\\ell, \\sigma\\times$ bf limits, ee channel")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ as a function of $c\\tau_0$, for a 600 GeV Higgs boson and several long-lived scalar masses, for the ee channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["50", "150"]
        reader = RootFileReader("data/HToSSTo4e/limit_plot_ee.root")

    elif mH=="1000":
        table = Table("H(1000) $\\to 4\\ell, \\sigma\\times$ bf limits, ee channel")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ as a function of $c\\tau_0$, for a 1000 GeV Higgs boson and several long-lived scalar masses, for the ee channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two electrons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["150", "350"]
        reader = RootFileReader("data/HToSSTo4e/limit_plot_ee.root")

    table.add_image("data/HToSSTo4e/limits_vs_lifetime_H"+mH+"_4e.pdf")
    table.keywords["observables"] = ["95% CL upper limits, ctau"]

    obs = []
    exp = []

    for mS in mSes:
        obs.append(reader.read_graph("h_m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))
        exp.append(reader.read_graph("h_Median expected: m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs[1]["x"]
    table.add_variable(ctau)

    for i,mS in enumerate(mSes):

        if mH=="125":        
            obsLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
            expLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
        else:
            obsLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")
            expLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")


        obsLimits.values = obs[i]["y"]
        obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
        obsLimits.add_qualifier("Limits","Observed")
        obsLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        expLimits.values = exp[i]["y"]
        expLimits.add_qualifier("SQRT(S)", 13, "TeV")
        expLimits.add_qualifier("Limits","Expected")
        expLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        #fix the H(125), S(30) case, where there's less values (set the BR to 1 for these):
        if len(obs[i]["y"]) != len(ctau.values):
            for j in range(abs(len(ctau.values) - len(obs[i]["y"]))):
                obsLimits.values.append(1)
        if len(exp[i]["y"]) != len(ctau.values):
            for j in range(abs(len(ctau.values) - len(exp[i]["y"]))):
                expLimits.values.append(1)

        #print("length of obs " +str(i) + "y is: "+str(len(obsLimits.values)))
        #print("length of exp " +str(i) + "y is: "+str(len(expLimits.values)))
        #print("")

        table.add_variable(obsLimits)
        table.add_variable(expLimits)

    return table

def makeHToSSTo4muLimitsTable(mH):

    if mH=="125":
        table = Table("H(125) $\\to 4\\ell$, bf limits, $\\mu\\mu$ channel")
        table.description = "The 95% CL upper limits on the $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ branching fraction as a function of $c\\tau_0$, for a Higgs boson with a mass of 125 GeV and a long-lived scalar with a mass of 30 GeV or 50 GeV, for the $\\mu\\mu$ channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two muons. The area above the solid (dashed) curve represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["30", "50"]
        reader = RootFileReader("data/HToSSTo4mu/limit_plot_mumuBR.root")

    elif mH=="600":
        table = Table("H(600) $\\to 4\\ell, \\sigma\\times$ bf limits, $\\mu\\mu$ channel")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ as a function of $c\\tau_0$, for a 600 GeV Higgs boson and several long-lived scalar masses, for the $\\mu\\mu$ channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["50", "150"]
        reader = RootFileReader("data/HToSSTo4mu/limit_plot_mumu.root")

    elif mH=="1000":
        table = Table("H(1000) $\\to 4\\ell, \\sigma\\times$ bf limits, $\\mu\\mu$ channel")
        table.description = "The 95% CL upper limits on the product of the cross section and branching fraction $\\mathrm{H} \\to \\mathrm{S}\\mathrm{S} \\to 4\\ell$ as a function of $c\\tau_0$, for a 1000 GeV Higgs boson and several long-lived scalar masses, for the $\\mu\\mu$ channel only. These limits assume that $\\mathcal{B}(H \\to SS)=100\\%$ and each S has a 50% probability of decaying to two muons. The area above the solid (dashed) curves represents the observed (expected) exclusion region."
        table.location = "Supplemental material"
        mSes = ["150", "350"]
        reader = RootFileReader("data/HToSSTo4mu/limit_plot_mumu.root")

    table.add_image("data/HToSSTo4mu/limits_vs_lifetime_H"+mH+"_4mu.pdf")
    table.keywords["observables"] = ["95% CL upper limits, ctau"]

    obs = []
    exp = []

    for mS in mSes:
        obs.append(reader.read_graph("h_m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))
        exp.append(reader.read_graph("h_Median expected: m_{H} = "+mH+" GeV, m_{S} = "+mS+" GeV"))

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=False, units="cm")
    ctau.values = obs[1]["x"]
    table.add_variable(ctau)

    for i,mS in enumerate(mSes):

        if mH=="125":        
            obsLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
            expLimits = Variable("95% CL upper limits on B(H $\\to$ SS)", is_independent=False, is_binned=False, units="")
        else:
            obsLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")
            expLimits = Variable("95% CL upper limits on $\\sigma \\times$ B(H $\\to$ SS)", is_independent=False, is_binned=False, units="pb")


        obsLimits.values = obs[i]["y"]
        obsLimits.add_qualifier("SQRT(S)", 13, "TeV")
        obsLimits.add_qualifier("Limits","Observed")
        obsLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        expLimits.values = exp[i]["y"]
        expLimits.add_qualifier("SQRT(S)", 13, "TeV")
        expLimits.add_qualifier("Limits","Expected")
        expLimits.add_qualifier("Masses","$m_{H} = "+mH+"$ GeV, $m_{S} = "+mS+"$ GeV")

        #fix the H(125), S(30) case, where there's less values (set the BR to 1 for these):
        if len(obs[i]["y"]) > len(ctau.values):
            for j in range(abs(len(ctau.values) - len(obs[i]["y"]))):
                obsLimits.values.pop()
        if len(exp[i]["y"]) > len(ctau.values):
            for j in range(abs(len(ctau.values) - len(exp[i]["y"]))):
                expLimits.values.pop()

        #print("length of obs " +str(i) + "y is: "+str(len(obsLimits.values)))
        #print("length of exp " +str(i) + "y is: "+str(len(expLimits.values)))
        #print("")

        table.add_variable(obsLimits)
        table.add_variable(expLimits)

    return table


def makeSignificanceTable(channel):
    #stopToLB significances

    reader = RootFileReader("data/significances/"+channel+"/limit_plot.root")

    if channel=="EMu":
        table = Table("Observed significance, e$\\mu$ channel")
        table.description = "The observed significance for the $\\tilde{t} \\to b\\ell $ process as a function of $\\tilde{t}$ mass and lifetime, for the e$\\mu$ channel."
        table.location = "Supplemental material"
        table.add_image("data/significances/"+channel+"/emu_lb_significance.pdf")
        data = reader.read_hist_2d("h_emu_standard_with_observed_limits")
    elif channel=="EE":
        table = Table("Observed significance, ee channel")
        table.description = "The observed significance for the $\\tilde{t} \\to b\\ell $ process as a function of $\\tilde{t}$ mass and lifetime, for the ee channel."
        table.location = "Supplemental material"
        table.add_image("data/significances/"+channel+"/ee_lb_significance.pdf")
        data = reader.read_hist_2d("h_ee_standard_with_observed_limits")
    elif channel=="MuMu":
        table = Table("Observed significance, $\\mu\\mu$ channel")
        table.description = "The observed significance for the $\\tilde{t} \\to b\\ell $ process as a function of $\\tilde{t}$ mass and lifetime, for the $\\mu\\mu$ channel."
        table.location = "Supplemental material"
        table.add_image("data/significances/"+channel+"/mumu_lb_significance.pdf")
        data = reader.read_hist_2d("h_mumu_standard_with_observed_limits")
    elif channel=="combined":
        table = Table("Observed significance, all channels")
        table.description = "The observed significance for the $\\tilde{t} \\to b\\ell $ process as a function of $\\tilde{t}$ mass and lifetime, for the three channels combined."
        table.location = "Supplemental material"
        table.add_image("data/significances/"+channel+"/combined_lb_significance.pdf")
        data = reader.read_hist_2d("h_emu_standard_with_observed_limits")
        
    table.keywords["observables"] = ["Significance, ctau, top squark mass"]

    ### define variables
    mass = Variable("$m_{\\tilde{t}}$", is_independent=True, is_binned=True, units="GeV")
    mass.values = data["x_edges"]

    ctau = Variable("$c\\tau_{0}$", is_independent=True, is_binned=True, units="cm")
    ctau.values = data["y_edges"]

    significance = Variable("Significance", is_independent=False, is_binned=False, units="")
    significance.values = data["z"]
    significance.add_qualifier("SQRT(S)", 13, "TeV")

    ### add variables and add table to submission
    table.add_variable(mass)
    table.add_variable(ctau)
    table.add_variable(significance)

    return table

###################################################################################################### 

def make1DD0PlotsTable(lepton):

    reader = RootFileReader("data/D01Dplots/stacked_histograms_Rebin5.root")

    if lepton=="electron":
        table = Table("Electron $|d_0|$")
        table.description = "The distribution of electron $|d_0|$ for the events in data and signal that pass the e$\\mu$ preselection. In all of the histograms, the last bin includes the overflow. The electron $|d_0|$ distributions have a longer tail than those of muons because the muon $|d_0|$ values are measured more precisely."
        table.location = "Supplemental material"
        table.add_image("data/D01Dplots/electronAbsD0_2000um.pdf")

        data = reader.read_hist_1d("PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_2000um;4")
        stopToLB700_1mm = reader.read_hist_1d("PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_2000um;1")
        stopToLB700_10mm = reader.read_hist_1d("PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_2000um;2")
        stopToLB700_100mm = reader.read_hist_1d("PreselectionPlotter/Electron-beamspot Plots/electronAbsD0_2000um;3")

        d0 = Variable("Electron $|d_0|$", is_independent=True, is_binned=True, units="$\\mu$m")

    elif lepton=="muon":
        table = Table("Muon $|d_0|$")
        table.description = "The distribution of muon $|d_0|$ for the events in data and signal that pass the e$\\mu$ preselection. In all of the histograms, the last bin includes the overflow. The electron $|d_0|$ distributions have a longer tail than those of muons because the muon $|d_0|$ values are measured more precisely."
        table.location = "Supplemental material"
        table.add_image("data/D01Dplots/muonAbsD0_2000um.pdf")

        data = reader.read_hist_1d("PreselectionPlotter/Muon-beamspot Plots/muonAbsD0_2000um;4")
        stopToLB700_1mm = reader.read_hist_1d("PreselectionPlotter/Muon-beamspot Plots/muonAbsD0_2000um;1")
        stopToLB700_10mm = reader.read_hist_1d("PreselectionPlotter/Muon-beamspot Plots/muonAbsD0_2000um;2")
        stopToLB700_100mm = reader.read_hist_1d("PreselectionPlotter/Muon-beamspot Plots/muonAbsD0_2000um;3")

        d0 = Variable("Muon $|d_0|$", is_independent=True, is_binned=True, units="$\\mu$m")

    ### define variables
    table.keywords["observables"] = ["Lepton D0"]
    d0.values = data["x_edges"]

    dataEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    dataEvents.values = data["y"]
    #dataUncert = Uncertainty("68% CL", is_symmetric=True)
    #dataUncert.values = data["dy"]
    #dataEvents.add_uncertainty(dataUncert)
    dataEvents.add_qualifier("SQRT(S)", 13, "TeV")
    dataEvents.add_qualifier("Sample","Data")
    

    stopToLB700_1mmEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    stopToLB700_1mmEvents.values = stopToLB700_1mm["y"]
    stopToLB700_1mmUncert = Uncertainty("Sample size", is_symmetric=True)
    stopToLB700_1mmUncert.values = stopToLB700_1mm["dy"]
    stopToLB700_1mmEvents.add_uncertainty(stopToLB700_1mmUncert)
    stopToLB700_1mmEvents.add_qualifier("SQRT(S)", 13, "TeV")
    stopToLB700_1mmEvents.add_qualifier("Sample","$\\tilde{t}\\to b\\ell$, $m_{\\tilde{t}}$=700 GeV, $c\\tau_{0}$=0.1 cm")

    stopToLB700_10mmEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    stopToLB700_10mmEvents.values = stopToLB700_10mm["y"]
    stopToLB700_10mmUncert = Uncertainty("Sample size", is_symmetric=True)
    stopToLB700_10mmUncert.values = stopToLB700_10mm["dy"]
    stopToLB700_10mmEvents.add_uncertainty(stopToLB700_10mmUncert)
    stopToLB700_10mmEvents.add_qualifier("SQRT(S)", 13, "TeV")
    stopToLB700_10mmEvents.add_qualifier("Sample","$\\tilde{t}\\to b\\ell$ events, $m_{\\tilde{t}}$=700 GeV, $c\\tau_{0}$=1 cm")

    stopToLB700_100mmEvents = Variable("Event yield", is_independent=False, is_binned=False, units="")
    stopToLB700_100mmEvents.values = stopToLB700_100mm["y"]
    stopToLB700_100mmUncert = Uncertainty("Sample size", is_symmetric=True)
    stopToLB700_100mmUncert.values = stopToLB700_100mm["dy"]
    stopToLB700_100mmEvents.add_uncertainty(stopToLB700_100mmUncert)
    stopToLB700_100mmEvents.add_qualifier("SQRT(S)", 13, "TeV")
    stopToLB700_100mmEvents.add_qualifier("Sample","$\\tilde{t}\\to b\\ell$ events, $m_{\\tilde{t}}$=700 GeV, $c\\tau_{0}$=10 cm")

    ### add variables and add table to submission
    table.add_variable(d0)
    table.add_variable(dataEvents)
    table.add_variable(stopToLB700_1mmEvents)
    table.add_variable(stopToLB700_10mmEvents)
    table.add_variable(stopToLB700_100mmEvents)

    return table
###################################################################################################### 

def main():

    #create submission
    submission = Submission()

    submission.read_abstract("data/abstract.txt")
    submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-18-003/")
    submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:2110.04809")
    submission.add_record_id(113658, "inspire")

    submission.add_table(make1DD0PlotsTable("electron"))
    submission.add_table(make1DD0PlotsTable("muon"))

    submission.add_table(makeD0D0table("emu_bkg"))
    submission.add_table(makeD0D0table("emu"))
    submission.add_table(makeD0D0table("ee"))
    submission.add_table(makeD0D0table("mumu"))

    submission.add_table(makeSRyieldsTable("Run2"))
    submission.add_table(makeSRyieldsTable("2016"))
    submission.add_table(makeSRyieldsTable("201718"))

    submission.add_table(makeStopPaper2DLimitsTable("lb"))
    submission.add_table(makeStopPaper2DLimitsTable("ld"))

    submission.add_table(makeStopPaperGraphLimitsTable("lb"))
    submission.add_table(makeStopPaperGraphLimitsTable("ld"))

    submission.add_table(makeStop3ChannelLimitsTable("lb"))
    submission.add_table(makeStop3ChannelLimitsTable("ld"))

    submission.add_table(makeGMSBPaperLimitsTable())
    submission.add_table(makeGMSBcoNLSP2DLimitsTable())
    submission.add_table(makeGMSBcoNLSPGraphLimitsTable())

    submission.add_table(makeHToSSLimitsTable("125"))
    submission.add_table(makeHToSSLimitsTable("300"))
    submission.add_table(makeHToSSLimitsTable("400"))
    submission.add_table(makeHToSSLimitsTable("600"))
    submission.add_table(makeHToSSLimitsTable("800"))
    submission.add_table(makeHToSSLimitsTable("1000"))

    submission.add_table(makeHToSSTo4eLimitsTable("125"))
    submission.add_table(makeHToSSTo4eLimitsTable("600"))
    submission.add_table(makeHToSSTo4eLimitsTable("1000"))

    submission.add_table(makeHToSSTo4muLimitsTable("125"))
    submission.add_table(makeHToSSTo4muLimitsTable("600"))
    submission.add_table(makeHToSSTo4muLimitsTable("1000"))

    for table in submission.tables:
        table.keywords["cmenergies"] = [13000]

    submission.add_additional_resource("Signal generation", "data/signalGeneration.tar.gz", copy_file=True)

    submission.create_files("hepdataRecord")

if __name__ == '__main__':
    main()


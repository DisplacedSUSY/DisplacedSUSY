import numpy as np
import math
from array import array
from ROOT import TGraphAsymmErrors, TLegend, TRatioPlot, TMultiGraph, TGaxis, TPad, TVector, TPaveLabel, TPaveText, gStyle, TFile, gRandom, gROOT, TCanvas, TGraph, TH1F, TH2F, TH1D, TH2D, TGraphErrors, Double, TF1, TF2

gROOT.Reset()

out_file = TFile("signal_eff.root", "recreate")
c = TCanvas("sigEff", "sigEff", 200, 10, 900, 850)

p2 = TPad("p1", "p1", 0., 0., 1., 0.3)
p2.Draw()
p2.SetTopMargin(0.003)
p2.SetBottomMargin(0.3)
p2.RangeAxis(0, 0, 500, 14)

p1 = TPad("p2", "p2", 0.,0.3,1.,1.)
p1.Draw()
p1.SetBottomMargin(0.001)
p1.RangeAxis(0,0,500,14)
p1.cd()

# data
mass200 = 200
mass300 = 300
mass400 = 400

parking200 = 8.06
parking300 = 8.97
parking400 = 9.42

mumu200 = 1.86
mumu300 = 2.9
mumu400 = 3.59

# fill values
x = array( 'd' )
x.append( mass200 )
x.append( mass300 )
x.append( mass400 )

y_parking = array( 'd', [parking200, parking300, parking400])
y_mumu = array( 'd', [mumu200, mumu300, mumu400])

test = math.sqrt(4)
error1_parking = math.sqrt((1.0-(parking200*.01))*(parking200*.01))
error2_parking = math.sqrt((1.0-(parking300*.01))*(parking300*.01))
error3_parking = math.sqrt((1.0-(parking400*.01))*(parking400*.01))

error1_mumu = math.sqrt((1.0-(mumu300*.01))*(mumu200*.01))
error2_mumu = math.sqrt((1.0-(mumu300*.01))*(mumu300*.01))
error3_mumu = math.sqrt((1.0-(mumu400*.01))*(mumu400*.01))

print(test)
print(error1_parking)
print(error2_parking)
print(error3_parking)

y_errors_parking = array( 'd', [error1_parking, error2_parking, error3_parking])
y_errors_mumu = array( 'd', [error1_mumu, error2_mumu, error3_mumu])
x_error = array( 'd', [0.0,0.0,0.0])

n = 3

hEff_parking = TGraphAsymmErrors(n, x, y_parking, x_error, x_error, y_errors_parking, y_errors_parking)
hEff_parking.SetMarkerStyle(20)
hEff_parking.SetMarkerColor(4)
hEff_parking.SetMarkerSize(1.5)
hEff_parking.GetXaxis().SetLabelSize(0.)
hEff_parking.GetYaxis().SetLabelSize(.04)
hEff_parking.GetYaxis().SetTitleSize(.04)
hEff_parking.GetYaxis().SetTitleOffset(1)
hEff_parking.SetTitle(";;Efficiency [%]")
hEff_parking.GetYaxis().SetRangeUser(0, 100)
hEff_mumu = TGraphAsymmErrors(n, x, y_mumu, x_error, x_error, y_errors_mumu, y_errors_mumu)
hEff_mumu.SetMarkerStyle(21)
hEff_mumu.SetMarkerColor(2)
hEff_mumu.SetMarkerSize(1.5)

hEff_parking.Draw("AP")
hEff_mumu.Draw("P")

multi = TMultiGraph()
multi.Add(hEff_parking)
multi.Add(hEff_mumu)
multi.SetTitle("")
#multi.Draw("AP")
#multi.GetXaxis().SetTitle("stop mass (GeV)")
#multi.GetXaxis().CenterTitle()
#multi.GetXaxis().SetRangeUser(0, 500)
#multi.GetXaxis().SetTickSize(0.)

#multi.GetYaxis().SetTitle("trigger efficiency (%)")

leg = TLegend(0.15,0.65,0.7,0.85)
leg.SetHeader("#tilde{t}#tilde{t}#rightarrow #mub #mub, c#tau_{#tilde{t}}=1000 mm","C")
leg.AddEntry(hEff_parking, "Parked data trigger", "p")
leg.AddEntry(hEff_mumu, "Double muon trigger", "p")
leg.SetBorderSize(0)
leg.Draw()

p2.cd()

y_ratio = np.divide(y_parking,y_mumu)

#y_ratio = array( 'd' )
#y_ratio.append(y_parking/y_mumu)

ratio = TGraphAsymmErrors(n,x,y_ratio)
ratio.SetTitle(";m_{#tilde{t}} [GeV];Ratio")
ratio.GetXaxis().SetRangeUser(50,450)
ratio.SetMarkerStyle(20)
ratio.SetMarkerColor(1)
ratio.SetMarkerSize(1.5)
ratio.GetXaxis().SetLabelSize(.1)
ratio.GetYaxis().SetLabelSize(.1)
ratio.GetXaxis().SetTitleSize(.1)
ratio.GetYaxis().SetTitleSize(.1)
ratio.GetYaxis().SetTitleOffset(.35)
#ratio.GetXaxis().SetTickSize(0.)
ratio.Draw("AP")

#ratio = TRatioPlot(hEff_parking, hEff_mumu)
#c.SetTicks(0, 1)
#ratio.Draw()
c.Update()

#hEff_parking.Draw("ALP")
#hEff_mumu.Draw("same")

c.Write()

#################
### attempt 2 ###
#################

#hEff_parking = TH1F("hEffParking", "parking trigger efficiency", 5, 0, 500)
#hEff_mumu = TH1F("hEffMuMu", "mumu trigger efficiency", 5, 0, 500)
#
#hEff_parking.Fill( mass200, parking200 )
#hEff_parking.Fill( mass300, parking300 )
#hEff_parking.Fill( mass400, parking400 )
#
#hEff_mumu.Fill( mass200, mumu200 )
#hEff_mumu.Fill( mass300, mumu300 )
#hEff_mumu.Fill( mass400, mumu400 )
#
#out_file = TFile("signal_eff.root", "recreate")
#c = TCanvas("sigEff", "sigEff", 800, 800, 800, 800)
#
#pad1 = TPad("pad1", "pad1", 0, 0.5, 1, 1.0)
#pad1.SetBottomMargin(1)
#pad1.SetGridx()
#pad1.Draw()
#pad1.cd()
#hEff_parking.SetStats(0)
#hEff_parking.SetLineColor(1)
#hEff_mumu.SetLineColor(2)
#hEff_parking.GetYaxis().SetTitle("efficiency (%)")
#hEff_parking.Draw()
#hEff_mumu.Draw("same")
#
#hEff_parking.GetXaxis().SetLabelSize(0.)
##axis = TGaxis(0, 0, 500, 10, 0, 500, 5, "")
##axis.SetLabelFont(43)
##axis.SetLabelSize(15)
##axis.Draw()
#
#c.cd()
#pad2 = TPad("pad2","pad2", 0, 0.5, 1, 0.3)
#pad2.SetTopMargin(0)
#pad2.SetBottomMargin(0.5)
#pad2.SetGridx()
#pad2.Draw()
#pad2.cd()
#
#ratio = hEff_parking.Clone("ratio")
#ratio.SetLineColor(0)
#ratio.SetMinimum(0)
#ratio.SetMaximum(10)
#ratio.Sumw2()
#ratio.SetStats(0)
#ratio.Divide(hEff_mumu)
#ratio.SetMarkerStyle(21)
#ratio.GetXaxis().SetTitle("stop mass (GeV)")
#ratio.Draw("ep")
#
#hEff_parking.SetLineColor(1)
#hEff_parking.SetLineWidth(2)
#
#hEff_parking.GetYaxis().SetTitleSize(20)
#hEff_parking.GetYaxis().SetTitleFont(43)
#hEff_parking.GetYaxis().SetTitleOffset(1.55)
#
#hEff_mumu.SetLineColor(2)
#hEff_mumu.SetLineWidth(2)
#
#ratio.SetTitle("")
#
#ratio.GetYaxis().SetTitle("ratio")
#ratio.GetYaxis().SetNdivisions(5)
#ratio.GetYaxis().SetTitleSize(20)
#ratio.GetYaxis().SetTitleFont(43)
#ratio.GetYaxis().SetTitleOffset(1.55)
#ratio.GetYaxis().SetLabelSize(15)
#ratio.GetYaxis().SetLabelFont(43)
#
#
#ratio.GetXaxis().SetTitleSize(20)
#ratio.GetXaxis().SetTitleFont(43)
#ratio.GetXaxis().SetTitleOffset(4.)
#ratio.GetXaxis().SetLabelSize(15)
#ratio.GetXaxis().SetLabelFont(43)
#
#
#
#
#c.Write()


#################
### attempt 1 ###
#################

#heff = TH1F("h1", "h1 title", 5, 100, 500)
#heff.Fill( mass200,parking200)
#heff.Fill( mass300,parking300)
#heff.Fill( mass400,parking400)
#
#heff_mumu = TH1F("h1", "h1 title", 5, 100, 500)
#heff_mumu.Fill( mass200,mumu200 )
#heff_mumu.Fill( mass300,mumu300 )
#heff_mumu.Fill( mass400,mumu400 )
#
#out_file = TFile("sigVbgEff.root", "recreate")
#c1 = TCanvas("sigVbgEff", "sigVbgEff",100,100,700,700)
#print("canvas created")
#
##dx = 0
##dy = 0
#
#gStyle.SetOptTitle(0)
##gStyle.SetErrorX(dx)
#
#
##gStyle.SetErrorY(dy)
#title = TPaveText(0.0,0.9,0.3,1,"brNDC")
##title = TPaveText(0.0,0.9,0.3,1)
#heff.GetXaxis().SetTitle("stop mass (GeV)")
##heff.GetYaxis().SetTitle("parking signal efficiency / mumu signal efficiency")
#heff.Draw("HIST")
#heff_mumu.Draw("SAMES")
#c1.Write()

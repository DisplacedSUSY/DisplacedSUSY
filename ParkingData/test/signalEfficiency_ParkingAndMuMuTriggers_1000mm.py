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

# data for lifetime = 1000mm
mass100 = 100
mass150 = 150
mass175 = 175
mass200 = 200
mass300 = 300
mass400 = 400

isGenMuon = 1670000

# trigger efficiency with no further selections: (events that pass trigger) / (all events ran over)
# parking Trigger yield for stop 1000mm
parking100 = 977000.0/10200000
parking150 = 178000.0/1670000
parking175 = 83600.0/792000
parking200 = 48900.0/429000
parking300 = 7160.0/55800
parking400 = 1520.0/12100

# mumu trigger yield for stop 1000mm
mumu100 = 409000.0/10200000
mumu150 = 132000.0/1670000
mumu175 = 69600.0/792000
mumu200 = 42200.0/429000
mumu300 = 7010.0/55800
mumu400 = 1710.0/12100

# fill values
x = array( 'd' )
x.append( mass100 )
x.append( mass150 )
x.append( mass175 )
x.append( mass200 )
x.append( mass300 )
x.append( mass400 )

y_parking = array( 'd', [parking100, parking150, parking175, parking200, parking300, parking400])
y_mumu = array( 'd', [mumu100, mumu150, mumu175, mumu200, mumu300, mumu400])

test = math.sqrt(4)
error4_parking = math.sqrt((1.0-(parking100*.01))*(parking100*.01))
error5_parking = math.sqrt((1.0-(parking150*.01))*(parking150*.01))
error6_parking = math.sqrt((1.0-(parking175*.01))*(parking175*.01))
error1_parking = math.sqrt((1.0-(parking200*.01))*(parking200*.01))
error2_parking = math.sqrt((1.0-(parking300*.01))*(parking300*.01))
error3_parking = math.sqrt((1.0-(parking400*.01))*(parking400*.01))

error4_mumu = math.sqrt((1.0-(mumu100*.01))*(mumu100*.01))
error5_mumu = math.sqrt((1.0-(mumu150*.01))*(mumu150*.01))
error6_mumu = math.sqrt((1.0-(mumu175*.01))*(mumu175*.01))
error1_mumu = math.sqrt((1.0-(mumu300*.01))*(mumu200*.01))
error2_mumu = math.sqrt((1.0-(mumu300*.01))*(mumu300*.01))
error3_mumu = math.sqrt((1.0-(mumu400*.01))*(mumu400*.01))

print(test)
print(error1_parking)
print(error2_parking)
print(error3_parking)

y_errors_parking = array( 'd', [error4_parking, error5_parking, error6_parking, error1_parking, error2_parking, error3_parking])
y_errors_mumu = array( 'd', [error4_mumu, error5_mumu, error6_mumu, error1_mumu, error2_mumu, error3_mumu])
x_error = array( 'd', [0.0,0.0,0.0,0.0,0.0,0.0])

n = 6

hEff_parking = TGraphAsymmErrors(n, x, y_parking, x_error, x_error, y_errors_parking, y_errors_parking)
hEff_parking.SetMarkerStyle(20)
hEff_parking.SetMarkerColor(4)
hEff_parking.SetMarkerSize(1.5)
hEff_parking.GetXaxis().SetLabelSize(0.)
hEff_parking.GetYaxis().SetLabelSize(.04)
hEff_parking.GetYaxis().SetTitleSize(.04)
hEff_parking.GetYaxis().SetTitleOffset(1)
hEff_parking.SetTitle(";;Efficiency")
hEff_parking.GetYaxis().SetRangeUser(0, 1)
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

leg = TLegend(0.15,0.55,0.7,0.75)
leg.SetHeader("#tilde{t}#tilde{t}#rightarrow #mub #mub, c#tau=1000 mm","C")
leg.AddEntry(hEff_parking, "Parked data trigger", "p")
leg.AddEntry(hEff_mumu, "Double muon trigger", "p")
leg.SetBorderSize(0)
leg.Draw()

topLeft_x_left    = 0.14
topLeft_y_bottom  = 0.832117
topLeft_x_right   = 0.49
topLeft_y_top     = 0.892944

header_x_left    = 0.55
header_y_bottom  = 0.90
header_x_right   = 0.91
header_y_top     = 0.95

LumiLabel = TPaveLabel(topLeft_x_left,topLeft_y_bottom,topLeft_x_right,topLeft_y_top,"CMS Internal Simulation","NDC")
LumiLabel.SetTextFont(62)
LumiLabel.SetTextSize(0.8)
LumiLabel.SetTextAlign(12)
LumiLabel.SetBorderSize(0)
LumiLabel.SetFillColor(0)
LumiLabel.SetFillStyle(0)
LumiLabel.Draw()

HeaderLabel = TPaveLabel(header_x_left,header_y_bottom,header_x_right,header_y_top,"13 TeV","NDC")
HeaderLabel.SetTextFont(42)
HeaderLabel.SetTextSize(0.697674)
HeaderLabel.SetTextAlign(32)
HeaderLabel.SetBorderSize(0)
HeaderLabel.SetFillColor(0)
HeaderLabel.SetFillStyle(0)
HeaderLabel.Draw()

p2.cd()

y_ratio = np.divide(y_parking,y_mumu)

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

c.Update()

c.Write()

{
#include <fstream>
#include <sstream>
  using namespace std;
  gROOT->Reset();
  gROOT->SetStyle("Plain");
  gROOT->ForceStyle(); //forces it to use the style set above, rather than the style the rootfile was made with
  gROOT->LoadMacro("./style.cpp");
  global_style();
  int color_plot=1;   // 1/0 for color/black&white plots
  //gStyle->SetOptStat(10); //print only entries in histogram
  //gStyle->SetOptStat("e"); //print only entries in histogram
  //gStyle->SetOptStat("nemrou"); //print histogram name, entries, mean, rms, overflow, underflow
  gStyle->SetOptStat("emrou"); //entries, mean, rms, overflow, underflow

  bool save_plots = true;

  TCanvas* canvas = new TCanvas("c1","c1",100,100,700,550);
  canvas_style(canvas);
  canvas->SetGrid();

  TH1* h_2018data_promptRegion_0mum=new TH1F("h_2018data_promptRegion_0mum","",9,0,9);//,100,0,20000);
  h_2018data_promptRegion_0mum->SetStats(kFALSE);
  h_2018data_promptRegion_0mum->SetTitle(";Subleading ele d0 range, Leading ele d0 range;D actual/estimate");
  h_2018data_promptRegion_0mum->GetYaxis()->SetRangeUser(0.9,1.4);
  h1_style(h_2018data_promptRegion_0mum,3,1,1,1001,50,-1111.,-1111.,510,510,20,1,1.4,0);

  TH1* h_2018data_promptRegion_10mum=new TH1F("h_2018data_promptRegion_10mum","",9,0,9);//,100,0,20000);
  h_2018data_promptRegion_10mum->SetStats(kFALSE);
  h_2018data_promptRegion_10mum->SetTitle(";Subleading ele d0 range, Leading ele d0 range;D actual/estimate");
  h_2018data_promptRegion_10mum->GetYaxis()->SetRangeUser(0.9,1.4);
  h1_style(h_2018data_promptRegion_10mum,3,2,2,1001,50,-1111.,-1111.,510,510,20,1,1.4,0);

  TH1* h_2018data_promptRegion_20mum=new TH1F("h_2018data_promptRegion_20mum","",9,0,9);//,100,0,20000);
  h_2018data_promptRegion_20mum->SetStats(kFALSE);
  h_2018data_promptRegion_20mum->SetTitle(";Subleading ele d0 range, Leading ele d0 range;D actual/estimate");
  h_2018data_promptRegion_20mum->GetYaxis()->SetRangeUser(0.9,1.4);
  h1_style(h_2018data_promptRegion_20mum,3,3,3,1001,50,-1111.,-1111.,510,510,20,1,1.4,0);

  TH1* h_2018data_promptRegion_30mum=new TH1F("h_2018data_promptRegion_30mum","",9,0,9);//,100,0,20000);
  h_2018data_promptRegion_30mum->SetStats(kFALSE);
  h_2018data_promptRegion_30mum->SetTitle(";Subleading ele d0 range, Leading ele d0 range;D actual/estimate");
  h_2018data_promptRegion_30mum->GetYaxis()->SetRangeUser(0.9,1.4);
  h1_style(h_2018data_promptRegion_30mum,3,4,4,1001,50,-1111.,-1111.,510,510,20,1,1.4,0);

  TH1* h_2018data_promptRegion_40mum=new TH1F("h_2018data_promptRegion_40mum","",9,0,9);//,100,0,20000);
  h_2018data_promptRegion_40mum->SetStats(kFALSE);
  h_2018data_promptRegion_40mum->SetTitle(";Subleading ele d0 range, Leading ele d0 range;D actual/estimate");
  h_2018data_promptRegion_40mum->GetYaxis()->SetRangeUser(0.9,1.4);
  h1_style(h_2018data_promptRegion_40mum,3,6,6,1001,50,-1111.,-1111.,510,510,20,1,1.4,0);

  const int n_rows = 9;
  Float_t rows[n_rows];
  Float_t ratios_2018data_promptRegion_0mum[n_rows]; 
  Float_t ratios_2018data_promptRegion_10mum[n_rows]; 
  Float_t ratios_2018data_promptRegion_20mum[n_rows]; 
  Float_t ratios_2018data_promptRegion_30mum[n_rows]; 
  Float_t ratios_2018data_promptRegion_40mum[n_rows]; 
  string d0Ranges[n_rows];

  ifstream infile_2018data_promptRegion_0mum;
  infile_2018data_promptRegion_0mum.open("./ratios_2018data_promptRegion_0mum.txt");

  ifstream infile_2018data_promptRegion_10mum;
  infile_2018data_promptRegion_10mum.open("./ratios_2018data_promptRegion_10mum.txt");

  ifstream infile_2018data_promptRegion_20mum;
  infile_2018data_promptRegion_20mum.open("./ratios_2018data_promptRegion_20mum.txt");

  ifstream infile_2018data_promptRegion_30mum;
  infile_2018data_promptRegion_30mum.open("./ratios_2018data_promptRegion_30mum.txt");

  ifstream infile_2018data_promptRegion_40mum;
  infile_2018data_promptRegion_40mum.open("./ratios_2018data_promptRegion_40mum.txt");

  for(int i=0; i<n_rows; i++){
    infile_2018data_promptRegion_0mum >> rows[i] >> ratios_2018data_promptRegion_0mum[i] >> d0Ranges[i];
    infile_2018data_promptRegion_10mum >> rows[i] >> ratios_2018data_promptRegion_10mum[i] >> d0Ranges[i];
    infile_2018data_promptRegion_20mum >> rows[i] >> ratios_2018data_promptRegion_20mum[i] >> d0Ranges[i];
    infile_2018data_promptRegion_30mum >> rows[i] >> ratios_2018data_promptRegion_30mum[i] >> d0Ranges[i];
    infile_2018data_promptRegion_40mum >> rows[i] >> ratios_2018data_promptRegion_40mum[i] >> d0Ranges[i];
    //cout<<"rows["<<i<<"] is: "<<rows[i]<<", ratios_2018data_promptRegion_0mum is: "<<ratios_2018data_promptRegion_0mum[i]<<endl;
  }
  infile_2018data_promptRegion_0mum.close();

  for(int i=0; i<n_rows; i++){
    h_2018data_promptRegion_0mum->SetBinContent(i+1,ratios_2018data_promptRegion_0mum[i]);
    h_2018data_promptRegion_0mum->GetXaxis()->SetBinLabel(i+1,d0Ranges[i].c_str());

    h_2018data_promptRegion_10mum->SetBinContent(i+1,ratios_2018data_promptRegion_10mum[i]);
    h_2018data_promptRegion_10mum->GetXaxis()->SetBinLabel(i+1,d0Ranges[i].c_str());

    h_2018data_promptRegion_20mum->SetBinContent(i+1,ratios_2018data_promptRegion_20mum[i]);
    h_2018data_promptRegion_20mum->GetXaxis()->SetBinLabel(i+1,d0Ranges[i].c_str());

    h_2018data_promptRegion_30mum->SetBinContent(i+1,ratios_2018data_promptRegion_30mum[i]);
    h_2018data_promptRegion_30mum->GetXaxis()->SetBinLabel(i+1,d0Ranges[i].c_str());

    h_2018data_promptRegion_40mum->SetBinContent(i+1,ratios_2018data_promptRegion_40mum[i]);
    h_2018data_promptRegion_40mum->GetXaxis()->SetBinLabel(i+1,d0Ranges[i].c_str());
  }

  Leg1 = new TLegend(0.15,0.65,0.30,0.85);
  Leg1->AddEntry(h_2018data_promptRegion_0mum,"2018 data, Prompt Region, starting at 0 mum","l");
  Leg1->AddEntry(h_2018data_promptRegion_10mum,"2018 data, Prompt Region, starting at 10 mum","l");
  Leg1->AddEntry(h_2018data_promptRegion_20mum,"2018 data, Prompt Region, starting at 20 mum","l");
  Leg1->AddEntry(h_2018data_promptRegion_30mum,"2018 data, Prompt Region, starting at 30 mum","l");
  Leg1->AddEntry(h_2018data_promptRegion_40mum,"2018 data, Prompt Region, starting at 40 mum","l");
  Leg1->SetBorderSize(0);
  Leg1->SetTextSize(0.04);
  Leg1->SetFillColor(0);

  TLine *line = new TLine(0,1.0,9,1);

  canvas->cd();
  h_2018data_promptRegion_0mum->Draw("hist");
  h_2018data_promptRegion_10mum->Draw("histsame");
  h_2018data_promptRegion_20mum->Draw("histsame");
  h_2018data_promptRegion_30mum->Draw("histsame");
  h_2018data_promptRegion_40mum->Draw("histsame");
  Leg1->Draw();
  line->Draw();
  if(save_plots) canvas->SaveAs("graph_2018data_PromptRegion.pdf");

}

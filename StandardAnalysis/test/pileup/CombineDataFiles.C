TString inputFiles[6] = {"puData_2016_central", "puData_2016_up", "puData_2016_down",
                          "puData_2016GH_central", "puData_2016GH_up", "puData_2016GH_down"};

TString histNames[6] = {"data2016", "data2016Up", "data2016Down",
                         "data2016_GH", "data2016_GHUp", "data2016_GHDown"};

void CombineDataFiles() {

  TFile * output = new TFile("puData.root", "RECREATE");

  for(int i = 0; i < 6; i++) {
    TFile * input = new TFile(inputFiles[i] + ".root");

    cout << "working on " << inputFiles[i] << ".root" << endl;

    TH1D * hist = (TH1D*)input->Get("pileup");
    if(!hist) continue;
    output->cd();
    hist->Write(histNames[i]);

    input->Close();
  }

  output->Write();
  output->Close();

}

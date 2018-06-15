
void CombineDataFiles() {

  TString inputFiles[6] = {"puData_central", "puData_up", "puData_down",
                            "puData_filtered_central", "puData_filtered_up", "puData_filtered_down"};
  TString histNames[6];
  if (strcmp(getenv("CMSSW_VERSION"), "CMSSW_8_0_21") == 0) {
      histNames[0] = "data2016";
      histNames[1] = "data2016Up";
      histNames[2] = "data2016Down";
      histNames[3] = "data2016_GH";
      histNames[4] = "data2016_GHUp";
      histNames[5] = "data2016_GHDown";
  }
  else if (strcmp(getenv("CMSSW_VERSION"), "CMSSW_9_4_8") == 0) {
      histNames[0] = "data2017";
      histNames[1] = "data2017Up";
      histNames[2] = "data2017Down";
      histNames[3] = "data2017_CDEF";
      histNames[4] = "data2017_CDEFUp";
      histNames[5] = "data2017_CDEFDown";
  }

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

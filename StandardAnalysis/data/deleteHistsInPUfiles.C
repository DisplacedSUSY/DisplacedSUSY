// Usage: root -b -q -l deleteHistsInPUfiles.C

void deleteHistsInPUfiles() {
  //TFile* file = new TFile("pu2016.root","update");
  //TFile* file = new TFile("pu2017.root","update");
  TFile* file = new TFile("pu2018.root","update");

  gDirectory->Delete("stopToLD100_0p01mm;1");
  gDirectory->Delete("stopToLD100_0p02mm;1");
  gDirectory->Delete("stopToLD100_0p03mm;1");
  gDirectory->Delete("stopToLD100_0p04mm;1");
  gDirectory->Delete("stopToLD100_0p05mm;1");
  gDirectory->Delete("stopToLD100_0p06mm;1");
  gDirectory->Delete("stopToLD100_0p07mm;1");
  gDirectory->Delete("stopToLD100_0p08mm;1");
  gDirectory->Delete("stopToLD100_0p09mm;1");
  gDirectory->Delete("stopToLD100_0p1mm;1");

  gDirectory->Delete("stopToLD200_0p01mm;1");
  gDirectory->Delete("stopToLD200_0p02mm;1");
  gDirectory->Delete("stopToLD200_0p03mm;1");
  gDirectory->Delete("stopToLD200_0p04mm;1");
  gDirectory->Delete("stopToLD200_0p05mm;1");
  gDirectory->Delete("stopToLD200_0p06mm;1");
  gDirectory->Delete("stopToLD200_0p07mm;1");
  gDirectory->Delete("stopToLD200_0p08mm;1");
  gDirectory->Delete("stopToLD200_0p09mm;1");
  gDirectory->Delete("stopToLD200_0p1mm;1");

  gDirectory->Delete("stopToLD300_0p01mm;1");
  gDirectory->Delete("stopToLD300_0p02mm;1");
  gDirectory->Delete("stopToLD300_0p03mm;1");
  gDirectory->Delete("stopToLD300_0p04mm;1");
  gDirectory->Delete("stopToLD300_0p05mm;1");
  gDirectory->Delete("stopToLD300_0p06mm;1");
  gDirectory->Delete("stopToLD300_0p07mm;1");
  gDirectory->Delete("stopToLD300_0p08mm;1");
  gDirectory->Delete("stopToLD300_0p09mm;1");
  gDirectory->Delete("stopToLD300_0p1mm;1");

  gDirectory->Delete("stopToLD400_0p01mm;1");
  gDirectory->Delete("stopToLD400_0p02mm;1");
  gDirectory->Delete("stopToLD400_0p03mm;1");
  gDirectory->Delete("stopToLD400_0p04mm;1");
  gDirectory->Delete("stopToLD400_0p05mm;1");
  gDirectory->Delete("stopToLD400_0p06mm;1");
  gDirectory->Delete("stopToLD400_0p07mm;1");
  gDirectory->Delete("stopToLD400_0p08mm;1");
  gDirectory->Delete("stopToLD400_0p09mm;1");
  gDirectory->Delete("stopToLD400_0p1mm;1");

  gDirectory->Delete("stopToLD500_0p01mm;1");
  gDirectory->Delete("stopToLD500_0p02mm;1");
  gDirectory->Delete("stopToLD500_0p03mm;1");
  gDirectory->Delete("stopToLD500_0p04mm;1");
  gDirectory->Delete("stopToLD500_0p05mm;1");
  gDirectory->Delete("stopToLD500_0p06mm;1");
  gDirectory->Delete("stopToLD500_0p07mm;1");
  gDirectory->Delete("stopToLD500_0p08mm;1");
  gDirectory->Delete("stopToLD500_0p09mm;1");
  gDirectory->Delete("stopToLD500_0p1mm;1");

  gDirectory->Delete("stopToLD600_0p01mm;1");
  gDirectory->Delete("stopToLD600_0p02mm;1");
  gDirectory->Delete("stopToLD600_0p03mm;1");
  gDirectory->Delete("stopToLD600_0p04mm;1");
  gDirectory->Delete("stopToLD600_0p05mm;1");
  gDirectory->Delete("stopToLD600_0p06mm;1");
  gDirectory->Delete("stopToLD600_0p07mm;1");
  gDirectory->Delete("stopToLD600_0p08mm;1");
  gDirectory->Delete("stopToLD600_0p09mm;1");
  gDirectory->Delete("stopToLD600_0p1mm;1");

  gDirectory->Delete("stopToLD700_0p01mm;1");
  gDirectory->Delete("stopToLD700_0p02mm;1");
  gDirectory->Delete("stopToLD700_0p03mm;1");
  gDirectory->Delete("stopToLD700_0p04mm;1");
  gDirectory->Delete("stopToLD700_0p05mm;1");
  gDirectory->Delete("stopToLD700_0p06mm;1");
  gDirectory->Delete("stopToLD700_0p07mm;1");
  gDirectory->Delete("stopToLD700_0p08mm;1");
  gDirectory->Delete("stopToLD700_0p09mm;1");
  gDirectory->Delete("stopToLD700_0p1mm;1");

  gDirectory->Delete("stopToLD800_0p01mm;1");
  gDirectory->Delete("stopToLD800_0p02mm;1");
  gDirectory->Delete("stopToLD800_0p03mm;1");
  gDirectory->Delete("stopToLD800_0p04mm;1");
  gDirectory->Delete("stopToLD800_0p05mm;1");
  gDirectory->Delete("stopToLD800_0p06mm;1");
  gDirectory->Delete("stopToLD800_0p07mm;1");
  gDirectory->Delete("stopToLD800_0p08mm;1");
  gDirectory->Delete("stopToLD800_0p09mm;1");
  gDirectory->Delete("stopToLD800_0p1mm;1");

  gDirectory->Delete("stopToLD900_0p01mm;1");
  gDirectory->Delete("stopToLD900_0p02mm;1");
  gDirectory->Delete("stopToLD900_0p03mm;1");
  gDirectory->Delete("stopToLD900_0p04mm;1");
  gDirectory->Delete("stopToLD900_0p05mm;1");
  gDirectory->Delete("stopToLD900_0p06mm;1");
  gDirectory->Delete("stopToLD900_0p07mm;1");
  gDirectory->Delete("stopToLD900_0p08mm;1");
  gDirectory->Delete("stopToLD900_0p09mm;1");
  gDirectory->Delete("stopToLD900_0p1mm;1");

  gDirectory->Delete("stopToLD1000_0p01mm;1");
  gDirectory->Delete("stopToLD1000_0p02mm;1");
  gDirectory->Delete("stopToLD1000_0p03mm;1");
  gDirectory->Delete("stopToLD1000_0p04mm;1");
  gDirectory->Delete("stopToLD1000_0p05mm;1");
  gDirectory->Delete("stopToLD1000_0p06mm;1");
  gDirectory->Delete("stopToLD1000_0p07mm;1");
  gDirectory->Delete("stopToLD1000_0p08mm;1");
  gDirectory->Delete("stopToLD1000_0p09mm;1");
  gDirectory->Delete("stopToLD1000_0p1mm;1");

  gDirectory->Delete("stopToLD1100_0p01mm;1");
  gDirectory->Delete("stopToLD1100_0p02mm;1");
  gDirectory->Delete("stopToLD1100_0p03mm;1");
  gDirectory->Delete("stopToLD1100_0p04mm;1");
  gDirectory->Delete("stopToLD1100_0p05mm;1");
  gDirectory->Delete("stopToLD1100_0p06mm;1");
  gDirectory->Delete("stopToLD1100_0p07mm;1");
  gDirectory->Delete("stopToLD1100_0p08mm;1");
  gDirectory->Delete("stopToLD1100_0p09mm;1");
  gDirectory->Delete("stopToLD1100_0p1mm;1");

  gDirectory->Delete("stopToLD1200_0p01mm;1");
  gDirectory->Delete("stopToLD1200_0p02mm;1");
  gDirectory->Delete("stopToLD1200_0p03mm;1");
  gDirectory->Delete("stopToLD1200_0p04mm;1");
  gDirectory->Delete("stopToLD1200_0p05mm;1");
  gDirectory->Delete("stopToLD1200_0p06mm;1");
  gDirectory->Delete("stopToLD1200_0p07mm;1");
  gDirectory->Delete("stopToLD1200_0p08mm;1");
  gDirectory->Delete("stopToLD1200_0p09mm;1");
  gDirectory->Delete("stopToLD1200_0p1mm;1");

  gDirectory->Delete("stopToLD1300_0p01mm;1");
  gDirectory->Delete("stopToLD1300_0p02mm;1");
  gDirectory->Delete("stopToLD1300_0p03mm;1");
  gDirectory->Delete("stopToLD1300_0p04mm;1");
  gDirectory->Delete("stopToLD1300_0p05mm;1");
  gDirectory->Delete("stopToLD1300_0p06mm;1");
  gDirectory->Delete("stopToLD1300_0p07mm;1");
  gDirectory->Delete("stopToLD1300_0p08mm;1");
  gDirectory->Delete("stopToLD1300_0p09mm;1");
  gDirectory->Delete("stopToLD1300_0p1mm;1");

  gDirectory->Delete("stopToLD1400_0p01mm;1");
  gDirectory->Delete("stopToLD1400_0p02mm;1");
  gDirectory->Delete("stopToLD1400_0p03mm;1");
  gDirectory->Delete("stopToLD1400_0p04mm;1");
  gDirectory->Delete("stopToLD1400_0p05mm;1");
  gDirectory->Delete("stopToLD1400_0p06mm;1");
  gDirectory->Delete("stopToLD1400_0p07mm;1");
  gDirectory->Delete("stopToLD1400_0p08mm;1");
  gDirectory->Delete("stopToLD1400_0p09mm;1");
  gDirectory->Delete("stopToLD1400_0p1mm;1");

  gDirectory->Delete("stopToLD1500_0p01mm;1");
  gDirectory->Delete("stopToLD1500_0p02mm;1");
  gDirectory->Delete("stopToLD1500_0p03mm;1");
  gDirectory->Delete("stopToLD1500_0p04mm;1");
  gDirectory->Delete("stopToLD1500_0p05mm;1");
  gDirectory->Delete("stopToLD1500_0p06mm;1");
  gDirectory->Delete("stopToLD1500_0p07mm;1");
  gDirectory->Delete("stopToLD1500_0p08mm;1");
  gDirectory->Delete("stopToLD1500_0p09mm;1");
  gDirectory->Delete("stopToLD1500_0p1mm;1");

  gDirectory->Delete("stopToLD1600_0p01mm;1");
  gDirectory->Delete("stopToLD1600_0p02mm;1");
  gDirectory->Delete("stopToLD1600_0p03mm;1");
  gDirectory->Delete("stopToLD1600_0p04mm;1");
  gDirectory->Delete("stopToLD1600_0p05mm;1");
  gDirectory->Delete("stopToLD1600_0p06mm;1");
  gDirectory->Delete("stopToLD1600_0p07mm;1");
  gDirectory->Delete("stopToLD1600_0p08mm;1");
  gDirectory->Delete("stopToLD1600_0p09mm;1");
  gDirectory->Delete("stopToLD1600_0p1mm;1");

  gDirectory->Delete("stopToLD1700_0p01mm;1");
  gDirectory->Delete("stopToLD1700_0p02mm;1");
  gDirectory->Delete("stopToLD1700_0p03mm;1");
  gDirectory->Delete("stopToLD1700_0p04mm;1");
  gDirectory->Delete("stopToLD1700_0p05mm;1");
  gDirectory->Delete("stopToLD1700_0p06mm;1");
  gDirectory->Delete("stopToLD1700_0p07mm;1");
  gDirectory->Delete("stopToLD1700_0p08mm;1");
  gDirectory->Delete("stopToLD1700_0p09mm;1");
  gDirectory->Delete("stopToLD1700_0p1mm;1");

  gDirectory->Delete("stopToLD1800_0p01mm;1");
  gDirectory->Delete("stopToLD1800_0p02mm;1");
  gDirectory->Delete("stopToLD1800_0p03mm;1");
  gDirectory->Delete("stopToLD1800_0p04mm;1");
  gDirectory->Delete("stopToLD1800_0p05mm;1");
  gDirectory->Delete("stopToLD1800_0p06mm;1");
  gDirectory->Delete("stopToLD1800_0p07mm;1");
  gDirectory->Delete("stopToLD1800_0p08mm;1");
  gDirectory->Delete("stopToLD1800_0p09mm;1");
  gDirectory->Delete("stopToLD1800_0p1mm;1");




  gDirectory->Delete("stopToLB100_0p01mm;1");
  gDirectory->Delete("stopToLB100_0p02mm;1");
  gDirectory->Delete("stopToLB100_0p03mm;1");
  gDirectory->Delete("stopToLB100_0p04mm;1");
  gDirectory->Delete("stopToLB100_0p05mm;1");
  gDirectory->Delete("stopToLB100_0p06mm;1");
  gDirectory->Delete("stopToLB100_0p07mm;1");
  gDirectory->Delete("stopToLB100_0p08mm;1");
  gDirectory->Delete("stopToLB100_0p09mm;1");
  gDirectory->Delete("stopToLB100_0p1mm;1");

  gDirectory->Delete("stopToLB200_0p01mm;1");
  gDirectory->Delete("stopToLB200_0p02mm;1");
  gDirectory->Delete("stopToLB200_0p03mm;1");
  gDirectory->Delete("stopToLB200_0p04mm;1");
  gDirectory->Delete("stopToLB200_0p05mm;1");
  gDirectory->Delete("stopToLB200_0p06mm;1");
  gDirectory->Delete("stopToLB200_0p07mm;1");
  gDirectory->Delete("stopToLB200_0p08mm;1");
  gDirectory->Delete("stopToLB200_0p09mm;1");
  gDirectory->Delete("stopToLB200_0p1mm;1");

  gDirectory->Delete("stopToLB300_0p01mm;1");
  gDirectory->Delete("stopToLB300_0p02mm;1");
  gDirectory->Delete("stopToLB300_0p03mm;1");
  gDirectory->Delete("stopToLB300_0p04mm;1");
  gDirectory->Delete("stopToLB300_0p05mm;1");
  gDirectory->Delete("stopToLB300_0p06mm;1");
  gDirectory->Delete("stopToLB300_0p07mm;1");
  gDirectory->Delete("stopToLB300_0p08mm;1");
  gDirectory->Delete("stopToLB300_0p09mm;1");
  gDirectory->Delete("stopToLB300_0p1mm;1");

  gDirectory->Delete("stopToLB400_0p01mm;1");
  gDirectory->Delete("stopToLB400_0p02mm;1");
  gDirectory->Delete("stopToLB400_0p03mm;1");
  gDirectory->Delete("stopToLB400_0p04mm;1");
  gDirectory->Delete("stopToLB400_0p05mm;1");
  gDirectory->Delete("stopToLB400_0p06mm;1");
  gDirectory->Delete("stopToLB400_0p07mm;1");
  gDirectory->Delete("stopToLB400_0p08mm;1");
  gDirectory->Delete("stopToLB400_0p09mm;1");
  gDirectory->Delete("stopToLB400_0p1mm;1");

  gDirectory->Delete("stopToLB500_0p01mm;1");
  gDirectory->Delete("stopToLB500_0p02mm;1");
  gDirectory->Delete("stopToLB500_0p03mm;1");
  gDirectory->Delete("stopToLB500_0p04mm;1");
  gDirectory->Delete("stopToLB500_0p05mm;1");
  gDirectory->Delete("stopToLB500_0p06mm;1");
  gDirectory->Delete("stopToLB500_0p07mm;1");
  gDirectory->Delete("stopToLB500_0p08mm;1");
  gDirectory->Delete("stopToLB500_0p09mm;1");
  gDirectory->Delete("stopToLB500_0p1mm;1");

  gDirectory->Delete("stopToLB600_0p01mm;1");
  gDirectory->Delete("stopToLB600_0p02mm;1");
  gDirectory->Delete("stopToLB600_0p03mm;1");
  gDirectory->Delete("stopToLB600_0p04mm;1");
  gDirectory->Delete("stopToLB600_0p05mm;1");
  gDirectory->Delete("stopToLB600_0p06mm;1");
  gDirectory->Delete("stopToLB600_0p07mm;1");
  gDirectory->Delete("stopToLB600_0p08mm;1");
  gDirectory->Delete("stopToLB600_0p09mm;1");
  gDirectory->Delete("stopToLB600_0p1mm;1");

  gDirectory->Delete("stopToLB700_0p01mm;1");
  gDirectory->Delete("stopToLB700_0p02mm;1");
  gDirectory->Delete("stopToLB700_0p03mm;1");
  gDirectory->Delete("stopToLB700_0p04mm;1");
  gDirectory->Delete("stopToLB700_0p05mm;1");
  gDirectory->Delete("stopToLB700_0p06mm;1");
  gDirectory->Delete("stopToLB700_0p07mm;1");
  gDirectory->Delete("stopToLB700_0p08mm;1");
  gDirectory->Delete("stopToLB700_0p09mm;1");
  gDirectory->Delete("stopToLB700_0p1mm;1");

  gDirectory->Delete("stopToLB800_0p01mm;1");
  gDirectory->Delete("stopToLB800_0p02mm;1");
  gDirectory->Delete("stopToLB800_0p03mm;1");
  gDirectory->Delete("stopToLB800_0p04mm;1");
  gDirectory->Delete("stopToLB800_0p05mm;1");
  gDirectory->Delete("stopToLB800_0p06mm;1");
  gDirectory->Delete("stopToLB800_0p07mm;1");
  gDirectory->Delete("stopToLB800_0p08mm;1");
  gDirectory->Delete("stopToLB800_0p09mm;1");
  gDirectory->Delete("stopToLB800_0p1mm;1");

  gDirectory->Delete("stopToLB900_0p01mm;1");
  gDirectory->Delete("stopToLB900_0p02mm;1");
  gDirectory->Delete("stopToLB900_0p03mm;1");
  gDirectory->Delete("stopToLB900_0p04mm;1");
  gDirectory->Delete("stopToLB900_0p05mm;1");
  gDirectory->Delete("stopToLB900_0p06mm;1");
  gDirectory->Delete("stopToLB900_0p07mm;1");
  gDirectory->Delete("stopToLB900_0p08mm;1");
  gDirectory->Delete("stopToLB900_0p09mm;1");
  gDirectory->Delete("stopToLB900_0p1mm;1");

  gDirectory->Delete("stopToLB1000_0p01mm;1");
  gDirectory->Delete("stopToLB1000_0p02mm;1");
  gDirectory->Delete("stopToLB1000_0p03mm;1");
  gDirectory->Delete("stopToLB1000_0p04mm;1");
  gDirectory->Delete("stopToLB1000_0p05mm;1");
  gDirectory->Delete("stopToLB1000_0p06mm;1");
  gDirectory->Delete("stopToLB1000_0p07mm;1");
  gDirectory->Delete("stopToLB1000_0p08mm;1");
  gDirectory->Delete("stopToLB1000_0p09mm;1");
  gDirectory->Delete("stopToLB1000_0p1mm;1");

  gDirectory->Delete("stopToLB1100_0p01mm;1");
  gDirectory->Delete("stopToLB1100_0p02mm;1");
  gDirectory->Delete("stopToLB1100_0p03mm;1");
  gDirectory->Delete("stopToLB1100_0p04mm;1");
  gDirectory->Delete("stopToLB1100_0p05mm;1");
  gDirectory->Delete("stopToLB1100_0p06mm;1");
  gDirectory->Delete("stopToLB1100_0p07mm;1");
  gDirectory->Delete("stopToLB1100_0p08mm;1");
  gDirectory->Delete("stopToLB1100_0p09mm;1");
  gDirectory->Delete("stopToLB1100_0p1mm;1");

  gDirectory->Delete("stopToLB1200_0p01mm;1");
  gDirectory->Delete("stopToLB1200_0p02mm;1");
  gDirectory->Delete("stopToLB1200_0p03mm;1");
  gDirectory->Delete("stopToLB1200_0p04mm;1");
  gDirectory->Delete("stopToLB1200_0p05mm;1");
  gDirectory->Delete("stopToLB1200_0p06mm;1");
  gDirectory->Delete("stopToLB1200_0p07mm;1");
  gDirectory->Delete("stopToLB1200_0p08mm;1");
  gDirectory->Delete("stopToLB1200_0p09mm;1");
  gDirectory->Delete("stopToLB1200_0p1mm;1");

  gDirectory->Delete("stopToLB1300_0p01mm;1");
  gDirectory->Delete("stopToLB1300_0p02mm;1");
  gDirectory->Delete("stopToLB1300_0p03mm;1");
  gDirectory->Delete("stopToLB1300_0p04mm;1");
  gDirectory->Delete("stopToLB1300_0p05mm;1");
  gDirectory->Delete("stopToLB1300_0p06mm;1");
  gDirectory->Delete("stopToLB1300_0p07mm;1");
  gDirectory->Delete("stopToLB1300_0p08mm;1");
  gDirectory->Delete("stopToLB1300_0p09mm;1");
  gDirectory->Delete("stopToLB1300_0p1mm;1");

  gDirectory->Delete("stopToLB1400_0p01mm;1");
  gDirectory->Delete("stopToLB1400_0p02mm;1");
  gDirectory->Delete("stopToLB1400_0p03mm;1");
  gDirectory->Delete("stopToLB1400_0p04mm;1");
  gDirectory->Delete("stopToLB1400_0p05mm;1");
  gDirectory->Delete("stopToLB1400_0p06mm;1");
  gDirectory->Delete("stopToLB1400_0p07mm;1");
  gDirectory->Delete("stopToLB1400_0p08mm;1");
  gDirectory->Delete("stopToLB1400_0p09mm;1");
  gDirectory->Delete("stopToLB1400_0p1mm;1");

  gDirectory->Delete("stopToLB1500_0p01mm;1");
  gDirectory->Delete("stopToLB1500_0p02mm;1");
  gDirectory->Delete("stopToLB1500_0p03mm;1");
  gDirectory->Delete("stopToLB1500_0p04mm;1");
  gDirectory->Delete("stopToLB1500_0p05mm;1");
  gDirectory->Delete("stopToLB1500_0p06mm;1");
  gDirectory->Delete("stopToLB1500_0p07mm;1");
  gDirectory->Delete("stopToLB1500_0p08mm;1");
  gDirectory->Delete("stopToLB1500_0p09mm;1");
  gDirectory->Delete("stopToLB1500_0p1mm;1");

  gDirectory->Delete("stopToLB1600_0p01mm;1");
  gDirectory->Delete("stopToLB1600_0p02mm;1");
  gDirectory->Delete("stopToLB1600_0p03mm;1");
  gDirectory->Delete("stopToLB1600_0p04mm;1");
  gDirectory->Delete("stopToLB1600_0p05mm;1");
  gDirectory->Delete("stopToLB1600_0p06mm;1");
  gDirectory->Delete("stopToLB1600_0p07mm;1");
  gDirectory->Delete("stopToLB1600_0p08mm;1");
  gDirectory->Delete("stopToLB1600_0p09mm;1");
  gDirectory->Delete("stopToLB1600_0p1mm;1");

  gDirectory->Delete("stopToLB1700_0p01mm;1");
  gDirectory->Delete("stopToLB1700_0p02mm;1");
  gDirectory->Delete("stopToLB1700_0p03mm;1");
  gDirectory->Delete("stopToLB1700_0p04mm;1");
  gDirectory->Delete("stopToLB1700_0p05mm;1");
  gDirectory->Delete("stopToLB1700_0p06mm;1");
  gDirectory->Delete("stopToLB1700_0p07mm;1");
  gDirectory->Delete("stopToLB1700_0p08mm;1");
  gDirectory->Delete("stopToLB1700_0p09mm;1");
  gDirectory->Delete("stopToLB1700_0p1mm;1");

  gDirectory->Delete("stopToLB1800_0p01mm;1");
  gDirectory->Delete("stopToLB1800_0p02mm;1");
  gDirectory->Delete("stopToLB1800_0p03mm;1");
  gDirectory->Delete("stopToLB1800_0p04mm;1");
  gDirectory->Delete("stopToLB1800_0p05mm;1");
  gDirectory->Delete("stopToLB1800_0p06mm;1");
  gDirectory->Delete("stopToLB1800_0p07mm;1");
  gDirectory->Delete("stopToLB1800_0p08mm;1");
  gDirectory->Delete("stopToLB1800_0p09mm;1");
  gDirectory->Delete("stopToLB1800_0p1mm;1");


  file->Close();
}

/* d02004style.C
   This routine defines a set of functions to setup
         general, canvas and histogram styles
   recommended by D0. "zmumu_1.C" macro illustrates its usage.
                                 Created: January 2003, Avto Kharchilava
                                 Updated: January 2004,      --"--
				  Modified: May 2011, Juliette, for compare_onoffHLT
*/

// ... Global attributes go here ...
void global_style() {
  gStyle->SetPalette(1); //better colors

  //gStyle->SetCanvasColor(0);
  gStyle->SetCanvasBorderMode(0);
  gStyle->SetPadColor(0);
  gStyle->SetPadBorderMode(0);
  gStyle->SetFrameBorderMode(0);
  //gStyle->SetFrameLineWidth(2); //make frame around histograms thicker
  
  gStyle->SetTitleColor(1);   // 0
  gStyle->SetTitleBorderSize(1);
  //gStyle->SetTitleX(0.10);
  //gStyle->SetTitleY(0.94);
  gStyle->SetTitleW(0.5);
  gStyle->SetTitleH(0.06);
  
  //gStyle->SetLabelOffset(1e-04);
  //gStyle->SetLabelSize(0.2);
  
  gStyle->SetStatColor(0);
  gStyle->SetStatBorderSize(1);
  //gStyle->SetStatX(0.90);
  //gStyle->SetStatY(0.90);
  gStyle->SetStatW(0.30);
  gStyle->SetStatH(0.15);
  gStyle->SetOptFit(0001); //print name and value of parameters for the gaussian fits  
  
  gStyle->SetErrorX(0.0);   // Horizontal error bar size
  //   gStyle->SetPaperSize(10.,12.);   // Printout size
}

// ... Canvas attributes ...
void canvas_style(TCanvas *c,
                  float left_margin=0.10,//0.15,//0.05,
		  float right_margin=0.20,//0.12,//0.04,
		  float top_margin=0.08,
		  float bottom_margin=0.3,//0.15,//0.45,
		  int canvas_color=0,
                  int frame_color=0) {
  
  c->SetLeftMargin(left_margin);
  c->SetRightMargin(right_margin);
  c->SetTopMargin(top_margin);
  c->SetBottomMargin(bottom_margin);
  c->SetFillColor(canvas_color);
  c->SetFrameFillColor(frame_color);
  
  c->SetBorderMode(0);
  c->SetBorderSize(1);
  c->SetFrameBorderMode(0);
}

// ... 1D histogram attributes; (2D to come) ...
void h1_style(TH1 *h,
	      int line_width=3,
	      int line_color=1,
	      int line_style=1, 
	      int fill_style=1001,
	      int fill_color=50,
	      float y_min=-1111.,
	      float y_max=-1111.,
	      int ndivx=510,
	      int ndivy=510,
	      int marker_style=6,
	      int marker_color=1,
	      float marker_size=0.5,
	      int optstat=0) {
  
  h->SetLineWidth(line_width);
  h->SetLineColor(line_color);
  h->SetLineStyle(line_style);
  //h->SetFillColor(fill_color);
  //h->SetFillStyle(fill_style);
  //h->SetMaximum(y_max);
  //h->SetMinimum(y_min);
  //h->GetXaxis()->SetNdivisions(ndivx);
  //h->GetYaxis()->SetNdivisions(ndivy);
  
  h->SetMarkerStyle(marker_style);
  h->SetMarkerColor(marker_color);
  h->SetMarkerSize(marker_size);
  h->SetStats(optstat);
  
  h->SetLabelFont(62,"X");       // 42
  h->SetLabelFont(62,"Y");       // 42
  h->SetLabelOffset(0.005,"X");  // D=0.005
  h->SetLabelOffset(0.005,"Y");  // D=0.005
  h->SetLabelSize(0.04,"X");
  h->SetLabelSize(0.045,"Y");
  h->SetTitleOffset(1.3,"X");
  h->SetTitleOffset(1,"Y");
  //h->SetTitleOffset(0.5,"Y");
  h->SetTitleSize(0.05,"X");
  h->SetTitleSize(0.05,"Y");
  //h->SetTitleSize(0.045,"Y");
  //h->SetTitle(0);

  h->GetXaxis()->CenterTitle();
  h->GetYaxis()->CenterTitle();
}

// ... 1D histogram attributes; (2D to come) ...
void h1_styleOBJ(TH1& hOBJ,
		 int line_width=3,
		 int line_color=1,
		 int line_style=1, 
		 int fill_style=1001,
		 int fill_color=50,
		 float y_min=-1111.,
		 float y_max=-1111.,
		 int ndivx=510,
		 int ndivy=510,
		 int marker_style=20,
		 int marker_color=1,
		 float marker_size=0.5,
		 int optstat=0) {
  
  hOBJ.SetLineWidth(line_width);
  hOBJ.SetLineColor(line_color);
  hOBJ.SetLineStyle(line_style);
  //h->SetFillColor(fill_color);
  //h->SetFillStyle(fill_style);
  //h->SetMaximum(y_max);
  //h->SetMinimum(y_min);
  //h->GetXaxis()->SetNdivisions(ndivx);
  //h->GetYaxis()->SetNdivisions(ndivy);
  
  hOBJ.SetMarkerStyle(marker_style);
  hOBJ.SetMarkerColor(marker_color);
  hOBJ.SetMarkerSize(marker_size);
  hOBJ.SetStats(optstat);
  
  hOBJ.SetLabelFont(62,"X");       // 42
  hOBJ.SetLabelFont(62,"Y");       // 42
  hOBJ.SetLabelOffset(0.000,"X");  // D=0.005
  hOBJ.SetLabelOffset(0.005,"Y");  // D=0.005
  hOBJ.SetLabelSize(0.055,"X");
  hOBJ.SetLabelSize(0.055,"Y");
  hOBJ.SetTitleOffset(1,"X");
  hOBJ.SetTitleOffset(1.3,"Y");
  hOBJ.SetTitleSize(0.06,"X");
  hOBJ.SetTitleSize(0.06,"Y");
  hOBJ.SetTitle(0);

  hOBJ.GetXaxis()->CenterTitle();
  hOBJ.GetYaxis()->CenterTitle();
}

// ... 2D histogram attributes
void h2_style(TH2 *h2,
	      int line_width=2,
	      int line_color=1,
	      int line_style=1, 
	      int fill_style=1001,
	      int fill_color=50,
	      float y_min=-1111.,
	      float y_max=-1111.,
	      int ndivx=510,
	      int ndivy=510,
	      int marker_style=20,
	      int marker_color=1,
	      float marker_size=0.5,
	      int optstat=0) {
  
  h2->SetLineWidth(line_width);
  h2->SetLineColor(line_color);
  h2->SetLineStyle(line_style);
  //h2->SetFillColor(fill_color);
  //h2->SetFillStyle(fill_style);
  //h2->SetMaximum(y_max);
  //h2->SetMinimum(y_min);
  //h2->GetXaxis()->SetNdivisions(ndivx);
  //h2->GetYaxis()->SetNdivisions(ndivy);
  
  h2->SetMarkerStyle(marker_style);
  h2->SetMarkerColor(marker_color);
  h2->SetMarkerSize(marker_size);
  h2->SetStats(optstat);
  
  h2->SetLabelFont(62,"X");       // 42
  h2->SetLabelFont(62,"Y");       // 42
  h2->SetLabelOffset(0.000,"X");  // D=0.005
  h2->SetLabelOffset(0.005,"Y");  // D=0.005
  h2->SetLabelSize(0.04,"X");
  h2->SetLabelSize(0.045,"Y");
  //h2->SetTitleOffset(1,"X");
  h2->SetTitleOffset(0.8,"X");
  h2->SetTitleOffset(1,"Y");
  h2->SetTitleSize(0.05,"X");
  h2->SetTitleSize(0.05,"Y");
  //h2->SetTitle(0);

  h2->GetXaxis()->CenterTitle();
  h2->GetYaxis()->CenterTitle();
}


void h2_styleOBJ(TH2& h2OBJ,
		 int line_width=2,
		 int line_color=1,
		 int line_style=1, 
		 int fill_style=1001,
		 int fill_color=50,
		 float y_min=-1111.,
		 float y_max=-1111.,
		 int ndivx=510,
		 int ndivy=510,
		 int marker_style=20,
		 int marker_color=1,
		 float marker_size=0.15,
		 int optstat=0) {
  
  h2OBJ.SetLineWidth(line_width);
  h2OBJ.SetLineColor(line_color);
  h2OBJ.SetLineStyle(line_style);
  //h2->SetFillColor(fill_color);
  //h2->SetFillStyle(fill_style);
  //h2->SetMaximum(y_max);
  //h2->SetMinimum(y_min);
  //h2->GetXaxis()->SetNdivisions(ndivx);
  //h2->GetYaxis()->SetNdivisions(ndivy);
  
  h2OBJ.SetMarkerStyle(marker_style);
  h2OBJ.SetMarkerColor(marker_color);
  h2OBJ.SetMarkerSize(marker_size);
  h2OBJ.SetStats(optstat);
  
  h2OBJ.SetLabelFont(62,"X");       // 42
  h2OBJ.SetLabelFont(62,"Y");       // 42
  h2OBJ.SetLabelOffset(0.000,"X");  // D=0.005
  h2OBJ.SetLabelOffset(0.005,"Y");  // D=0.005
  h2OBJ.SetLabelSize(0.055,"X");
  h2OBJ.SetLabelSize(0.055,"Y");
  h2OBJ.SetTitleOffset(1,"X");
  h2OBJ.SetTitleOffset(1.3,"Y");
  h2OBJ.SetTitleSize(0.06,"X");
  h2OBJ.SetTitleSize(0.06,"Y");
  h2OBJ.SetTitle(0);

  h2OBJ.GetXaxis()->CenterTitle();
  h2OBJ.GetYaxis()->CenterTitle();
}

void gr_style(TGraph *gr,
	      int line_width=2,
	      int line_color=1,
	      int line_style=1, 
	      int fill_style=1001,
	      int fill_color=50,
	      float y_min=-1111.,
	      float y_max=-1111.,
	      int ndivx=510,
	      int ndivy=510,
	      int marker_style=20,
	      int marker_color=1,
	      float marker_size=1,
	      int optstat=1) {
  
  gr->SetLineWidth(line_width);
  gr->SetLineColor(line_color);
  gr->SetLineStyle(line_style);
  //h2->SetFillColor(fill_color);
  //h2->SetFillStyle(fill_style);
  //h2->SetMaximum(y_max);
  //h2->SetMinimum(y_min);
  //h2->GetXaxis()->SetNdivisions(ndivx);
  //h2->GetYaxis()->SetNdivisions(ndivy);
  
  gr->SetMarkerStyle(marker_style);
  gr->SetMarkerColor(marker_color);
  gr->SetMarkerSize(marker_size);
  
  gr->GetXaxis()->SetLabelFont(62);       // 42
  gr->GetYaxis()->SetLabelFont(62);       // 42
  gr->GetXaxis()->SetLabelOffset(0.000);  // D=0.005
  gr->GetYaxis()->SetLabelOffset(0.005);  // D=0.005
  gr->GetXaxis()->SetLabelSize(0.05);
  gr->GetYaxis()->SetLabelSize(0.045);
  gr->GetXaxis()->SetTitleOffset(.95);
  gr->GetYaxis()->SetTitleOffset(1.);
  gr->GetXaxis()->SetTitleSize(0.05);
  gr->GetYaxis()->SetTitleSize(0.05);
  gr->SetTitle(0);

  gr->GetXaxis()->CenterTitle();
  gr->GetYaxis()->CenterTitle();
}

#include "Riostream.h"
#include "TH1.h"
#include "TChain.h"
#include "TString.h"
#include "TLegend.h"
#include "TTree.h"
#include "TPad.h"
#include "TLine.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TLatex.h"
#include <string.h> // used in another function within the same file
#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

void drawTChain() {
	TCanvas *c1 = new TCanvas("c5","c5",600,400);
	TH1 *h2 = new TH1F("h2","h2",150,500,2000);

	string root_lists = "/eos/user/e/esaraiva/dijet_pythia_bdt.txt";
	//string root_lists = "/eos/user/w/wasu/AQT_dijet_data_bdt/dijet_data_bdt.txt";
	string sLine="";
	ifstream infile;
	infile.open(root_lists.c_str());//Data());

	while(!infile.eof())  {
		getline(infile,sLine);

		TFile f2(sLine.c_str());

		TTree *t1 = (TTree*)f2.Get("AntiKt4EMPFlow_dijet_insitu");

		Bool_t pass_HLT_j400; 
		UInt_t mcChannelNumber;
		Float_t j1_pT;
		Float_t j2_pT;
		Float_t weight;
		Float_t weight_pileup;
		Float_t pdfWeights[101];
		Float_t j1_eta;
		Float_t j2_eta;

		t1->SetBranchStatus("*",0);
		t1->SetBranchStatus("pass_HLT_j400",1);
		t1->SetBranchStatus("mcChannelNumber",1);
		t1->SetBranchStatus("j1_pT",1);
		t1->SetBranchStatus("j2_pT",1);
		t1->SetBranchStatus("j1_eta",1);
		t1->SetBranchStatus("j2_eta",1);
		t1->SetBranchStatus("weight",1);
		t1->SetBranchStatus("weight_pileup",1);
		t1->SetBranchStatus("pdfWeights",1);

		t1->SetBranchAddress("mcChannelNumber",&mcChannelNumber);
		mcChannelNumber = t1->GetEntry(1);

		t1->SetBranchAddress("weight",&weight);
		weight = t1->GetEntry(1);

		t1->SetBranchAddress("weight_pileup",&weight_pileup);
		weight_pileup = t1->GetEntry(1);

		float mc_weight;
		int mc_mod;

		mc_mod = mcChannelNumber % 100;
		TString mod = Form("AntiKt4EMPFlow_J%d_sumOfWeights",mc_mod);
		TH1 *h = (TH1F*)f2.Get(mod);
		mc_weight = h->GetBinContent(1);

		float w;
		w = pdfWeights[0] * weight * mc_weight;

		t1->SetBranchAddress("j1_pT",&j1_pT);
		t1->SetBranchAddress("j2_pT",&j2_pT);
		t1->SetBranchAddress("pass_HLT_j400",&pass_HLT_j400);

		int entries;
		entries = t1->GetEntries();

		for (int i=0; i<entries; ++i) {
			t1->GetEvent(i);
			if(pass_HLT_j400 == true && j1_pT > 500 && j1_pT < 2000 && abs(j1_eta) < 2.1 && j1_eta/j2_eta < 1.5) {
				h2->Fill(j1_pT,w);
				h2->Fill(j2_pT,w);
			}
		}
	}
	gStyle->SetOptStat(0);

	h2->Draw("");

	TLatex l1;
	l1.SetTextSize(0.025);
	l1.SetNDC();
	l1.SetTextColor(1);
	l1.DrawLatex(0.15,0.84,"#it{#bf{#scale[1.8]{#bf{ATLAS} Simulation Preliminary}}}");
	l1.DrawLatex(0.15,0.80,"#bf{#scale[1.5]{#sqrt{s} = 13 TeV}}");
	l1.DrawLatex(0.15,0.76,"#bf{#scale[1.5]{Dijet Event, Trigger = HLT_j400}}");

	c1->Print("pt-spectrum.pdf");

	h2->Draw("HIST");

	TLatex l2;
	l2.SetTextSize(0.025);
	l2.SetNDC();
	l2.SetTextColor(1);
	l2.DrawLatex(0.15,0.84,"#it{#bf{#scale[1.8]{#bf{ATLAS} Simulation Preliminary}}}");
	l2.DrawLatex(0.15,0.80,"#bf{#scale[1.5]{#sqrt{s} = 13 TeV}}");
	l2.DrawLatex(0.15,0.76,"#bf{#scale[1.5]{Dijet Event, Trigger = HLT_j400}}");

	c1->Print("pt-spectrum-hist.pdf");
	
	h2->Draw("");
	c1->Print("pt-spectrm-dijet.root");
}

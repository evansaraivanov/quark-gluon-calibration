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
using namespace std;

void drawPTspectrum(){

TCanvas* c1 = new TCanvas("c1","c1",600,400);
TFile *f = new TFile("/eos/user/e/esaraiva/dijet_pythia_bdt_pt.root","recreate");
//TFile *f = new TFile("/eos/user/w/wasu/AQT_dijet_data_bdt/dijet_data_bdt.root","recreate");

TChain* fChain = new TChain("AntiKt4EMPFlow_dijet_insitu");

string root_lists = "/eos/user/e/esaraiva/dijet_pythia_bdt.txt";
//string root_lists = "/eos/user/w/wasu/AQT_dijet_data_bdt/dijet_data_bdt.txt";
string sLine="";
ifstream infile;
infile.open(root_lists.c_str());//Data());

TFile f2(sLine.c_str());

while(!infile.eof())
{
	getline(infile,sLine);
	fChain->Add(sLine.c_str());
}

//cout << sLine.c_str() << endl;

//TFile f2(sLine.c_str());

//infile.close();


UInt_t mcChannelNumber; 
Bool_t pass_HLT_j400; 
Bool_t j1_is_truth_jet; 
Bool_t j2_is_truth_jet; 
Float_t j1_pT;
Float_t j2_pT;
Float_t j1_pT_truth;
Float_t j2_pT_truth;
Float_t j1_eta;
Float_t j2_eta;
Float_t j1_eta_truth;
Float_t j2_eta_truth;
Float_t weight;
Float_t weight_ptslice;
Float_t weight_pileup;
Float_t pdfWeights[101];
Float_t j2_bdt_resp;
Float_t j1_bdt_resp;
Float_t j1_trackWidth;
Float_t j2_trackWidth;
Float_t j1_trackC1;
Float_t j2_trackC1;
Int_t j1_NumTrkPt500;
Int_t j2_NumTrkPt500;
Int_t j1_partonLabel;
Int_t j2_partonLabel;




fChain->SetBranchStatus("*",0);
fChain->SetBranchStatus("mcChannelNumber",1);
fChain->SetBranchStatus("pass_HLT_j400",1);
fChain->SetBranchStatus("j1_is_truth_jet",1);
fChain->SetBranchStatus("j2_is_truth_jet",1);
fChain->SetBranchStatus("j1_pT",1);
fChain->SetBranchStatus("j2_pT",1);
fChain->SetBranchStatus("j1_pT_truth",1);
fChain->SetBranchStatus("j2_pT_truth",1);
fChain->SetBranchStatus("j1_eta",1);
fChain->SetBranchStatus("j2_eta",1);
fChain->SetBranchStatus("j1_eta_truth",1);
fChain->SetBranchStatus("j2_eta_truth",1);
fChain->SetBranchStatus("weight_ptslice",1);
fChain->SetBranchStatus("weight",1);
fChain->SetBranchStatus("weight_pileup",1);
fChain->SetBranchStatus("pdfWeights",1);
fChain->SetBranchStatus("j1_NumTrkPt500",1);
fChain->SetBranchStatus("j2_NumTrkPt500",1);
fChain->SetBranchStatus("j1_trackWidth",1);
fChain->SetBranchStatus("j2_trackWidth",1);
fChain->SetBranchStatus("j1_trackC1",1);
fChain->SetBranchStatus("j2_trackC1",1);
fChain->SetBranchStatus("j1_bdt_resp",1);
fChain->SetBranchStatus("j2_bdt_resp",1);
fChain->SetBranchStatus("j1_partonLabel",1);
fChain->SetBranchStatus("j2_partonLabel",1); 


//TTree *t2 = fChain->CloneTree(0);
//t2->CopyEntries(fChain);

fChain->SetBranchAddress("mcChannelNumber",&mcChannelNumber);
mcChannelNumber = fChain->GetEntry(1);

fChain->SetBranchAddress("weight_ptslice",&weight_ptslice);
weight_ptslice = fChain->GetEntry(1);

fChain->SetBranchAddress("weight",&weight);
weight = fChain->GetEntry(1);

fChain->SetBranchAddress("weight_pileup",&weight_pileup);
weight_pileup = fChain->GetEntry(1);

float mc_weight;

if(mcChannelNumber == 364700) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J0_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364701) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J1_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364702) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J2_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364703) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J3_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364704) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J4_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364705) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J5_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364706) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J6_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364707) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J7_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364708) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J8_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364709) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J9_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364710) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J10_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364711) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J11_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}
if(mcChannelNumber == 364712) { 
	TH1 *h = (TH1F*)f2.Get("AntiKt4EMPFlow_J12_sumOfWeights");
	mc_weight = h->GetBinContent(1);
}

float w;
w = -1*weight_pileup*weight_ptslice*mc_weight;

//cout << weight << ", " << weight_pileup << ", " << mc_weight << ", " << w;

TCanvas *c5 = new TCanvas("c5","c5",600,400);
TH1 *h2 = new TH1F("h2","h2",150,500,2000);

fChain->SetBranchAddress("j1_pT",&j1_pT);
fChain->SetBranchAddress("j2_pT",&j2_pT);

int entries;
entries = fChain->GetEntries();
for (int i=0; i<entries; ++i) {
	fChain->GetEntry(i);
//	cout >> j1_pT >> ", " >> j2_pT >> ", " >> w;
	h2->Fill(j1_pT,w);
	h2->Fill(j2_pT,w);
}

h2->Draw("");
c5->Print("pt-spectrum.root");
h2->Draw("");
c5->Print("pt-spectrum.pdf");

cout << "done.";

//TTree *t2 = fChain->CopyTree("j1_pT>500 && j1_is_truth_jet &&j2_is_truth_jet && j3_is_truth_jet");
//delete f;
//t2->Print();
//f->Write();
f->Close();
//f2.Close();
//infile.close();
}

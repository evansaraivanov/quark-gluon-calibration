from ROOT import *

var = "ntrk" #analysis variable,pick from  ntrk, bdt

#varData = TFile("dijet_data_py.root")
varMC = TFile("dijet_sherpa_py.root")

bin = [300,400,500,600,800,1000,1200,1500]

def myText(x,y,text, color=1):
    l= TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    

for i in range(2,8):
    higherQuark = varMC.Get(str(bin[i])+"_LeadingJet_Forward_Quark_"+var+";1")
    higherQuark2 = varMC.Get(str(bin[i])+"_SubJet_Forward_Quark_"+var+";1")
    lowerQuark = varMC.Get(str(bin[i])+"_LeadingJet_Central_Quark_"+var+";1")
    lowerQuark2 = varMC.Get(str(bin[i])+"_SubJet_Central_Quark_"+var+";1")

    higherQuark.Add(higherQuark2)
    lowerQuark.Add(lowerQuark2)

    higherGluon = varMC.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_"+var+";1")
    higherGluon2 = varMC.Get(str(bin[i])+"_SubJet_Forward_Gluon_"+var+";1")
    lowerGluon = varMC.Get(str(bin[i])+"_LeadingJet_Central_Gluon_"+var+";1")
    lowerGluon2 = varMC.Get(str(bin[i])+"_SubJet_Central_Gluon_"+var+";1")

    higherGluon.Add(higherGluon2)
    lowerGluon.Add(lowerGluon2)

    #Normalize histograms
    if(higherQuark.Integral() != 0):
        higherQuark.Scale(1./higherQuark.Integral())
    if(lowerQuark.Integral() != 0 ):
        lowerQuark.Scale(1./lowerQuark.Integral())
    if(higherGluon.Integral() != 0):
        higherGluon.Scale(1./higherGluon.Integral())
    if(lowerGluon.Integral() != 0):
        lowerGluon.Scale(1./lowerGluon.Integral())

    if(bin[i] == 500):
        higherQuark500 = higherQuark
        lowerQuark500 = lowerQuark
        higherGluon500 = higherGluon
        lowerGluon500 = lowerGluon
    if(bin[i] == 1000):
        higherQuark800 = higherQuark
        lowerQuark800 = lowerQuark
        higherGluon800 = higherGluon
        lowerGluon800 = lowerGluon
    if(bin[i] == 1500):
        higherQuark1200 = higherQuark
        lowerQuark1200 = lowerQuark
        higherGluon1200 = higherGluon
        lowerGluon1200 = lowerGluon

#Create plots
c1 = TCanvas("c1","c1",500,500)
gStyle.SetOptStat(0)

higherQuark500.GetXaxis().SetTitle(var)
higherQuark500.GetYaxis().SetTitle("Normalized")

if(var == "bdt"):
    higherQuark500.GetYaxis().SetRangeUser(0,.075)
if(var == "ntrk"):
    higherQuark500.GetYaxis().SetRangeUser(0,.12)

higherQuark500.SetLineColor(1)
higherQuark500.SetLineStyle(1)
lowerQuark500.SetLineColor(1)
lowerQuark500.SetLineStyle(1)
higherGluon500.SetLineColor(1)
higherGluon500.SetLineStyle(2)
lowerGluon500.SetLineColor(1)
lowerGluon500.SetLineStyle(2)

higherQuark800.SetLineColor(2)
higherQuark800.SetLineStyle(1)
lowerQuark800.SetLineColor(2)
lowerQuark800.SetLineStyle(1)
higherGluon800.SetLineColor(2)
higherGluon800.SetLineStyle(2)
lowerGluon800.SetLineColor(2)
lowerGluon800.SetLineStyle(2)

higherQuark1200.SetLineColor(3)
higherQuark1200.SetLineStyle(1)
lowerQuark1200.SetLineColor(3)
lowerQuark1200.SetLineStyle(1)
higherGluon1200.SetLineColor(3)
higherGluon1200.SetLineStyle(2)
lowerGluon1200.SetLineColor(3)
lowerGluon1200.SetLineStyle(2)

leg1 = TLegend(.72,.72,.92,.92)
leg1.AddEntry(higherQuark500,"Quark Jet","L")
leg1.AddEntry(higherGluon500,"Gluon Jet","L")
leg1.AddEntry(higherQuark500,"500<pt<600 GeV","F")
leg1.AddEntry(higherQuark800,"1000<pt<1200 GeV","F")
leg1.AddEntry(higherQuark1200,"1200<pt<1500 GeV","F")

higherQuark500.Draw("HIST")
higherQuark800.Draw("HIST same")
higherQuark1200.Draw("HIST same")
higherGluon500.Draw("dash same")
higherGluon800.Draw("HIST same")
higherGluon1200.Draw("HIST same")
leg1.Draw("same")

myText(0.14,0.84,"#it{#bf{#scale[1.8]{#bf{ATLAS} Simulation Preliminary}}}")
myText(0.14,0.80,"#bf{#scale[1.5]{#sqrt{s}=13 GeV}}")
myText(0.14,0.76,"#bf{#scale[1.5]{Anti-K_{t} EM+JES R=0.4}}")
myText(0.14,0.72,"#bf{#scale[1.5]{|\eta|<2.1}}")

c1.Print("summary-higher-"+var+".pdf")

if(var == "bdt"):
    lowerQuark500.GetYaxis().SetRangeUser(0,.075)
if(var == "ntrk"):
    lowerQuark500.GetYaxis().SetRangeUser(0,.12)

lowerQuark500.Draw("HIST")
lowerQuark800.Draw("HIST same")
lowerQuark1200.Draw("HIST same") 
lowerGluon500.Draw("HIST same")
lowerGluon800.Draw("HIST same")
lowerGluon1200.Draw("HIST same")
leg1.Draw("same")

myText(0.14,0.84,"#it{#bf{#scale[1.8]{#bf{ATLAS} Simulation Preliminary}}}")
myText(0.14,0.80,"#bf{#scale[1.5]{#sqrt{s}=13 GeV}}")
myText(0.14,0.76,"#bf{#scale[1.5]{Anti-K_{t} EM+JES R=0.4}}")
myText(0.14,0.72,"#bf{#scale[1.5]{|\eta|<2.1}}")

c1.Print("summary-lower-"+var+".pdf")

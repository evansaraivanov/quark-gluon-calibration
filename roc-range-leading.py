from ROOT import *
import numpy as np

var1 = "bdt" #name of variable as shown in .root file
varmc = TFile("dijet-sherpa-eta.root")
VAR1 = "BDT" #this is how the variable will be displayed on the graph.

bin = [0.0,0.5,1.0,2.1]

def myText(x,y,text, color=1):
    l = TLatex()
    l.SetTextSize(0.025)
    l.SetNDC()
    l.SetTextColor(color)
    l.DrawLatex(x,y,text)
    pass

higherGraph = []
lowerGraph = []

for i in range(0,3):
    if(bin[i] != 1.0):
        higherQuark = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Quark_"+var1+";1")
        higherGluon = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_"+var1+";1")
    
    lowerQuark = varmc.Get(str(bin[i])+"_LeadingJet_Central_Quark_"+var1+";1")
    lowerGluon = varmc.Get(str(bin[i])+"_LeadingJet_Central_Gluon_"+var1+";1")

    #Normalize histograms
    if(higherQuark.Integral() != 0):
        higherQuark.Scale(1./higherQuark.Integral())
    if(lowerQuark.Integral() != 0):
        lowerQuark.Scale(1./lowerQuark.Integral())
    if(higherGluon.Integral() != 0):
        higherGluon.Scale(1./higherGluon.Integral())
    if(lowerGluon.Integral() != 0):
        lowerGluon.Scale(1./lowerGluon.Integral())

    u = np.empty(60)
    v = np.empty(60)
    x = np.empty(60)
    y = np.empty(60)

    if(bin[i] != 800):
        for j in range(60):
            x[j] = (higherQuark.Integral(0,j))
            y[j] = (1. - higherGluon.Integral(0,j))
            u[j] = (lowerQuark.Integral(0,j))
            v[j] = (1. - lowerGluon.Integral(0,j))

        higherGraph.append(x)
        higherGraph.append(y)
        lowerGraph.append(u)
        lowerGraph.append(v)

a = np.array([0.0000001,0.9999999])
b = np.array([0.9999999,0.0000001])

c1 = TCanvas("c1","c1",500,500)
c1.SetGrid()

gr1 = TGraph(60,higherGraph[0],higherGraph[1])
gr2 = TGraph(60,higherGraph[2],higherGraph[3])
gr3 = TGraph(60,higherGraph[4],higherGraph[5])
gr5 = TGraph(2,a,b)

gr1.SetLineColor(8)
gr2.SetLineColor(6)
gr3.SetLineColor(4)
gr5.SetLineStyle(2)

gr5.GetXaxis().SetTitle("Quark Efficiency")
gr5.GetYaxis().SetTitle("Gluon Rejection")

gr5.GetXaxis().SetLimits(0.,1.)
gr5.SetMinimum(0.)
gr5.SetMaximum(1.)

gr5.GetXaxis().SetLimits(0.,1.)
gr5.SetMinimum(0.)
gr5.SetMaximum(1.)

gPad.SetTickx()
gPad.SetTicky()
gStyle.SetGridStyle(2)
gStyle.SetGridColor(15)
gr5.SetLineStyle(2)

leg1 = TLegend(0.14,0.42,0.38,0.6)
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)
leg1.AddEntry("","Quark Jet Tagging, "+VAR1+" < X","")
leg1.AddEntry("","Forward Jet","")
leg1.AddEntry(gr1,"0.0 < |\eta| < 0.5","L")
leg1.AddEntry(gr2,"0.5 < |\eta| < 1.0","L")
leg1.AddEntry(gr3,"1.0 < |\eta| < 2.1","L")

gr5.SetTitle("")

gr5.Draw("AL")
gr1.Draw("C same")
gr2.Draw("C same")
gr3.Draw("C same")
leg1.Draw("same")

myText(0.13,0.30,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
myText(0.13,0.26,'#bf{#scale[1.2]{#sqrt{s}=13 GeV}}')
myText(0.13,0.22,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')
myText(0.13,0.18,'#bf{#scale[1.2]{|\eta|<2.1}}')

c1.Print("./roc-"+var1+"-higher.pdf")

c1 = TCanvas("c1","c1",500,500)
c1.SetGrid()

gr1 = TGraph(60,lowerGraph[0],lowerGraph[1])
gr2 = TGraph(60,lowerGraph[2],lowerGraph[3])
gr3 = TGraph(60,lowerGraph[4],lowerGraph[5])
gr5 = TGraph(2,a,b)

gr5.SetTitle("")

gr1.SetLineColor(8)
gr2.SetLineColor(6)
gr3.SetLineColor(4)
gr5.SetLineStyle(2)

gr5.GetXaxis().SetTitle("Quark Efficiency")
gr5.GetYaxis().SetTitle("Gluon Rejection")

gr5.GetXaxis().SetLimits(0.,1.)
gr5.SetMinimum(0.)
gr5.SetMaximum(1.)

gr5.GetXaxis().SetLimits(0.,1.)
gr5.SetMinimum(0.)
gr5.SetMaximum(1.)

gPad.SetTickx()
gPad.SetTicky()
gStyle.SetGridStyle(2)
gStyle.SetGridColor(15)

leg1 = TLegend(0.14,0.42,0.38,0.6)
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)
leg1.AddEntry("","Quark Jet Tagging, "+VAR1+" < X","")
leg1.AddEntry("","Central Jet","")
leg1.AddEntry(gr1,"0.0 < |\eta| < 0.5","L")
leg1.AddEntry(gr2,"0.5 < |\eta| < 1.0","L")
leg1.AddEntry(gr3,"1.0 < |\eta| < 2.1","L")

gr5.Draw("AL")
gr1.Draw("C same")
gr2.Draw("C same")
gr3.Draw("C same")
leg1.Draw("same")

myText(0.13,0.30,'#it{#bf{#scale[1.4]{#bf{ATLAS} Simulation Preliminary}}}')
myText(0.13,0.26,'#bf{#scale[1.2]{#sqrt{s}=13 GeV}}')
myText(0.13,0.22,'#bf{#scale[1.2]{Anti-K_{t} EM+JES R=0.4}}')
myText(0.13,0.18,'#bf{#scale[1.2]{|\eta|<2.1}}')

c1.Print("./roc-"+var1+"-lower.pdf")

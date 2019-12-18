from ROOT import *
import numpy as np

var = ["ntrk","width","c1","bdt"]
varmc = TFile("dijet_sherpa_py.root")

bin = [300,400,500,600,800,1000,1200,1500]

for i in range(2,8):
    higherGraph = [] #will hold list of plot x and y variabls in pairs for each analysis variable.
    lowerGraph = []

    for k in range(0,4):
        var1 = var[k] #iterate through

        higherQuark = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Quark_"+var1+";1")
        higherQuark2 = varmc.Get(str(bin[i])+"_SubJet_Forward_Quark_"+var1+";1")
        lowerQuark = varmc.Get(str(bin[i])+"_LeadingJet_Central_Quark_"+var1+";1")
        lowerQuark2 = varmc.Get(str(bin[i])+"_SubJet_Central_Quark_"+var1+";1")
    
        higherQuark.Add(higherQuark2)
        lowerQuark.Add(lowerQuark2)
    
        higherGluon = varmc.Get(str(bin[i])+"_LeadingJet_Forward_Gluon_"+var1+";1")
        higherGluon2 = varmc.Get(str(bin[i])+"_SubJet_Forward_Gluon_"+var1+";1")
        lowerGluon = varmc.Get(str(bin[i])+"_LeadingJet_Central_Gluon_"+var1+";1")
        lowerGluon2 = varmc.Get(str(bin[i])+"_SubJet_Central_Gluon_"+var1+";1")

        higherGluon.Add(higherGluon2)
        lowerGluon.Add(lowerGluon2)

        #Normalize histograms
        if(higherQuark.Integral() != 0):
            higherQuark.Scale(1./higherQuark.Integral())
        if(lowerQuark.Integral() != 0):
            lowerQuark.Scale(1./lowerQuark.Integral())
        if(higherGluon.Integral() != 0):
            higherGluon.Scale(1./higherGluon.Integral())
        if(lowerGluon.Integral() != 0):
            lowerGluon.Scale(1./lowerGluon.Integral())

        x = np.empty(60)
        y = np.empty(60)
        u = np.empty(60)
        v = np.empty(60)
    
        for j in range(60):
            x[j] = (higherQuark.Integral(0,j))
            y[j] = (1. - higherGluon.Integral(0,j))
            u[j] = (lowerQuark.Integral(0,j))
            v[j] = (1. - lowerGluon.Integral(0,j))

        higherGraph.append(x)
        higherGraph.append(y)
        lowerGraph.append(u)
        lowerGraph.append(v)

    a = np.array([0,1])
    b = np.array([1,0])

    c1 = TCanvas("c1","c1",500,500)
    c1.SetGrid()
    
    gr1 = TGraph(60,higherGraph[0],higherGraph[1])
    gr2 = TGraph(60,higherGraph[2],higherGraph[3])
    gr3 = TGraph(60,higherGraph[4],higherGraph[5])
    gr4 = TGraph(60,higherGraph[6],higherGraph[7])
    gr5 = TGraph(2,a,b)

    gr1.SetLineColor(1)
    gr2.SetLineColor(2)
    gr3.SetLineColor(3)
    gr4.SetLineColor(4)

    gr1.GetXaxis().SetTitle("Quark Efficiency")
    gr1.GetYaxis().SetTitle("Gluon Rejection")

    gPad.SetTickx()
    gPad.SetTicky()
    gStyle.SetGridStyle(0)

    gr1.Draw("")
    gr2.Draw("same")
    gr3.Draw("same")
    gr4.Draw("same")
    gr5.Draw("same")

    c1.Print(str(bin[i])+"-higher-ROC-plots.pdf")
    
    c1 = TCanvas("c1","c1",500,500)
    c1.SetGrid()

    gr1 = TGraph(60,lowerGraph[0],lowerGraph[1])
    gr2 = TGraph(60,lowerGraph[2],lowerGraph[3])
    gr3 = TGraph(60,lowerGraph[4],lowerGraph[5])
    gr4 = TGraph(60,lowerGraph[6],lowerGraph[7])
    gr5 = TGraph(2,a,b)

    gr1.SetLineColor(1)
    gr2.SetLineColor(2)
    gr3.SetLineColor(3)
    gr4.SetLineColor(4)

    gr1.GetXaxis().SetTitle("Quark Efficiency")
    gr1.GetYaxis().SetTitle("Gluon Rejection")

    gPad.SetTickx()
    gPad.SetTicky()
    gStyle.SetGridStyle(0)

    gPad.SetTickx()
    gPad.SetTicky()
    gStyle.SetGridStyle(0)

    gr1.Draw("")
    gr2.Draw("same")
    gr3.Draw("same")
    gr4.Draw("same")
    gr5.Draw("same")

    c1.Print(str(bin[i])+"-lower-ROC-plots.pdf")

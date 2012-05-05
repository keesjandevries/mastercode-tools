#! /usr/bin/env python
import ROOT as r

from histogramProcessing import entry_histo_name as histn

def HistExists(name,mcf):
    f=r.TFile.Open(mcf.FileName)
    hp=f.Get(name)
    if hp :
        f.Close()
        return name
    else :
        f.Close()
        return 0

def ParseVar(arg):
    s=arg.split("=")
    var=s[0].replace(' ','')
    val=float(s[1])
    return var, val

def search_hist_name(vars,mcf):
    name="_"
    vl = vars.keys()
    if len(vl)==1:
        name=histn(vl,mcf)
        return HistExists(name,mcf), vl

    if len(vl)==2:
        name=histn(vl,mcf)
        if HistExists(name,mcf):
            return name, vl
        else:
            vl.reverse()
            name=histn(vl,mcf)
            return HistExists(name,mcf), vl

    else:
        print "The given coordinate(s) could not be found in a histogram "
        return 0


def GetEntryFromHisto(vars,order,name,mcf):
    f=r.TFile.Open(mcf.FileName)
    hist=f.Get(name).Clone()

    if len(order)==1:
        var=order[0]
        bin=hist.FindBin(vars[var])
        n=hist.GetBinContent(bin)

    if len(order)==2:
        var1=order[0]
        var2=order[1]
        bin=hist.FindBin(vars[var1],vars[var2])
        n=int(hist.GetBinContent(bin))
        
    f.Close()

    return n

def GetVars(argv):
    # will output something like  {"m0" : 500, "m12" : 1000}
    vars={}
    for arg in argv:
        var,val=  ParseVar(arg)  
        vars[var]=val
    return vars
                        
def GetEntry(vars,mcf):
    name,order=search_hist_name(vars,mcf)

    if name:
        print "Coordinates found in ", name
        n=GetEntryFromHisto(vars,order,name,mcf)
        return n   
    else :
        return -1

def PrintInfo(n,mcf):
    print "Found entry number: ", n



#! /usr/bin/env python
import ROOT as r
from itertools import permutations

from histogramProcessing import entry_histo_full_path as histn
import MCchain as MCC

def getVars(argv) :
    # will output something like  {"m0" : 500, "m12" : 1000}
    vars={}
    for arg in argv:
        var,val=  parseVar(arg)
        vars[var]=val
    return vars

def parseVar(arg) :
    s=arg.split("=")
    var=s[0].replace(' ','')
    val=float(s[1])
    return var, val

def getEntry(vars,mcf) :
    name,order=searchHistName(vars,mcf)

    if name:
        print "Coordinates found in ", name
        n=getEntryFromHisto(vars,order,name,mcf)
        return n
    else :
        return -1

def getEntryFromHisto(vars,order,name,mcf) :
    f = r.TFile.Open(mcf.FileName)
    hist = f.Get(name).Clone()
    hist.SetDirectory(0)
    f.Close()

    vals = [ vars[var] for var in order ]
    print vals

    hBin = hist.FindBin( *vals )
    n = hist.GetBinContent(hBin)
    return int(n)

def histExists(name, mcf) :
    filename = mcf.FileName
    f = r.TFile(filename)
    assert not f.IsZombie(), filename

    hOld = f.Get(name)
    exists = True
    try :
        hOld.ClassName()
    except ReferenceError :
        exists = False
    return exists

def listPermutations( l ) :
    return list( permutations(l) )

def searchHistName(vars,mcf) :
    var_perms = listPermutations( vars.keys() )
    h = iter(var_perms)

    hExist = False
    try :
        while not hExist :
            p = h.next()
            name = histn(p, mcf)
            hExist = histExists( name, mcf )
    except StopIteration  :
        assert False, "The given coordinate(s) could not be found in a histogram "
    return name, p

def printAfterBurnerCoordinates(chain, mcf, n):
    chain.GetEntry(n)
    N=mcf.Inputs

    print "Command for AfterBurner.exe is:  "
    print "../bin/AfterBurner.exe 1 " ,
    for i in range(1,N+1):
        print chain.chi2vars[i], " ",  


def printInfo(n,mcf) :
    chain = MCC.MCchain( mcf )
    print "Found entry number: ", n
    printAfterBurnerCoordinates(chain, mcf, n)


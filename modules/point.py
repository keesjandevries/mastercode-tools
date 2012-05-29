#! /usr/bin/env python
import ROOT as r
from itertools import permutations

from histogramProcessing import entry_histo_full_path as histn
from modules.MCChain import MCAnalysisChain

AB_binary = "../bin/Afterburner.exe"

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

def getCoorEntry(vars,mcf) :
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
        assert False, "The given coordinate(s) could not be found in a histogram. Please make a corresponding EntryHist. "
    return name, p

def printAfterBurnerCoordinates(chain, mcf, n):
    print"\nCommand for AfterBurner.exe is: \n "
    print getAfterBurnerCommand(chain, mcf, n)
    print "\n"

def getAfterBurnerCommand( chain, mfc, n) : 
    input_coords = getInputCoordinates( chain, mfc, n )
    input_strings = [ str(input) for input in input_coords ]
    return "%s 0 %s" % ( AB_binary, " ".join( input_strings ) )
    
def getInputCoordinates( chain, mfc, n ) :
    chain.GetEntry(n)
    return [chain.treeVars["predictions"][ input ]   for input in range(1,mfc.Inputs+1) ]

def getBfEntry(mcf):
    f=r.TFile(mcf.FileName)
    bfName=getattr(mcf,"BestFitEntryName","BestFitEntry" )
    #check wheterh best fit point is in the file
    try:
        t=f.Get(bfName).Clone()
    except ReferenceError:
        assert False,   "\n\n%s does not contain a tree with the best fit point \n\n " % mcf.FileName
    
    for entry in t:
        n=entry.EntryNo

    f.Close()
    return n

def printChi2(chain, n):
    chain.GetEntry(n)
    print "\nTotal X^2 = ", chain.treeVars["predictions"][ 0 ]   , " \n"

def printN(n):
    print "\nFound entry number: ", n , "\n"

def printX2BreakDown(chain,mcf,n):
    import models
    import variables as v
    model  = models.get_model_from_file(mcf)
    lhoods = models.get_lhood_names(mcf)
    MCVdict=v.mc_variables()
    print "\nThe gaussian constraints give penalties:\n"
    print "    Penalty       Value Name            Type        Constraint"
    print "==================================================================="
    for constraint in model:
        sn=constraint.short_name
        MCV=MCVdict[sn]
        v_index = MCV.getIndex(mcf)
        chi2=chain.treeVars["contributions"][v_index]
        pred=chain.treeVars["predictions"][v_index]
        #print "{:11g} {:<{width}{precision}{base}}{c!r}".format(chi2, pred, base='g', width=1, precision=4, c=constraint)
        print "{:11.4g} {:11.4g} {!r}".format(chi2, pred, constraint)
        #print "{chi2:>f} {".format(chi2=chi2)
    print "==================================================================="

    print "\nThe likelihoods give penalties:\n"
    for i, lhood in enumerate(lhoods):
        chi2=chain.treeVars["lhoods"][i]
        print "{:11.4g} {!r}". format( chi2, lhood )

    
def printInfo(n,mcf) :
    chain = MCAnalysisChain( mcf )
    printN(n)
    printChi2(chain, n)
    printAfterBurnerCoordinates(chain, mcf, n)
    printX2BreakDown(chain,mcf,n)

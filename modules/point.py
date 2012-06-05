#! /usr/bin/env python
import ROOT as r
from itertools import permutations

from histogramProcessing import entry_histo_full_path as histn
from modules.MCChain import MCAnalysisChain

AB_binary = "../bin/AfterBurner.exe"

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

def printAfterBurnerCoordinates(chain, mcf):
    print"Command for AfterBurner.exe is: "
    print "\t%s" % getAfterBurnerCommand(chain, mcf)

def getAfterBurnerCommand( chain, mfc) : 
    input_coords = getInputCoordinates( chain, mfc )
    input_strings = [ str(input) for input in input_coords ]
    return "%s 0 %s" % ( AB_binary, " ".join( input_strings ) )
    
def getInputCoordinates( chain, mfc ) :
    return [chain.treeVars["predictions"][ input ]   for input in range(1,mfc.Inputs+1) ]

def getBfEntry(mcf):
    f=r.TFile(mcf.FileName)
    bfName=getattr(mcf,"BestFitEntryName","BestFitEntry" )
    #check wheterh best fit point is in the file
    try:
        t=f.Get(bfName).Clone()
    except ReferenceError:
        assert False,   "%s does not contain a tree with the best fit point" % mcf.FileName
    
    for entry in t:
        n=entry.EntryNo

    f.Close()
    return n

def printChi2(chain):
    print "\nTotal X^2 = %f" % chain.treeVars["predictions"][ 0 ]

def printN(n):
    print "Found entry number: %d" % n

def printX2BreakDown(chain,mcf,n):
    import models
    import variables as v
    model  = models.get_model_from_file(mcf)
    lhoods = models.get_lhood_names(mcf)
    MCVdict=v.mc_variables()
    if len( model ) > 0 :
        print "\nchi2 penalties from gaussian constraints :"
        print "==================================================================="
        print "    Penalty  Prediction   Name            Type       Constraint"
        print "==================================================================="
    for constraint in model:
        sn=constraint.short_name
        MCV=MCVdict[sn]
        v_index = MCV.getIndex(mcf)
        chi2=chain.treeVars["contributions"][v_index]
        pred=chain.treeVars["predictions"][v_index]
        #print "{:11g} {:<{width}{precision}{base}}{c!r}".format(chi2, pred, base='g', width=1, precision=4, c=constraint)
        print "{:11.2f} {:11.4g}   {!r}".format(chi2, pred, constraint)
        #print "{chi2:>f} {".format(chi2=chi2)
    print "==================================================================="

    if len(lhoods.keys()) > 0 : print "\nThe likelihoods give penalties:\n"
    for i, lhood in enumerate(lhoods.items()):
        chi2=chain.treeVars["lhoods"][i]
        print "{:11.2f} {:16} {:16}". format( chi2, lhood[0], lhood[1] )

def printMAInfo(chain,mcf):
    from math import sqrt
    MA =getPrediction(chain,mcf,"mA0")
    MAQ=sqrt(getPrediction(chain,mcf,"mA0^2"))
    a=(MAQ-MA)/MA
    print "\nMA info: \n "
    print "MA(Q=M_Z)    = %f" %MA 
    print "MA(Q=M_SUSY) = %f" %MAQ 
    print "a            = %f" % a
    
def getPrediction(chain,mcf,shortname):
    import variables as v
    MCVdict=v.mc_variables()
    index = MCVdict[shortname].getIndex(mcf)
    prediction=chain.treeVars["predictions"][index]
    return prediction


def printPrediction(chain,mcf,shortname):
    p=getPrediction(chain,mcf,shortname)
    print "{:11.2f} {!r}". format(p    , shortname) 


def printSpectrum(chain,mcf):
    spectrum_shortnames=[
    "chi1"    , 
    "chi2"    , 
    "neu1"    , 
    "neu2"    , 
    "neu3"    , 
    "neu4"    , 
    "sel_r"   , 
    "sel_l"   , 
    "snu_e"   , 
    "smu_r"   , 
    "smu_l"   , 
    "snu_mu"  , 
    "stau_1"  , 
    "stau_2"  , 
    "snu_tau" , 
    "squark_r",  
    "squark_l", 
    "stop1"   , 
    "stop2"   , 
    "sbottom1", 
    "sbottom2", 
    "gluino"  , 
    "mh0"     , 
    "mH0"     , 
    "mA0"     , 
    "mH+-"    ]

    print "\nMass spectrum:\n"
    for sn in spectrum_shortnames:
        printPrediction(chain,mcf,sn)

def printParameters(chain,mcf):
    para_shortnames=[
    "m0"  ,   
    "m12" ,  
    "A0"  ,  
    "tanb",  ]
    print "\nParameters:   \n"
    for sn in para_shortnames:
        printPrediction(chain,mcf,sn)
    if mcf.PredictionIndex==12:
        printPrediction(chain,mcf,"mh2")
        
def printMu(chain,mcf):
    print "\nmu:\n"
    printPrediction(chain,mcf,"mu")

def printInfo(n,mcf) :
    chain = MCAnalysisChain( mcf )
    chain.GetEntry(n)
    printN(n)
    printAfterBurnerCoordinates(chain, mcf)
    printChi2(chain)
    printParameters(chain,mcf)
    printMu(chain,mcf)
    printSpectrum(chain,mcf) 
    printX2BreakDown(chain,mcf,n)
    printMAInfo(chain,mcf)

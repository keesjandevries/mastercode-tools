#! /usr/bin/env python
import ROOT as r
from itertools import permutations

from histogramProcessing import entry_histo_full_path as histn
from modules.mcchain import MCAnalysisChain

AB_binary = "../bin/Afterburner.exe"

def get_vars(argv) :
    # will output something like  {"m0" : 500, "m12" : 1000}
    vars={}
    for arg in argv:
        var,val=  parse_var(arg)
        vars[var]=val
    return vars

def parse_var(arg) :
    s=arg.split("=")
    var=s[0].replace(' ','')
    val=float(s[1])
    return var, val

def get_coor_entry(vars,mcf) :
    name,order=search_hist_name(vars,mcf)

    if name:
        print "Coordinates found in ", name
        n=get_entry_from_histo(vars,order,name,mcf)
        return n
    else :
        return -1

def get_entry_from_histo(vars,order,name,mcf) :
    f = r.TFile.Open(mcf.FileName)
    hist = f.Get(name).Clone()
    hist.SetDirectory(0)
    f.Close()

    vals = [ vars[var] for var in order ]
    print vals

    hBin = hist.FindBin( *vals )
    n = hist.GetBinContent(hBin)
    return int(n)

def hist_exists(name, mcf) :
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

def list_permutations( l ) :
    return list( permutations(l) )

def search_hist_name(vars,mcf) :
    var_perms = list_permutations( vars.keys() )
    h = iter(var_perms)

    hExist = False
    try :
        while not hExist :
            p = h.next()
            name = histn(p, mcf)
            hExist = hist_exists( name, mcf )
    except StopIteration  :
        assert False, "The given coordinate(s) could not be found in a histogram. Please make a corresponding EntryHist. "
    return name, p

def print_afterburner_coordinates(chain, mcf, n):
    print"Command for AfterBurner.exe is: "
    print "\t%s" % get_afterburner_command(chain, mcf, n)

def get_afterburner_command( chain, mfc, n) :
    input_coords = get_input_coordinates( chain, mfc, n )
    input_strings = [ str(input) for input in input_coords ]
    return "%s 0 %s" % ( AB_binary, " ".join( input_strings ) )

def get_input_coordinates( chain, mfc, n ) :
    chain.GetEntry(n)
    return [chain.treeVars["predictions"][ input ]   for input in range(1,mfc.Inputs+1) ]

def get_best_fit_entry(mcf):
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

def print_chi2(chain, n):
    chain.GetEntry(n)
    print "Total X^2 = %f" % chain.treeVars["predictions"][ 0 ]

def print_n(n):
    print "Found entry number: %d" % n

def print_chi2_breakdown(chain,mcf,n):
    import models
    import variables as v
    model  = models.get_model_from_file(mcf)
    lhoods = models.get_lhood_names(mcf)
    MCVdict=v.mc_variables()
    if len( model ) > 0 :
        print "\nchi2 penalties from gaussian constraints :"
        print "==================================================================="
        print "    Penalty       Value Name            Type       Constraint"
        print "==================================================================="
    for constraint in model:
        sn=constraint.short_name
        MCV=MCVdict[sn]
        v_index = MCV.get_index(mcf)
        chi2=chain.treeVars["contributions"][v_index]
        pred=chain.treeVars["predictions"][v_index]
        #print "{:11g} {:<{width}{precision}{base}}{c!r}".format(chi2, pred, base='g', width=1, precision=4, c=constraint)
        print "{:11.4g} {:11.4g} {!r}".format(chi2, pred, constraint)
        #print "{chi2:>f} {".format(chi2=chi2)
    print "==================================================================="

    if len(lhoods.keys()) > 0 : print "\nThe likelihoods give penalties:\n"
    for i, lhood in enumerate(lhoods):
        chi2=chain.treeVars["lhoods"][i]
        print "{:11.4g} {!r}". format( chi2, lhood )


def print_info(n,mcf) :
    chain = MCAnalysisChain( mcf )
    print_n(n)
    print_chi2(chain, n)
    print_afterburner_coordinates(chain, mcf, n)
    print_chi2_breakdown(chain,mcf,n)

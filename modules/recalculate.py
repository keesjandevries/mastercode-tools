#! /usr/bin/env python
import models

import ROOT as r
import MCchain as MCC

from progress_bar import ProgressBar
from sys import stdout
from array import array

# avoid namespace clash
__DEBUG=False

def recalc_to_file( chain, model, lhoods, outfile, begin = None, end = None ) :
    nentries = chain.GetEntries()
    total_delta = 0

    # create trees in scope of outfile
    out = r.TFile(outfile,"recreate")
    chi2tree = chain.chi2chain.CloneTree(0)

    # might need to do address of on contirbvars
    contribvars = array('d',[0.0]*chain.nTotVars)
    contribtree = r.TTree( "contribtree", "chi2 contributions")
    varsOutName = "vars[%d]/D" % ( chain.nTotVars )
    contribtree.SetMaxTreeSize(10*chi2tree.GetMaxTreeSize())
    contribtree.Branch("vars",contribvars,varsOutName)

    if begin is None : begin = 0 
    if end is None   : end   = nentries+1 
    prog = ProgressBar(begin, end, 77, mode='fixed', char='#')
    for entry in range(begin,end) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()

        chain.GetEntry(entry)
        delta = 0.
        chi2 = 0

        for key in model.keys() :
            chi2_t = model[key].get_chi2( chain.chi2vars[key] )
            contribvars[key] = chi2_t
            chi2 += chi2_t
        for i,lh in enumerate(lhoods.values()) :
            chi2_t = lh.get_chi2( chain.chi2vars )
            contribvars[i+1] = chi2_t 
            chi2 += chi2_t

        # This was inserted to check on if there was a significant
        # calculation error ( average deltachi2 per entry: 1e-15 )
            if __DEBUG :
                delta_chi2_val = chi2_t - chain.contribvars[key]
                delta = delta + delta_chi2_val
                total_delta = total_delta + abs(delta)
        chain.chi2vars[0] = chi2
        contribvars[0] = chi2
        chi2tree.Fill()
        contribtree.Fill()

    chi2tree.AutoSave()
    contribtree.AutoSave()

    out.Close()

    if __DEBUG :
        print "\n--------------------------\n"
        print "   TOTAL    (    MEAN    )"
        print "%10e(%10e)" % ( total_delta, (total_delta/(end-begin)) )
        print "\n--------------------------\n"

def go( collection ) :
    m = models.get_model_from_file(collection.ModelFile)
    l = models.get_lhood_from_file( getattr(collection,"LHoodFile", None) )
    chain = MCC.MCchain( collection )
    nentries = chain.GetEntries()
    start = getattr( collection, "StartEntry", 0)
    end   = getattr( collection, "EndEntry", nentries)
    recalc_to_file( chain, m, l, collection.OutputFile, start, end )

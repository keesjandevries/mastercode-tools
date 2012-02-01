#! /usr/bin/env python
import models

import ROOT as r
import MCchain as MCC

from progress_bar import ProgressBar
from sys import stdout
from array import array

# avoid namespace clash
__DEBUG=True

def setup_chain( fd ) :
    filenames = sorted(fd.keys())
    chain = MCC.MCchain(filenames[0],fd[filenames[0]])
    # check all our fd have the same properties
    comp_dict = fd[filenames[0]]
    for f in filenames :
        for prop in comp_dict.keys() : assert fd[f][prop] == comp_dict[prop]
    
    if len(filenames) > 1 :
        chain.Add(filenames[1::])

    return chain

def recalc_to_file( chain, model, outfile ) :
    nentries = chain.GetEntries()
    total_delta = 0

    # create trees in scope of outfile
    out = r.TFile(outfile,"recreate")
    chi2tree = chain.chi2chain.CloneTree(0)
    contribvars = array('d',[0]*chain.nTotVars)
    contribtree = r.TTree( "contribtree", "chi2 contributions")
    varsOutName = "vars[%d]" % ( chain.nTotVars )
    contribtree.SetMaxTreeSize(10*chi2tree.GetMaxTreeSize())
    contribtree.Branch("vars",contribvars,varsOutName)

    prog = ProgressBar(0, nentries, 77, mode='fixed', char='#')
    for entry in range(0,nentries) :
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
        print "%10e(%10e)" % ( total_delta, (total_delta/nentries) )
        print "\n--------------------------\n"

def go( fd, output ) :
    indict = fd[sorted(fd.keys())[0]]
    m = models.get_model_from_file(indict["ModelFile"])
    chain = setup_chain( fd )
    assert chain.chi2_state, "Unable to retrieve chi2 tree (%s) from all files" % (chain.chi2treename)
    recalc_to_file( chain, m, output )

#! /usr/bin/env python
import models

import ROOT as r
import MCchain as MCC

from progress_bar import ProgressBar
from sys import stdout

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

    prog = ProgressBar(0, nentries, 77, mode='fixed', char='#')
    for entry in range(0,nentries) :
        prog.increment_amount()
        print prog,'\r',
        stdout.flush()
        chain.GetEntry(entry)
        delta = 0.
        for key in model.keys() :
            chi2 = model[key].get_chi2( chain.chi2vars[key] )
            delta_chi2_val = chi2 - chain.contribvars[key]
            delta = delta + delta_chi2_val
        total_delta = total_delta + abs(delta)

    print "   TOTAL    (    MEAN    )"
    print "%10e(%10e)" % ( total_delta, (total_delta/nentries) )

def go( fd, output ) :
    indict = fd[sorted(fd.keys())[0]]
    m = models.get_model_from_file(indict["ModelFile"])
    chain = setup_chain( fd )
    recalc_to_file( chain, m, output )

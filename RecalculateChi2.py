#! /usr/bin/env python

import models
import ROOT as r
import MCchain as MCC
from optparse import OptionParser

############################################
def opts():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option( "-m", "--model", action="store", dest="model",
        default="", 
        help = "model file containing list of constraints" )
    parser.add_option( "-o", "--output", action="store", dest="output",
        default="recalc_out.root", 
        help = "name for output file" )
    options,args = parser.parse_args()
    assert len(args) > 0,"File must be specified"
    assert len(options.model) > 0,"Model must be specified with -(-m)odel \
        command line argument"
    return options, args
############################################

def main( argv=None ) :
    options,args = opts()
    m = models.get_model_from_file(options.model)
    print args
    test = MCC.MCchain(args[0],"tree")
    test.Add(args[0::])
    nentries = test.GetEntries()
    total_delta = 0
    for entry in range(0, nentries ) :
        test.GetEntry(entry)
        delta = 0.
        for key in m.keys() :
            chi2 = m[key].get_chi2( test.chi2vars[key] )
            delta_chi2_val = chi2 - test.contribvars[key]
            delta = delta + delta_chi2_val
        total_delta = total_delta + abs(delta)

    print total_delta, "(", total_delta/nentries, ")"



if __name__ == "__main__":
    main()

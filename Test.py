#! /usr/bin/env python
import ROOT as r
from optparse import OptionParser


############################################
def opts():
    parser = OptionParser("usage: %prog [options] [args]")
    parser.add_option( "-c", "--constraint", action="store", dest="constraint"  ,
                       default=None , help="test a constraint for an input value" )
    parser.add_option( "-l", "--likelihood", action="store", dest="likelihood",
                       default=None , help="print info for specified likelihood" )
    options,args = parser.parse_args()
    if options.constraint is not None : 
        assert len(args) == 1, "Wrong number of parameters passed to constraint (expected 1, got %d)" % len(args)
    return options, args
############################################

    

def main( argv=None ) :
    options, args = opts()  
    
    if options.likelihood is not None :
        import modules.lhood_module as lhm
        import modules.lhood_dict as lhd
        lh_opts = lhd.get_lhood_dict().get(options.likelihood,None)
        assert lh_opts is not None, \
            "Likelihood provided does not exist, likelihoods are %s" % \
            lhd.get_lhood_dict().keys()
        assert len(args) == len(lh_opts["vars"]), \
            "Wrong number of inputs for likelihood (expected %d, got %d)" % \
            (len(lh_opts["vars"]),len(args))
        lh = lhm.LHood( var_pos=[None]*len(args), lhd=lh_opts )
        vals = [ eval(a) for a in args ]
        chi2 = lh.testChi2(vals)
        print "{lhname} @ {args} => {chi2}".format( lhname=lh, args=vals, chi2=chi2 )


if __name__ == "__main__":
    main()

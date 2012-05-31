import modules.lhood_module as lhm
import modules.lhood_dict as lhd

import modules.constraint_dict as ctd

def getNoVarLikelihood( lh_name, carg_len ) :
    lh_opts = lhd.get_lhood_dict().get(likelihood,None)
    assert lh_opts is not None, \
        "Likelihood provided does not exist, likelihoods are %s" % \
        lhd.get_lhood_dict().keys()
    assert carg_len == len(lh_opts["vars"]), \
        "Wrong number of inputs for likelihood (expected %d, got %d)" % \
        (len(lh_opts["vars"]),len(args))
    lh = lhm.LHood( var_pos=[None]*len(args), lhd=lh_opts )
    return lh

def runLikelihood( likelihood, argset ) :
    for args in argset[1:] : assert len(args) == len(argset[0]), \
        "different length arguments passed to likelihood"
    lh = getNoVarLikelihood( lh_name, len(argset[0]) )
    for args in argset : 
        chi2 = lh.testChi2(args)
        print "{lhname} @ {args} => {chi2}".format( lhname=lh, args=args, chi2=chi2 )

def runConstraint( constraint, args ) :
    con = ctd.get_constraint_dict().get(constraint,None)
    assert con is not None, \
        "Constraint provided doe not exist, constraints are %s" % \
        ctd.get_constraint_dict().keys()
    for arg in args :
        chi2 = con.getChi2(arg)
        print "{cname} @ {arg} => {chi2}".format( cname=con, arg=arg, chi2=chi2 )

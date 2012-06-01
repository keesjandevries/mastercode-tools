import modules.lhood_module as lhm
import modules.lhood_dict as lhd

import modules.constraint_dict as ctd

def processArgs( args, l = 0 ) :
    # could be a list of strings, or a list of args on tehir own, or a list of list of args
    out = []
    if isinstance(args, list) :
        vals = []
        for a in args :
            if isinstance(a, list) :
                out.append(a)
            if isinstance(a, str) :
                out += readInputFile(a)
            else :
                vals.append(a)
        if vals != [] : out.append(vals)
    elif isinstance(args, str) : out += readInputFile(args)
    else : out.append( [args] )
    print out
    checkArgLength( out, l )

    return out

def readInputFile( name ) :
    try :
        f = open(name, 'r')
    except IOError as e :
        print "File {0} doesn't exist, skipping".format(e)
        return []
    out  = []
    for line in f :
        inputs = line.split()
        x = [ eval(i) for i in inputs ]
        out.append(x)
    f.close()
    return out

def checkArgLength( args, l = 0 ) :
    for arg in args :
        if isinstance(arg,list) :
            if l==0 : assert len(arg)==len(args[0]), \
            "must provide same number of arguments to the likelihood"
            else : assert len(arg) == l, \
            "expected {l}, got {a} arguments".format(l=l, a=arg)

def getNoVarLikelihood( lh_name, carg_len ) :
    lh_opts = lhd.get_lhood_dict().get(lh_name,None)
    assert lh_opts is not None, \
        "Likelihood provided does not exist, likelihoods are %s" % \
        lhd.get_lhood_dict().keys()
    assert carg_len == len(lh_opts["vars"]), \
        "Wrong number of inputs for likelihood (expected %d, got %d)" % \
        (len(lh_opts["vars"]),len(args))
    lh = lhm.LHood( var_pos=[None]*carg_len, lhd=lh_opts )
    return lh

def runLikelihood( likelihood, args ) :
    argset = processArgs( args )
    if len(argset) > 0 :
        lh = getNoVarLikelihood( likelihood, len(argset[0]) )
        for arg in argset :
            chi2 = lh.testChi2(arg)
            print "{lhname} @ {arg} => {chi2}".format( lhname=lh, arg=arg, chi2=chi2 )
    else :
        print "Got no valid inputs for the likelihood"

# CONSTRAINTS
def runConstraint( constraint, args ) :
    argset = processArgs(args,1)
    con = ctd.get_constraint_dict().get(constraint,None)
    assert con is not None, \
        "Constraint provided doe not exist, constraints are %s" % \
        ctd.get_constraint_dict().keys()
    for arg in argset :
        chi2 = con.getChi2(arg[0])
        print "{cname} @ {arg} => {chi2}".format( cname=con, arg=arg[0], chi2=chi2 )

#! /usr/bin/env python
import ROOT as r
from itertools import permutations

from histogram_processing import entry_histo_full_path
from modules.mcchain import MCAnalysisChain

AB_BINARY = "../bin/AfterBurner.exe"

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

def print_bin_edges(hist,bin,vars):
    axes=['X','Y']
    nX,nY,nZ=r.Long(0),r.Long(0),r.Long(0)
    hist.GetBinXYZ(bin,nX,nY,nZ)
    print "The bin edges are:"
    for var,axis in zip(vars,axes):
        low_edge=eval("hist.Get%saxis().GetBinLowEdge(n%s)" % (axis,axis) )
        up_edge =eval("hist.Get%saxis().GetBinUpEdge(n%s)" % (axis,axis) )
        print low_edge, "<", var, "<", up_edge

def get_entry_from_histo(vars,order,name,mcf) :
    f = r.TFile.Open(mcf.FileName)
    hist = f.Get(name).Clone()
    hist.SetDirectory(0)
    f.Close()

    vals = [ vars[var] for var in order ]
    print vals

    hBin = hist.FindBin( *vals )
    n = hist.GetBinContent(hBin)
    print_bin_edges(hist,hBin,order)
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
    f.Close()
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
            name = entry_histo_full_path(p, mcf)
            hExist = hist_exists( name, mcf )
    except StopIteration  :
        assert False, "The given coordinate(s) could not be found in a histogram. Please make a corresponding EntryHist. "
    return name, p

def print_afterburner_coordinates(chain, mcf):
    print"Command for AfterBurner.exe is: "
    print "\t%s" % get_afterburner_command(chain, mcf)

def get_afterburner_command( chain, mfc) : 
    input_coords = get_input_coordinates( chain, mfc )
    input_strings = [ str(input) for input in input_coords ]
    return "%s 0 %s" % ( AB_BINARY, " ".join( input_strings ) )
    
def get_input_coordinates( chain, mfc ) :
    return [chain.treeVars["predictions"][ input ]   for input in range(1,mfc.Inputs+5) ]

def get_best_fit_entry(mcf):
    f=r.TFile(mcf.FileName)
    bfName=getattr(mcf,"BestFitEntryName","BestFitEntry" )
    #check wheterh best fit point is in the file
    try:
        t=f.Get(bfName).Clone()
    except ReferenceError:
        print "%s does not contain a tree with the best fit point" % mcf.FileName
        return -1
#        assert False,   "%s does not contain a tree with the best fit point" % mcf.FileName

    for entry in t:
        n=entry.EntryNo

    f.Close()
    return n

def print_chi2(chain,n,mcf):
    chi2=chain.treeVars["predictions"][ 0 ]
#    print "\nTotal X^2 = %f" % chain.treeVars["predictions"][ 0 ]
    n_bf=get_best_fit_entry(mcf)
    chain.GetEntry(n_bf)
    chi2_bf=chain.treeVars["predictions"][ 0 ]
    print "\nTotal X^2 = %f, DX^2 = %f" % (chi2 ,(chi2-chi2_bf))
    chain.GetEntry(n)
    p_value, n_dof = get_p_value_n_dof(chain,mcf)
    perc_p_value = p_value*100.
#    print "N_dof = ", n_dof, "p-value = ", p_value 
    print "N_dof = {:d}, p-value = {:2.1f} ".format(n_dof,perc_p_value)


def print_n(n):
    print "Found entry number: %d" % n

def print_chi2_breakdown(chain,mcf):
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
        v_index = MCV.get_index(mcf)
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

def get_p_value_n_dof(chain,mcf):
    import models
    import variables as v
    model  = models.get_model_from_file(mcf)
    lhoods = models.get_lhood_names(mcf)
    MCVdict=v.mc_variables()
    chi2_s=[]
    for constraint in model:
        sn=constraint.short_name
        chi2_s.append(get_contribution(chain,mcf,sn))

    for i, lhood in enumerate(lhoods.items()):
        chi2_s.append(chain.treeVars["lhoods"][i])

    count=0
    for chi2 in chi2_s:
        if chi2 > 0 : count += 1

    n_dof = count - mcf.Inputs
    chi2_tot = chain.treeVars["predictions"][0]

    p_value= r.TMath.Prob(chi2_tot, n_dof)

    return p_value, n_dof


def print_ma_info(chain,mcf):
    from math import sqrt
    MA =get_prediction(chain,mcf,"mA0")
    MAQ=sqrt(get_prediction(chain,mcf,"mA0^2"))
    a=(MAQ-MA)/MA
    print "\nMA info: \n "
    print "MA(Q=M_Z)    = %f" %MA 
    print "MA(Q=M_SUSY) = %f" %MAQ 
    print "a            = %f" % a
    
def get_prediction(chain,mcf,shortname):
    import variables as v
    MCVdict=v.mc_variables()
    index = MCVdict[shortname].get_index(mcf)
    prediction=chain.treeVars["predictions"][index]
    return prediction

def get_contribution(chain,mcf,shortname):
    import variables as v
    MCVdict=v.mc_variables()
    index = MCVdict[shortname].get_index(mcf)
    contribution=chain.treeVars["contributions"][index]
    return contribution


def print_prediction(chain,mcf,shortname):
    p=get_prediction(chain,mcf,shortname)
    if p > 0.0001:
        print "{:11.2f} {!r}". format(p    , shortname) 
    else:
        print "{:11.4g} {!r}". format(p    , shortname)

def print_spectrum(chain,mcf):
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
        print_prediction(chain,mcf,sn)

def print_parameters(chain,mcf):
    para_shortnames=[
    "m0"  ,   
    "m12" ,  
    "A0"  ,  
    "tanb",  ]
    print "\nParameters:   \n"
    for sn in para_shortnames:
        print_prediction(chain,mcf,sn)
    if mcf.PredictionIndex==12:
        print_prediction(chain,mcf,"mhu2")
        print_prediction(chain,mcf,"mhd2")
        
def print_mu(chain,mcf):
    #print "\nmu:\n"
    print_prediction(chain,mcf,"mu")

def print_bsmmm(chain,mcf):
    print "\nbsmm:\n"
    print_prediction(chain,mcf,"Bsmumu")

def print_sigma_si(chain,mcf):
    print "\nsigma^SI from MicroOMEGAs [pb]:\n"
    print_prediction(chain,mcf,"sigma_pp^SI")
    
#    print "\nsigma^SI from modified dmtool [pb]:\n"
#    print_prediction(chain,mcf,"KOsigma_pp^SI_cen50")
#    print_prediction(chain,mcf,"KOsigma_pp^SI_unc50_14")
#    print_prediction(chain,mcf,"KOsigma_pp^SI_unc50_7")
   
#    print "\nsigma^SI values [pb] from Keith's code with Sigma_pi_N = 50 +- Z*14:\n"
#    import variables as v
#    MCVdict=v.mc_variables()
#    index = MCVdict["KOsigma_pp^SI"].get_index(mcf)
##    ZSigPiNs=[0, 0.2,-0.2, 0.4,-0.4, 0.6,-0.6, 0.8,-0.8, 1.0,-1.0,
##               1.33,-1.33, 1.66,-1.66, 2.0,-2.0, 2.5,-2.5, 3.0,-3.0]
#    Zs=[ 0.2, 0.4, 0.6, 0.8, 1.0,  1.33, 1.66, 2.0, 2.5, 3.0]
#    ZSigPiNs=[0.]+Zs+[-Z for Z in Zs]
#    print "Z    :   ssi"
#    for i ,Z in enumerate(ZSigPiNs):
#        prediction=chain.treeVars["predictions"][index+i]
#        print  "{:3.2f} :  {:11.4g}   ,".format(Z, prediction)
#    print "\nsigma^SI values [pb] from Keith's code with Sigma_pi_N = 64 +- Z*8:\n"
#    for i ,Z in enumerate(ZSigPiNs):
#        prediction=chain.treeVars["predictions"][index+i+21]
#        print  "{:3.2f} :  {:11.4g}   ,".format(Z, prediction)
def print_mcpp_coord_dict(chain,mcf):
    d={'mc_slha_update':{
                ('SMINPUTS', 'MZ'): get_prediction(chain,mcf,"MZ")
                }, 
            'SUSY-POPE': {
                'non_slha_inputs': {
                    'DeltaAlfa5had': get_prediction(chain,mcf,"DAlpha_had")
                    }
                }, 
            'SoftSUSY': {
                ('MINPAR', 'M0'): get_prediction(chain,mcf,"m0"),
                ('MINPAR', 'M12'): get_prediction(chain,mcf,"m12"),
                ('MINPAR', 'A'): get_prediction(chain,mcf,"A0"),
                ('MINPAR', 'TB'): get_prediction(chain,mcf,"tanb"),
                ('SMINPUTS', 'Mt'): get_prediction(chain,mcf,"mtop"),
                ('MINPAR', 'signMUE') : 1,
                }
            }
    print d

def print_info(n,mcf) :
    if n >=0:
        chain = MCAnalysisChain( mcf )
        chain.GetEntry(n)
        print_n(n)
        print_afterburner_coordinates(chain, mcf)
        print_mcpp_coord_dict(chain,mcf)
        print_chi2(chain,n,mcf)
        print_parameters(chain,mcf)
    #    print_mu(chain,mcf)
    #    print_bsmmm(chain,mcf)
        print_sigma_si(chain,mcf)
        print_spectrum(chain,mcf) 
        print_chi2_breakdown(chain,mcf)
    #    print_ma_info(chain,mcf)
    else:
        print "\nEntry number was ", n, " probably an Error has occurred\n"

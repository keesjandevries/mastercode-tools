#! /usr/bin/env python
import models

import ROOT as r
import MCchain as MCC

from progress_bar import ProgressBar
from sys import stdout
from array import array
from math import sqrt

# avoid namespace clash
__DEBUG=False

def good_point( point, mcfc, verbose = 0) :
    problem = ""
    good = True

    m32 = point[1] # mSUGRA m_{3/2} = m0
    mneu1 = point[2+mcfc.SpectrumIndex]
    if getattr( mcfc, "DisallowGravitinoLSP", False ) and mneu1 > m32 :
        good = False
        if verbose > 0 : problem += "\t! Gravitino LSP (mSUGRA)\n"

    tanb = point[4]
    if tanb > 70 :
        good = False
        if verbose > 0 : problem += "\t! tanb > 70\n"

    #if getattr( mcfc, "MaxMADiff", 1e9 )a < 5.0 and tanb > 80 :
    #    good = False
    ## no point checking this

    if tanb < -900 :
        # tanb was set to -999 when softsusy produced a tachyonic error but didnt dump the point
        if verbose > 0 : problem += "\t! mSUGRA: error value for tanb found (mSUGRA tachyon check)\n"
        good = False

    mstau = point[ mcfc.SpectrumIndex + 12 ]
    if mneu1 > mstau :
        good = False
        if verbose > 0 : problem += "\t! stau LSP\n"

    sigma_pp_ds = point[ mcfc.PredictionIndex + 30 ]
    if sigma_pp_ds > 0.001 :
        good = False
        if verbose > 0 : problem += "\t! sigma_p^SI from DarkSUSY non-zero\n"


    mA02 = point[mcfc.PredictionIndex+35]
    mA   = point[mcfc.SpectrumIndex+24]
    if hasattr( mcfc, "MaxMADiff" ) :
        mAdiff = ( mA02 - sqrt(mA02) ) / mA
        if mA > 0 and mA02 > 0 and mAdiff > mcfc.MaxMADiff :
            good = False
            if verbose > 0 : problem += "\t! Too large a difference between mA and sqrt(mA02)\n"

    if verbose > 0 : print problem

    return good

def spectrum_constraints( point, collection, verbose = 0 ) :
    ch1, ch2, neu1, neu2, neu3, neu4, er, el, nue, mur, mul, numu, tau1, tau2, \
        nut, qr, ql, t1, t2, b1, b2, g, h0, H0, A0, Hp = \
        range(collection.SpectrumIndex, collection.SpectrumIndex+26 )

    penalty=0.0

    values = []
    values.append( min( [point[ch1], point[ch2]] ) ) # lightest chargino
    values.append( point[neu1] ) # neutralino
    values.append( min( [ point[x] for x in [er, el, mur, mul, tau1, tau2] ] ) ) # charged sleptons
    values.append( min( [ point[x] for x in [nue, numu, nut] ] ) ) # sneutrinos
    values.append( min( [ point[x] for x in [t1, t2, b1, b2, qr, ql] ] ) ) # squarks
    limits = [ 103.0, 50.0, 90.0, 90.0, 90.0 ]
    names = [ "lightest chargino", "charged slepton", "sneutrino", "squark" ]

    for value, limit, name in zip( values, limits, names ) :
        if value < limit :
            ipen = (value   -limit*0.95)**2
            if verbose>2 :
                print "%s: %f < %f -> adding %f" % ( name, value, limit, ipen )
            penalty += ipen

    for val, name in zip(values, names) :
        if point[neu1] > val :
            ipen = (val - point[neu1])**2
            if verbose>2 :
                print "m_%s < m_neu1: adding %f" % ( name, ipen )
            penalty += ipen

    if verbose>2 and penalty > 0 :
        print "Total penalty: %f" % penalty

    return penalty

def recalc_to_file( collection ) :
    model  = models.get_model_from_file(collection.ModelFile)
    lhoods = models.get_lhood_from_file( getattr(collection,"LHoodFile", None) )
    outfile = collection.OutputFile

    chain = MCC.MCchain( collection )
    nentries = chain.GetEntries()

    begin = getattr( collection, "StartEntry", 0)
    end   = getattr( collection, "EndEntry", nentries+1)

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
    
    # want to save best fit point entry number: create new tree and branch
    bfname = getattr( collection, "BestFitEntryName", "BestFitEntry"  ) 
    bft=r.TTree(bfname, "Entry")
    bfn=array('i',[0])
    bft.Branch('EntryNo',bfn,'EntryNo/I')
    
    # and the minChi minEntry
    minChi=1e9
    minEntry=-1

    prog = ProgressBar(begin, end, 77, mode='fixed', char='#')
    for entry in range(begin,end) :

        prog.increment_amount()
        print prog,'\r',
        stdout.flush()

        chain.GetEntry(entry)
        if good_point( chain.chi2vars, collection ) :
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

            chi2 += spectrum_constraints( chain.chi2vars, collection )

            if chain.chi2vars[0] > getattr(collection, "MinChi2", 0 ) and \
               chain.chi2vars[0] < getattr(collection, "MaxChi2", 1e9 ) :
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
                #dealing with minChi
                if chi2 < minChi:
                    minChi=chi2
                    minEntry=entry

    #Saving best fit Entry number
    bft.GetEntry(0)
    bfn[0]=minEntry-begin
    bft.Fill()

    bft.AutoSave()
    chi2tree.AutoSave()
    contribtree.AutoSave()


    out.Close()

    if __DEBUG :
        print "\n--------------------------\n"
        print "   TOTAL    (    MEAN    )"
        print "%10e(%10e)" % ( total_delta, (total_delta/(end-begin)) )
        print "\n--------------------------\n"

def go( collection ) :
    recalc_to_file( collection )

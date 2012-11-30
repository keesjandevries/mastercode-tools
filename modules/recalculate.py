#! /usr/bin/env python
import models

import ROOT as r
from modules.mcchain import MCRecalcChain
import variables as v

from progress_bar import ProgressBar
from sys import stdout
from array import array
from math import sqrt

# avoid namespace clash
__DEBUG=False


def good_point( point, mcfc,MCVdict,verbose = 0 ) :
    problem = ""
    good = True

    m32 = point[1] # mSUGRA m_{3/2} = m0
    mneu1 = point[2+mcfc.SpectrumIndex]
    if getattr( mcfc, "DisallowGravitinoLSP", False ) and mneu1 > m32 :
        good = False
        if verbose > 0 : problem += "\t! Gravitino LSP (mSUGRA)\n"


    #29/11/2012: Only keep points with m_stau - m_neutralino < m_tau
    if getattr( mcfc, "LongLivedStua", False ): 
        mneu1 = point[MCVdict["neu1"].get_index(mcfc)]
        mstau = point[MCVdict["stau_1"].get_index(mcfc)]
        if  mstau-mneu1 > 1.777 :
            good = False
            if verbose > 0 : problem += "\t! Cut away mstau-mneu1 > mstau. \n"

    #16/08/2012: cut on tanb for long lived stau's  
    if getattr( mcfc, "LongLivedStuaTanbCut", False ): 
        tanb = point[4]
        if not tanb < 41.:
            good = False
            if verbose > 0 : problem += "\t! Cut away tanb > 41. \n"

    #10/09/2012 
    if getattr( mcfc, "CharginoNLSPCut", False ): 
        index_offset=mcfc.SpectrumIndex
#        spectrum=[abs(m) for m in (point[spi:spi+1]+point[spi+3:spi+21])]
#        m_nlsp=min(spectrum)
#        m_stau=point[spi+12]
#        m_char=point[spi]
        chi1     =  abs(point[index_offset+0 ])  
#       chi2     =  abs(point[index_offset+1 ])  
#       neu1     =  abs(point[index_offset+2 ])  
        neu2     =  abs(point[index_offset+3 ])  
        neu3     =  abs(point[index_offset+4 ])  
        neu4     =  abs(point[index_offset+5 ])  
        sel_r    =  abs(point[index_offset+6 ])  
        sel_l    =  abs(point[index_offset+7 ])  
        snu_e    =  abs(point[index_offset+8 ])  
        smu_r    =  abs(point[index_offset+9 ])  
        smu_l    =  abs(point[index_offset+10])
        snu_mu   =  abs(point[index_offset+11])
        stau_1   =  abs(point[index_offset+12])
#       stau_2   =  abs(point[index_offset+13])
        snu_tau  =  abs(point[index_offset+14])
        squark_r =  abs(point[index_offset+15])
        squark_l =  abs(point[index_offset+16])
        stop1    =  abs(point[index_offset+17])
#       stop2    =  abs(point[index_offset+18])
        sbottom1 =  abs(point[index_offset+19])
#       sbottom2 =  abs(point[index_offset+20])
        gluino   =  abs(point[index_offset+21])
#       mh0      =  abs(point[index_offset+22])
        mH0      =  abs(point[index_offset+23])
        mA0      =  abs(point[index_offset+24])
        mH       =  abs(point[index_offset+25])
        spectrum=[
        chi1     ,  
#       chi2     ,  
#       neu1     ,  
        neu2     ,  
        neu3     ,  
        neu4     ,  
        sel_r    ,  
        sel_l    ,  
        snu_e    ,  
        smu_r    ,  
        smu_l    ,
        snu_mu   ,
        stau_1   ,
#       stau_2   ,
        snu_tau  ,
        squark_r ,
        squark_l ,
        stop1    ,
#       stop2    ,
        sbottom1 ,
#       sbottom2 ,
        gluino   ,
#       mh0      ,
        mH0      ,
        mA0      ,
        mH       ,
                        ]
        abs_spectrum=[abs(m) for m in spectrum]
        m_nlsp = min(abs_spectrum)
#        print  abs_spectrum
#        if not m_nlsp==stau_1  :
        if not m_nlsp==neu2    :
#            print abs_spectrum
            good = False
            if verbose > 0 : problem += "\t! Cut away Chargino is not LSP \n"

    #June 2012: make the cut for resampling the SuFla buggy points, see mail (Final (?) reprocessing? II)
    if getattr( mcfc, "SelectSuFlaBugPoints", False ): 
        MA = point[mcfc.SpectrumIndex+24]
        tanb = point[4]
        if not ( (mcfc.SpectrumIndex==117 and tanb >40) or (mcfc.SpectrumIndex==119 and( ( tanb >30 and MA<2000) or (tanb>40 and MA>=200) ))):
            good = False
            if verbose > 0 : problem += "\t! In bugged region \n"

    # July 2012: to redo the CMSSM points in the lower triangle, see mail (tanb cut for the CMSSM probably to sharp )
    if getattr( mcfc, "SelectSuFlaCMSSMLowerTrianglePoints", False ): 
        m0  = point[1]
        m12 = point[2]
        tanb = point[4]
        if not ( mcfc.SpectrumIndex==117 and tanb < 40 and m12 < (0.3995*m0 -388  )  ):
            good = False
            if verbose > 0 : problem += "\t! Not in triangle \n"

    #July 2012: to redo the NUHM1 point with low tanb and MA>1500
    if getattr( mcfc, "SelectSuFlaNUHM1LowTanbPoints", False ): 
        tanb = point[4]
        MA = point[mcfc.SpectrumIndex+24]
        if not ( mcfc.SpectrumIndex==119 and ((MA > 1500 and tanb <30 ) or (MA>2000 and tanb<40)  )):
            good = False
            if verbose > 0 : problem += "\t! Not in the NUHM1 low tanb high MA region \n"

    # make the cut for resampling the SuFla buggy points, see mail (Final (?) reprocessing? II)
    if getattr( mcfc, "SelectSuFlaNoneBugPoints", False ): 
        m0  = point[1]
        m12 = point[2]
        MA = point[mcfc.SpectrumIndex+24]
        tanb = point[4]
        if ((mcfc.SpectrumIndex==117 and tanb >40 or (tanb < 40 and m12 < (0.3995*m0 -388  ))) or  
            (mcfc.SpectrumIndex==119 and  (tanb>30 or MA>1500   ) )):
            good = False
            if verbose > 0 : problem += "\t! Not in bugged region \n"

    # The so called surgical amputation: removing points from " the infamous region C  "
    if getattr( mcfc, "SelectRegionC", False ) and point[2] < (600+2.7*point[1]) :
        good = False
        if verbose > 0 : problem += "\t! Point not in region C\n"

    # The so called surgical amputation: removing points from " the infamous region C  "
    if getattr( mcfc, "SurgicalAmputation", False ) and point[2] > (600+2.7*point[1]) :
        good = False
        if verbose > 0 : problem += "\t! Apply surgical amputation of point in region C\n"

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
        if mA > 0 and mA02 > 0:
            mAdiff = abs( ( mA - sqrt(mA02) ) / mA )
        else :
            mAdiff = 0 
        if mAdiff > mcfc.MaxMADiff :
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
            ipen = (value   -limit*1.05)**2
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

def recalc_to_file( collection, output_file = "" ) :
    model  = models.get_model_from_file(collection)
    lhoods = models.get_lhood_from_file(collection)
    outfile = collection.FileName if output_file == "" else output_file
    print "Output file is %s" % outfile

    # initialise the MC-variables
    MCVdict=v.mc_variables()

    chain = MCRecalcChain( collection )
    if not chain.state :
        return
    nentries = chain.GetEntries()

    begin = getattr( collection, "StartEntry", 0)
    end   = getattr( collection, "EndEntry", nentries+1)

    # want to keep track of this
    count_fill_points = 0

    total_delta = 0

    # create trees in scope of outfile
    out = r.TFile(outfile,"recreate")
    chi2tree = chain.chains["predictions"].CloneTree(0)

    # might need to do address of on contirbvars
    nTotVars = chain.nTotVars["predictions"]
    contribvars = array('d',[0.0]*nTotVars)
    contribtree = r.TTree( 'contribtree', 'chi2 contributions')
    varsOutName = "vars[%d]/D" % ( nTotVars )
#    contribtree.SetMaxTreeSize(10*chi2tree.GetMaxTreeSize())
    contribtree.Branch("vars",contribvars,varsOutName)

    # same with lhood
    nLHoods = len(lhoods.keys())
    lhoodvars = array('d',[0.0]*nLHoods)
    lhoodtree = r.TTree( 'lhoodtree', 'lhood contributions')
    varsOutName = "vars[%d]/D" % ( nLHoods )
#    lhoodtree.SetMaxTreeSize(10*chi2tree.GetMaxTreeSize())
    lhoodtree.Branch("vars",lhoodvars,varsOutName)

    # want to save best fit point entry number: create new tree and branch
    bfname = getattr( collection, "BestFitEntryName", "BestFitEntry"  )
    bft=r.TTree(bfname, "Entry")
    bfn=array('i',[0])
    bft.Branch('EntryNo',bfn,'EntryNo/I')

    # and the minChi minEntry
    minChi=1e9
    minEntry=-1
    count=-1 # becuase the first entry has number 0

    prog = ProgressBar(begin, end, 77, mode='fixed', char='#')
    print end-begin, " points to process..."
    for entry in xrange(begin,end) :

        prog.increment_amount()
        print prog,'\r',
        stdout.flush()

        chain.GetEntry(entry)
        if good_point( chain.treeVars["predictions"], collection,MCVdict ) :
            delta = 0.
            chi2 = 0

            for constraint in model :
                MCV=MCVdict[constraint.short_name]
                v_index = MCV.get_index(collection)

                chi2_t = constraint.get_chi2( chain.treeVars["predictions"][v_index] )
                contribvars[v_index] = chi2_t
                chi2 += chi2_t
            for i,lh in enumerate(lhoods.values()) :
                chi2_t = lh.get_chi2( chain.treeVars["predictions"] )
                lhoodvars[i] = chi2_t
                chi2 += chi2_t

            chi2 += spectrum_constraints( chain.treeVars["predictions"], collection )

            if chi2 > getattr(collection, "MinChi2", 0 ) and \
               chi2 < getattr(collection, "MaxChi2", 1e9 ) :
                # This was inserted to check on if there was a significant
                # calculation error ( average deltachi2 per entry: 1e-15 )
                if __DEBUG :
                    delta_chi2_val = chi2_t - chain.treeVars["contributions"][key]
                    delta = delta + delta_chi2_val
                    total_delta = total_delta + abs(delta)
                chain.treeVars["predictions"][0] = chi2
                contribvars[0] = chi2
                chi2tree.Fill()
                count_fill_points+=1
                contribtree.Fill()
                lhoodtree.Fill()
                count+=1
                #dealing with minChi
                if chi2 < minChi:
                    minChi=chi2
                    minEntry=count

    #Saving best fit Entry number
    bft.GetEntry(0)
    bfn[0]=minEntry
    bft.Fill()

    bft.AutoSave()
    chi2tree.AutoSave()
    contribtree.AutoSave()
    lhoodtree.AutoSave()

    out.Close()
    # some output for Monitoring:
    print "Total number of points       : ",end-begin
    print "Accepted number of points    : ",count_fill_points

    if __DEBUG :
        print "\n--------------------------\n"
        print "   TOTAL    (    MEAN    )"
        print "%10e(%10e)" % ( total_delta, (total_delta/(end-begin)) )
        print "\n--------------------------\n"

def go( collection, output_file ) :
    recalc_to_file( collection, output_file )

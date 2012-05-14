#! /usr/bin/env python
from modules.Space import Space
from modules.Space import Contribution
import sys

# this is what you edit
def plots_to_make() :
    l = [
            [ "m0", "m12" ],
            [ "tanb", "m12" ],
            [ "MA"  ,"tanb" ],
            [ "mneu1","ssi" ],
            [ "mstau1" ],
            [ "mg" ],
            [ "msqr"],
            [ "bsmm" ]
#            [ "m0", "tanb" ],
#            [ "mneu1" ],
#            [ "mh" ]
        ]
    return l

def contributions_to_make() :
#    l = [ "g-2", "Oh2" ]
    l = [  ]
    return l

def standard_variables( pindex, sindex, nbins ) :
    sv = {
            #shortname     index,    min,   max, nbins,                                   title,   log
            "m0"       : [         1,     0,  2500, nbins,                    r"$m_{0} [GeV/c^{2}]$", False ],
            "m12"      : [         2,     0,  2500, nbins,                  r"$m_{1/2} [GeV/c^{2}]$", False ],
            "a0"       : [         3, -5000,  5000, nbins,                          r"$A_{0} [GeV]$", False ],
            "tanb"     : [         4,     0,    60, nbins,                          r"$\tan(\beta)$", False ],
            "mtop"     : [ pindex-4 ,    0 ,  1e9 , nbins,            r"$ m_{top}$"                 , False ],    
            "MZ"       : [ pindex-3 ,    0 ,  1e9 , nbins,            r"$ m_{Z}$"                   , False ],    
            "DAHad"    : [ pindex-1 ,    0 ,  1e9 , nbins,            r"$ \Delta\alpha_{had}$"      , False ],            
            "Rbsg"     : [ pindex   ,    0 ,  1e9 , nbins,            r"$  R(b->sg) $"              , False ],    
            "RDms"     : [ pindex+1 ,    0 ,  1e9 , nbins,            r"$  R(Delta_ms) $"           , False ],    
            "bsmm"     : [ pindex+2 ,     0, 26e-9, nbins,            r"$BR(B_{s}\rightarrow\mu\mu)", False ],
            "RBtn"     : [ pindex+3 ,    0 ,  1e9 , nbins,            r"$  R(B->tau nu) $"          , False ],        
            "RBXsll"   : [ pindex+4 ,    0 ,  1e9 , nbins,            r"$  R(B->Xsll) $"            , False ],    
            "RKlnu"    : [ pindex+5 ,    0 ,  1e9 , nbins,            r"$  R(K->lnu) $"             , False ],    
            "g-2"      : [ pindex+6 ,     0, 10e-9, nbins,                     r"$\Delta(g-2)_{\mu}", False ],
            "MW"       : [ pindex+7 ,    0 ,  1e9 , nbins,            r"$  MW $"                    , False ], 
            "STeQfb"   : [ pindex+8 ,    0 ,  1e9 , nbins,            r"$  \sin\theta_{eff}(Qfb)$"  , False ],                
            "GamZ"     : [ pindex+9 ,    0 ,  1e9 , nbins,            r"$  \Gamma_{z}$"             , False ],    
            "Rl"       : [ pindex+10,    0 ,  1e9 , nbins,            r"$  Rl l=e,mu$"              , False ],    
            "Rb"       : [ pindex+11,    0 ,  1e9 , nbins,            r"$  Rb$"                     , False ],
            "Rc"       : [ pindex+12,    0 ,  1e9 , nbins,            r"$  Rc$"                     , False ],
            "Afbb"     : [ pindex+13,    0 ,  1e9 , nbins,            r"$  Afb(b)$"                 , False ],
            "Afbc"     : [ pindex+14,    0 ,  1e9 , nbins,            r"$  Afb(c)$"                 , False ],
            "Ab16"     : [ pindex+15,    0 ,  1e9 , nbins,            r"$  Ab 16$"                  , False ],
            "Ac17"     : [ pindex+16,    0 ,  1e9 , nbins,            r"$  Ac 17 $"                 , False ],
            "AlSLD"    : [ pindex+17,    0 ,  1e9 , nbins,            r"$  Al(SLD)$"                , False ],
            "h0"       : [ pindex+18,    85,   140, nbins,                r"$m_{h^{0}} [GeV/c^{2}]$", False ],
            "Oh2"      : [ pindex+19,  0.07,  0.15, nbins,                          r"$\Omega h^{2}", False ],
            "AlPtau"   : [ pindex+20,    0 ,  1e9 , nbins,            r"$  Al(P_tau)$"              , False ],    
            "Alfb"     : [ pindex+21,    0 ,  1e9 , nbins,            r"$  Al_fb$"                  , False ],
            "sighad"   : [ pindex+22,    0 ,  1e9 , nbins,            r"$  sigma_had^0 (nb)$"       , False ],        
            "RDmk"     : [ pindex+24,    0 ,  1e9 , nbins,            r"$  R(Delta_mk) $"           , False ],    
            "RKppinn"  : [ pindex+25,    0 ,  1e9 , nbins,            r"$  R(Kp->\pi nn) $"         , False ],        
            "RBdll"    : [ pindex+26,    0 ,  1e9 , nbins,            r"$  BR(Bd->ll) $"            , False ],    
            "RDmsRDmd" : [ pindex+27,    0 ,  1e9 , nbins,            r"$  R(Dms)/R(Dmd) $"         , False ],                      
            "ssi"      : [ pindex+64, 1e-48, 1e-40, nbins,            r"$\sigma_{p}^{SI} [cm^{-2}]$", True  ],
            "mneu1"    : [  sindex+2,     0,  2000, nbins, r"$m_{\tilde{\chi}^{0}_{1}} [GeV/c^{2}]$", True  ],
            "mstau1"   : [ sindex+12,     0,  4000, nbins,     r"$m_{\tilde{\tau}_{1}} [GeV/c^{2}]$", False ],
            "msqr"     : [ sindex+15,     0,  4000, nbins,        r"$m_{\tilde{q}_{R}} [GeV/c^{2}]$", False ],
            "mg"       : [ sindex+21,     0,  4000, nbins,            r"$m_{\tilde{g}} [GeV/c^{2}]$", False ],
            "MA"       : [ sindex+24,     0,  2000, nbins,                    r"$M_{A} [GeV/c^{2}]$", False ],
         }
    return sv

###########################################
### Dont edit for run: only development ###
###########################################

def standard_plots( pindex, sindex, nbins = 100 ) :
    v = standard_variables( pindex, sindex, nbins )
    plots = plots_to_make()
    l = []
    for p in plots :
        l.append([ v[s]+[s] for s in p])
    spaces = map( make_space, l )

    return spaces

def standard_contribs( pindex, sindex, ) :
    v = standard_variables( pindex, sindex, None )
    c = contributions_to_make()
    contribs = []
    for contrib in c :
        opts = v[contrib]
        contribs.append( Contribution( opts[0], opts[-2], contrib ) )
    return contribs

def make_space( l ) :
    args = [ [],[],[],[],[],[], [] ]
    for v in l :
        for o,a in zip(v,args) :
            a.append(o)
    s = Space( *args )
    return s

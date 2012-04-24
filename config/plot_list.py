#! /usr/bin/env python
from modules.Space import Space
from modules.Space import Contribution
import sys

# this is what you edit
def plots_to_make() :
    l = [
            [ "m0", "m12" ],
            [ "m0", "tanb" ],
            [ "tanb", "m12" ],
            [ "mneu1" ],
            [ "mh" ]
        ]
    return l

def contributions_to_make() :
    l = [ "g-2" ]
    return l

def standard_variables( pindex, sindex, nbins ) :
    sv = {
            #shortname     index,    min,   max, nbins,                                   title,   log
            "m0"    : [         1,     0,  2500, nbins,                    r"$m_{0} [GeV/c^{2}]$", False ],
            "m12"   : [         2,     0,  2500, nbins,                  r"$m_{1/2} [GeV/c^{2}]$", False ],
            "a0"    : [         3, -5000,  5000, nbins,                          r"$A_{0} [GeV]$", False ],
            "tanb"  : [         4,     0,    60, nbins,                          r"$\tan(\beta)$", False ],
            "h0"    : [ pindex+20,    85,   140, nbins,                r"$m_{h^{0}} [GeV/c^{2}]$", False ],
            "ssi"   : [ pindex+64, 1e-48, 1e-40, nbins,            r"$\sigma_{p}^{SI} [cm^{-2}]$", False ],
            "mneu1" : [  sindex+2,     0,  1000, nbins, r"$m_{\tilde{\chi}^{0}_{1}} [GeV/c^{2}]$", False ],
            "mh"    : [ pindex+18,    85,   140, nbins,                 r"$m_{h^{0}} [GeV/c^{2}$", False ],
            "g-2"   : [  pindex+6,     0, 10e-9, nbins,                     r"$\Delta(g-2)_{\mu}", False ],
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

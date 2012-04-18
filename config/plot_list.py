#! /usr/bin/env python
from modules import Variables as v

import sys
sys.path.append( "./modules/" )
from Variables import *

def get_plots( pindex, sindex, nbins = 100 ) :
    return standard_plots(pindex, sindex, nbins )

def standard_plots( pindex, sindex, nbins = 100) :
    # local assignment
    d = standard_variables( pindex, sindex, nbins )
    return standard_1d_histos(d), standard_spaces(d)

def standard_spaces( d ) :
    l = [
            v.Space( d["m0"],    d["m12"]  ),
            v.Space( d["m0"],    d["tanb"] ),
            v.Space( d["tanb"],  d["m12"]  ),
#            Space( d["mneu1"], d["ssi"], logx = True, logy = True )
        ]
    return l

def standard_1d_histos( d ) :
    l = [
            d["mneu1"].update( { "log" : False } ),
            d["mh"]
        ]
    return l

def standard_variables( pindex, sindex, nbins ) :
    sv = { 
            "m0"    : v.Variable(         1,     0,  2500, nbins,                    "m_{0} [GeV/c^{2}]" ),
            "m12"   : v.Variable(         2,     0,  2500, nbins,                  "m_{1/2} [GeV/c^{2}]" ),
            "a0"    : v.Variable(         3, -5000,  5000, nbins,                          "A_{0} [GeV]" ),
            "tanb"  : v.Variable(         4,     0,    60, nbins,                           "tan(#beta)" ),
            "h0"    : v.Variable( pindex+20,    85,   140, nbins,                "m_{h^{0}} [GeV/c^{2}]" ),
            "ssi"   : v.Variable( pindex+64, 1e-48, 1e-40, nbins,            "#sigma_{p}^{SI} [cm^{-2}]" ),
            "mneu1" : v.Variable(  sindex+2,    10,  1000, nbins, "m_{#tilde{#chi}^{0}_{1}} [GeV/c^{2}]" ),
            "mh"    : v.Variable( pindex+18,    85,   140, nbins,                 "m_{h^{0}} [GeV/c^{2}" ),
         }
    return sv

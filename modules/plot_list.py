#! /usr/bin/env python

from Variables import *

def get_list( pindex, sindex, nbins = 100 ) :
    return standard_list(pindex, sindex, nbins )

def standard_list( pindex, sindex, nbins = 100) :
    # local assignment
    d = standard_variables( pindex, sindex, nbins )
    l = [
            Space( d["m0"],    d["m12"]  ),
            Space( d["m0"],    d["tanb"] ),
            Space( d["m12"],   d["tanb"] ),
            Space( d["mneu1"], d["ssi"], logx = True, logy = True )
        ]
    return l

def standard_variables( pindex, sindex, nbins ) :
    sv = { 
            "m0"    : Variable(         1,     0,  2500, nbins,                    "m_{0} [GeV/c^{2}]" ),
            "m12"   : Variable(         2,     0,  2500, nbins,                  "m_{1/2} [GeV/c^{2}]" ),
            "a0"    : Variable(         3, -5000,  5000, nbins,                          "A_{0} [GeV]" ),
            "tanb"  : Variable(         4,     0,    60, nbins,                           "tan(#beta)" ),
            "h0"    : Variable( pindex+20,    85,   140, nbins,                "m_{h^{0}} [GeV/c^{2}]" ),
            "ssi"   : Variable( pindex+64, 1e-48, 1e-40, nbins,            "#sigma_{p}^{SI} [cm^{-2}]" ),
            "mneu1" : Variable(  sindex+2,    10,  1000, nbins, "m_{#tilde{#chi}^{0}_{1}} [GeV/c^{2}]" ),
         }
    return sv
